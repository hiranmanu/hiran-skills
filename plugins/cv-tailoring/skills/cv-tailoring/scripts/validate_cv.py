#!/usr/bin/env python3
"""
validate_cv.py — Automated Phase 5.3 format validation for the cv-tailoring skill.

Works directly against the rendered .docx's XML — no external tools
(LibreOffice, poppler) required, pure Python stdlib. Runs every
DOCX-checkable hard constraint from cv-formatting.md and prints a single
PASS/FAIL report.

Usage:
    python3 validate_cv.py <path-to.docx>

Exit code: 0 if every check passes, 1 if any check fails (so this can gate
a workflow, not just report).

What this deliberately does NOT check (needs a human, not this script —
see cv-formatting.md "Output Format" and the Validation Checklist in
SKILL.md): page count, bullet-wrap-to-second-line, and role-split-across-
a-page-break. Those depend on real pagination, and cv-formatting.md is
explicit that a LibreOffice-rendered PDF's pagination isn't trustworthy
(Carlito substitutes for Calibri, so line wraps/page breaks can disagree
with real Word) — that mismatch is literally how the 3-page/role-split
bug happened previously. An earlier version of this script shelled out to
soffice/pdftotext/pdfinfo to approximate these checks anyway; that
dependency wasn't installed on this machine, wasn't adding reliable
signal over a human glance at the real Word render, and left a stray
converted .pdf sitting next to the shipped .docx. Removed. If you want a
pagination gut-check, open the .docx in real Word (or export a PDF from
there) and look — that's the only render cv-formatting.md treats as
authoritative anyway.
"""

import argparse
import re
import sys
import zipfile
from pathlib import Path

EXPECTED_AUTHOR = "Hiran Patel"
GENERIC_AUTHOR_DEFAULTS = {"", "python-docx", "docx-js", "unknown", "libreoffice", "microsoft office user"}

DASH_CHARS = {"—": "em dash (—)", "–": "en dash (–)"}

REFERENCES_HEADING_RE = re.compile(r"^\s*(references|recommendations)\s*$", re.IGNORECASE)
REFERENCES_DOWNGRADE_RE = re.compile(r"available\s+(up\s*on|on)\s+request", re.IGNORECASE)

W_T_RE = re.compile(r"<w:t[^>]*>(.*?)</w:t>", re.DOTALL)
W_P_RE = re.compile(r"<w:p[ >].*?</w:p>", re.DOTALL)


def extract_paragraphs(docx_path: Path):
    """Returns a list of plain-text paragraphs from word/document.xml."""
    with zipfile.ZipFile(docx_path) as z:
        xml = z.read("word/document.xml").decode("utf-8")
    paragraphs = []
    for p_match in W_P_RE.finditer(xml):
        p_xml = p_match.group(0)
        text = "".join(W_T_RE.findall(p_xml))
        paragraphs.append(text)
    return paragraphs


def check_docx_author(docx_path: Path):
    """Returns (creator, last_modified_by) from docProps/core.xml."""
    with zipfile.ZipFile(docx_path) as z:
        core_xml = z.read("docProps/core.xml").decode("utf-8")
    creator_m = re.search(r"<dc:creator>(.*?)</dc:creator>", core_xml)
    lmb_m = re.search(r"<cp:lastModifiedBy>(.*?)</cp:lastModifiedBy>", core_xml)
    creator = creator_m.group(1).strip() if creator_m else None
    last_modified_by = lmb_m.group(1).strip() if lmb_m else None
    return creator, last_modified_by


def check_dashes(paragraphs):
    all_text = "\n".join(paragraphs)
    failures = []
    for ch, label in DASH_CHARS.items():
        count = all_text.count(ch)
        if count:
            sample_lines = [ln.strip() for ln in paragraphs if ch in ln][:5]
            failures.append(f"{count}x {label} found. Examples:\n    " + "\n    ".join(sample_lines))
    return failures


def check_references_section(paragraphs):
    """Flags a References/Recommendations heading, or a downgraded
    'available on request' placeholder line, anywhere in the document —
    both are banned per cv-formatting.md, not just the heading form."""
    failures = []
    for line in paragraphs:
        stripped = line.strip()
        if not stripped:
            continue
        if REFERENCES_HEADING_RE.match(stripped):
            failures.append(f'heading found: "{stripped}"')
        elif REFERENCES_DOWNGRADE_RE.search(stripped):
            failures.append(f'downgraded placeholder line found: "{stripped}"')
    return failures


def main():
    ap = argparse.ArgumentParser(description="Validate a tailored CV .docx against cv-formatting.md's DOCX-checkable hard constraints.")
    ap.add_argument("path", type=Path, help="Path to the .docx to validate")
    args = ap.parse_args()

    if not args.path.exists():
        print(f"FAIL: file not found: {args.path}")
        sys.exit(1)
    if args.path.suffix.lower() != ".docx":
        print(f"FAIL: expected a .docx, got: {args.path.suffix}")
        sys.exit(1)

    paragraphs = extract_paragraphs(args.path)

    report = []
    ok = True

    # Check 1: em/en dashes
    dash_failures = check_dashes(paragraphs)
    if dash_failures:
        ok = False
        report.append("FAIL  dash check:\n  " + "\n  ".join(dash_failures))
    else:
        report.append("PASS  dash check: no em dashes or en dashes found")

    # Check 2: References/Recommendations section removed
    references_failures = check_references_section(paragraphs)
    if references_failures:
        ok = False
        report.append("FAIL  references-section check:\n  " + "\n  ".join(references_failures))
    else:
        report.append("PASS  references-section check: no References/Recommendations heading or placeholder found")

    # Check 3: authenticity metadata (Author)
    docx_creator, docx_lmb = check_docx_author(args.path)
    author_problems = []
    if docx_creator is None or docx_creator.strip().lower() in GENERIC_AUTHOR_DEFAULTS or docx_creator != EXPECTED_AUTHOR:
        author_problems.append(f'docx dc:creator is "{docx_creator}", expected "{EXPECTED_AUTHOR}"')
    if docx_lmb and docx_lmb != EXPECTED_AUTHOR:
        author_problems.append(f'docx cp:lastModifiedBy is "{docx_lmb}", expected "{EXPECTED_AUTHOR}"')
    if author_problems:
        ok = False
        report.append("FAIL  authenticity metadata check:\n  " + "\n  ".join(author_problems))
    else:
        report.append(f'PASS  authenticity metadata check: Author is "{EXPECTED_AUTHOR}"')

    print(f"\nvalidate_cv.py — {args.path.name}\n" + "=" * 60)
    for line in report:
        print(line)
    print("=" * 60)
    print("Not checked here (verify manually against a real Word render):")
    print("  - page count (cap: 2)")
    print("  - bullet wraps to a second line")
    print("  - a role split across a page boundary")
    print("=" * 60)
    print("OVERALL: " + ("PASS" if ok else "FAIL"))

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
