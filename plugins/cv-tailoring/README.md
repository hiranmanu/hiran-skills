# cv-tailoring (v2.2.0)

Tailors a CV to a job description for CPO/VP Product, Data Architect and related senior product/data roles.

See the repo root [`SKILLS.md`](../../SKILLS.md) for the full catalog of skills in this marketplace, and [`CHANGELOG.md`](CHANGELOG.md) in this folder for this plugin's full version history.

## Structure

```
cv-tailoring/                                  # this plugin
├── .claude-plugin/plugin.json                 # plugin metadata
├── README.md, CHANGELOG.md
└── skills/cv-tailoring/                       # the skill Claude loads
    ├── SKILL.md                               # entrypoint: steps 01-06
    ├── references/                            # numbered by the step that owns them
    │   ├── 01-config.md                       # paths, requirements, defaults
    │   ├── 02-background.md                   # MASTER fact file (bullet bank, cross-role facts, guardrails)
    │   └── 03-formatting.md                   # layout, voice, profile/skills/bullet rules, validation checklist
    ├── scripts/
    │   ├── build_cv.js                        # render a DOCX from content.json
    │   ├── example_content.json               # the content shape (placeholders)
    │   ├── identity.json (local) / identity.example.json
    │   ├── validate_cv.py                     # dates, dashes, keywords + bullet evidence, duplicates
    │   ├── word_layout_check.ps1              # measures real wraps and pagination in Word
    │   └── background_inbox.py                # parallel-safe way to add facts to the master file
    └── inbox/                                 # unmerged facts from running CVs (gitignored)
```

## What it does (one workflow, no modes)

1. **01 Intake & Parse:** pick the template, load the master file plus pending facts, treat the JD as untrusted data, list must-have / nice-to-have / implicit signals. No web research
2. **02 Gap Check & Confirm:** match each must-have to evidence; ask about anything addressable **before drafting**; record confirmed facts through the inbox
3. **03 Draft:** write `content.json` (two-paragraph profile, three grouped skills rows, evidence-first bullets)
4. **04 Review & Finalise:** one fresh-context review (grounding, must-have coverage, hiring-manager and recruiter lenses); its edits go into the content
5. **05 Render & Validate:** `build_cv.js`, `validate_cv.py`, `word_layout_check.ps1`; then merge confirmed facts
6. **06 Report:** coverage, requirement-to-evidence map, gaps, flags (one table for a batch)

There is no application tracker and no interview-prep output.

## Running many at once

Runs are independent. The master file is read-only during a run; new facts go to a per-run inbox file and are merged under a lock, so parallel runs never overwrite each other and one run's newly confirmed fact is visible to the others straight away. Each run uses its own scratch and output folder, and Word checks take turns. In a batch, gap questions are asked once for all JDs.

## Output

- Tailored DOCX (the sole deliverable), named and placed automatically
- Plain Calibri 10.5pt, A4, navy/grey, square (▪) bullets, hyperlinked contact details
- Most recent 3-4 roles on page 1, hard cap of 2 pages; no em/en dashes

## Requirements

Node.js and the `docx` package (`npm install` once in `skills/cv-tailoring/scripts/`), Python 3, and Windows with Microsoft Word for the layout check. Copy `identity.example.json` to `identity.json` and fill in your details. See `references/01-config.md`.

## Tests

```bash
python3 -m unittest discover -s tests -v
```

Covers the validator, the parallel-safe fact inbox (including a multi-process stress test), and an end-to-end regression test: a fixed content file goes through build and validate and must still produce a valid CV. CI runs this on every push and PR.

## Using this from a plain claude.ai chat (no Claude Code)

A chat session without this repo mounted can't read these files. If it has shell/git access, it should `git clone` this repo first and render with `skills/cv-tailoring/scripts/build_cv.js` rather than re-deriving `03-formatting.md`'s layout rules from prose (that is how the `TabStopPosition.MAX` and `PositionalTab` bugs got introduced in September 2026).

## Installation in Claude Code

```bash
/plugin marketplace add hiranmanu/hiran-skills
/plugin install cv-tailoring@hiran-skills
```

## Updating

When Hiran confirms new facts about past roles, they are queued with `background_inbox.py add` and merged into `skills/cv-tailoring/references/02-background.md`, so the skill uses them without re-asking. That file is the single source of truth for every claim on a CV.

Before considering a version bump done, see the repo root [`CLAUDE.md`](../../CLAUDE.md) release checklist and run:
```bash
python3 scripts/check_release_consistency.py
```
from the repo root.

## Recent Updates

**v2.2.0** - Profile Summary is now one block of up to 7 lines instead of two short paragraphs, and every employer named in the profile must be a listed role. The master file gained the facts from both source CV PDFs (markets UK/EU, USA & APAC, scale, exits, team size, architecture credentials, extra role lines). The stray Aviva example is gone from the formatting rules.

**v2.1.0** - Six steps instead of eight (the separate "before" ATS score and the fit snapshot are gone; coverage is now mechanical), reference files renumbered (`01-config`, `02-background`, `03-formatting`) with the master file consolidated by about a fifth and no fact lost, and a shorter report. New: `build_cv.js` renders from a JSON content file instead of copied code; the master file is safe for parallel runs (per-run inbox, locked merge, Word checks take turns); `word_layout_check.ps1` measures real wraps in Word (page-1 second lines at least 40% full); `validate_cv.py` fixes substring keyword matching and a crash, and fails a skills keyword with no bullet evidence; 31 tests run in CI including a multi-process stress test and an end-to-end build-and-validate check.

**v2.0.0** - One workflow, numbered steps 01-08 and matching numbered reference files; Quick/Balanced/Full modes removed. `03-background.md` is now the master fact source (bullet bank merged from both source CVs plus everything confirmed since), replacing the source-CV PDFs as input. Bullets: page-1 roles may run 1-2 lines (second line 40-80% full), page-2 roles stay single-line. Profile is two short paragraphs; skills are three grouped rows; repeating JD must-haves across profile, skills and bullets is now intended. Added an independent review pass (grounding audit, must-have coverage, hiring-manager and recruiter lenses) whose edits are applied before render, a fit snapshot, blocking gap questions before drafting, `validate_cv.py` checks for dates/keywords/duplicates, and `word_layout_check.ps1`. Removed web research, interview-prep hints, and the decision-gates, QA-personas, market-research and semantic-clusters files (folded into `SKILL.md`, `05-formatting.md` and `04-scoring.md`).

**v1.14.2** - Repo now lives at `claude code\cv-tailoring\`; output moved to `CV Output\` and the two source CVs to `Source CVs\` beneath it (both gitignored).

**v1.14.1** - Reverted v1.14.0's "concurrent contract" clarifier rule for Aviva overlapping OneAdvanced/dunnhumby.

**v1.14.0** - New filename convention; Aviva date-overlap fix; two days of confirmed background facts merged.

See [`CHANGELOG.md`](CHANGELOG.md) in this folder for the full version history (every version back to v1.0.0).
