# Changelog — interview-prep

All notable changes to the `interview-prep` plugin/skill are documented
here. This file versions independently of other skills in this
marketplace — see the repo root `CHANGELOG.md` for marketplace-level
changes (new skills added, shared tooling, manifest schema).

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
