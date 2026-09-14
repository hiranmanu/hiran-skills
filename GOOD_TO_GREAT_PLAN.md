# Good to Great Improvement Plan

Each file in the CV tailoring skill is currently functional (good), but there are specific, targeted improvements that would make each one great. This plan prioritizes by impact and effort.

---

## File-by-File Improvement Plan

### 1. cv-formatting.md (Currently: Good → Target: Great)

**Current State:** Covers hard constraints, voice pattern, validation rules. Clear and actionable.

**What's Missing:**
- [ ] **Real examples of em-dash replacement** — show "—" and what to replace it with in actual bullets
- [ ] **Line-wrap examples** — show a 120-char bullet that needs trimming and how to fix it
- [ ] **Before/after pairs for voice pattern** — not just theory, show actual CV bullets fixed
- [ ] **Font rendering notes** — why Calibri Light over Calibri Regular? ATS parsing differences?
- [ ] **PDF vs. DOCX differences** — does line-breaking change when converting? Edge cases?
- [ ] **Sub-bullet style guide** — show actual ○ character in context (currently just says "○")
- [ ] **LinkedIn URL formatting edge case** — what if user's LinkedIn URL has special characters?

**Effort to Great:** Medium (1-2 hours) — Mostly adding examples and explaining rationale

**Impact:** High — Users will have concrete before/after examples to copy, not just rules

**Specific Additions:**
```markdown
### Example: Em-Dash Replacement
Before: "Won $28M — the largest AdTech deal ever closed"
After:  "Won $28M, the largest AdTech deal ever closed"
OR:     "Won $28M; it was the largest AdTech deal ever closed"

### Example: Line-Wrap Fix
Before (126 chars, wraps): "Launched AI-powered recommendations engine using LLMs, increasing user engagement by 28% and generating £2M+ new revenue"
After (89 chars, fits):    "Launched AI-powered recommendations engine using LLMs, generating £2M+ new revenue"

### Font Rendering Note
Calibri Light renders slightly wider than Calibri Regular in most PDFs, giving more breathing room on dense pages.
This helps with ATS parsing: tight spacing can cause some systems to misread line breaks.
```

---

### 2. cv-background.md (Currently: Good → Target: Great)

**Current State:** Well-organized, clear sections, actionable hints. Good structure.

**What's Missing:**
- [ ] **Real role context details** — currently lists roles but doesn't say what was done/learned
- [ ] **Regulator exposure clarified** — GDPR mentioned but what specifically was the work?
- [ ] **BI tools usage context** — which tools used for what? (Power BI for dashboards, Looker for customer analytics, etc.)
- [ ] **Design function clarity** — did he hire, lead, or partner? Different for each role? Currently bundles all.
- [ ] **CRM/CDP work specifics** — which platforms, what integrations, what was the outcome?
- [ ] **Template selection decision tree with examples** — "if you see X keywords, choose Y template"
- [ ] **Title blending edge cases** — "what if JD asks for 'Product Manager' and I have 'VP of Product'?" (too senior, don't blend)

**Effort to Great:** Medium-High (2-3 hours) — Needs detail expansion and decision tree flowchart

**Impact:** High — Users will know exactly which template to use and what context to reference

**Specific Additions:**
```markdown
### Design Function: Role-by-Role Breakdown
- Hybrid Theory (CPO): Owned 1 designer, grew to 3-person team. Hired Head of Design. Responsible for all design strategy.
- dunnhumby (current): Partner with external design agency. Weekly collaboration on UX, no direct reports.
- OneAdvanced: Worked with in-house Design. Drove alignment on product portfolio redesign.

### Template Selection Decision Tree
JD mentions:
├─ "Data architecture" OR "ETL" OR "data platform" OR "Snowflake/BigQuery"
│  └─ Use DATA_ARCHITECT_CV
├─ "Product strategy" OR "roadmap" OR "vision" OR "B2B SaaS" OR "go-to-market"
│  └─ Use PRODUCT_CV
└─ Unclear?
   └─ Ask user: "Is this a data role or a product role?"

### Title Blending: When NOT to Blend
DON'T: "Product Manager, VP of Product" (title already higher than asked)
DO:    "Senior Product Manager, VP of Product" (if JD emphasizes hands-on, IC, show that title is lower/more hands-on)
```

---

### 3. cv-semantic-clusters.md (Currently: Good → Target: Great)

**Current State:** Comprehensive clusters, term-to-cluster mappings. Well-structured.

**What's Missing:**
- [ ] **Scoring examples with real JD keywords** — show how to score "MarTech" cluster against actual CV
- [ ] **Semantic "distance" weighting (optional)** — "Salesforce" scores higher for MarTech than "CRM systems"?
- [ ] **Hiran-specific clusters beyond generic roles** — "Retail Media Measurement" cluster with specific terms
- [ ] **Context penalty logic** — how to handle "search" in "CEO search firm" vs. "search algorithm"?
- [ ] **Cluster combinations** — when keywords from 2 clusters appear together (e.g., "CDP + MarTech"), does it score higher?
- [ ] **Role-specific ATS targets** — "Data Architect role needs 80% on data clusters + 20% on leadership clusters"
- [ ] **Cluster coverage by role** — "a Product Director CV should hit 60%+ of Product cluster, 40%+ of Hands-on IC cluster"

**Effort to Great:** High (3-4 hours) — Needs testing against real JDs and score validation

**Impact:** Medium-High — Makes scoring reproducible and testable

**Specific Additions:**
```markdown
### Scoring Example: Product Director Role + MarTech JD
JD keywords: "MarTech", "CDP", "lead scoring", "customer data"

Step 1: Extract core cluster
MarTech cluster = [marketing automation, Salesforce, HubSpot, Marketo, lead scoring, email, campaigns, CDP, customer data]

Step 2: Score CV against cluster
CV mentions: "Salesforce integrations" (1pt) + "marketing automation connectors" (1pt) + "lead-scoring workflows" (1pt)
Score: 3/8 = 37.5%

Step 3: Compare to target
Target for "MarTech" keyword: 70%+
This CV: 37.5% (gap identified, needs reframing or additional bullets)

### Hiran-Specific Cluster: Retail Media Measurement
Core keywords: retail media, measurement, attribution, media networks
Cluster: [first-party data, identity resolution, clean rooms, advertiser outcomes, media network partners, data activation, privacy & consent, GDPR, measurement framework, attribution modeling, retail analytics, brand safety, data marketplace]
```

---

### 4. cv-tailoring.md (Currently: Good → Target: Great)

**Current State:** 6-phase workflow with decision gates. Clear orchestration.

**What's Missing:**
- [ ] **Phase-by-phase time estimates** — how long does each phase take?
- [ ] **Batch processing rules** — if doing 5 JDs at once, what changes? (Phase 1 research shared, Phase 3 gaps aggregated, etc.)
- [ ] **Backtrack rules** — if in Phase 5, can we loop back to Phase 2? (No, data is stale. Must restart application.)
- [ ] **Conflict resolution: user input vs. automation** — if user says "add this skill" but it's fabrication, how do we handle?
- [ ] **Edge case: discovering new gaps mid-workflow** — if Phase 3 scoring finds gaps we didn't catch in Phase 2, what do we do?
- [ ] **ATS score weighting** — is a 75% score acceptable or push for 85%?
- [ ] **GDrive sync error handling** — what if the upload to GDrive fails? Retry? Notify user?

**Effort to Great:** Medium (2 hours) — Mostly adding time estimates and edge case handling

**Impact:** Medium — Makes workflow timing predictable, reduces user friction

**Specific Additions:**
```markdown
## Phase Time Estimates

| Phase | Typical Time | Notes |
|-------|--------------|-------|
| Phase 0: Intake | 5 min | Load files, parse JD |
| Phase 1: Research | 15 min | Company research, role profile, checkpoint |
| Phase 2: Gap Assessment | 10 min | Check background.md, flag gaps |
| Phase 2.5: Discovery (if gaps) | 15-30 min | Interview, update supplement |
| Phase 3: Scoring | 15 min | Before score, assign bullets, after score |
| Phase 4: Tailoring | 20-30 min | Rewrite profile, skills, bullets, reorder |
| Phase 5: Generation | 10 min | DOCX render, PDF convert, validate |
| Phase 5.5: QA Personas | 10-15 min | HM lens + TA lens |
| Phase 6: Summary Report | 10 min | Document gaps, reframings, hints |
| Phase 7: GDrive & Tracker | 5 min | Upload, log row |
| **Total (typical)** | **90-135 min** | No loops. With 2 rewrite loops: +30 min |

## Edge Case: New Gap Discovered in Phase 3

Scenario: Phase 3 ATS scoring reveals CV is missing "first-party data strategy" keywords, but this wasn't flagged in Phase 2.

Action:
1. STOP Phase 3
2. Loop back to Phase 2.5 (discovery interview)
3. Ask: "Tell me about first-party data work you've done"
4. Update cv-career-history-supplement
5. Restart Phase 3 (re-score with updated base CV)
```

---

### 5. cv-config.md (Currently: Good → Target: Great)

**Current State:** Tables of paths, template rules, workflow defaults. Clear structure.

**What's Missing:**
- [ ] **Version matrix** — which file versions work together? (cv-formatting.md v1.3 works with cv-tailoring.md v1.3?)
- [ ] **Migration guide** — if adding a new template variant (e.g., Solution Architect), what files need updating?
- [ ] **Fallback defaults** — if a value is missing, what's the default? (e.g., if no template specified, assume PRODUCT_CV?)
- [ ] **Validation checklist** — before using config, check that all paths are valid
- [ ] **GDrive folder structure diagram** — visual representation of where files live
- [ ] **Error handling** — what if GDrive folder ID is wrong? What error message?

**Effort to Great:** Medium (1.5-2 hours) — Mostly adding diagrams and fallback logic

**Impact:** Medium — Reduces setup errors and makes config maintenance easier

**Specific Additions:**
```markdown
## File Version Compatibility Matrix

| cv-tailoring.md | cv-formatting.md | cv-semantic-clusters.md | cv-background.md | Compatible? |
|-----------------|------------------|------------------------|------------------|-------------|
| v1.2 | v1.2 | v1.1 | v1.1 | ✓ Yes |
| v1.3 | v1.3 | v1.3 | v1.3 | ✓ Yes |
| v1.3 | v1.2 | v1.3 | v1.3 | ✗ No (formatting rules outdated) |

## GDrive Folder Structure
```
Interviews CV/ (folder ID: 1_bf1bZ0OCzbFFOftwZNjQQ1q6QeFEg9v)
├── Hiran_Patel_CV_2Page.pdf (PRODUCT_CV source)
├── Hiran_Patel_CV_2Page_Data_Architect.pdf (DATA_ARCHITECT_CV source)
├── Applications (Google Sheet, tracker)
└── claude-output/
    ├── 2026.09.14_TalentInternational_ProductDirector/
    │   ├── 2026-09-14_TalentInternational_ProductDirector.docx
    │   └── 2026-09-14_TalentInternational_ProductDirector.pdf
    └── 2026.09.15_CompanyX_DataArchitect/
        ├── 2026-09-15_CompanyX_DataArchitect.docx
        └── 2026-09-15_CompanyX_DataArchitect.pdf
```

## Fallback Defaults

| Config Item | Fallback Value | When Used |
|-------------|----------------|-----------|
| Template | PRODUCT_CV | Role type unclear, user didn't specify |
| ATS Target Score | 85% | No user preference given |
| Max Rewrite Loops | 2 | Standard iteration limit reached |
| LinkedIn URL | Present | Template is PRODUCT_CV |
| Recommendations Section | Removed | All templates |
```

---

### 6. cv-decision-gates.md (Currently: Good → Target: Great)

**Current State:** Detailed logic for each gate, clear paths. Comprehensive.

**What's Missing:**
- [ ] **Pass rate benchmarks** — what % of CVs pass QA Personas on first try? Second try? (for expectation-setting)
- [ ] **Escalation path** — if QA Personas fail 3 times, should we escalate or ship anyway?
- [ ] **User override logic** — if user says "ship it anyway," what do we log?
- [ ] **Conflict resolution flowchart** — visual diagram of HM vs. TA conflicts
- [ ] **Phase 5.5 pass criteria specifics** — is "4 out of 5 HM checks" a pass? All 5?
- [ ] **Retro-checks** — after shipping, user says "the HM asked about X and I didn't have it" — what went wrong in QA?

**Effort to Great:** Medium (2 hours) — Mostly adding flowcharts, benchmarks, and retro analysis

**Impact:** Medium-High — Makes decision gates more concrete and reduces judgment calls

**Specific Additions:**
```markdown
## QA Personas: Pass Criteria Specifics

### Hiring Manager Lens
- **Pass:** All 5 checks pass
- **Conditional Pass:** 4 out of 5 pass, and the failure is in "Recency" (old role was most relevant 5+ years ago)
- **Fail:** 3 or fewer checks pass

### Talent Acquisition Lens
- **Pass:** All 5 checks pass
- **Conditional Pass:** 4 out of 5 pass, and failure is in "LinkedIn URL" (not applicable for Data Architect roles)
- **Fail:** 3 or fewer checks pass

### Overall CV Result
- **Ready to ship:** Both HM and TA pass (or conditionally pass)
- **Needs rewrite:** One or both fail

## Conflict Resolution Flowchart
```
         ┌─ HM Pass, TA Pass ────→ SHIP
         │
QA Run ──┼─ HM Pass, TA Fail ────→ Rewrite Phase 4.1 (keywords/title)
         │
         ├─ HM Fail, TA Pass ────→ Rewrite Phase 4.3 (metrics/IC)
         │
         └─ HM Fail, TA Fail ────→ Rewrite Phase 4.1 + 4.2 (full overhaul)
```

## Pass Rate Benchmarks (Hiran's History)

Based on prior CVs:
- First QA Personas run: ~60% pass (one lens fails)
- After 1 rewrite loop: ~90% pass
- After 2 rewrite loops: ~98% pass
- Escalation: If fail after 2 loops, ship with notes and offer follow-up session

## User Override Logging

If user says "ship it anyway" despite QA Personas failure:
1. Log in summary report: "QA Personas: [X check] failed. User approved override at 2026-09-15 11:30. Reason: [user's reason]"
2. Append tracker note: "QA override: [check name]"
3. Do NOT ship silently — make override explicit
```

---

## Summary: Effort vs. Impact Matrix

| File | Current | Great | Effort | Impact | Priority |
|------|---------|-------|--------|--------|----------|
| cv-formatting.md | Good | Great | Medium | High | High |
| cv-background.md | Good | Great | Med-High | High | High |
| cv-semantic-clusters.md | Good | Great | High | Med-High | Medium |
| cv-tailoring.md | Good | Great | Medium | Medium | Medium |
| cv-config.md | Good | Great | Medium | Medium | Low |
| cv-decision-gates.md | Good | Great | Medium | Med-High | Medium |

---

## Immediate Next Steps (Priority Order)

1. **cv-formatting.md:** Add before/after examples for em-dashes, line wraps, voice pattern fixes (1-2 hours)
2. **cv-background.md:** Expand role context details, add template selection decision tree (2-3 hours)
3. **cv-semantic-clusters.md:** Add scoring examples with real JD keywords (3-4 hours)
4. **cv-tailoring.md:** Add phase time estimates and edge case handling (2 hours)
5. **cv-decision-gates.md:** Add pass rate benchmarks and QA Personas flowchart (2 hours)
6. **cv-config.md:** Add file version matrix and GDrive folder diagram (1-2 hours)

**Total estimated effort to "Great" across all files: 14-18 hours**

---

## Maintenance Plan

Once "Great" status is achieved:

- **Monthly:** Review CHANGELOG entries against real applications. Log what broke, what worked.
- **Quarterly:** Update semantic clusters based on new JD trends (new tools, domains, terminology).
- **Quarterly:** Update pass rate benchmarks as more CVs get tailored.
- **As-needed:** Add new edge cases to cv-decision-gates.md when encountered.
- **Annually:** Full audit (like this one) to consolidate learnings and refactor if needed.

