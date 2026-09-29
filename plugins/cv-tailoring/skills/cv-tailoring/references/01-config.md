# 01 - Configuration

Owned by **step 01 (Intake)** in `SKILL.md`. Paths and fixed defaults only; workflow
logic lives in `SKILL.md`, formatting rules in `05-formatting.md`. Update this file
once and reference it everywhere.

## File numbering

Reference files are numbered by the workflow step that owns them. Steps 02, 06
and 08 live entirely in `SKILL.md`, so there is no `02-`, `06-` or `08-` file.

| File | Owning step | Purpose |
|---|---|---|
| `01-config.md` | 01 Intake | Paths, output folder, defaults (this file) |
| `03-background.md` | 03 Gap Check | **Master fact source**: bullet bank, confirmed facts, template selection, title blending. Write target for confirmed facts |
| `04-scoring.md` | 04 Score | ATS method plus cluster data |
| `05-formatting.md` | 05 Draft, 07 Validate | Layout, voice, profile/skills/bullet rules, validation checklist |

Scripts (`scripts/`, step 07): `build_cv_reference.js` (render), `validate_cv.py`
(automated checks), `word_layout_check.ps1` (page count, role splits, via Word).

## Output configuration

All generated CVs are saved locally. Nothing is uploaded anywhere. Fixed folder;
don't pick a different location per session.

| Setting | Value | Notes |
|---|---|---|
| Output base path | `C:\Users\hiran\Downloads\claude code\cv-tailoring\CV Output\` | Inside the repo folder but gitignored: never commit generated CVs |
| Folder naming | `{YYYY.MM.DD}_{Company}_{Role}\` | Example: `2026.09.14_TalentInternational_ProductDirector\` |
| File naming (DOCX only) | `Hiran_CV_{YYYY.MM.DD}_{Company}_{BriefRole}.docx` | Example: `Hiran_CV_2026.09.19_Citi_PMGenAI.docx`. Full rules in `05-formatting.md` "Output Format" |

There is no applications tracker. Track applications outside this skill.

## Archived source CVs

`C:\Users\hiran\Downloads\claude code\cv-tailoring\Source CVs\` holds
`Hiran_Patel_CV_2Page.pdf` and `Hiran_Patel_CV_2Page_Data_Architect.pdf`
(gitignored). **The workflow no longer reads them**: their content lives in
`03-background.md` Section 1. Keep them as an archive; if one and the bank ever
disagree, the bank wins.

## Requirements

| Needed for | What |
|---|---|
| Render (step 07) | Node.js and the `docx` npm package. Copy `scripts/build_cv_reference.js` (and `scripts/package.json`) into a **scratch folder**, not the plugin folder, run `npm install` there once, then `node build_<company>.js` |
| `validate_cv.py` | Python 3, standard library only |
| `word_layout_check.ps1` | Windows and Microsoft Word (exit code 2 = Word unavailable, check by eye) |
| Review (step 06) | An Agent tool for the fresh-context reviewer; without one, run the rubric as a separate pass yourself |

## Template selection

```
What is the target role type?
├─ Product Director, VP of Product, CPO, Head of Product, Senior Product Manager
│  └─ PRODUCT_CV
├─ Data Architect, Data Engineer, Analytics Engineer, Data Scientist, ML Engineer
│  └─ DATA_ARCHITECT_CV
├─ Solution Architect, Enterprise Architect
│  └─ Not yet templated: ask whether to build the variant now or hold off
└─ Other
   └─ Ask which template to use
```

Details (titles, emphasis, LinkedIn rule) are in `03-background.md` Section 2.

## Defaults

| Parameter | Default |
|---|---|
| ATS target score | 85%+ (aim 90%+ for complex JDs) |
| Review loops | 2 max, then ship with notes |
| Recommendations / References section | Never included |
| Blended titles | Max 1-2 per CV (rules in `03-background.md` Section 4) |
| LinkedIn URL | Product roles only: `https://www.linkedin.com/in/hiran-patel/` (this file is the source of truth for the URL) |
| Pages | Hard cap 2; most recent 3-4 roles on page 1 |

## File modification notes

- Last updated: 2026-09-29 (v2.0.0).
- When adding a template, update this file first.
- When changing the output path, update this file and `SKILL.md` step 07.
- When adding a cluster, update `04-scoring.md` Part 2.
