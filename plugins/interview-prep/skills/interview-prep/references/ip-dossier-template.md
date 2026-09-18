---
title: Dossier Output Template
---

# Dossier Template

Used in Phase 7 when a file deliverable is produced (Standard: if
confirmed; Deep: always — see `ip-config.md` Output). Structured so a
later session can hand this straight to the `pptx` skill for a board-style
deck without re-deriving the research.

```markdown
# Interview Dossier: {Company} — {Role}

Generated {YYYY-MM-DD} · Interview stage: {stage} · Prep mode: {Rapid/Standard/Deep}

## Company Snapshot
- What they do: {1-2 lines}
- Entity check: {confirm which entity, if any name ambiguity exists — see ip-research.md §0}
- How they make money: {revenue model, customer segment}
- Recent news: {2-3 dated items with source}
- Partnership/hiring cadence: {pattern across last 6-12mo, if Standard/Deep}
- Strategic signal: {from annual report/earnings call/funding announcement, if researched}

## People in the Room
{per named interviewer, if known: role, tenure, one distinctive researched
fact — public writing, prior role, industry-body position — per
ip-research.md §2.5}

## Role Fit
- Must-haves from JD: {list}
- Where this role sits relative to the revenue engine: {cost center / growth lever / infrastructure}

## Your Intro
- 3-sentence version: {text}
- 60-second version: {text}
- 2-minute version: {text, Deep mode only}

## Likely Questions & STAR Answers
{numbered list, per ip-question-bank.md Part A format}

## Smart Questions to Ask
{numbered list, per ip-question-bank.md Part B format, tiered by stage if known}

## HR Screen Basics
{only if interview stage is HR/recruiter screen — per ip-question-bank.md Part C}

## Verify Before You Say This Out Loud
{anything modeled, inferred, or unconfirmed — per ip-research.md Checkpoint}

## Gaps / Things to Have Ready
- {salary number, notice period, visa status if not yet confirmed}
- {any competency with no strong story on file}

## Round History
{appended after each transcript debrief — per ip-transcript-debrief.md.
One entry per completed round:}

### Round {N} — {date} — {stage/who}
- Confirmed: {brief}
- Corrected: {brief, with what it changes for sequencing/next round}
- Genuinely new: {brief}
- Carried into next round: {updated questions/stories/posture}

## Sources
{links/references used in Phase 1 research, with dates}
```

Filename: `{company}-interview-dossier-{YYYY-MM-DD}.md`, written to the
working directory unless the user's files show an existing pattern for
where interview prep lives (e.g. a folder already used by `cv-tailoring`
for this same application). **This file is append-only across rounds** —
when a transcript debrief runs for a later round, update it in place by
adding a new "Round History" entry and refreshing sections that changed
(Smart Questions, Verify-Before-Saying), rather than starting a fresh
dossier file per round.
