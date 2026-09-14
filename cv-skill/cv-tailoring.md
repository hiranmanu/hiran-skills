---
name: cv-tailoring
description: >
  Tailors a CV/resume to a specific job description for CPO/VP Product, Data
  Architect, Solution/Enterprise Architect, and related senior product/data
  roles. Use this whenever the user pastes or attaches a job description (JD),
  a job posting URL, or LinkedIn text and asks to tailor, update, or generate
  a CV/resume against it — or asks things like "tailor my CV to this",
  "does my CV match this JD", "what's my ATS score for this role", "build me
  a CV for [Company]", or "log this application". Also use for building or
  updating the underlying CV content library, computing a before/after ATS
  keyword-coverage score, generating the tailored DOCX/PDF, and logging the
  application to the applications tracker workbook. Trigger even if the user
  doesn't say "resume" or "CV" explicitly — a pasted job description plus any
  intent to apply is enough.
---

# CV Tailoring

Turns a job description into a tailored, ATS-clean CV — sourced from the
user's real CV library, never invented — plus a before/after keyword-coverage
score and a logged row in the applications tracker.

**Core principle — truth-preserving optimisation.** Reframe, reorder, and
re-emphasise real experience. Never fabricate a skill, metric, or
responsibility the user hasn't stated. If a JD requirement has no real
match, say so and mark it as a gap — don't paper over it.

**Read `references/formatting-rules.md` before writing a single line.** It
encodes hard constraints (single-line bullets, section titles, keyword
placement) established over many prior sessions with this user — violating
them is a bug, not a style choice.

## Trigger phrases

- "Tailor my CV/resume to this JD/role/posting"
- "What's my ATS score for this?" / "Will this pass ATS?"
- A pasted job description, job URL, or "help me apply for [Company]"
- "Build me a CV for [Company/role]"
- "Log this application" / "add this to the tracker"
- "Update my CV library with this"

## Phase 0 — Intake

**Resume content.** In priority order:
1. An existing library at `resumes/*.md` in the working directory, if present.
2. An attached CV file (PDF/DOCX) — read it (`pandoc -t markdown` for docx,
   or read the PDF directly) and treat it as the library seed.
3. Pasted CV text or LinkedIn profile text/URL — same treatment.
4. No CV at all — ask for one. Don't build content from nothing.

Also check `references/career-history-supplement.md` (per-role board/
investor, BI-tool, and Design facts this user has confirmed outside the
base CV — mirrored in project memory too, see that file's header for
which copy is authoritative if they ever disagree). This is often the
fastest way to pre-close a gap before ever asking about it — check it
before running the Phase 3 gap-confirmation pass, not after.

If the library is being seeded for the first time, split it into role-based
variant files (this user has at least three live variants — CPO/VP Product,
Data Architect, Solution/Enterprise Architect — see
`references/formatting-rules.md` for the keywords each must keep live) and
save them to `resumes/` so future runs don't need to re-parse the source file.

**Job description.** Text, a pasted URL (`web_fetch` it), or a LinkedIn job
URL. If several JDs arrive at once, process them as a batch — run Phase 1
research once per company where companies repeat, then Phases 2-6 per role.

## Phase 1 — Research (understand the market)

See `references/market-research.md` for the full prompt set. Summary:
company mission/culture/recent news, role benchmarking (who else holds this
title, what backgrounds they share), and a salary reality check where data
exists. Present a short success-profile summary and get a one-line
confirmation before moving on — don't silently assume the research is right.

## Phase 2 — Template selection

Pick the closest existing variant (CPO/VP Product, Data Architect,
Solution/Enterprise Architect) as the base rather than starting blank.
State which one and why in one line. If none fit well, say so before forcing
a match.

## Phase 3 — Matching, scoring, and gap handling

See `references/scoring.md`. Produces:
- A confidence-scored bullet-by-bullet match (direct / transferable /
  adjacent / gap) — same as before, nothing new here.
- **ATS coverage score, before.** Score the *unedited* base CV variant
  against this JD's extracted keywords before making any changes. Keep this
  number — it's the baseline.
- **Target 85%+ coverage.** Check the career-history-supplement memory file
  first (see Phase 0), then run the gap-confirmation pass on whatever's
  still unconfirmed — *before* Phase 4 generation, not as a note attached
  to the after-score. If a flagged gap would plausibly be true given the
  person's seniority and role history, ask directly rather than assuming
  it's a real gap; only list something as genuinely missing once they've
  confirmed it. Gaps under 60% confidence, or ones the user confirms as
  genuinely absent, get flagged — not silently dropped or forced.

## Phase 4 — Generation

See `references/generation-and-qa.md`. Produces the tailored `.docx` via the
`docx` skill, enforcing the single-line bullet budget from
`references/formatting-rules.md` as it writes — not just checking after the
fact.

**Filename:** `{FirstName}_{LastName}_{Company}_CV.docx` /
`.pdf` — pull the name from the CV source, company name from the JD, both
underscore-joined, no spaces. Read `references/generation-and-qa.md` for the
full convention including disambiguating multiple roles at one company.

## Phase 5 — QA and after-score

1. Render to PDF and visually inspect each page (per the `docx` skill's
   verify step) — confirm no bullet wrapped to a second line and no section
   grid crept back in.
2. Run `pdftotext` against the export and confirm it returns clean, ordered
   text (see `references/generation-and-qa.md`) — this is the closest
   available proxy for "will a real ATS parser choke on this," not a
   guarantee.
3. **ATS coverage score, after.** Score the tailored CV the same way as the
   Phase 3 baseline. Report both numbers to the user as a before → after
   with the delta, plus what's still missing. State plainly that this is a
   transparent keyword-coverage heuristic this skill computes — not the
   actual scoring algorithm any specific vendor's ATS (Workday, Greenhouse,
   Taleo, etc.) runs internally, which is proprietary and undocumented. Useful
   as a directional signal, not a guaranteed pass mark.

## Phase 6 — Tracker + library update

See `references/tracker.md`. Append one row to
`Hiran_Applications_Tracker.xlsx` (create it from
`references/tracker.md`'s schema if it doesn't exist yet) with the JD, both
ATS scores, the CV file used, and today's date. Then ask, same as before:
save this tailored version into the `resumes/` library for future reuse, or
keep it one-off.

## What this skill does not do (yet)

- **Cover letters.** Different job — say so if asked, don't attempt one
  inline.
- **Interview prep / STAR stories.** Planned as a companion skill, not built
  yet — say so if asked.
- **Finding or auto-applying to roles on LinkedIn or other job boards.**
  Out of scope by design — see the notes in this project's memory on why.
  This skill only acts once the user has a specific JD in hand.
