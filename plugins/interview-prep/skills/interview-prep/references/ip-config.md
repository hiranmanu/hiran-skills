---
title: Configuration & Defaults
---

# Configuration Reference

Single source of truth for paths, defaults, and workflow parameters. If
another reference file states one of these values differently, this file
wins — fix the other file rather than trusting it.

## Speed Modes

| | Rapid | Standard | Deep |
|---|---|---|---|
| **Trigger** | "interview in X min", any X ≤ 15, or explicit "quick brief" | Default when a JD + company is given with no time pressure stated | "board-level", "final round", "build me a dossier", "this is a big one" |
| **Typical time to produce** | 3-5 min of work | 10-15 min of work | 20-40 min of work |
| Phase 1 (Company Intel) | Company site headlines + top 2-3 news hits only, entity check still mandatory. Skip named-interviewer research, annual report/earnings call unless already summarized publicly in a recent article. | Full: entity check, site, news + cadence timeline, named-interviewer research, revenue model, most recent annual report or earnings call. | Full + prior year(s) comparison, competitor landscape, adjacent-industry playbook translation, analyst commentary if available. |
| Phase 1.5 (Transcript debrief) | Only if a transcript exists; lightweight 3-bucket pass, skip escalating-posture guidance | Full reconciliation + posture update | Full + explicit sequencing-impact call-out |
| Phase 2 (JD breakdown) | Skim for must-haves only | Full must-have/nice-to-have/signal breakdown | Full + mapped to company strategy from Phase 1 |
| Phase 3 (Question bank) | Top 5 likely questions, STAR-lite (2-3 sentences each) | 8-10 questions, full STAR | 10-15 questions, full STAR + backup story per theme |
| Phase 4 (Smart questions to ask) | 3, each tied to one Phase 1 fact | 5-6, each tied to a specific fact, annotated with what it tests | 6-8, tiered by interviewer seniority, annotated, round-posture calibrated |
| Phase 4.5 (Diagram pack) | Skip — no time | Only if explicitly asked, single tab | Only if explicitly asked, full pack available |
| Phase 5 (Intro) | 3-sentence version only | 3-sentence + 60-second version | Both + a 2-minute board-level version |
| Phase 6 (HR-screen basics) | Always included if stage is HR/recruiter screen, in any mode | Always included | Always included |
| Phase 6.5 (Diligence prep) | Skip | Only if stage is final/exec | Only if stage is final/exec |
| Phase 7 (Dossier file) | Skip — chat output only | Offer; write if user confirms | Always write, structured for later PPTX reuse |

If unsure which mode fits and there's no time pressure stated, ask once —
don't default to Deep, it's the slowest path and wasn't asked for. If time
pressure is stated ("in 10 minutes"), skip straight to Rapid without asking.

## Interview Stage

Determines what's mandatory in Phase 6 and how questions in Phase 3 are
weighted. Ask if not stated, or infer from context (e.g. "first call with
their recruiter" = HR screen; "meeting the CPO" = Hiring Manager).

| Stage | Phase 3 weighting | Phase 6 |
|---|---|---|
| HR / Recruiter screen | Motivation, culture-fit, logistics-adjacent | Mandatory — see `ip-question-bank.md` §HR Screen Basics |
| Hiring Manager | Role-specific competency, team fit, ownership | Optional — only if salary/logistics likely to come up |
| Panel / Technical | Deep competency, scenario/case questions | Skip unless explicitly asked |
| Final / Exec | Strategic alignment, vision, culture at leadership level | Skip |

## Output

- **Chat output is the primary deliverable in every mode** — this is
  time-pressured prep, not a document-generation workflow. Don't hold the
  brief hostage to file-writing.
- **Dossier file** (Standard: offered; Deep: always): a single Markdown
  file at `{company}-interview-dossier-{YYYY-MM-DD}.md` in the working
  directory (or wherever the user's other interview files live, if a
  pattern is already visible in the working directory). Structured per
  `ip-dossier-template.md` so it can be handed to the `pptx` skill later
  without re-deriving the research.
- This skill produces **no CV or resume changes** — if the user also wants
  their CV tailored to this JD, that's the separate `cv-tailoring` skill.
  Don't do both in one pass unless asked.

## Portability note

This skill's `ip-background.md` duplicates career facts that also live in
the separate `cv-tailoring` plugin's `cv-background.md`. That's
intentional (see the marketplace root `CLAUDE.md` "Plugin
self-containment" rule) — plugins are installed independently, so this
file can't reach across to the other plugin's folder. If a fact changes in
one, it needs updating in both by hand.
