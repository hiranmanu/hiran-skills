# Applications tracker (Phase 6)

A single workbook, `Hiran_Applications_Tracker.xlsx`, that this skill
appends to every time it completes a tailoring run. Lives wherever the
user's `resumes/` library lives — same working directory — so it travels
with the library rather than being recreated per session.

## Schema (sheet: "Applications")

| Column | Notes |
|---|---|
| Date Applied | Date the user confirms they've actually submitted — not the date the CV was generated, if different. Ask if unclear. |
| Company | Matches the filename convention's company name. |
| Role Title | As stated in the JD. |
| CV Variant | Which of the three base templates was used (see `formatting-rules.md`). |
| JD Source | URL if pasted as a link, else "Pasted text". |
| ATS Score – Before | From Phase 3. |
| ATS Score – After | From Phase 5. |
| CV File Used | The exact filename generated. |
| Status | Applied / Screening / Interview / Offer / Rejected / Withdrawn — this user updates it manually after the fact; the skill only ever writes "Applied" on the row it creates. |
| Next Action | Free text, optional. |
| Notes | Free text, optional. |

## Update logic

1. If `Hiran_Applications_Tracker.xlsx` doesn't exist yet, create it with
   the xlsx skill: header row bold, one legend note in a cell above the
   table explaining the Status column's allowed values, and one clearly-
   marked example row ("EXAMPLE — delete me") showing realistic formatting.
   Add a small summary block (Total applications, count by Status) using
   `COUNTA`/`COUNTIF` — real formulas, not hardcoded numbers — and run
   `recalc.py` before handing it over.
2. If it exists, open it, append one new row at the bottom of the
   Applications table (don't touch existing rows or the summary formulas),
   and re-run `recalc.py` so the summary block picks up the new row.
3. Never overwrite a user-edited Status cell — this skill only ever adds
   new rows, never edits existing ones.

## What this deliberately doesn't do

No cross-tool sync (Google Sheets, Notion, etc.) — this user has said
elsewhere he prefers no multi-tool integrations for this kind of thing, so
the workbook stays a local file he can move himself if he wants it
somewhere else.
