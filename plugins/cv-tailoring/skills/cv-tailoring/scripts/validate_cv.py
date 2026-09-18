#!/usr/bin/env python3
"""
validate_cv.py — Automated Phase 5.3 format validation for the cv-tailoring skill.

Replaces the manual "run soffice, run pdftoppm, eyeball it, grep it" sequence
previously described only in prose in cv-decision-gates.md §5.3. Takes a
rendered CV (.docx or .pdf) and runs every hard-constraint check from
cv-formatting.md automatically, printing a single PASS/FAIL report.

Requires: soffice (LibreOffice), pdftotext + pdfinfo (poppler-utils) — the
same tools the docx skill's own verify step already uses.

Usage:
    python3 validate_cv.py <path-to.docx-or-.pdf> [--max-pages 2]

Exit code: 0 if every check passes, 1 if any check fails (so this can gate
a workflow, not just report).

Known limitations (see cv-formatting.md "Known gaps" for the fuller list):
  - Bullet-wrap and role-page-split detection are heuristics over
    `pdftotext -layout` output, not a true layout engine. They work well
    for this skill's bullet-glyph + role-header-with-date-range structure,
    but a very unusual layout could confuse them. Always still glance at
    the rendered page images for anything the report flags as uncertain.
  - Character-budget guidance in cv-formatting.md is a pre-writing aid;
    this script checks the actual render, which is the real source of truth.
"""

import argparse
import re
import subprocess
import sys
import zipfile
from pathlib import Path

EXPECTED_AUTHOR = "Hiran Patel"
GENERIC_AUTHOR_DEFAULTS = {"", "python-docx", "docx-js", "unknown", "libreoffice", "microsoft office user"}

BULLET_GLYPHS = ["\u2022", "\u25AA", "\u25A0", "\u25CB", "\u2023", "-", "\u25E6"]
DASH_CHARS = {"\u2014": "em dash (—)", "\u2013": "en dash (–)"}
DATE_RANGE_RE = re.compile(
    r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s*\d{4}"
    r"\s*[-\u2013\u2014]\s*"
    r"((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s*\d{4}|[Pp]resent)"
)
SECTION_HEADING_HINTS = [
    "profile", "key skills", "competencies", "career", "achievements",
    "qualifications", "certifications", "personal details", "earlier career",
]


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def to_pdf(input_path: Path, workdir: Path) -> Path:
    if input_path.suffix.lower() == ".pdf":
        return input_path
    soffice_candidates = ["soffice", "libreoffice"]
    last_err = None
    for exe in soffice_candidates:
        r = run([exe, "--headless", "--convert-to", "pdf", "--outdir", str(workdir), str(input_path)])
        if r.returncode == 0:
            pdf_path = workdir / (input_path.stem + ".pdf")
            if pdf_path.exists():
                return pdf_path
        last_err = r.stderr
    raise RuntimeError(f"Could not convert {input_path} to PDF via soffice/libreoffice.\n{last_err}")


def page_count(pdf_path: Path) -> int:
    r = run(["pdfinfo", str(pdf_path)])
    m = re.search(r"^Pages:\s+(\d+)", r.stdout, re.MULTILINE)
    if not m:
        raise RuntimeError(f"Could not read page count from pdfinfo output:\n{r.stdout}\n{r.stderr}")
    return int(m.group(1))


def extract_pages(pdf_path: Path):
    """Returns a list of per-page text blocks using pdftotext's form-feed page breaks."""
    r = run(["pdftotext", "-layout", str(pdf_path), "-"])
    if r.returncode != 0:
        raise RuntimeError(f"pdftotext failed:\n{r.stderr}")
    pages = r.stdout.split("\x0c")
    # pdftotext often emits a trailing empty page after the last form feed
    while pages and not pages[-1].strip():
        pages.pop()
    return pages


def check_docx_author(docx_path: Path):
    """Returns (creator, last_modified_by) from docProps/core.xml, or (None, None) if not a docx."""
    if docx_path.suffix.lower() != ".docx":
        return None, None
    try:
        with zipfile.ZipFile(docx_path) as z:
            core_xml = z.read("docProps/core.xml").decode("utf-8")
    except (KeyError, zipfile.BadZipFile):
        return None, None
    creator_m = re.search(r"<dc:creator>(.*?)</dc:creator>", core_xml)
    lmb_m = re.search(r"<cp:lastModifiedBy>(.*?)</cp:lastModifiedBy>", core_xml)
    creator = creator_m.group(1).strip() if creator_m else None
    last_modified_by = lmb_m.group(1).strip() if lmb_m else None
    return creator, last_modified_by


def check_pdf_author(pdf_path: Path):
    r = run(["pdfinfo", str(pdf_path)])
    m = re.search(r"^Author:\s+(.*)$", r.stdout, re.MULTILINE)
    return m.group(1).strip() if m else None


REFERENCES_HEADING_RE = re.compile(r"^\s*(references|recommendations)\s*$", re.IGNORECASE)
REFERENCES_DOWNGRADE_RE = re.compile(r"available\s+(up\s*on|on)\s+request", re.IGNORECASE)


def check_references_section(all_text: str):
    """Flags a References/Recommendations heading, or a downgraded
    'available on request' placeholder line, anywhere in the document —
    both are banned per cv-formatting.md, not just the heading form."""
    failures = []
    for line in all_text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if REFERENCES_HEADING_RE.match(stripped):
            failures.append(f'heading found: "{stripped}"')
        elif REFERENCES_DOWNGRADE_RE.search(stripped):
            failures.append(f'downgraded placeholder line found: "{stripped}"')
    return failures


def check_dashes(all_text: str):
    failures = []
    for ch, label in DASH_CHARS.items():
        count = all_text.count(ch)
        if count:
            sample_lines = [ln.strip() for ln in all_text.splitlines() if ch in ln][:5]
            failures.append(f"{count}x {label} found. Examples:\n    " + "\n    ".join(sample_lines))
    return failures


def looks_like_role_or_heading(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return True
    if DATE_RANGE_RE.search(stripped):
        return True
    lowered = stripped.lower()
    if any(h in lowered for h in SECTION_HEADING_HINTS):
        return True
    # Italic company/descriptor lines typically contain ", UK:" / ", USA:" style descriptors
    if re.search(r",\s*(UK|USA|US)[,:]", stripped):
        return True
    return False


def check_bullet_wraps(pages):
    """
    Heuristic: within each page's text, a bulleted line is one that starts
    with a bullet glyph. A wrap is a non-empty line that (a) doesn't start
    with a bullet glyph, (b) isn't a role/heading/date line, and (c) directly
    follows a line that either started a bullet or was itself flagged as a
    continuation (so a 3-line wrap still gets caught, not just 2-line).
    """
    issues = []
    for page_num, page_text in enumerate(pages, start=1):
        lines = page_text.splitlines()
        prev_was_bullet_or_continuation = False
        for i, line in enumerate(lines):
            stripped = line.strip()
            if not stripped:
                prev_was_bullet_or_continuation = False
                continue
            starts_with_bullet = any(stripped.startswith(g) for g in BULLET_GLYPHS)
            if starts_with_bullet:
                prev_was_bullet_or_continuation = True
                continue
            if prev_was_bullet_or_continuation and not looks_like_role_or_heading(stripped):
                issues.append(
                    f"page {page_num}, line {i + 1}: suspected bullet-wrap continuation: \"{stripped[:90]}\""
                )
                prev_was_bullet_or_continuation = True  # allow catching a 3rd wrapped line
            else:
                prev_was_bullet_or_continuation = False
    return issues


def check_role_page_splits(pages):
    """
    Heuristic: find lines that look like a role-header (contain a date range).
    For each such role, everything until the next role-header or section
    heading should be on the same page. If a bullet glyph line for that role
    appears on a *different* page than its role-header line, flag a split.
    """
    issues = []
    current_role = None
    current_role_page = None
    for page_num, page_text in enumerate(pages, start=1):
        for line in page_text.splitlines():
            stripped = line.strip()
            if not stripped:
                continue
            if DATE_RANGE_RE.search(stripped):
                current_role = stripped[:70]
                current_role_page = page_num
                continue
            lowered = stripped.lower()
            if any(h in lowered for h in SECTION_HEADING_HINTS):
                current_role = None
                current_role_page = None
                continue
            starts_with_bullet = any(stripped.startswith(g) for g in BULLET_GLYPHS)
            if starts_with_bullet and current_role is not None and page_num != current_role_page:
                issues.append(
                    f"role starting \"{current_role}\" (header on page {current_role_page}) "
                    f"has a bullet on page {page_num}: \"{stripped[:70]}\""
                )
    return issues


def main():
    ap = argparse.ArgumentParser(description="Validate a tailored CV render against cv-formatting.md hard constraints.")
    ap.add_argument("path", type=Path, help="Path to the .docx or .pdf to validate")
    ap.add_argument("--max-pages", type=int, default=2, help="Hard cap on page count (default: 2)")
    args = ap.parse_args()

    if not args.path.exists():
        print(f"FAIL: file not found: {args.path}")
        sys.exit(1)

    workdir = args.path.parent
    pdf_path = to_pdf(args.path, workdir)
    pages = extract_pages(pdf_path)
    all_text = "\n".join(pages)
    n_pages = page_count(pdf_path)

    report = []
    ok = True

    # Check 1: page count
    if n_pages > args.max_pages:
        ok = False
        report.append(f"FAIL  page count: {n_pages} pages (max {args.max_pages})")
    else:
        report.append(f"PASS  page count: {n_pages} page(s), within max {args.max_pages}")

    # Check 2: em/en dashes
    dash_failures = check_dashes(all_text)
    if dash_failures:
        ok = False
        report.append("FAIL  dash check:\n  " + "\n  ".join(dash_failures))
    else:
        report.append("PASS  dash check: no em dashes or en dashes found")

    # Check 3: bullet wraps
    wrap_issues = check_bullet_wraps(pages)
    if wrap_issues:
        ok = False
        report.append("FAIL  bullet-wrap check:\n  " + "\n  ".join(wrap_issues))
    else:
        report.append("PASS  bullet-wrap check: no suspected wrapped bullets")

    # Check 4: role page-splits
    split_issues = check_role_page_splits(pages)
    if split_issues:
        ok = False
        report.append("FAIL  role-page-split check:\n  " + "\n  ".join(split_issues))
    else:
        report.append("PASS  role-page-split check: no role appears split across a page boundary")

    # Check 5: References/Recommendations section removed
    references_failures = check_references_section(all_text)
    if references_failures:
        ok = False
        report.append("FAIL  references-section check:\n  " + "\n  ".join(references_failures))
    else:
        report.append("PASS  references-section check: no References/Recommendations heading or placeholder found")

    # Check 6: authenticity metadata (Author)
    docx_creator, docx_lmb = check_docx_author(args.path)
    pdf_author = check_pdf_author(pdf_path)
    author_problems = []
    if docx_creator is not None:
        if docx_creator.strip().lower() in GENERIC_AUTHOR_DEFAULTS or docx_creator != EXPECTED_AUTHOR:
            author_problems.append(f'docx dc:creator is "{docx_creator}", expected "{EXPECTED_AUTHOR}"')
        if docx_lmb and docx_lmb != EXPECTED_AUTHOR:
            author_problems.append(f'docx cp:lastModifiedBy is "{docx_lmb}", expected "{EXPECTED_AUTHOR}"')
    if pdf_author is not None and (not pdf_author or pdf_author.strip().lower() in GENERIC_AUTHOR_DEFAULTS or pdf_author != EXPECTED_AUTHOR):
        author_problems.append(f'PDF Author is "{pdf_author}", expected "{EXPECTED_AUTHOR}"')
    if author_problems:
        ok = False
        report.append("FAIL  authenticity metadata check:\n  " + "\n  ".join(author_problems))
    else:
        report.append(f'PASS  authenticity metadata check: Author is "{EXPECTED_AUTHOR}"')

    print(f"\nvalidate_cv.py — {args.path.name}\n" + "=" * 60)
    for line in report:
        print(line)
    print("=" * 60)
    print("OVERALL: " + ("PASS" if ok else "FAIL"))

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
