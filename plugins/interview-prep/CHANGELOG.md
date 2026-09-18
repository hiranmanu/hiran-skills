# Changelog — interview-prep

All notable changes to the `interview-prep` plugin/skill are documented
here. This file versions independently of other skills in this
marketplace — see the repo root `CHANGELOG.md` for marketplace-level
changes (new skills added, shared tooling, manifest schema).

## [1.1.0] - 2026-09-18 (Multi-Round Support: Transcript Debrief, Named-Interviewer Research, Diagrams, Diligence Prep)

Built after reviewing an actual multi-round interview-prep conversation
(a real CPO-hire process) that this skill hadn't been built from yet.
That session went further than v1.0.0's single-round model in several
concrete ways — reconciling later rounds against a recorded transcript,
researching named interviewers rather than only the company, catching a
real entity-confusion error, translating an adjacent industry's playbook,
and shifting question posture by round. Folded in what's genuinely
reusable interview-prep methodology; explicitly left out what belonged to
that session's later drift into building actual paid-engagement
deliverables (workshop decks, prototypes) — that's a different job, noted
as out of scope rather than absorbed.

### Added
- **Phase 1.5 — Prior-Stage Transcript Debrief**
  (`references/ip-transcript-debrief.md`): feed a transcript/recording/
  notes from a completed round and it reconciles prior assumptions into
  Confirmed / Corrected / Genuinely New, explicitly calls out anything
  that changes next-round sequencing (e.g. a compressed exit timeline),
  includes transcription-hygiene guidance (auto-transcripts misname
  people routinely), and writes the result into the dossier's new "Round
  History" section (append-only, not overwritten) rather than starting
  fresh each round. This is the feature directly requested after
  reviewing the reference conversation — Hiran records first/second-stage
  calls and needs prep built on what was actually said, not just public
  research.
- **Named-interviewer research** (`ip-research.md` §2.5): research the
  people in the room, not only the company — public writing, prior roles,
  industry-body positions. Citing an interviewer's own stated thesis back
  to them, accurately, turned out to be the single highest-signal prep
  move in the reference conversation.
- **Entity disambiguation as a standing rule** (`ip-research.md` §0): the
  reference conversation initially misattributed a fact between two
  similarly-branded companies sharing a founder; this is now a mandatory
  check before citing any figure, not a one-off fix.
- **Partnership-cadence timeline and adjacent-industry playbook
  translation** (`ip-research.md`, Standard/Deep): ordering news by date
  to reveal an implicit strategic pattern, and translating how a more
  mature adjacent market's leaders actually grew into a sequence for the
  target company's market — both proved to be stronger prep than
  isolated fact-gathering in the reference conversation.
- **Round-posture calibration** (`ip-question-bank.md`): first-round
  questions hold back anything presuming mutual commitment (reporting
  lines, comp specifics); later rounds can escalate to stating a
  falsifiable position rather than only asking open questions, when a
  transcript debrief shows the conversation already has real depth.
  Every Standard/Deep question now also gets a one-line "what this
  tests" annotation.
- **Phase 4.5 — Strategic Diagram Pack** (`references/ip-diagrams.md`,
  optional, only when explicitly asked): a single editable `.drawio` file
  with up to seven tabs (capability map, architecture stack, business
  model, revenue model, investment bets, ecosystem, managed-vs-self-serve)
  — any modeled/assumed figure (e.g. a revenue projection) must carry a
  visible in-diagram disclaimer distinguishing it from a verified source
  figure, a rule added after the reference conversation's own modeled
  revenue bridge needed exactly this caveat spelled out explicitly.
- **Phase 6.5 — Late-Stage / Diligence Prep** (`references/ip-diligence.md`,
  final/exec rounds only): reframes the question list into a formal,
  categorized document-request list once a process moves past initial
  screening, and — if the company has shared internal documents — mines
  them for internal contradictions rather than paraphrasing them back
  generically.
- Dossier template (`ip-dossier-template.md`) gained "People in the Room,"
  "Verify Before You Say This Out Loud," and "Round History" sections, and
  is now explicitly append-only across rounds rather than one file per
  round.

### Changed
- `SKILL.md`'s phase table now shows 11 phases (3 conditional: 1.5, 4.5,
  6.5), and its frontmatter description now states the multi-round
  transcript-debrief capability.
- `ip-config.md`'s speed-mode table extended to cover the new conditional
  phases per mode.

## [1.0.0] - 2026-09-18 (Initial Release)

### Added
- `SKILL.md` — 8-phase orchestrator (intake → company research → JD
  breakdown → likely questions/STAR answers → smart questions to ask →
  self-intro → HR-screen basics → dossier), with three speed modes
  (Rapid/Standard/Deep) so a "interview in 10 minutes" request and a
  "build me a full dossier" request are handled by the same skill without
  either shortchanging the other.
- `references/ip-config.md` — single source of truth for speed-mode and
  interview-stage behavior, and output conventions.
- `references/ip-research.md` — company research methodology (site news,
  internet news, revenue model, annual reports/earnings calls, competitive
  landscape), with source-checkpointing before questions get generated
  from it.
- `references/ip-background.md` — STAR story bank organized by
  competency, seeded from Hiran's confirmed career history (dunnhumby,
  OneAdvanced, Hybrid Theory, Amazon, Dentsu, Sage) plus a "Notable Gaps"
  section so the skill answers weakness/gap questions honestly instead of
  reaching for a forced story. Deliberately duplicates facts also held in
  the separate `cv-tailoring` plugin's `cv-background.md` — see that
  file's own duplication note and the root `CLAUDE.md` plugin
  self-containment rule for why this isn't a shared file instead.
- `references/ip-question-bank.md` — methodology for (A) likely
  interviewer questions with full STAR answers, (B) smart questions to
  ask that must each cite a specific fact from Phase 1 research (the
  "could a candidate with zero research have asked this?" test), and (C)
  mandatory HR-screen basics (motivation, salary, notice period,
  visa/right-to-work, logistics) whenever the interview stage is an
  HR/recruiter screen.
- `references/ip-dossier-template.md` — the Phase 7 output structure,
  written so a later session can hand it straight to the `pptx` skill
  without re-deriving the research.

### Notes
- Built from two prior ad-hoc chat sessions' worth of interview-prep
  prompts (a fast pre-call brief and a fuller company-intel build), turned
  into a reusable, speed-mode-aware skill rather than a one-off prompt
  each time.
