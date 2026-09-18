# interview-prep (v1.0.0)

Builds interview intel from a job description and company name — not CV
tailoring, interview prep specifically.

See the repo root [`SKILLS.md`](../../SKILLS.md) for the full catalog of
skills in this marketplace, and [`CHANGELOG.md`](CHANGELOG.md) in this
folder for this plugin's full version history.

## Structure

```
interview-prep/                                  # this plugin
├── .claude-plugin/
│   └── plugin.json                              # plugin metadata
├── README.md                                    # this file
├── CHANGELOG.md                                  # full version history for this plugin
└── skills/
    └── interview-prep/                          # the actual skill Claude loads
        ├── SKILL.md                             # entrypoint — 8-phase orchestrator
        └── references/                          # loaded on demand, not upfront
            ├── ip-config.md                      # speed modes, interview stages, output conventions
            ├── ip-research.md                    # company research methodology
            ├── ip-background.md                  # STAR story bank + confirmed career facts
            ├── ip-question-bank.md                # likely-Q/STAR, smart-questions, HR-screen basics
            └── ip-dossier-template.md             # Phase 7 output structure
```

## What it does (Phases 0-7, see `skills/interview-prep/SKILL.md` for the full sequence)

1. Intake — speed mode, interview stage, JD, company (Phase 0)
2. Researches the company: site news, internet news, revenue model,
   annual reports/earnings calls (Phase 1)
3. Breaks the JD into must-have/nice-to-have/signal (Phase 2)
4. Generates likely interviewer questions with STAR-format answers, pulled
   from a real background story bank — never a fabricated metric (Phase 3)
5. Generates smart questions to ask back, each tied to a specific fact
   from the company research — no generic questions (Phase 4)
6. Builds a self-introduction, length scaled to speed mode (Phase 5)
7. Preps HR-screen basics — motivation, salary, notice period,
   visa/right-to-work — whenever the stage is an HR/recruiter screen
   (Phase 6)
8. Writes a dossier file for later reuse (e.g. by the `pptx` skill),
   depending on speed mode (Phase 7)

## Speed modes

Three modes, defined and enforced in `SKILL.md` Phase 0 / `ip-config.md`
(not just described here — the orchestrator actually scales phase depth
per mode):

### Rapid (3-5 min of work)
"Interview in 10 minutes" — skips deep research, top 3-5 likely questions
with lightweight STAR, 3 smart questions, a 3-sentence intro, HR-screen
basics if the stage is unknown or is a screen. No dossier file.

### Standard (10-15 min of work)
Full company research, 8-10 questions with full STAR, 5-6 smart questions,
3-sentence + 60-second intro. Dossier file offered.

### Deep (20-40 min of work)
Standard + prior-period comparison, competitive landscape, 10-15
questions with backup stories per theme, board-level 2-minute intro
version. Dossier file always written.

## Interview stages

HR/recruiter screen, hiring manager, panel/technical, or final/exec —
changes which questions get weighted and whether HR-screen basics
(salary, notice period, visa status — always asked of the user directly,
never assumed) are mandatory. See `ip-config.md`'s stage table.

## Relationship to `cv-tailoring`

Separate plugin, no shared files (each installs independently — see the
repo root `CLAUDE.md` "Plugin self-containment" rule). `ip-background.md`
here deliberately duplicates some of the same career facts as
`cv-tailoring`'s `cv-background.md`; the two are not auto-synced, so a
newly confirmed fact needs updating in both if it matters to both
workflows.

## Installation in Claude Code

```bash
/plugin marketplace add hiranmanu/hiran-skills
/plugin install interview-prep@hiran-skills
```

## Updating

When Hiran confirms new facts about past roles during a prep session,
update `skills/interview-prep/references/ip-background.md` so the skill
uses them without re-asking (and update `cv-tailoring`'s
`cv-background.md` too if the fact is CV-relevant — see the duplication
note above).

Before considering a version bump done, see the repo root
[`CLAUDE.md`](../../CLAUDE.md) release checklist and run:
```bash
python3 scripts/check_release_consistency.py
```
from the repo root.

## Recent Updates

**v1.0.0** — Initial release.

See [`CHANGELOG.md`](CHANGELOG.md) in this folder for the full version history.
