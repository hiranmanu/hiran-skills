# cv-tailoring (v1.12.0)

Tailors a CV to a job description for CPO/VP Product, Data Architect, Solution/Enterprise Architect, and related senior product/data roles.

See the repo root [`SKILLS.md`](../../SKILLS.md) for the full catalog of skills in this marketplace, and [`CHANGELOG.md`](CHANGELOG.md) in this folder for this plugin's full version history.

## Structure

```
cv-tailoring/                                  # this plugin
├── .claude-plugin/
│   └── plugin.json                            # plugin metadata
├── README.md                                  # this file
├── CHANGELOG.md                                # full version history for this plugin
└── skills/
    └── cv-tailoring/                          # the actual skill Claude loads
        ├── SKILL.md                           # entrypoint — 8-phase orchestrator
        ├── scripts/
        │   ├── validate_cv.py                  # automated Phase 5.3 checks
        │   └── build_cv_reference.js           # reference docx-js house-style implementation
        └── references/                        # loaded on demand, not upfront
            ├── cv-background.md                # role facts, template selection — write target for Phase 2.5
            ├── cv-formatting.md                # hard constraints + voice patterns
            ├── cv-config.md                    # centralized configuration
            ├── cv-decision-gates.md            # phase decision logic (loop targets)
            ├── cv-semantic-clusters.md         # cluster lookup data only
            ├── cv-scoring.md                   # ATS methodology (single source of truth)
            ├── cv-qa-personas.md               # HM + TA checklists (single source of truth)
            └── cv-market-research.md           # research patterns
```

## What it does (Phases 0-6, see `skills/cv-tailoring/SKILL.md` for the full sequence)

1. Intake — load CV library and reference files (Phase 0)
2. Researches the role and company signals (Phase 1)
3. Assesses gaps against JD requirements, checking `cv-background.md` first (Phase 2)
4. Runs a discovery interview for addressable gaps, writes confirmed facts back to `cv-background.md` (Phase 2.5)
5. Scores ATS keyword coverage before/after via semantic clustering, target 85%+ (Phase 3)
6. Rewrites profile, skills, and bullets to match the JD (Phase 4)
7. Reviews draft text via Hiring Manager + Talent Acquisition lenses before rendering (Phase 5.1), then validates the render's hard constraints (Phase 5.3)
8. Generates a summary report (Phase 6)

There is no application-tracker step — the skill doesn't log anywhere,
GDrive or otherwise. Output is a local DOCX only.

## Workflow modes

Three speed modes, defined and enforced in `SKILL.md` Phase 0 (not just described here — the orchestrator actually skips the right phases per mode):

### Quick (1-2 min)
Paste JD → get a tailored DOCX → done. Skips web research and the discovery interview; never skips validation. Default when you just paste a JD with no other instruction.

### Balanced (15-20 min)
Paste JD → 2-3 quick questions (only for gaps that move the ATS score) → generate → review once → upload.

### Full Manual (90-135 min)
All 8 phases with full discovery interview, gap assessment, QA, decision loops. Best for high-stakes roles or skill refinement.

## Output

- Tailored DOCX (the sole deliverable — see `cv-formatting.md` "Output Format"; a self-generated PDF is never shipped, only used internally for Phase 5.3 validation)
- Plain Calibri 10.5pt, A4, navy/grey colour scheme, square (▪) bullets, hyperlinked contact details
- LinkedIn URL for Product roles only (see `cv-config.md`)
- All sub-bullets preserved; no em-dashes; proper spacing and alignment

## Recent Example

TalentInternational Product Director role:
- **Before:** 64% ATS coverage (18/28 keywords)
- **After:** 93% ATS coverage (26/28 keywords)
- **Profile rewrite:** "Senior Product Director" + search/discovery + hands-on IC + prototyping tools (Claude Code, Cursor, Lovable, Bolt)
- **Skills regenerated:** 5 lines of JD-only keywords, search/discovery front-loaded

## Using this from a plain claude.ai chat (no Claude Code)

A chat session without this repo mounted can't read these files directly, so it's tempting to regenerate the house style from memory/prose rules alone. That's how the `TabStopPosition.MAX` bug (dates not flush right) and the `PositionalTab`/LibreOffice bug got introduced in September 2026 — a chat session re-derived the docx-js layout from scratch instead of starting from the tested reference. If a chat session has shell/git access, it should `git clone` this repo first and copy `skills/cv-tailoring/scripts/build_cv_reference.js` as the literal starting point (see that file's own header comment), rather than reimplementing `cv-formatting.md`'s rules from prose each time.

## Installation in Claude Code

```bash
/plugin marketplace add hiranmanu/hiran-skills
/plugin install cv-tailoring@hiran-skills
```

## Updating

When Hiran confirms new facts about past roles, update `skills/cv-tailoring/references/cv-background.md` so the skill uses them without re-asking.

Before considering a version bump done, see the repo root [`CLAUDE.md`](../../CLAUDE.md) release checklist and run:
```bash
python3 scripts/check_release_consistency.py
```
from the repo root.

## Recent Updates

**v1.12.0** — Removed GDrive output and the Google Sheets applications tracker entirely; output is now a local DOCX in a fixed local folder (see `cv-config.md`). Redacted real personal data (name/email/LinkedIn/CV content) that had been committed in `build_cv_reference.js` since v1.8.0.

See [`CHANGELOG.md`](CHANGELOG.md) in this folder for the full version history (every version back to v1.0.0).
