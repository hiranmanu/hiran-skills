---
name: interview-prep
description: >
  Builds interview intel from a job description and company name — company
  and named-interviewer research (site news, internet news, revenue model,
  annual reports, earnings calls), STAR-format answers to likely questions,
  a genuine self-introduction, smart questions to ask that are baked with
  real company knowledge (not generic), and HR-screen basics (motivation,
  salary, notice period, logistics). Scales from a 10-minute rapid brief
  before a call to a full dossier for later reuse. Multi-round aware: feed
  it a transcript/recording from a completed round and it reconciles prior
  assumptions against what was actually said, then carries the update into
  the next round's prep. This is interview prep — it does not touch the CV.
---

# Interview Prep

Turns a job description + company into a tight, genuine interview brief —
not a script. The differentiator is that every question the user asks the
interviewer, and every answer they give, should demonstrably reflect real
homework on the company, not generic prep.

**Core principle — genuine over generic.** A smart question that could
have been asked by someone who read nothing is worse than no question. A
STAR answer built on a fabricated metric is worse than an honest "no hard
number on file." See `references/ip-question-bank.md` for how this is
enforced in both directions.

**This is not CV tailoring.** If the user also wants their CV tailored to
this JD, that's the separate `cv-tailoring` skill — don't run both in one
pass unless asked.

## Trigger phrases

- "Build me interview intel/prep for [Company/role]"
- "I have an interview in [X minutes/hours], help me prep"
- A pasted JD with "interview" mentioned, not "tailor my CV"
- "What questions should I ask them?" / "STAR answers for this JD"
- "HR screen prep for [Company]"
- "Here's the transcript/recording from the first/last call, help me prep
  for round 2" (or any similar reference to a prior round's material)

## Workflow overview

| Phase | Name | Reference file |
|---|---|---|
| 0 | Intake (mode, stage, JD, company) | `references/ip-config.md` |
| 1 | Company Intel Research (incl. named-interviewer research, entity check) | `references/ip-research.md` |
| 1.5 | Prior-Stage Transcript Debrief (only if a prior round's transcript/notes exist) | `references/ip-transcript-debrief.md` |
| 2 | JD Breakdown | — |
| 3 | Likely Questions + STAR Answers | `references/ip-question-bank.md` (Part A), `references/ip-background.md` |
| 4 | Smart Questions to Ask | `references/ip-question-bank.md` (Part B) |
| 4.5 | Strategic Diagram Pack (only if asked for) | `references/ip-diagrams.md` |
| 5 | Self-Introduction | — |
| 6 | HR Screen Basics (if applicable) | `references/ip-question-bank.md` (Part C) |
| 6.5 | Late-Stage / Diligence Prep (final/exec rounds only) | `references/ip-diligence.md` |
| 7 | Dossier (if applicable) | `references/ip-dossier-template.md` |

Speed mode and interview stage (set in Phase 0) determine what each later
phase actually does — both tables live in `references/ip-config.md` and
are the single source of truth; don't restate them here. Phases 1.5, 4.5,
and 6.5 are conditional — most single-round Rapid/Standard sessions never
touch them; they exist for the multi-round, higher-stakes case.

## Phase 0 — Intake

Need, in order of how fast they matter:
1. **Time pressure** — "in 10 minutes" etc. means Rapid mode, skip
   straight to it without asking. Otherwise ask once if genuinely unclear
   whether this is Rapid/Standard/Deep — see `references/ip-config.md`.
2. **JD** — pasted text preferred; PDF/DOCX attached; or job title +
   company if no JD text is available (research the public posting).
3. **Company name** — required for Phase 1.
4. **Interview stage** — HR screen / hiring manager / panel / final. Ask
   if not stated, unless Rapid mode with no time to ask — in that case,
   default to including HR Screen Basics anyway (Phase 6), since it's
   cheap to include and costly to have missed if wrong.
5. **Background context** — always check `references/ip-background.md`
   first for STAR material before asking the user for anything; only run
   its Discovery prompt for a genuine gap.
6. **Prior-round material** — ask (or check the working directory for an
   existing `{company}-interview-dossier-*.md`) whether this is a later
   round with a transcript, recording, or notes from a completed prior
   stage. If yes, that's Phase 1.5. If a dossier already exists for this
   application, read it first — it carries the prior round's confirmed
   facts and posture forward; don't re-research from scratch.

## Phase 1 — Company Intel Research

Full method and depth-by-mode in `references/ip-research.md`. In brief:
entity check → site news (+ partnership-cadence timeline) → internet news
→ named-interviewer research → revenue model → annual report/earnings
call → (Deep only) competitive landscape + adjacent-industry playbook
translation. Checkpoint with a 3-5 line summary **plus a "verify before
you say this" list** before moving on, except in Rapid mode where there's
no time for a checkpoint — proceed straight through.

## Phase 1.5 — Prior-Stage Transcript Debrief (conditional)

Only runs if Phase 0 surfaced a transcript/recording/notes from a
completed prior round, or an existing dossier for this application. Full
method in `references/ip-transcript-debrief.md`: reconcile prior
assumptions against the transcript into Confirmed / Corrected / Genuinely
New, call out anything that changes sequencing for the next round, update
the smart-questions list so nothing already answered gets asked again,
and append the result to the dossier's Round History rather than starting
fresh. If this reveals the process has moved into final-round/diligence
territory, hand off to `references/ip-diligence.md` for Phase 6.5 instead
of continuing with round-one framing.

## Phase 2 — JD Breakdown

Parse into must-have / nice-to-have / implicit-signal buckets (same
categories as `cv-tailoring`'s job research, kept independent here since
this skill doesn't share files with that plugin). This feeds Phase 3's
question generation and Phase 4's "where does this role sit relative to
the revenue engine" framing from Phase 1.

## Phase 3 — Likely Questions + STAR Answers

Full method in `references/ip-question-bank.md` Part A. Pull stories from
`references/ip-background.md`'s STAR bank by competency match — never
invent a metric or story. If a likely question has no matching story, use
that file's Discovery prompt rather than fabricating one.

## Phase 4 — Smart Questions to Ask

Full method in `references/ip-question-bank.md` Part B. Every question in
Standard/Deep mode must cite a specific Phase 1 fact, and should be
annotated with what it tests. Tier by interview stage if known, and apply
the round-posture calibration in that file — first-conversation questions
are not the same set as final-round questions.

## Phase 4.5 — Strategic Diagram Pack (conditional)

Only if the user explicitly asks for a visual/diagram/north star/deck
material — never by default. Full method in `references/ip-diagrams.md`:
produced as a single editable `.drawio` file, build only the tab(s)
asked for, and any modeled/assumed figure (e.g. a revenue projection)
must carry a visible disclaimer in the diagram itself distinguishing it
from a verified source figure.

## Phase 5 — Self-Introduction

Produce the version(s) called for by speed mode (`references/ip-config.md`):
3-sentence always, 60-second for Standard+, 2-minute board-level for Deep.
Ground it in real background (`references/ip-background.md`) and mirror
language from Phase 1's company research where genuine (not forced
keyword-matching — this is a spoken intro, not an ATS pass).

## Phase 6 — HR Screen Basics

Only when the interview stage is HR/recruiter screen (or defaulted to in
Phase 0 for Rapid mode with unknown stage). Full checklist in
`references/ip-question-bank.md` Part C — includes asking the user
directly for salary expectations, notice period, and visa/right-to-work
status rather than assuming any of them.

## Phase 6.5 — Late-Stage / Diligence Prep (conditional)

Only when the interview stage is final/exec-level, or Phase 1.5's
transcript debrief indicates the process has moved into offer-adjacent or
document-sharing territory. Full method in `references/ip-diligence.md`:
reframes the question list into a formal diligence-style document request
by category, and — if the company has shared internal documents — mines
them for internal tensions and contradictions rather than paraphrasing
them back generically. Does not extend into building actual engagement
deliverables (workshop decks, prototypes) — that's explicitly out of
scope, see that file's closing note.

## Phase 7 — Dossier

Per the Output table in `references/ip-config.md`: skip in Rapid, offer in
Standard, always produce in Deep. Use the structure in
`references/ip-dossier-template.md` so a later session (or the `pptx`
skill) can build on it directly rather than re-deriving research. If a
dossier already exists for this application (multi-round case), update it
in place per that file's append-only convention rather than creating a
new one.

## Edge Cases

1. **No time for research at all** (interview starting now): skip
   straight to Phase 3/5/6 using JD text + `ip-background.md` only, flag
   clearly that Phase 1 research was skipped so the smart questions in
   Phase 4 will necessarily be generic — say so rather than faking
   specificity.
2. **Private/early-stage company, no public info:** see
   `references/ip-research.md` "If research is blocked."
3. **User wants both interview prep and CV tailoring:** confirm they want
   both in one session; run this skill's phases first (they're faster),
   then hand off to `cv-tailoring` — don't interleave the two workflows.
4. **Multiple interviewers/panel, mixed seniority:** produce one question
   set but tier the smart-questions list (Phase 4) so the user can pick
   per-interviewer rather than asking a board-level question of an HR
   screener.
5. **User wants an actual deliverable built for the company** (a workshop
   deck, a working prototype, a formal proposal document): that's past
   this skill's scope — see `references/ip-diligence.md`'s closing note.
   Point to using the dossier this skill produced as input to the
   `pptx`/`docx`/`artifact-design` tooling directly, rather than
   expanding this workflow to cover it.
6. **A transcript arrives with no prior dossier/context for this
   application:** still run Phase 1.5 (`ip-transcript-debrief.md`) — it
   can reconcile against this session's own fresh Phase 1 research
   instead of a prior dossier; just skip the "append to existing dossier"
   step and create one fresh in Phase 7 instead.
