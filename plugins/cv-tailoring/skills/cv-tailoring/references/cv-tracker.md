# Applications tracker (Phase 7)

A Google Sheets tab named "Applications", inside the `Interviews CV` GDrive
folder (see `cv-config.md` for the folder ID and Sheet ID), that this skill
appends to every time it completes a tailoring run.

**Note on history:** an earlier version of this skill tracked applications
in a local `Hiran_Applications_Tracker.xlsx` file with no cross-tool sync.
That changed with the move to GDrive-based output storage (Phase 4) — the
tracker moved with it so both live in the same place. If you've reverted to
a local workbook since, this file is the one that's now out of date, not
`cv-config.md` / `cv-tailoring.md`.

## Schema (sheet: "Applications")

| Column | Notes |
|---|---|
| Date Applied | Date the user confirms they've actually submitted — not the date the CV was generated, if different. Ask if unclear. |
| Company | Matches the filename convention's company name. |
| Role Title | As stated in the JD. |
| CV Variant | PRODUCT_CV or DATA_ARCHITECT_CV (see `cv-background.md` §1). |
| JD Source | URL if pasted as a link, else "Pasted text". |
| ATS Score – Before | From Phase 3. |
| ATS Score – After | From Phase 3 (after tailoring). |
| CV File Used | Link to the GDrive folder from Phase 4. |
| Status | Applied / Screening / Interview / Offer / Rejected / Withdrawn — this user updates it manually after the fact; the skill only ever writes "Applied" on the row it creates. |
| Next Action | Free text, optional. |
| Notes | Free text — gaps, differentiators, prep hints from the Phase 6 summary. |

## Update logic

1. Append one new row at the bottom of the Applications table — don't touch
   existing rows.
2. Never overwrite a user-edited Status cell — this skill only ever adds
   new rows, never edits existing ones.
3. Before logging, always ask for confirmation (see `cv-tailoring.md`
   Phase 7) — don't log silently.

## Multiple applications to same company/role

See `cv-decision-gates.md` "Multiple Applications to Same Company" for the
reapplication vs. new-row logic.
