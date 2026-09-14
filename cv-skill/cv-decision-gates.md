# Decision Gates & Rewrite Loops

Explicit logic for what happens when checks fail, how to resolve conflicts, and when to ship vs. iterate.

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
3. Add confirmed details to cv-career-history-supplement
4. Continue to Phase 3 with updated base CV

### Path C: Gap Doesn't Actually Exist
**Example:** JD says "board-level reporting experience" and cv-job-context.md already lists Hybrid Theory, OneAdvanced, dunnhumby.

**Action:**
1. Close the gap immediately
2. Note in Phase 3 that this is covered
3. Proceed to Phase 3 (scoring & matching)

---

## Phase 5.3: Validation → Decision Gate

**Input:** Generated PDF of tailored CV

**Checks:**
1. grep "—" on pdftotext output → 0 matches (no em-dashes)
2. Visual PDF check → no bullets wrap to second line
3. pdftotext -layout output → readable, sensible text extraction

### Check 1 Fails: Em-dashes Found

**Root cause:** Likely in profile, bullets, or role context line

**Action:**
1. Identify which section has em-dashes
2. Loop back to Phase 4.1 (profile rewrite) if em-dashes in profile
3. Or loop back to Phase 4.3 (bullet matching) if em-dashes in bullets
4. Replace em-dashes with commas, semicolons, or split into two sentences
5. Re-render DOCX → PDF
6. Re-validate
7. If pass, proceed to Phase 5.5

### Check 2 Fails: Bullet Wraps to Second Line

**Root cause:** Bullet text exceeds ~90 char budget (including spaces)

**Action:**
1. Identify which bullets wrap
2. Loop back to Phase 4.4 (bullet reordering/shortening)
3. Trim each over-budget bullet: cut adjectives, collapse phrases, or break into two separate points (only if justified)
4. Re-render DOCX → PDF
5. Re-validate
6. If pass, proceed to Phase 5.5

### Check 3 Fails: pdftotext Unreadable

**Root cause:** Usually heading structure, embedded images, or PDF corruption

**Action:**
1. Re-generate DOCX from scratch (suspected rendering issue)
2. Simplify formatting: remove tables, remove bold/italics if present, use plain Calibri Light only
3. Re-render PDF
4. Re-validate
5. If still fails, ask user: "PDF extraction failed. Suspect formatting issue. Should I regenerate with simpler structure?"

### All Checks Pass

**Action:**
1. Proceed to Phase 5.5 (QA Personas review)

---

## Phase 5.5: QA Personas → Decision Gate

Two independent review lenses: **Hiring Manager (HM)** and **Talent Acquisition (TA)**. Both must pass.

### Hiring Manager Lens: Checks

1. **Specific problem understanding:** Does the CV show that you understood the role's core challenge? (e.g., "search/discovery is central to this role, and I've done this work at scale")
2. **3+ numbers in top bullets:** Do top 1-2 bullets per role include metrics? (e.g., "500M+ queries," "40% growth")
3. **Hands-on IC visible:** If JD emphasizes "hands-on," does the CV show execution, not just oversight?
4. **Scale match:** Does the CV's scale (team size, revenue impact, user count) match the role's scale?
5. **Recency:** Are the most relevant achievements recent enough? (Within last 5 years is typical for IC roles)

**Fails if:**
- Top bullets lack numbers or impact statements
- "Hands-on IC" emphasis in JD but CV shows only management
- Scale mismatch (e.g., led 100-person team for IC role)
- Most relevant work is >8 years old

**Action if fails:**
1. Identify which check failed
2. Loop back to Phase 4.1 (profile rewrite) if problem understanding is weak
3. Loop back to Phase 4.3 (bullet matching) if lacking metrics or hands-on IC visibility
4. Loop back to Phase 4.4 (bullet reordering) if recency/scale mismatch
5. Re-run QA Personas
6. If pass, proceed to Phase 6

### Talent Acquisition Lens: Checks

1. **JD keywords in profile:** Do the first 2 sentences of the profile include 3-4 JD keywords? (e.g., "search," "discovery," "B2B SaaS")
2. **Title matches search:** Does the profile title match (or reasonably align with) what a recruiter searches? (e.g., JD: "Senior Product Director" → Profile: "Senior Product Director" or "VP of Product")
3. **Relevant bullets surfaced first:** Are JD-relevant bullets in the top 1-2 per role, not buried?
4. **Skills section tailored:** Does the skills line include JD keywords only, no speculative tech?
5. **LinkedIn URL present (Product roles only):** If this is a Product role, is LinkedIn URL in profile?

**Fails if:**
- Profile starts with generic "Product executive" instead of "Senior Product Director"
- Keywords from JD (search, CDP, AI) missing from profile entirely
- Most JD-relevant bullets are in the 3rd or 4th position of a role
- Skills section includes tech not mentioned in JD
- LinkedIn URL missing for Product role

**Action if fails:**
1. Identify which check failed
2. Loop back to Phase 4.1 (profile rewrite) if keywords missing or title mismatches
3. Loop back to Phase 4.2 (skills section regenerate) if tools are speculative
4. Loop back to Phase 4.4 (bullet reordering) if relevant bullets buried
5. Re-run QA Personas
6. If pass, proceed to Phase 6

### Conflict Resolution: HM Pass, TA Fail (or vice versa)

**If HM passes but TA fails:**
- TA failures are about discoverability (ATS, keyword matching, title matching)
- Fix with targeted Phase 4.1 (profile rewrite) to add keywords and mirror title
- Re-run QA; if TA passes, HM usually still passes (we didn't remove impact)

**If TA passes but HM fails:**
- HM failures are about execution/impact clarity (numbers, hands-on IC, scale)
- Fix with targeted Phase 4.3 (bullet matching) to add metrics or Phase 4.4 (reordering) to surface execution
- Re-run QA; if HM passes, TA usually still passes (we didn't remove keywords)

**If both fail:**
- Loop back to Phase 4.1 (full profile rewrite incorporating keywords AND impact)
- Then Phase 4.2 (skills regenerate, JD-only)
- Then Phase 4.4 (reorder to surface both keywords and metrics)
- Re-run QA

### All Checks Pass (Both HM & TA)

**Action:**
1. Proceed to Phase 6 (summary report)

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
- All validation checks pass (Phase 5.3)
- Both QA Personas pass (Phase 5.5)
- Gaps are documented in the summary report but not forcing fabrication

### Iterate (loop back to a phase):
- Validation check fails → loop back to Phase 4.x (rewrite)
- HM Lens fails → loop back to Phase 4.1 or 4.3 (metrics/execution)
- TA Lens fails → loop back to Phase 4.1 or 4.2 (keywords/title)
- User requests changes after QA → loop back to relevant phase (4.1, 4.2, 4.4)

**Max iterations:** Typically 2 full loops through 5.3-5.5. If still failing after 2 iterations, ship with notes and offer a follow-up session.

---

## Multiple Applications to Same Company

### Scenario: User applies to Company X for Role A, then later applies to Company X for Role B (different role)

**Action:**
1. Check the tracker (Phase 0 Intake)
2. If same role at same company → note as "reapplication," update existing row, flag with timestamp
3. If different role at same company → create new row, note the prior application in comments
4. If role appears to be same but with minor JD variation → ask user: "Is this the same role as [prior application] or a different opening?"

### Scenario: User wants to reapply to the same role after 3 months

**Action:**
1. Note the reapplication in tracker
2. Flag that prior CV was for this role
3. Proceed with fresh tailoring (JD may have changed, market may have shifted)
4. Compare before/after ATS score to show improvement in the summary report
