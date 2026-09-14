---
name: cv-tailoring
description: >
  Tailors a CV/resume to a specific job description for CPO/VP Product, Data
  Architect, Solution/Enterprise Architect, and related senior product/data
  roles. Scores ATS keyword coverage (target 85%+), generates DOCX + PDF with
  timestamps, and syncs the application to Google Drive tracker. Supports batch
  processing of multiple JDs, experience discovery when gaps appear, and
  generates a summary report per CV.
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

**Read `cv-formatting-rules.md` before writing a single line.** It encodes
hard constraints (single-line bullets, no em dashes, keyword placement)
established over many prior sessions with this user — violating them is a
bug, not a style choice.

## Trigger phrases

- "Tailor my CV to this JD/role/posting"
- "What's my ATS score for this?" / "Will this pass ATS?"
- A pasted job description or LinkedIn job posting
- "Help me apply for [Company]" / "Build me a CV for [Company/role]"
- "Log this application" / "add this to the tracker"
- "Batch these JDs" / "tailor for multiple roles at once"
- "Update my CV library with this"

## Workflow Overview

1. **Phase 0: Intake & Context Assembly** — Load CV library, reference files,
   and JD(s). For batch: aggregate research and gaps across all JDs.
2. **Phase 1: Job Research** — Extract role profile, key requirements, company
   context. Checkpoint with user before proceeding.
3. **Phase 2: Gap Assessment** — Check `cv-job-context.md` and
   `cv-career-history-supplement.md` first. Flag unconfirmed gaps.
4. **Phase 2.5: Experience Discovery (if gaps exist)** — Interview to surface
   undocumented work, past roles used a skill, adjacent experience.
5. **Phase 3: Scoring & Matching** — ATS coverage before/after. Assign bullets
   to slots with confidence scoring.
6. **Phase 4: Generation** — Produce tailored DOCX + PDF with timestamp. Validate
   for line wraps, em dashes, ATS parseability.
7. **Phase 5: Summary Report** — Per-CV markdown: gaps addressed, reframings,
   key differentiators, interview-prep hints.
8. **Phase 6: Tracker Sync** — Log to Google Drive `Interviews CV` folder,
   store PDF/DOCX in `claude-output/<timestamp>_<Company>_<Role>/`.

## Phase 0 — Intake & Context Assembly

**Resume content.** In priority order:
1. Existing library at `resumes/*.md` in the working directory.
2. Attached CV file (PDF/DOCX).
3. Pasted CV text or LinkedIn profile.
4. No CV? Ask for one.

**Reference files (always check these first):**
- `cv-job-context.md` — undocumented background (board/investor, BI tools,
  Design involvement per role) with JD-matching hints.
- `cv-career-history-supplement.md` — confirmed facts per role.
- `cv-formatting-rules.md` — hard constraints on generation.
- `cv-scoring.md` — ATS coverage methodology.

**Job description input:**
- Pasted text (full posting) — preferred
- PDF/DOCX attached
- LinkedIn URL or pasted LinkedIn job text
- Job title + company (research from public postings)

**Batch mode (if multiple JDs):**
If 2+ JDs, ask:
> "Want to batch these? I'll aggregate the gap analysis across all roles at
> once, run one discovery interview covering all gaps, then tailor each CV
> separately."

If yes: collect all JDs, proceed as batch.

## Phase 1 — Job Research

Parse each JD for:
- **Role profile:** Title, seniority, primary function, key outcomes.
- **Key requirements:** Hard skills, title/function terms, business domain.
- **Company context:** Industry, scale, business model, recent news/funding.
- **Red flags:** Impossible combinations, malformed posting, skills don't align.

**Checkpoint (critical — don't skip):**

Present your research as a 2-3 line summary with 3-4 key findings:

> Based on research: {success profile}.
> Key findings: {finding 1} / {finding 2} / {finding 3}.
> Does this match your read, or anything to adjust?

Wait for confirmation before proceeding.

## Phase 2 — Gap Assessment

**Always check reference files first:**
1. Read `cv-job-context.md`. If JD mentions "investor relations" or "board
   reporting," check the board/investor section before flagging a gap.
2. Read `cv-career-history-supplement.md` for confirmed facts.
3. Score each requirement: direct (90-100%) / transferable (75-89%) /
   adjacent (60-74%) / gap (<60%).

**Output:** Gap list with scores. Show top 1-2 candidate bullets per slot
with reasoning.

## Phase 2.5 — Experience Discovery (only if gaps exist)

If a gap appears in a domain you're senior in, or if `cv-job-context.md`
hints at undocumented experience, run a brief discovery interview:

> I flagged a gap on "stakeholder reporting" but I noticed you have
> investor-facing work at Hybrid Theory. Did you do regular board or investor
> updates there?

For each gap, ask:
1. "Did you do this at [company] in [role]?" (Check cv-job-context hints)
2. "How did you approach it? (Tools, outcomes?)"
3. "Proof points (metrics, feedback, talks)?"

Collect 1-2 sentences per gap. If confirmed, rewrite a truthful bullet and
update `cv-career-history-supplement.md`.

## Phase 3 — Scoring & Matching

**ATS Coverage Score (before/after).**

This is a **directional heuristic**, not a vendor algorithm. Workday,
Greenhouse, Taleo each score differently.

**Method:**
1. From Phase 1 research, pull three keyword sets:
   - Hard skills (tools, platforms, methodologies) — weight **2x**
   - Title/function terms — weight **1.5x**
   - Business context (industry, scale, domain) — weight **1x**
2. Check presence in CV text: exact match or clear synonym.
3. Weighted found ÷ weighted total = coverage percentage.

**Report:**
> Before (base CV): {score}%
> After (tailored): {score}%
> Remaining gaps: {gaps if any}

Target 85%+.

## Phase 4 — Generation

**Input:** Template variant, selected bullets per slot, custom text.

**Process:**
1. Render DOCX.
2. Convert to PDF via LibreOffice.
3. **Validate:**
   - No em dashes (grep check)
   - No bullet wraps (visual check)
   - ATS parseability (pdftotext check)
   - Filename: `{YYYY-MM-DD}_{Company}_{Role}`

**Output location:**
Google Drive `Interviews CV/claude-output/{YYYY.MM.DD}_{Company}_{Role}/`
with both DOCX and PDF.

Example: `2026.09.14_Monzo_ChiefOfStaff/` containing both files.

## Phase 5 — Generation & Validation

**Before generating DOCX:**
1. Compute honest ATS score using keyword-presence methodology (see cv-scoring.md)
2. Build the tailored profile using JD-title mirroring and keyword-first placement
3. Rebuild skills section using JD-only keywords (no speculative tech)
4. Reorder bullets to surface JD-relevant work first (search/discovery/ranking → hands-on IC → commercial)
5. Apply blended titles where scope justifies it (e.g., "Senior Product Director, VP of Product")

**Validation:**
- No em dashes (grep "—" on PDF text extract)
- No bullet wraps (visual PDF check)
- pdftotext -layout readable (spot-check 3-4 bullets)
- Filename format: {YYYY-MM-DD}_{Company}_{Role}

## Phase 6 — Generation Summary Report

After generation, output a markdown summary:

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
- Skills: Narrowed to JD-only keywords (removed speculative tech)
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

Share with user before logging.

## Phase 6 — Tracker Sync

Google Sheets `Interviews CV` tracker row:
- **Date Applied:** {today}
- **Company:** {company}
- **Role:** {role}
- **CV Variant:** {template used}
- **JD Source:** {URL or "pasted"}
- **ATS Score Before:** {%}
- **ATS Score After:** {%}
- **CV File Used:** Link to GDrive folder
- **Status:** "Applied"
- **Next Action:** {user fills}
- **Notes:** {gaps, differentiators, prep hints}

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

## Validation Checklist

Before handing off:
- [ ] No em dashes (grep + visual)
- [ ] No bullet wraps (visual PDF check)
- [ ] pdftotext readable (spot-check 3-4 bullets)
- [ ] Filename: {YYYY-MM-DD}_{Company}_{Role}
- [ ] GDrive location correct
- [ ] Tracker row ready
- [ ] Summary report generated
- [ ] User confirmed before logging
