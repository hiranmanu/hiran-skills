"""Unit tests for plugins/cv-tailoring/skills/cv-tailoring/scripts/validate_cv.py.

Run from the repo root:  python3 -m unittest discover -s tests -v

Stdlib only. Builds tiny in-memory DOCX files, so no Word, Node or docx
package is needed. Covers the checks that gate a CV: keyword matching,
bullet evidence, skills duplicates, date format, dashes, metadata.
"""

import importlib.util
import io
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "plugins/cv-tailoring/skills/cv-tailoring/scripts/validate_cv.py"

spec = importlib.util.spec_from_file_location("validate_cv", SCRIPT)
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def para(text, bullet=False, section=None):
    return {"text": text, "bullet": bullet, "section": section}


def make_docx(paragraph_xml: str, author="Hiran Patel", with_core=True) -> Path:
    body = f'<w:document xmlns:w="w"><w:body>{paragraph_xml}</w:body></w:document>'
    core = (f'<cp:coreProperties xmlns:cp="c" xmlns:dc="d"><dc:creator>{author}</dc:creator>'
            f'<cp:lastModifiedBy>{author}</cp:lastModifiedBy></cp:coreProperties>')
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        z.writestr("word/document.xml", body)
        if with_core:
            z.writestr("docProps/core.xml", core)
    f = tempfile.NamedTemporaryFile(suffix=".docx", delete=False)
    f.write(buf.getvalue())
    f.close()
    return Path(f.name)


def p_xml(text, bullet=False):
    num = "<w:pPr><w:numPr/></w:pPr>" if bullet else ""
    return f"<w:p>{num}<w:r><w:t>{text}</w:t></w:r></w:p>"


class KeywordMatching(unittest.TestCase):
    def test_short_keyword_does_not_match_inside_words(self):
        paras = [para("Maintained the retail said plan", True, "career"), para("Skills: retail", False, "skills")]
        fails, _, _ = v.check_keywords(paras, ["AI"])
        self.assertTrue(any("appears nowhere" in f for f in fails))

    def test_plural_and_hyphen_variants_match(self):
        paras = [para("Set OKRs and a value-stream view", True, "career"), para("Skills: OKR", False, "skills")]
        fails, _, _ = v.check_keywords(paras, ["OKR", "value stream"])
        self.assertEqual(fails, [])

    def test_synonym_alternatives(self):
        paras = [para("Ran demand intake", True, "career"), para("Skills: demand intake", False, "skills")]
        fails, _, _ = v.check_keywords(paras, ["demand management|demand intake"])
        self.assertEqual(fails, [])

    def test_skills_keyword_without_bullet_evidence_fails(self):
        paras = [para("Skills: Agile", False, "skills"), para("Built a team", True, "career")]
        fails, _, _ = v.check_keywords(paras, ["agile"])
        self.assertTrue(any("no bullet evidence" in f for f in fails))

    def test_bullet_only_keyword_warns(self):
        paras = [para("Ran agile delivery", True, "career"), para("Skills: other", False, "skills")]
        fails, warns, _ = v.check_keywords(paras, ["agile"])
        self.assertEqual(fails, [])
        self.assertTrue(any("only in bullets" in w for w in warns))


class Checks(unittest.TestCase):
    def test_skills_duplicate_detected(self):
        paras = [para("Skills & Competencies", False, "skills"),
                 para("A: OKRs · Roadmaps", False, "skills"),
                 para("B: okrs · Data", False, "skills")]
        self.assertEqual(len(v.check_skills_duplicates(paras)), 1)

    def test_dates(self):
        ok = [para("Role\tJan 2026 - Sep 2026"), para("Role\tApr 2019 - present"), para("Role\t2019 - 2021")]
        self.assertEqual(v.check_dates(ok), [])
        bad = [para("Role\t2019"), para("Role\tJan 2019 – Feb 2020"), para("Role\tJan 2019 - ")]
        self.assertEqual(len(v.check_dates(bad)), 3)

    def test_dashes(self):
        self.assertTrue(v.check_dashes([para("a — b")]))
        self.assertEqual(v.check_dashes([para("a - b")]), [])

    def test_references_section(self):
        self.assertTrue(v.check_references_section([para("References")]))
        self.assertTrue(v.check_references_section([para("Available on request")]))
        self.assertEqual(v.check_references_section([para("Profile Summary")]), [])

    def test_email(self):
        self.assertTrue(v.check_email([para("no contact here")]))
        self.assertEqual(v.check_email([para("me@example.com")]), [])


class DocxHandling(unittest.TestCase):
    def test_missing_core_xml_does_not_crash(self):
        path = make_docx(p_xml("Profile Summary"), with_core=False)
        self.assertEqual(v.check_docx_author(path), (None, None))

    def test_author_read(self):
        path = make_docx(p_xml("x"), author="Hiran Patel")
        self.assertEqual(v.check_docx_author(path), ("Hiran Patel", "Hiran Patel"))

    def test_extraction_marks_bullets_and_sections(self):
        xml = p_xml("Profile Summary") + p_xml("Hello") + p_xml("Career &amp; Key Achievements to Date") + p_xml("Did a thing", bullet=True)
        paras = v.extract_paragraphs(make_docx(xml))
        self.assertEqual(paras[1]["section"], "profile")
        self.assertTrue(paras[3]["bullet"])
        self.assertEqual(paras[3]["section"], "career")
        self.assertIn("Career & Key", paras[2]["text"])  # entities decoded

    def test_tab_is_kept_and_not_swallowed(self):
        xml = '<w:p><w:r><w:t>Role</w:t></w:r><w:r><w:tab/></w:r><w:r><w:t>Jan 2026 - Sep 2026</w:t></w:r></w:p>'
        paras = v.extract_paragraphs(make_docx(xml))
        self.assertEqual(paras[0]["text"], "Role\tJan 2026 - Sep 2026")


if __name__ == "__main__":
    unittest.main()
