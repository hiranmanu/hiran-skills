"""End-to-end regression test for the render + validate chain.

"Regression" here means: a fixed, known input (scripts/example_content.json) goes
through the whole pipeline (content file -> build_cv.js -> DOCX -> validate_cv.py),
and the test checks the result is still a valid CV. If a later change to the
builder or validator breaks the chain, this fails.

Needs Node.js and the `docx` package (`npm install` in scripts/). Skipped, not
failed, when they are missing. The Word layout check needs Word, so it is not run
here (CI has no Word); run word_layout_check.ps1 locally.

Run from the repo root:  python3 -m unittest discover -s tests -v
"""

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "plugins/cv-tailoring/skills/cv-tailoring/scripts"
BUILD = SCRIPTS / "build_cv.js"
VALIDATE = SCRIPTS / "validate_cv.py"
EXAMPLE = SCRIPTS / "example_content.json"
IDENTITY = SCRIPTS / "identity.example.json"


def node_ready() -> bool:
    node = shutil.which("node")
    if not node:
        return False
    r = subprocess.run([node, "-e", "require('docx')"], cwd=SCRIPTS, capture_output=True)
    return r.returncode == 0


NODE_OK = node_ready()


def build(content_path, *extra):
    return subprocess.run(["node", str(BUILD), str(content_path), *extra], capture_output=True, text=True)


def validate(docx, content_path):
    return subprocess.run([sys.executable, str(VALIDATE), str(docx), "--content", str(content_path), "--identity", str(IDENTITY)],
                          capture_output=True, text=True)


@unittest.skipUnless(NODE_OK, "Node.js + the docx package are not available (npm install in scripts/)")
class Pipeline(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def content(self, mutate=None):
        data = json.loads(EXAMPLE.read_text(encoding="utf-8"))
        if mutate:
            mutate(data)
        p = self.dir / "content.json"
        p.write_text(json.dumps(data), encoding="utf-8")
        return p

    def test_example_builds_and_validates(self):
        content = self.content()
        out = self.dir / "cv.docx"
        r = build(content, str(out), "--identity", str(IDENTITY))
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertTrue(zipfile.is_zipfile(out))
        v = validate(out, content)
        self.assertEqual(v.returncode, 0, v.stdout)
        self.assertIn("Coverage: 6/6 must-haves evidenced (100%)", v.stdout)

    def test_metadata_and_layout_constants(self):
        out = self.dir / "cv.docx"
        build(self.content(), str(out), "--identity", str(IDENTITY))
        with zipfile.ZipFile(out) as z:
            core = z.read("docProps/core.xml").decode()
            doc = z.read("word/document.xml").decode()
            styles = z.read("word/styles.xml").decode()
        self.assertIn("Jordan Smith", core)
        self.assertIn('w:w="11906"', doc)      # A4 width
        self.assertIn('w:left="680"', doc)     # house margins
        self.assertIn("Calibri", styles)       # house font

    def test_auto_output_path_and_filename(self):
        ident = json.loads(IDENTITY.read_text(encoding="utf-8"))
        ident["output_base"] = str(self.dir / "CV Output")
        idp = self.dir / "identity.json"
        idp.write_text(json.dumps(ident), encoding="utf-8")
        r = build(self.content(), "--identity", str(idp))
        self.assertEqual(r.returncode, 0, r.stderr)
        expected = self.dir / "CV Output" / "2026.01.01_ExampleCo_DirectorOfProduct" / "Jordan_CV_2026.01.01_ExampleCo_DirProduct.docx"
        self.assertTrue(expected.exists(), f"missing {expected}; got {r.stdout}")

    def test_linkedin_only_on_product_template(self):
        for template, expect in (("product", True), ("data_architect", False)):
            out = self.dir / f"{template}.docx"
            build(self.content(lambda d, t=template: d.__setitem__("template", t)), str(out), "--identity", str(IDENTITY))
            with zipfile.ZipFile(out) as z:
                rels = z.read("word/_rels/document.xml.rels").decode()
            self.assertEqual("linkedin.com" in rels, expect, template)

    def test_builder_rejects_dashes(self):
        c = self.content(lambda d: d["roles"][0]["bullets"].append("Grew revenue — fast"))
        r = build(c, str(self.dir / "x.docx"), "--identity", str(IDENTITY))
        self.assertEqual(r.returncode, 1)
        self.assertIn("dash", r.stderr)

    def test_builder_rejects_wrong_number_of_skill_rows(self):
        c = self.content(lambda d: d["skills"].pop())
        r = build(c, str(self.dir / "x.docx"), "--identity", str(IDENTITY))
        self.assertEqual(r.returncode, 1)
        self.assertIn("exactly 3 rows", r.stderr)

    def test_validator_catches_a_skills_keyword_with_no_bullet_evidence(self):
        content = self.content(lambda d: d["must_haves"].append("kubernetes"))
        out = self.dir / "cv.docx"
        build(content, str(out), "--identity", str(IDENTITY))
        v = validate(out, content)
        self.assertEqual(v.returncode, 1)
        self.assertIn("kubernetes", v.stdout)

    def test_validator_catches_duplicate_skill_and_bad_date(self):
        # (an en dash in a date is rejected by the builder itself, so use a bare year here)
        def mutate(d):
            d["skills"][1]["items"].append("Product Strategy")  # duplicate of row 1
            d["roles"][0]["dates"] = "2025"                     # no start/end range
        content = self.content(mutate)
        out = self.dir / "cv.docx"
        self.assertEqual(build(content, str(out), "--identity", str(IDENTITY)).returncode, 0)
        v = validate(out, content)
        self.assertEqual(v.returncode, 1)
        self.assertIn("more than once in the skills rows", v.stdout)
        self.assertIn("date is not an ASCII-hyphen range", v.stdout)


if __name__ == "__main__":
    unittest.main()
