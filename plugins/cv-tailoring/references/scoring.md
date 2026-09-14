# Matching and scoring (Phase 3 + Phase 5)

Two separate scores happen in this skill. Don't conflate them.

## A. Bullet-match confidence (which content goes where)

For each slot in the chosen template, score every candidate bullet from the
library against the JD requirement it could fill:

- **Direct (90-100%)** — same keyword, domain, technology, and outcome type.
- **Transferable (75-89%)** — same capability demonstrated in a different
  context.
- **Adjacent (60-74%)** — related tools/methods/problem space, real gap in
  directness.
- **Weak/gap (<60%)** — flag it, don't force it. Offer the user options:
  reframe truthfully, omit the slot, or note the gap for the cover letter
  (once that skill exists).

Show the top 1-2 candidates per slot with the reasoning, not just the
winner — this user reads the working, not just the output (see
`formatting-rules.md` and this project's ways-of-working notes: iterative,
section-by-section, wants the reasoning shown).

Never reframe a bullet past what's truthful. A title or emphasis shift is
fine ("Graduate Researcher" → "Research Software Engineer" if the work was
genuinely coding-heavy); claiming scope, seniority, or outcomes that didn't
happen is not, regardless of how well it would score.

## B. ATS keyword-coverage score (before/after)

This is a **transparent heuristic this skill computes**, not a proprietary
vendor algorithm. Say so every time it's shown — Workday, Greenhouse,
Taleo, iCIMS etc. each score differently and don't publish the method, so
this is a directional coverage signal, not a predicted outcome.

**Method:**

1. From the Phase 1 JD parse, pull three keyword sets:
   - Hard skills (tools, platforms, named methodologies, certifications) —
     weight **2x**
   - Title/function terms (the role title and close synonyms) — weight
     **1.5x**
   - Business/domain context terms (industry, business model, scale
     language) — weight **1x**
2. For each set, check presence in the CV text — exact match or a clear
   synonym (e.g. "A/B testing" ~ "A/B test", "stakeholder management" ~
   "cross-functional stakeholder alignment"). Don't count a loose thematic
   match as coverage.
3. Score = weighted found / weighted total, as a percentage.
4. Run this once against the **unedited base variant** (Phase 3, "before")
   and once against the **finished tailored CV** (Phase 5, "after").

**Report format:**

> ATS coverage: 58% → 84% (+26pts)
> Still missing: {term} (hard skill, not in library — real gap, not a
> writing problem), {term} (present but only in an older role, consider
> resurfacing)

Keep the "still missing" list honest — a term with no real backing in the
library stays listed as a gap rather than getting quietly keyword-stuffed
into the skills line to close the score. A high coverage score on a CV that
doesn't survive an interview is a worse outcome than a lower, honest one.

**Before finalizing the "still missing" list, ask.** A gap flagged from the
base CV alone is often just unstated, not absent — this user has repeatedly
turned out to have real experience (board/investor work, BI tools, owning
Design) that simply wasn't in the library yet. Don't present a gap as final
without a quick confirm/deny from the user first. If confirmed, get the
specific role/company/tool needed to write a real bullet (not a vague
add-on), fold it into the library and the tailored CV, then rescore —
in the same pass, not a separate round-trip.
