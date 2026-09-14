# Generation and QA (Phase 4 + Phase 5)

Use the `docx` skill for creation — don't reinvent document generation
here. This file covers what's specific to CVs on top of that skill's normal
guidance.

## Preventing line-wrap, not just catching it

Bullets that wrap to a second line are the #1 repeated complaint across
prior sessions. Catching it after export is too late to feel reliable —
budget the character count *while writing* each bullet:

- At Calibri 10.5pt on a US Letter page with ~1" margins and a ~6.5" text
  width, a plain (non-indented) full-width line holds roughly **95-105
  characters** including spaces and punctuation. A bulleted line (with the
  bullet glyph and its indent) holds roughly **90-100**.
- Aptos 11pt is slightly wider per character — budget closer to **85-95**
  for a bulleted line.
- Treat 90 characters as the safe target for any bullet regardless of which
  font ends up selected, and only push toward the upper end of the range
  once the exact font/size for this document is confirmed.
- When a bullet's content genuinely doesn't fit in budget, cut a weaker
  clause rather than shrinking font size or margins to force it — those are
  layout constraints from `formatting-rules.md`, not available levers.

This is a proactive budget, not a guarantee — always still verify per the
QA step below, since actual rendering also depends on kerning and any bold
runs (company names, metrics) which render wider than plain text.

## Filename convention

`{FirstName}_{LastName}_{Company}_CV.docx` and matching `.pdf`, both
underscore-joined, no spaces, company name taken from the JD/company
research in Phase 1 (not the JD's internal req ID or team name — the
company itself).

- Strip Inc./Ltd./plc-type suffixes unless the user's own past filenames
  kept them.
- Multiple roles at the same company in one session: append the role's
  key differentiator, e.g. `..._Google_CV_CloudTPM.docx`, so files don't
  silently overwrite each other.
- Multi-word companies: PascalCase or keep spaces as underscores
  consistently within a session — don't mix conventions across a batch.

## QA sequence (run every time, in order)

1. **Render and look at it.** Per the `docx` skill's verify step:
   ```
   python scripts/office/soffice.py --headless --convert-to pdf output.docx
   pdftoppm -jpeg -r 100 output.pdf page
   ```
   Read the resulting page image(s). Confirm: no bullet wraps to a second
   line, the skills line is still a single flowing line (not reverted to a
   grid), and nothing overflows onto an unwanted second page.
2. **ATS text-extraction check.** `pdftotext -layout output.pdf -` and read
   it back. It should come back as clean, ordered, readable text in the
   same sequence as the visual document — if it comes back garbled,
   reordered, or with dropped sections, something in the layout (a table, a
   text box, a multi-column section) is going to confuse a real ATS parser
   too. Fix the layout, don't just accept the garbled extraction.
3. Only after both checks pass: report the after-score (see
   `scoring.md`) and hand the files to the user.

## Metadata

Set DOCX/PDF core properties (Author, Company/Manager) to the user's own
name — not left as a generic tool default — before handing the files over.
