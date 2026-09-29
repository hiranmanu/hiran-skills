# 01 - Configuration

Owned by **step 01 (Intake & Parse)** in `SKILL.md`. Paths, requirements and fixed
defaults only; workflow logic lives in `SKILL.md`, format rules in `03-formatting.md`.

## Files

Reference files are numbered by the workflow step that owns them; steps 04-06 need no
reference file beyond `03-formatting.md`.

| File | Owning step | Purpose |
|---|---|---|
| `01-config.md` | 01 | Paths, requirements, defaults (this file) |
| `02-background.md` | 02 | **Master fact file**: bullet bank, cross-role facts and guardrails, absences, template selection, title blending. Read-only during a run; updated through the inbox |
| `03-formatting.md` | 03, 05 | Layout, voice, profile/skills/bullet rules, validation checklist |

Scripts (`scripts/`): `build_cv.js` (render from JSON), `validate_cv.py`,
`word_layout_check.ps1`, `background_inbox.py`; `example_content.json` (the content
shape), `identity.json` (your details, gitignored) and `identity.example.json`.
`inbox/` holds facts confirmed by runs that haven't been merged yet (gitignored).

## Output

All CVs are saved locally; nothing is uploaded. The folder and filename are derived by
`build_cv.js` from `content.meta` and `identity.json`:

| Setting | Value |
|---|---|
| Output base | `identity.json` `output_base`: `C:/Users/hiran/Downloads/claude code/cv-tailoring/CV Output` (gitignored) |
| Folder | `{YYYY.MM.DD}_{Company}_{Role}\` |
| File (DOCX only) | `Hiran_CV_{YYYY.MM.DD}_{Company}_{BriefRole}.docx` |

There is no applications tracker: track applications outside this skill.

## Identity

Name, contact details, LinkedIn URL, languages, nationality and the output base live in
`scripts/identity.json` (local, gitignored). Copy `identity.example.json` to create it on
a new machine. LinkedIn URL for Product roles: `https://www.linkedin.com/in/hiran-patel/`
(this is the source of truth; the DATA_ARCHITECT template omits it).

## Requirements

| Needed for | What |
|---|---|
| Render (step 05) | Node.js and the `docx` package: run `npm install` once in `scripts/` |
| Validation | Python 3, standard library only |
| Layout check | Windows and Microsoft Word (installed on this machine). Exit code 2 = Word unavailable, check by eye |
| Review (step 04) | Self-review by default; an Agent tool only for the optional independent reviewer |

## Archived source CVs

`Source CVs\` (gitignored) holds the two original PDFs. The workflow no longer reads
them: their content lives in `02-background.md` Section 1, which wins if they disagree.

## Defaults

| Parameter | Default |
|---|---|
| Review loops | 2 max, then ship with notes |
| Recommendations / References section | Never included |
| Blended titles | Max 1-2 per CV (rules in `02-background.md` Section 5) |
| LinkedIn URL | Product roles only |
| Pages | Hard cap 2; most recent 3-4 roles on page 1 |

## Modification notes

Last updated 2026-09-29 (v2.2.0). Changing the output path means editing `identity.json`.
