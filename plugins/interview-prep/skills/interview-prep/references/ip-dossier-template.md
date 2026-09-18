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
- How they make money: {revenue model, customer segment}
- Recent news: {2-3 dated items with source}
- Strategic signal: {from annual report/earnings call/funding announcement, if researched}

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

## Gaps / Things to Have Ready
- {salary number, notice period, visa status if not yet confirmed}
- {any competency with no strong story on file}

## Sources
{links/references used in Phase 1 research, with dates}
```

Filename: `{company}-interview-dossier-{YYYY-MM-DD}.md`, written to the
working directory unless the user's files show an existing pattern for
where interview prep lives (e.g. a folder already used by `cv-tailoring`
for this same application).
