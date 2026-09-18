# interview-prep (v1.2.0)

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
        ├── SKILL.md                             # entrypoint — 12-phase orchestrator (4 conditional)
        └── references/                          # loaded on demand, not upfront
            ├── ip-config.md                      # speed modes, interview stages, engagement types, output conventions
            ├── ip-research.md                    # company + named-interviewer + filings/hiring-signal research methodology
            ├── ip-background.md                  # STAR story bank + confirmed career facts
            ├── ip-question-bank.md                # likely-Q/STAR, smart-questions, stakeholder-alignment, HR-screen basics
            ├── ip-transcript-debrief.md           # Phase 1.5 — prior-round transcript reconciliation
            ├── ip-diagrams.md                     # Phase 4.5 — optional strategic diagram pack
            ├── ip-presentation.md                 # Phase 4.7 — presentation-round prep (when the round requires it)
            ├── ip-diligence.md                    # Phase 6.5 — final-round/diligence-level prep
            └── ip-dossier-template.md             # Phase 7 output structure, append-only across rounds
```

## What it does (see `skills/interview-prep/SKILL.md` for the full sequence)

1. Intake — speed mode, interview stage, JD, company, prior-round material (Phase 0)
2. Researches the company and named interviewers: entity check, site
   news + partnership cadence, hiring signals, filings registries
   (Companies House/SEC/OpenCorporates), internet news, revenue model,
   annual reports/earnings calls, employer reputation + existing-team
   research (Phase 1)
3. **If a transcript/recording from a completed prior round exists:**
   reconciles prior assumptions into Confirmed / Corrected / Genuinely New,
   flags anything that changes next-round sequencing, and carries the
   update forward (Phase 1.5, conditional)
4. Breaks the JD into must-have/nice-to-have/signal (Phase 2)
5. Generates likely interviewer questions with STAR-format answers, pulled
   from a real background story bank — never a fabricated metric (Phase 3)
6. Generates smart questions to ask back, each tied to a specific fact
   from the company research, annotated with what each tests, calibrated
   to the interview round, and including a stakeholder-alignment check
   when 2+ senior stakeholders are in the process — no generic questions
   (Phase 4)
7. **If asked:** builds an editable strategic diagram pack (capability
   map, architecture, business model, revenue model, ecosystem — modeled
   figures always visibly disclaimed) (Phase 4.5, conditional)
8. **If the round requires presenting back** (a case-study round, "bring
   your 90-day plan"): builds the actual presentation using the
   appropriate tool for the format asked for, with a narrative arc and
   posture matched to the round — still in scope because the interview
   process itself requires it (Phase 4.7, conditional)
9. Builds a self-introduction, length scaled to speed mode (Phase 5)
10. Preps HR-screen basics — branched by engagement type: permanent
    (salary, notice period, visa/right-to-work) or fractional/interim/
    advisory (day rate/retainer, availability, engagement structure,
    IR35) — whenever the stage is an HR/recruiter screen (Phase 6)
11. **For final-round/diligence-level stages:** reframes into a formal
    document-request list and mines any shared company documents for
    internal contradictions (Phase 6.5, conditional)
12. Writes (or updates, append-only) a dossier file for later reuse (e.g.
    by the `pptx` skill), depending on speed mode (Phase 7)

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

**v1.2.0** — Senior/exec-round gaps closed: research broadened to filings
registries, hiring signals, employer-review sites, and existing-team
research (not just site + news); a stakeholder-alignment question check
for multi-senior-stakeholder processes; a genuine presentation-round
capability (Phase 4.7) for when the interview itself requires presenting
back, clearly distinguished from out-of-scope post-hire deliverables; and
engagement-type-aware HR basics (fractional/interim/advisory vs.
permanent).

**v1.1.0** — Multi-round support: transcript debrief (Phase 1.5), named-
interviewer research and entity disambiguation, round-posture-calibrated
questions, an optional strategic diagram pack (Phase 4.5), and final-round
diligence prep (Phase 6.5). Built from reviewing an actual multi-round
interview-prep conversation.

**v1.0.0** — Initial release.

See [`CHANGELOG.md`](CHANGELOG.md) in this folder for the full version history.
