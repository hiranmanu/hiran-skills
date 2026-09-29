# cv-tailoring (v2.0.1)

Tailors a CV to a job description for CPO/VP Product, Data Architect, Solution/Enterprise Architect, and related senior product/data roles.

See the repo root [`SKILLS.md`](../../SKILLS.md) for the full catalog of skills in this marketplace, and [`CHANGELOG.md`](CHANGELOG.md) in this folder for this plugin's full version history.

## Structure

```
cv-tailoring/                                  # this plugin
├── .claude-plugin/
│   └── plugin.json                            # plugin metadata
├── README.md                                  # this file
├── CHANGELOG.md                               # full version history for this plugin
└── skills/
    └── cv-tailoring/                          # the actual skill Claude loads
        ├── SKILL.md                           # entrypoint: steps 01-08 (02, 06, 08 live here)
        ├── scripts/                           # step 07
        │   ├── build_cv_reference.js          # reference docx-js house-style implementation
        │   ├── validate_cv.py                 # automated checks (dates, dashes, keywords, duplicates)
        │   └── word_layout_check.ps1          # page count, roles on page 1, role splits (needs Word)
        └── references/                        # numbered by the step that owns them
            ├── 01-config.md                   # paths, output folder, defaults
            ├── 03-background.md               # MASTER fact source: bullet bank, confirmed facts, titles
            ├── 04-scoring.md                  # ATS method + cluster data
            └── 05-formatting.md               # layout, voice, profile/skills/bullet rules, validation checklist
```

## What it does (one workflow, no modes)

1. **01 Intake:** pick the template, load the master fact file, treat the JD as untrusted data
2. **02 Parse the JD:** must-have / nice-to-have / implicit signals, plus a five-line fit snapshot (clearance, location, contract vs permanent). No web research
3. **03 Gap Check & Confirm:** match each must-have to evidence; ask about anything addressable **before drafting**; write confirmed facts back to `03-background.md`
4. **04 Score:** ATS coverage before, via semantic clustering
5. **05 Draft:** two-paragraph profile, three grouped skills rows, evidence-first bullets
6. **06 Review & Finalise:** one fresh-context review (grounding, must-have coverage, hiring-manager and recruiter lenses); its edits go into the final text; ATS coverage after
7. **07 Render & Validate:** DOCX, `validate_cv.py`, `word_layout_check.ps1`
8. **08 Report:** ATS before/after, must-have to evidence map, gaps, what changed

There is no application tracker and no interview-prep output: this skill produces the CV and its report only.

## Output

- Tailored DOCX (the sole deliverable; see `05-formatting.md` "Output Format")
- Plain Calibri 10.5pt, A4, navy/grey, square (▪) bullets, hyperlinked contact details
- Most recent 3-4 roles on page 1, hard cap of 2 pages
- LinkedIn URL for Product roles only (see `01-config.md`)
- No em/en dashes anywhere

## Requirements

Node.js and the `docx` npm package (render), Python 3 (validation), and, optionally, Windows with Microsoft Word (`word_layout_check.ps1`). Details in `skills/cv-tailoring/references/01-config.md`. Copy the builder into a scratch folder to run it; don't write into the plugin folder.

## Using this from a plain claude.ai chat (no Claude Code)

A chat session without this repo mounted can't read these files. If it has shell/git access, it should `git clone` this repo first and copy `skills/cv-tailoring/scripts/build_cv_reference.js` as the literal starting point rather than re-deriving `05-formatting.md`'s layout rules from prose (that is how the `TabStopPosition.MAX` and `PositionalTab` bugs got introduced in September 2026).

## Installation in Claude Code

```bash
/plugin marketplace add hiranmanu/hiran-skills
/plugin install cv-tailoring@hiran-skills
```

## Updating

When Hiran confirms new facts about past roles, they are written to `skills/cv-tailoring/references/03-background.md` so the skill uses them without re-asking. That file is the single source of truth for every claim on a CV.

Before considering a version bump done, see the repo root [`CLAUDE.md`](../../CLAUDE.md) release checklist and run:
```bash
python3 scripts/check_release_consistency.py
```
from the repo root.

## Recent Updates

**v2.0.1** - Code-review fixes. `validate_cv.py` matched keywords as substrings ("AI" matched "retail", so a missing keyword could pass); it is now whole-word, no longer crashes on a DOCX without `core.xml`, and has 14 unit tests run in CI. `word_layout_check.ps1` reports "Word unavailable" cleanly (exit 2). Closed doc gaps: the reviewer now reads `03-background.md` to check grounding, the skill description carries explicit "use when" triggers, "before" ATS score is defined, the LinkedIn URL has one home (`01-config.md`), requirements and the builder's `package.json` are documented, and a wrong "no C-level title held" note is corrected.

**v2.0.0** - One workflow, numbered steps 01-08 and matching numbered reference files; Quick/Balanced/Full modes removed. `03-background.md` is now the master fact source (bullet bank merged from both source CVs plus everything confirmed since), replacing the source-CV PDFs as input. Bullets: page-1 roles may run 1-2 lines (second line 40-80% full), page-2 roles stay single-line. Profile is two short paragraphs; skills are three grouped rows; repeating JD must-haves across profile, skills and bullets is now intended. Added an independent review pass (grounding audit, must-have coverage, hiring-manager and recruiter lenses) whose edits are applied before render, a fit snapshot, blocking gap questions before drafting, `validate_cv.py` checks for dates/keywords/duplicates, and `word_layout_check.ps1`. Removed web research, interview-prep hints, and the decision-gates, QA-personas, market-research and semantic-clusters files (folded into `SKILL.md`, `05-formatting.md` and `04-scoring.md`).

**v1.14.2** - Repo now lives at `claude code\cv-tailoring\`; output moved to `CV Output\` and the two source CVs to `Source CVs\` beneath it (both gitignored).

**v1.14.1** - Reverted v1.14.0's "concurrent contract" clarifier rule for Aviva overlapping OneAdvanced/dunnhumby.

**v1.14.0** - New filename convention; Aviva date-overlap fix; two days of confirmed background facts merged.

See [`CHANGELOG.md`](CHANGELOG.md) in this folder for the full version history (every version back to v1.0.0).
