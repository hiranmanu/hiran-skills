#!/usr/bin/env python3
"""
validate_cv.py - automated step 07 validation for the cv-tailoring skill.

Works directly against the rendered .docx's XML: no external tools, pure Python
stdlib. Runs every DOCX-checkable constraint from references/05-formatting.md
and prints one PASS/WARN/FAIL report.

Usage:
    python3 validate_cv.py <path-to.docx>
    python3 validate_cv.py <path-to.docx> --keywords "a;b|c;d"
    python3 validate_cv.py <path-to.docx> --keywords-file must-haves.txt

--keywords / --keywords-file give the JD must-haves the master file SUPPORTS
(never gap keywords). Separate keywords with ";" (or one per line in the file);
use "|" for synonyms inside one keyword ("first-party data|1st party data").

Checks:
  FAIL-gating : em/en dashes, References/Recommendations section, Author
                metadata, role dates (ASCII-hyphen range with start and end),
                email as literal text, duplicate keyword inside the skills rows,
                a must-have that appears nowhere, a must-have with no bullet
                evidence (if it is in the profile/skills it must also be in a
                bullet).
  WARN-only   : a must-have found only in bullets (add it to profile/skills for
                ATS visibility), bullets long enough to wrap to a third line,
                over-long Qualifications lines.

Exit code: 0 if no FAIL, 1 otherwise (WARNs never fail the run).

Deliberately NOT checked here (needs real Word pagination; use
scripts/word_layout_check.ps1 or open the DOCX): page count, which roles sit
on page 1, role split across a page break, bullet wraps.
"""

import argparse
import html
import re
import sys
import zipfile
from pathlib import Path

EXPECTED_AUTHOR = "Hiran Patel"
GENERIC_AUTHOR_DEFAULTS = {"", "python-docx", "docx-js", "unknown", "libreoffice", "microsoft office user"}

DASH_CHARS = {"—": "em dash", "–": "en dash"}

REFERENCES_HEADING_RE = re.compile(r"^\s*(references|recommendations)\s*$", re.IGNORECASE)
REFERENCES_DOWNGRADE_RE = re.compile(r"available\s+(up\s*on|on)\s+request", re.IGNORECASE)

# <w:t> or <w:t xml:space="preserve"> only: NOT <w:tab/> or <w:tabs>
W_T_RE = re.compile(r"<w:t(?:\s[^>]*)?>(.*?)</w:t>", re.DOTALL)
W_P_RE = re.compile(r"<w:p[ >].*?</w:p>", re.DOTALL)
W_TAB_RE = re.compile(r"<w:tab\s*/>")

SECTION_HEADINGS = {
    "profile": "profile summary",
    "skills": "key skills & competencies",
    "career": "career & key achievements to date",
    "quals": "qualifications, certifications & personal details",
}

DATE_RANGE_RE = re.compile(
    r"\t((?:[A-Z][a-z]{2} )?\d{4} - (?:(?:[A-Z][a-z]{2} )?\d{4}|[Pp]resent))\s*$"
)
YEAR_RE = re.compile(r"\b(19|20)\d{2}\b")
EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")

BULLET_WARN_CHARS = 215   # about 2 full lines; beyond this a third line is likely
QUALS_WARN_CHARS = 108    # single-line ceiling for Qualifications lines


def extract_paragraphs(docx_path: Path):
    """Return a list of {text, bullet, section} from word/document.xml."""
    with zipfile.ZipFile(docx_path) as z:
        xml = z.read("word/document.xml").decode("utf-8")
    paragraphs = []
    section = None
    for p_match in W_P_RE.finditer(xml):
        p_xml = p_match.group(0)
        bullet = "<w:numPr>" in p_xml
        p_xml = W_TAB_RE.sub("<w:t>\t</w:t>", p_xml)
        text = html.unescape("".join(W_T_RE.findall(p_xml)))
        norm = text.strip().lower()
        for key, heading in SECTION_HEADINGS.items():
            if norm == heading:
                section = key
        paragraphs.append({"text": text, "bullet": bullet, "section": section})
    return paragraphs


def check_docx_author(docx_path: Path):
    with zipfile.ZipFile(docx_path) as z:
        core_xml = z.read("docProps/core.xml").decode("utf-8")
    creator_m = re.search(r"<dc:creator>(.*?)</dc:creator>", core_xml)
    lmb_m = re.search(r"<cp:lastModifiedBy>(.*?)</cp:lastModifiedBy>", core_xml)
    return (creator_m.group(1).strip() if creator_m else None,
            lmb_m.group(1).strip() if lmb_m else None)


def check_dashes(paras):
    all_text = "\n".join(p["text"] for p in paras)
    failures = []
    for ch, label in DASH_CHARS.items():
        count = all_text.count(ch)
        if count:
            samples = [p["text"].strip() for p in paras if ch in p["text"]][:5]
            failures.append(f"{count}x {label} found. Examples:\n    " + "\n    ".join(samples))
    return failures


def check_references_section(paras):
    failures = []
    for p in paras:
        stripped = p["text"].strip()
        if not stripped:
            continue
        if REFERENCES_HEADING_RE.match(stripped):
            failures.append(f'heading found: "{stripped}"')
        elif REFERENCES_DOWNGRADE_RE.search(stripped):
            failures.append(f'downgraded placeholder line found: "{stripped}"')
    return failures


def check_dates(paras):
    """Every paragraph with a tab and a year must end in an ASCII-hyphen date
    range with a start and an end (or 'present'). Bare years and en dashes can
    drop the date on ATS import."""
    failures = []
    for p in paras:
        t = p["text"]
        if "\t" in t and YEAR_RE.search(t) and not DATE_RANGE_RE.search(t):
            failures.append(f'date is not an ASCII-hyphen range with start and end: "{t.strip()}"')
    return failures


def check_email(paras):
    text = "\n".join(p["text"] for p in paras)
    return [] if EMAIL_RE.search(text) else ["no email address found as literal text"]


def skills_rows(paras):
    return [p["text"] for p in paras if p["section"] == "skills" and p["text"].strip()
            and p["text"].strip().lower() != SECTION_HEADINGS["skills"]]


def check_skills_duplicates(paras):
    seen, dupes = {}, []
    for row in skills_rows(paras):
        body = row.split(":", 1)[1] if ":" in row else row
        for item in body.split("·"):
            key = re.sub(r"\s+", " ", item).strip().lower()
            if not key:
                continue
            if key in seen:
                dupes.append(f'"{item.strip()}" appears more than once in the skills rows')
            seen[key] = True
    return dupes


def section_text(paras, key):
    return "\n".join(p["text"] for p in paras if p["section"] == key).lower()


def check_keywords(paras, keywords):
    """Returns (fails, warns, table_lines)."""
    fails, warns, table = [], [], []
    profile = section_text(paras, "profile")
    skills = section_text(paras, "skills")
    career = section_text(paras, "career")
    for kw in keywords:
        alts = [a.strip().lower() for a in kw.split("|") if a.strip()]

        def count(blob):
            return sum(len(re.findall(re.escape(a), blob)) for a in alts)

        counts = {"profile": count(profile), "skills": count(skills), "bullets": count(career)}
        where = [k for k, v in counts.items() if v]
        table.append(f'  {kw:<42} profile:{counts["profile"]}  skills:{counts["skills"]}  bullets:{counts["bullets"]}')
        if not where:
            fails.append(f'must-have "{kw}" appears nowhere')
        elif counts["bullets"] == 0:
            fails.append(f'must-have "{kw}" has no bullet evidence: add it to a bullet the master file supports, '
                         f'or drop it from the profile/skills (a skills keyword with no bullet behind it is a claim without proof)')
        elif counts["profile"] + counts["skills"] == 0:
            warns.append(f'must-have "{kw}" is only in bullets: add it to the profile or skills for ATS visibility')
    return fails, warns, table


def check_lengths(paras):
    warns = []
    for p in paras:
        if not p["bullet"]:
            continue
        n = len(p["text"].strip())
        if p["section"] == "career" and n > BULLET_WARN_CHARS:
            warns.append(f"{n} chars, may wrap to a third line: {p['text'].strip()[:70]}...")
        if p["section"] == "quals" and n > QUALS_WARN_CHARS:
            warns.append(f"{n} chars, Qualifications line may wrap: {p['text'].strip()[:70]}...")
    return warns


def load_keywords(args):
    kws = []
    if args.keywords:
        kws += [k.strip() for k in args.keywords.split(";") if k.strip()]
    if args.keywords_file:
        for line in Path(args.keywords_file).read_text(encoding="utf-8-sig").splitlines():
            if line.strip() and not line.strip().startswith("#"):
                kws.append(line.strip())
    return kws


def main():
    ap = argparse.ArgumentParser(description="Validate a tailored CV .docx against 05-formatting.md.")
    ap.add_argument("path", type=Path, help="Path to the .docx to validate")
    ap.add_argument("--keywords", help='JD must-haves the master file supports, ";"-separated ("|" for synonyms)')
    ap.add_argument("--keywords-file", help="Text file, one must-have per line (# comments allowed)")
    args = ap.parse_args()

    if not args.path.exists():
        print(f"FAIL: file not found: {args.path}")
        sys.exit(1)
    if args.path.suffix.lower() != ".docx":
        print(f"FAIL: expected a .docx, got: {args.path.suffix}")
        sys.exit(1)

    paras = extract_paragraphs(args.path)
    report, ok = [], True

    def gate(name, failures, ok_msg):
        nonlocal ok
        if failures:
            ok = False
            report.append(f"FAIL  {name}:\n  " + "\n  ".join(failures))
        else:
            report.append(f"PASS  {name}: {ok_msg}")

    gate("dash check", check_dashes(paras), "no em dashes or en dashes found")
    gate("references-section check", check_references_section(paras),
         "no References/Recommendations heading or placeholder found")

    creator, lmb = check_docx_author(args.path)
    author_problems = []
    if creator is None or creator.strip().lower() in GENERIC_AUTHOR_DEFAULTS or creator != EXPECTED_AUTHOR:
        author_problems.append(f'docx dc:creator is "{creator}", expected "{EXPECTED_AUTHOR}"')
    if lmb and lmb != EXPECTED_AUTHOR:
        author_problems.append(f'docx cp:lastModifiedBy is "{lmb}", expected "{EXPECTED_AUTHOR}"')
    gate("authenticity metadata check", author_problems, f'Author is "{EXPECTED_AUTHOR}"')

    gate("role-date check", check_dates(paras), "every role date is an ASCII-hyphen range with start and end")
    gate("email check", check_email(paras), "email present as literal text")
    gate("skills-duplicate check", check_skills_duplicates(paras), "no verbatim duplicate inside the skills rows")

    warns = check_lengths(paras)

    keywords = load_keywords(args)
    table = []
    if keywords:
        kfails, kwarns, table = check_keywords(paras, keywords)
        gate("must-have coverage", kfails, f"all {len(keywords)} must-haves appear")
        warns += kwarns
    else:
        report.append("SKIP  must-have coverage: no --keywords / --keywords-file given")

    print(f"\nvalidate_cv.py - {args.path.name}\n" + "=" * 60)
    for line in report:
        print(line)
    if table:
        print("\nMust-have counts (profile / skills / bullets):")
        print("\n".join(table))
    if warns:
        print("\nWARN:")
        for w in warns:
            print("  - " + w)
    print("=" * 60)
    print("Not checked here (use scripts/word_layout_check.ps1 or open the DOCX):")
    print("  - page count (cap 2), roles on page 1, role split across a page")
    print("  - bullet wraps, skills row balance, profile orphans")
    print("=" * 60)
    print("OVERALL: " + ("PASS" if ok else "FAIL") + (f" ({len(warns)} warning(s))" if warns else ""))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
