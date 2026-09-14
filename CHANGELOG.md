# Changelog

All notable changes to the cv-tailoring skill and supporting reference files are documented here.

## [1.3.0] - 2026-09-15 (Comprehensive Audit & File Consolidation)

### Merged Files (Consolidation for Clarity)
- **cv-formatting-rules.md + cv-voice-guide.md → cv-formatting.md**
  - Section 1: Hard Constraints (em dashes, line wraps, font: Calibri Light 10.5pt, layout: date/citizenship right-aligned, rounded sub-bullets ○)
  - Section 2: Voice & Style (Action + Number + Method + Scale pattern, examples, don't-say list, Data Architect variant patterns)
  - Section 3: ATS & Validation (pdftotext rules, filename format, profile/headline/skills section rules, validation checklist)
  - **Addition:** Font specification (Calibri Light confirmed), layout rules (date right-aligned, citizenship right-aligned), LinkedIn handling (Product roles only), rounded bullet replacement rule, Recommendations section removal (all roles)
  - **Addition:** Data Architect voice patterns (metrics-first with data/architecture terminology)

- **cv-job-context.md + cv-career-history-supplement.md → cv-background.md**
  - Section 1: Template Selection (which CV to use: PRODUCT_CV for Director/VP/CPO roles, DATA_ARCHITECT_CV for data/analytics roles)
  - Section 2: Confirmed Facts by Role (board/investor exposure, BI tools, Design ownership, CRM/CDP/MarTech, regulator exposure, notable absences)
  - Section 3: Title Blending Strategy (when/how to blend titles, rules, when NOT to blend)
  - **Note:** Removed redundancy — combined two overlapping files into one with clear sections. Template selection now explicit.

### Updated Files (Content Enhancements)
- **cv-semantic-clusters.md** — Added missing clusters
  - NEW: Data Architect/Data Engineer role cluster (data architecture, ETL, data pipeline, Spark, dbt, Airflow, Python, SQL, big data, Snowflake, BigQuery, Redshift, Databricks, Kafka, streaming)
  - NEW: Retail Media/First-Party Data domain cluster (identity resolution, clean rooms, privacy & consent, measurement, data activation, GDPR)
  - NEW: AdTech/Measurement domain cluster (programmatic, RTB, attribution, brand safety, campaign optimization, conversion tracking)
  - NEW: Term-to-cluster mappings for Data Architect, First-Party Data, Retail Media, AdTech roles
  - **Impact:** Semantic clustering now covers Hiran's specialty domains (retail media, AdTech, measurement, first-party data) plus new role types (Data Architect)

- **cv-tailoring.md** — Added decision gates and template selection
  - NEW: Decision Gates & Rewrite Loops section (explicit logic for what happens when Phase 2 gaps are found, Phase 5.3 validation fails, Phase 5.5 QA Personas fail)
  - NEW: Template Selection guidance (use PRODUCT_CV or DATA_ARCHITECT_CV based on role type)
  - NEW: Recommendations Section note (removed from all CVs)
  - NEW: Multiple applications to same company edge case
  - **Added references to:** cv-formatting.md (instead of cv-formatting-rules.md), cv-background.md (for template selection)
  - **Impact:** Workflow now has explicit decision points and rewrite loop logic. No more "what do we do if validation fails?" ambiguity.

### New Files (Infrastructure)
- **cv-config.md** — Centralized configuration
  - File locations table (all CV skill files, GDrive folders, paths)
  - Source CVs table (PRODUCT_CV vs. DATA_ARCHITECT_CV, GDrive folder ID, LinkedIn URL handling)
  - Output configuration (GDrive paths, naming conventions, tracker sheet location)
  - Template Selection Rules (decision tree for which CV template to use)
  - Workflow Execution Defaults (ATS target score, rewrite loop limits, decision gate rules)
  - **Purpose:** Single source of truth for all paths and configuration. Eliminates hardcoded paths scattered across files.

- **cv-decision-gates.md** — Explicit rewrite logic
  - Phase 2 Gap Assessment: 3 paths (genuine gap, addressable gap, no gap)
  - Phase 5.3 Validation: 3 checks (em-dashes, bullet wraps, pdftotext readability) with loops back to Phase 4.x
  - Phase 5.5 QA Personas: HM lens (5 checks) + TA lens (5 checks) with conflict resolution
  - When to Ship vs. Iterate
  - Multiple applications to same company logic
  - **Purpose:** Takes ambiguity out of review phases. Every check has an action. Every failure has a loop target.

### Improvements & Additions

**From Formatting/Voice Merge:**
- Added font recommendation: Calibri Light 10.5pt (confirmed working)
- Added layout rules: date right-aligned, citizenship right-aligned (matches desired output)
- Added rounded bullet replacement rule: ○ for sub-bullets instead of em-dashes
- Added LinkedIn URL rule: Product roles only, format as plain text
- Added Recommendations section rule: Remove from all roles (not needed for ATS)
- Documented Data Architect voice patterns (same Action + Number + Method + Scale pattern as Product)

**From Semantic Clusters:**
- Added Data Architect role cluster (was completely missing)
- Added Hiran's specialty domain clusters (retail media, AdTech, measurement, first-party data)
- Filled gap: Privacy, GDPR, consent management now explicitly mapped
- Filled gap: Measurement and attribution now explicitly mapped
- Term-to-cluster mappings now cover all new clusters

**From Tailoring Rewrite:**
- Made template selection explicit (phase 0, cv-background.md)
- Made decision gates explicit (when to loop, where to loop to, pass criteria)
- Made rewrite loop limits explicit (max 2 full iterations through validation/QA)
- Made conflict resolution explicit (HM pass but TA fail, or vice versa)
- Documented edge case: multiple applications to same company

### Removed Files (Consolidation)
- cv-formatting-rules.md → merged into cv-formatting.md
- cv-voice-guide.md → merged into cv-formatting.md
- cv-job-context.md → merged into cv-background.md
- cv-career-history-supplement.md → merged into cv-background.md

**Note:** Old files remain in repo for history, but should not be referenced in cv-tailoring.md. All references now point to merged files.

### Files Still in Original Form (No Change)
- cv-market-research.md (research prompts, role benchmarking)
- cv-generation-and-qa.md (line-wrap, filename conventions, QA sequence)
- cv-qa-personas.md (checklists — enhanced decision-gates.md but QA personas still referenced)
- cv-scoring.md (keyword + semantic methodology — still accurate, but now feeds into decision-gates logic)
- cv-tracker.md (tracker schema — still accurate)

---

## [1.2.0] - 2026-09-15

### Added
- Semantic clustering for ATS scoring (MarTech → marketing automation, lead scoring, CDP, CRM, customer data, etc.)
- QA personas framework (Hiring Manager lens + Talent Acquisition lens, Phase 5.5)
- Voice guide (metrics-first pattern preservation from original CVs)
- Title blending strategy (only 1-2 roles max per CV, documented rule to avoid manufactured appearance)
- cv-job-context.md (undocumented background facts indexed by role: board/investor, BI tools, Design, regulator exposure, CRM/CDP/MarTech)
- cv-semantic-clusters.md (role-type clusters and term-to-cluster mappings for semantic ATS scoring)
- cv-qa-personas.md (independent reviewer frameworks: Hiring Manager lens + TA lens checklists)

### Changed
- ATS scoring methodology: moved from weighted heuristic (2x/1.5x/1x) to keyword presence + semantic clustering
- Profile/headline rules: now require JD-title mirroring (e.g., "Senior Product Director" for Director roles)
- Skills section rules: JD-only keywords, no speculative tech (e.g., don't list Power BI if JD doesn't mention it)
- Blended titles rule: only 1-2 roles max per CV (was: suggested for all roles)
- Bullet ordering: chronological by role, but within each role reorder to surface JD-relevant bullets first
- cv-formatting-rules.md: added keyword-first placement rules, blended-title constraints, JD-mirroring requirements
- cv-voice-guide.md: added action-verb-first pattern, specific-metrics-only rule, don't-say list (no "passionate", "leveraged", etc.)

### Fixed
- em-dash rule now explicitly enforced: grep check added to Phase 4 validation
- Line-wrap detection: character budget documented (90 chars for bulleted lines at Calibri 10.5pt)
- Scoring methodology: documented semantic clustering approach with examples (MarTech cluster, CDP cluster, etc.)

### Updated Files (reviewed against source CVs)
- cv-tailoring.md: added semantic clustering to Phase 3, QA personas to Phase 5.5, GDrive integration to Phase 6
- cv-formatting-rules.md: added title-blending rule, keyword-first placement, no-em-dashes validation
- cv-voice-guide.md: extracted patterns from Hiran_Patel_CV_2Page.pdf (metrics-first, action-verb-first, specific numbers)
- cv-career-history-supplement.md: cross-checked against both Product and Data Architect CVs
- cv-semantic-clusters.md: built from scratch with Product Director JD as test case

---

## [1.1.0] - 2026-09-14

### Added
- Monzo Chief of Staff → CPO tailoring (initial full workflow test)
- cv-career-history-supplement.md (board/investor facts, BI tools, Design ownership per role)
- cv-formatting-rules.md (single-line bullets, no em dashes, blended titles, profile opening rules)
- cv-generation-and-qa.md (line-wrap prevention, filename conventions, QA sequence)
- cv-market-research.md (JD parsing, company research, role benchmarking, checkpoint)
- cv-scoring.md (keyword presence methodology, example scoring, reporting format)
- cv-tracker.md (applications tracker schema, update logic)

### Changed
- CV template: added "Chief of Staff to CPO" blended title for Monzo
- ATS score computation: before 60% → after 91% (Monzo application)
- Tracker: added Monzo row, formulas recalculated

### Fixed
- Title blending: formalized "VP of Product" → "Head of Product, VP of Product" pattern
- ATS gaps: confirmed board/investor, BI tools, Design facts in cv-career-history-supplement.md (no fabrication)

---

## [1.0.0] - 2026-09-13

### Initial Release
- cv-tailoring.md: main skill documentation (Phases 0-6)
- cv-job-context.md: undocumented background facts placeholder
- Three CV template variants (CPO/VP Product, Data Architect, Solution Architect)
- ATS scoring (weighted keyword heuristic)
- Applications tracker workbook
- GitHub repository initialization

