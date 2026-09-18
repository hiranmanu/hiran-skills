# Decision Gates & Rewrite Loops

Explicit logic for what happens when checks fail, how to resolve conflicts, and when to ship vs. iterate. This file owns the *decision logic* — pass/fail, loop targets, conflict resolution. It doesn't restate the QA checklists themselves; those live in `cv-qa-personas.md` so there's one copy, not two.

---

## Phase 2: Gap Assessment → Decision Gate

**Input:** List of flagged gaps from comparing CV against JD requirements.

**Decision question:** Is this gap addressable?

### Path A: Genuine Gap, Not Recoverable
**Example:** JD requires "CFO experience" and Hiran has no CFO background.

**Action:**
1. Note the gap plainly in the summary report (Phase 6)
2. Don't force or fabricate
3. Ship the CV anyway
4. In interview prep hints, suggest ways to speak to adjacent experience ("P&L management" instead of "CFO role")

### Path B: Gap Might Be Addressable
**Example:** JD mentions "first-party data strategy" and Hiran has done this work but it's not prominent in the base CV.

**Action:**
1. Loop back to Phase 2.5 (experience discovery interview)
2. Ask: "Did you do [specific work]? Can you tell me about it?"
3. Add confirmed details to `cv-background.md` §2 (Confirmed Facts by Role)
4. Continue to Phase 3 with updated base CV

### Path C: Gap Doesn't Actually Exist
**Example:** JD says "board-level reporting experience" and `cv-background.md` §2 already lists Hybrid Theory, OneAdvanced, dunnhumby.

**Action:**
1. Close the gap immediately
2. Note in Phase 3 that this is covered
3. Proceed to Phase 3 (scoring & matching)

---

## Phase 5.1: QA Personas → Decision Gate (runs BEFORE rendering, on draft text)

**Input:** Draft profile, skills, and bullets from Phase 4 — no rendered file exists yet. Full checklists (with the reasoning and red/green-flag detail behind each check) live in `cv-qa-personas.md` — read that first, then come back here for what to do on failure.

Two independent lenses, both must pass: **Hiring Manager (HM)** and **Talent Acquisition (TA)**.

### HM Lens fails

**Action:**
1. Identify which check failed (see `cv-qa-personas.md`'s HM checklist)
2. Loop back to Phase 4.1 (profile rewrite) if problem understanding is weak
3. Loop back to Phase 4.3 (bullet matching) if lacking metrics or hands-on IC visibility
4. Loop back to Phase 4.4 (bullet reordering) if recency/scale mismatch
5. Re-run Phase 5.1 on the revised draft text (still pre-render — no render cost yet)
6. If pass, proceed to Render

### TA Lens fails

**Action:**
1. Identify which check failed (see `cv-qa-personas.md`'s TA checklist)
2. Loop back to Phase 4.1 (profile rewrite) if keywords missing or title mismatches
3. Loop back to Phase 4.2 (skills section regenerate) if tools are speculative
4. Loop back to Phase 4.4 (bullet reordering) if relevant bullets buried
5. Re-run Phase 5.1 on the revised draft text
6. If pass, proceed to Render

### Conflict Resolution: HM Pass, TA Fail (or vice versa)

**If HM passes but TA fails:**
- TA failures are about discoverability (ATS, keyword matching, title matching)
- Fix with targeted Phase 4.1 (profile rewrite) to add keywords and mirror title
- Re-run Phase 5.1; if TA passes, HM usually still passes (we didn't remove impact)

**If TA passes but HM fails:**
- HM failures are about execution/impact clarity (numbers, hands-on IC, scale)
- Fix with targeted Phase 4.3 (bullet matching) to add metrics or Phase 4.4 (reordering) to surface execution
- Re-run Phase 5.1; if HM passes, TA usually still passes (we didn't remove keywords)

**If both fail:**
- Loop back to Phase 4.1 (full profile rewrite incorporating keywords AND impact)
- Then Phase 4.2 (skills regenerate)
- Then Phase 4.4 (reorder to surface both keywords and metrics)
- Re-run Phase 5.1

### Both Lenses Pass

**Action:** Proceed to Render, then Phase 5.3.

---

## Render

Renders the DOCX from the text that just passed Phase 5.1 (plus an internal-only PDF for Phase 5.3's validation checks — never a shipped deliverable). See `SKILL.md` "Render" section for the mechanics (filenames, local output path, metadata).

---

## Phase 5.3: Format Validation → Decision Gate (runs AFTER rendering)

**Input:** Rendered PDF of the tailored CV.

**Run, in order, every time:**
1. Render the DOCX using the `docx` skill's own build/verify pattern (soffice → PDF).
2. Run the automated check: `python3 scripts/validate_cv.py <path-to.docx> --max-pages 2`
   — this runs checks 2-4 below (em/en dashes, bullet-wrap detection, role-page-split
   detection) plus the page-count cap in one pass and exits non-zero on any failure.
   It replaces doing these by hand; still read the rendered page images for anything
   it flags, since its wrap/split detection is a heuristic over `pdftotext -layout`
   output, not a true layout engine (see the script's docstring for exact limits).
3. `pdftoppm -jpeg -r 100 output.pdf page` and read the resulting page image(s) —
   `validate_cv.py` doesn't replace looking at it; skills/layout issues outside its
   four checks (colour, alignment, font substitution) still need eyes on it.
4. `pdftotext -layout output.pdf -` → read it back; it should come back as
   clean, ordered, readable text in the same sequence as the visual
   document. Garbled, reordered, or dropped sections mean the layout (a
   table, text box, multi-column section) will confuse a real ATS parser
   too — fix the layout, don't just accept the garbled extraction.

These are render-dependent by nature — they can't be checked on draft text,
which is why they run after Render rather than folded into Phase 5.1.

### Check 1 Fails: Em-dashes Found

**Root cause:** Likely in profile, bullets, or role context line

**Action:**
1. Identify which section has em-dashes
2. Loop back to Phase 4.1 (profile rewrite) if em-dashes in profile
3. Or loop back to Phase 4.3 (bullet matching) if em-dashes in bullets
4. Replace em-dashes with commas, semicolons, or split into two sentences
5. Re-render DOCX → PDF (no need to re-run Phase 5.1 for a punctuation-only fix)
6. Re-validate (Phase 5.3)
7. If pass, proceed to Phase 6

### Check 2 Fails: Bullet Wraps to Second Line

**Root cause:** Bullet text exceeds ~90 char budget (including spaces)

**Action:**
1. Identify which bullets wrap
2. Loop back to Phase 4.4 (bullet reordering/shortening)
3. Trim each over-budget bullet: cut adjectives, collapse phrases, or break into two separate points (only if justified)
4. Re-render DOCX → PDF
5. Re-validate (Phase 5.3) — and re-run Phase 5.1 only if the trim removed a keyword or metric, since that's a content change, not just a formatting one
6. If pass, proceed to Phase 6

### Check 3 Fails: pdftotext Unreadable

**Root cause:** Usually heading structure, embedded images, or PDF corruption

**Action:**
1. Re-generate DOCX from scratch (suspected rendering issue)
2. Simplify formatting: remove tables, remove bold/italics if present, use plain Calibri Light only
3. Re-render PDF
4. Re-validate (Phase 5.3)
5. If still fails, ask user: "PDF extraction failed. Suspect formatting issue. Should I regenerate with simpler structure?"

### All Checks Pass

**Action:** Proceed to Phase 6 (summary report).

---

## Phase 6: Summary Report

**No decision gate.** Always ship. Report includes:
- Gaps addressed (what was changed and why)
- Reframings (how was experience positioned differently)
- Differentiators (unique strengths highlighted)
- Interview prep hints (how to speak to gaps or weak areas)
- ATS score before/after

---

## When to Ship vs. Iterate

### Ship (accept the CV as-is, move to Phase 7):
- Both QA Personas pass (Phase 5.1)
- All format validation checks pass (Phase 5.3)
- Gaps are documented in the summary report but not forcing fabrication

### Iterate (loop back to a phase):
- HM Lens fails (Phase 5.1) → loop back to Phase 4.1 or 4.3 (metrics/execution)
- TA Lens fails (Phase 5.1) → loop back to Phase 4.1 or 4.2 (keywords/title)
- Format validation fails (Phase 5.3) → loop back to Phase 4.x (rewrite), re-render
- User requests changes after either gate → loop back to relevant phase (4.1, 4.2, 4.4)

**Max iterations:** Typically 2 full loops through 5.1 + Render + 5.3. If still failing after 2 iterations, ship with notes and offer a follow-up session.

---

## Multiple Applications to Same Company

There's no tracker to check this against — ask the user directly.

### Scenario: User applies to Company X for Role A, then later applies to Company X for Role B (different role)

**Action:**
1. Ask: "Is this the same role you applied for before, or a different opening?"
2. If different role → proceed as a fresh tailoring run, no special handling needed.
3. If it might be the same role with a minor JD variation → confirm with the user before treating it as a reapplication.

### Scenario: User wants to reapply to the same role after some time has passed

**Action:**
1. Confirm this is a reapplication to the same role.
2. Proceed with fresh tailoring (JD may have changed, market may have shifted).
3. Compare before/after ATS score to show improvement in the summary report.
