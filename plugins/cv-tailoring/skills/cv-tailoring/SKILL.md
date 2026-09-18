---
name: cv-tailoring
description: >
  Tailors a CV/resume to a specific job description for CPO/VP Product, Data
  Architect, Solution/Enterprise Architect, and related senior product/data
  roles. Scores ATS keyword coverage (target 85%+) via semantic clustering,
  generates a timestamped DOCX (the only deliverable format), and syncs the
  application to a Google Sheets tracker in GDrive. Supports batch processing of multiple JDs,
  experience discovery when gaps appear, and generates a summary report per CV.
---

# CV Tailoring

Turns a job description into a tailored, ATS-clean CV — sourced from the
user's real CV library, never invented — plus a before/after keyword-coverage
score, a generation summary report, and a logged row in the applications
tracker (synced to Google Drive).

**Core principle — truth-preserving optimisation.** Reframe, reorder, and
re-emphasise real experience. Never fabricate a skill, metric, or
responsibility the user hasn't stated. If a JD requirement has no real
match, surface it as a gap. If a gap might be addressable via undocumented
experience, run an experience-discovery interview. Otherwise, note it plainly.

**Read `references/cv-formatting.md` before writing a single line.** It encodes
hard constraints (single-line bullets, no em dashes, keyword placement, font,
layout) and voice patterns established over many prior sessions with this
user — violating them is a bug, not a style choice.

**Read `references/cv-background.md` in Phase 0 to select the correct template**
(PRODUCT_CV or DATA_ARCHITECT_CV) based on role type, and to check confirmed
facts before flagging a gap.
- Use PRODUCT_CV for: Product Director, VP of Product, CPO, Senior Product
  Manager, Head of Product roles.
- Use DATA_ARCHITECT_CV for: Data Architect, Data Engineer, Analytics
  Engineer, Data Science roles.

**Recommendations section is removed from all CVs** (all role types). This
section is never included in tailored output.

## Trigger phrases

- "Tailor my CV to this JD/role/posting"
- "What's my ATS score for this?" / "Will this pass ATS?"
- A pasted job description or LinkedIn job posting
- "Help me apply for [Company]" / "Build me a CV for [Company/role]"
- "Log this application" / "add this to the tracker"
- "Batch these JDs" / "tailor for multiple roles at once"
- "Update my CV library with this"

## Workflow overview (9 phases)

| Phase | Name | Reference file |
|---|---|---|
| 0 | Intake & Context Assembly | `references/cv-background.md`, `references/cv-config.md` |
| 1 | Job Research | `references/cv-market-research.md` |
| 2 | Gap Assessment | `references/cv-background.md` |
| 2.5 | Experience Discovery (if gaps exist) | `references/cv-background.md` (written back to) |
| 3 | Scoring & Matching | `references/cv-scoring.md`, `references/cv-semantic-clusters.md` |
| 4 | Generation (draft text) | `references/cv-formatting.md` |
| 5.1 | QA Personas (on draft text, before render) | `references/cv-qa-personas.md`, `references/cv-decision-gates.md` |
| — | Render DOCX (internal PDF for validation only) | `references/cv-formatting.md` |
| 5.3 | Format Validation (on the render) | `references/cv-decision-gates.md` |
| 6 | Summary Report | — |
| 7 | Tracker Sync | `references/cv-tracker.md` |

For what happens when a phase fails a check, see `references/cv-decision-gates.md` —
that file is the authority on loop targets and pass/fail criteria; this file
just orchestrates the sequence.

**Why QA comes before rendering, not after:** the Hiring Manager and Talent
Acquisition lenses (5.1) review keywords, numbers, ordering, and title —
all text-level, all fixable without touching layout. Rendering is expensive
to redo. So content gets reviewed and looped on *as text* first; only once
it passes does it get rendered, and only render-dependent things (em dashes,
line wraps, PDF text extraction) get checked after that. This avoids
re-rendering a PDF just to fix a missing keyword.

## Phase 0 — Intake & Context Assembly

**Resume content.** In priority order:
1. Existing library at `resumes/*.md` in the working directory.
2. Attached CV file (PDF/DOCX).
3. Pasted CV text or LinkedIn profile.
4. No CV? Ask for one.

**Reference files (always check these first):**
- `references/cv-background.md` — confirmed facts per role (board/investor, BI tools,
  Design involvement, CRM/CDP/MarTech, notable absences), template
  selection, and title-blending rules. This is also where Phase 2.5 writes
  new confirmed facts, so re-read it if this is a repeat session.
- `references/cv-formatting.md` — hard constraints and voice on generation.
- `references/cv-scoring.md` — ATS coverage methodology.
- `references/cv-config.md` — file paths, GDrive folder IDs, workflow defaults.

**Job description input:**
- Pasted text (full posting) — preferred
- PDF/DOCX attached
- LinkedIn URL or pasted LinkedIn job text
- Job title + company (research from public postings)

**Speed mode.** Pick one before starting Phase 1 — this determines what
gets skipped, not what gets rushed; the truth-preserving core principle and
the Phase 5.3 render-validation checks never get skipped in any mode.

| | Quick | Balanced | Full Manual |
|---|---|---|---|
| **Trigger** | Default — a JD pasted with no other signal ("tailor my CV to this", just a paste) | "quick questions first" / role is mid-stakes | "do the full workflow" / "high-stakes role" / user asks for discovery |
| **Phase 1 research** | Skip web research; parse the JD text only | Full research, one checkpoint | Full research, one checkpoint |
| **Phase 1 checkpoint** | Skip — proceed straight to Phase 2 | Wait for confirmation | Wait for confirmation |
| **Phase 2.5 discovery** | Skip entirely — genuine gaps ship noted, no interview | Only for gaps that move the ATS score materially (cap at 2-3 questions) | Full interview for every addressable gap |
| **Phase 5.1 QA personas** | Skip — Phase 5.3 alone is the gate | Run once, no loop back if it's a near-pass on one lens only | Full, up to 2 rewrite loops |
| **Phase 5.3 validation** | Full — never skipped | Full | Full |
| **Phase 6 summary** | Short form: ATS score + gap list only | Full | Full |
| **Typical time** | 1-2 min | 15-20 min | 90-135 min |

If unsure which mode fits, ask once, briefly — don't default silently into
Full Manual, since that's the slowest path and wasn't asked for.

**Batch mode (if multiple JDs):**
If 2+ JDs, ask:
> "Want to batch these? I'll aggregate the gap analysis across all roles at
> once, run one discovery interview covering all gaps, then tailor each CV
> separately."

If yes: collect all JDs, proceed as batch. Batch mode uses Balanced or Full
speed by default — Quick mode's "no discovery" trade-off compounds badly
across multiple roles, so don't combine Quick + batch without saying so
explicitly.

## Phase 1 — Job Research

See `references/cv-market-research.md` for the full research and checkpoint procedure.
In brief: parse the JD into must-have / nice-to-have / implicit-signal
buckets, research the company and role benchmark, then present a 2-3 line
summary and wait for confirmation before proceeding — don't tailor against
an unconfirmed research read.

## Phase 2 — Gap Assessment

**Always check `references/cv-background.md` first**, specifically the "Confirmed
Facts by Role" section — it often pre-closes a gap before you need to ask
(e.g. board/investor exposure, BI tools, Design partnership, CRM/CDP/MarTech
all have JD-matching hints there).

Score each requirement: direct (90-100%) / transferable (75-89%) /
adjacent (60-74%) / gap (<60%). See `references/cv-decision-gates.md` for the three
paths a gap can take (genuine/not-recoverable, addressable, or doesn't
actually exist).

**Output:** Gap list with scores. Show top 1-2 candidate bullets per slot
with reasoning.

## Phase 2.5 — Experience Discovery (only if gaps exist)

If a gap appears in a domain the user is senior in, or if `references/cv-background.md`
hints at undocumented experience, run a brief discovery interview:

> I flagged a gap on "stakeholder reporting" but I noticed you have
> investor-facing work at Hybrid Theory. Did you do regular board or investor
> updates there?

For each gap, ask:
1. "Did you do this at [company] in [role]?" (check `references/cv-background.md` hints)
2. "How did you approach it? (Tools, outcomes?)"
3. "Proof points (metrics, feedback, talks)?"

Collect 1-2 sentences per gap. If confirmed:
1. Rewrite a truthful bullet for this CV.
2. **Append the confirmed fact to `references/cv-background.md` §2 (Confirmed Facts by
   Role)**, under the relevant role, with a JD-matching hint — the same
   format as the existing entries — so future sessions don't re-ask. This
   is the only way this interview's findings outlive the current session.

## Phase 3 — Scoring & Matching

**ATS Coverage Score (before/after)**, using the semantic-clustering method
in `references/cv-scoring.md` (cluster data lives in `references/cv-semantic-clusters.md`). This
is a **directional heuristic**, not a vendor algorithm — Workday, Greenhouse,
and Taleo each score differently; see `references/cv-scoring.md` for that caveat in
full and don't restate it elsewhere.

**Report:**
> Before (base CV): {score}%
> After (tailored): {score}%
> Remaining gaps: {gaps if any}

Target 85%+.

## Phase 4 — Generation (draft text, not yet rendered)

Produces the tailored *text*, not the file yet — rendering happens after
Phase 5.1 passes (see below). Read `references/cv-formatting.md` (hard constraints,
voice pattern, character budgets) before starting. Four sub-steps,
referenced by number from `references/cv-decision-gates.md`'s loop targets:

- **4.1 Profile rewrite** — mirror the JD's title language, front-load 3-4
  JD keywords in the first two sentences, apply title blending only where
  `references/cv-background.md` §3 justifies it (max 1-2 blended roles per CV).
- **4.2 Skills section regenerate** — JD-priority ordering (see
  `references/cv-formatting.md` for the current policy on how many non-JD skills, if
  any, can stay). No speculative tech — every skill listed must be true.
- **4.3 Bullet matching** — assign the highest-confidence bullet per slot
  from Phase 3's scoring; use the Action + Number + Method + Scale voice
  pattern from `references/cv-formatting.md`.
- **4.4 Bullet reordering** — surface JD-relevant work first within each
  role, even if it means moving older achievements up.

## Phase 5.1 — QA Personas (on the draft text, before rendering)

Two review lenses — Hiring Manager and Talent Acquisition — run on the
**draft text from Phase 4**, not a rendered file. Full checklists and
red/green-flag detail live in `references/cv-qa-personas.md`; pass/fail loop-back
targets live in `references/cv-decision-gates.md`. Both lenses must pass before moving
on. Skipped in Quick mode (see Phase 0's mode table).

## Render

Once Phase 5.1 passes:
1. Render DOCX (use the `docx` skill for the mechanics; this file only
   covers what's CV-specific).
2. **DOCX is the only deliverable** — see `references/cv-formatting.md`
   "Output Format" for why a self-generated PDF is never presented as the
   final artifact (font-substitution/pagination bug). A LibreOffice PDF is
   still produced internally for Phase 5.3's validation checks, but it is
   not shipped or stored as output.
3. Filename: `{YYYY-MM-DD}_{Company}_{Role}.docx`.
4. Output location: Google Drive `Interviews CV/claude-output/
   {YYYY.MM.DD}_{Company}_{Role}/` — example:
   `2026.09.14_Monzo_ChiefOfStaff/` containing the `.docx`.
5. Set DOCX core properties (Author) to the user's own name.

## Phase 5.3 — Format Validation (on the render)

Checks that only make sense once a real file exists: no em dashes, no
bullet wraps, `pdftotext -layout` reads clean. Full command sequence and
loop-back targets in `references/cv-decision-gates.md` §5.3. On failure, fix the
specific 4.x sub-step it points to, then **re-render only** (5.1 already
passed on this text — no need to re-run the content review unless the fix
changes wording meaningfully, e.g. trimming a bullet to fit the character
budget).

**Max iterations:** 2 full loops through 5.1 and 5.3 combined. If still
failing after 2, ship with notes and offer a follow-up session.

## Phase 6 — Summary Report

**Never skipped, in any mode** — Quick mode shortens it to ATS score + gap
list only (see the mode table in Phase 0), it doesn't remove it. A chat
session working without this file loaded is the likeliest way this gets
silently dropped — it did, in practice, once. If you're generating a CV
without `SKILL.md` in front of you, that's exactly the situation to watch
for.

After 5.1 and 5.3 both pass, output a markdown summary:

```markdown
# CV Summary: [Company] – [Role]

## ATS Coverage
- Before: X%
- After: Y%
- Keywords found: Z/[total]

## Gaps Addressed
- [Gap 1]: Addressed via [bullet/approach]
- [Gap 2]: Left as-is (noted elsewhere)
- [Gap 3]: No match (genuine gap)

## Key Reframings & Bullet Reordering
- Profile: Mirrored "[JD Title]" + surfaced [top 3 keywords]
- Skills: Narrowed to JD-priority order (removed speculative tech)
- Top bullets: Reordered to surface [domain] work first
- Titles: Blended [Functional Title] with [Actual Title] for role alignment

## Key Differentiators
- [Strongest proof point 1 from CV]
- [Strongest proof point 2]

## Interview Prep Hints
- Likely questions on [gap/strength], prepare [STAR story/proof point]
- [Company/role analogue in your background]
- Watch for [red flag], have examples ready for [related skill]
```

Share with the user before logging. No decision gate here — always ship the
report.

## Phase 7 — Tracker Sync

See `references/cv-tracker.md` for the full schema and update logic (a Google Sheets
tab inside the `Interviews CV` GDrive folder, one row appended per run —
never edits an existing row's Status).

Ask before logging:
> Ready to log to the tracker? I'll add the row with scores, file location,
> and summary.

## Edge Cases

1. **Thin library:** If <5 relevant bullets, say so. Offer to proceed or
   gather more context first.
2. **Research failure:** If JD is behind login or malformed, ask for text.
3. **No good match:** If <3 bullets transfer, flag as domain-mismatch risk.
4. **Batch complexity:** If 5+ JDs, split into (1) discovery + update, then
   (2) per-role generation.
5. **User requests fabrication:** "I can reframe that, but it wouldn't be
   true. Here's what's actually there. Use as-is or leave blank?"
6. **Multiple applications to same company:** Check the tracker (Phase 0).
   See `references/cv-decision-gates.md` for same-role vs. different-role handling.
7. **Solution Architect / Enterprise Architect JD:** No template exists yet
   (`references/cv-config.md`'s template rules flag this explicitly). Don't force
   PRODUCT_CV or DATA_ARCHITECT_CV silently — ask whether to use one as a
   starting structure and build the variant now, or hold off.

## Validation Checklist

Before handing off:
- [ ] No em dashes (grep + visual)
- [ ] No bullet wraps (visual PDF check)
- [ ] pdftotext readable (spot-check 3-4 bullets)
- [ ] Filename: `{YYYY-MM-DD}_{Company}_{Role}`
- [ ] GDrive location correct
- [ ] Tracker row ready
- [ ] Summary report generated
- [ ] User confirmed before logging
