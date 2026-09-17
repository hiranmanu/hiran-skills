# Changelog

All notable changes to the cv-tailoring skill and supporting reference files are documented here.

## [1.8.0] - 2026-09-17 (House Style Confirmed + Authenticity Metadata)

Hiran confirmed the other session's conventions (flagged as an open question
in v1.7.0) ARE the house style going forward. No more open question.

### Changed
- `cv-formatting.md` Font & Layout section rewritten: plain Calibri 10.5pt
  uniform across every section (not Calibri Light), A4 not US Letter,
  navy/grey colour scheme (not black-and-white), square ▪ primary bullets
  (not round), hyperlinked email/LinkedIn (not plain text), "Profile
  Summary" heading (not "Profile"), ~105-108 char bullet budget (was ~90,
  different page/margin/font), dual nationality right-aligned to the date
  tab stop at the bottom only. Also added: no en dashes (previously only
  em dashes were banned), zero spacing between bullets within a role, and
  explicit page-split protection wording.
- `cv-config.md` and `cv-background.md`'s "shared formatting" summaries
  updated to match.
- `README.md`'s historical "black-and-white" example output annotated as
  predating this change, rather than rewritten as if it always used colour.

### Added
- **Authenticity metadata requirement:** every generated DOCX must set
  `creator`/`lastModifiedBy` to "Hiran Patel" (not a generic tool default
  like "Un-named" or "python-docx") — verified to carry through to the
  PDF's Author field on soffice conversion.
- `scripts/validate_cv.py` now has a 5th automated check for this: reads
  `docProps/core.xml` from the docx and the PDF's `pdfinfo` Author field,
  fails if either is empty, a known generic default, or not exactly "Hiran
  Patel". Tested against a docx with no author set (correctly fails) and
  the real CV (correctly passes).
- `scripts/build_cv_reference.js` — a full docx-js implementation of every
  rule in the now-updated `cv-formatting.md` (fonts, colours, spacing,
  hyperlinks, page-split protection, document properties), so future
  sessions have a working reference to copy and adapt per JD instead of
  re-deriving the styling from prose each time.

## [1.7.0] - 2026-09-17 (Automated Phase 5.3 Validation + Cross-Session Audit)

A separate Claude chat session had been iterating on CV formatting without knowing
this skill existed, and built its own standalone (now-deleted) repo instead of
updating this one. Pulled that session's learning back in where it was
unambiguously an improvement, and flagged the rest rather than silently merging it.

### Added
- `plugins/cv-tailoring/skills/cv-tailoring/scripts/validate_cv.py` — the
  automated check that Phase 5.3 previously only described in prose ("run
  pdftotext, grep it, eyeball the PDF"). Takes a rendered `.docx`/`.pdf` and
  checks, in one pass: page count vs. a configurable cap (default 2), em/en
  dashes, bullet-wrap detection (a bullet spilling onto a stray second line),
  and role-page-split detection (a role's bullets landing on a different page
  than its header) — the last two were previously **manual-only and had no
  tooling at all**, confirmed gaps from the other session's own audit.
  Exits non-zero on any failure so it can gate a workflow, not just report.
  Tested against both a clean render (all 4 checks pass) and a deliberately
  overflowing bullet (correctly caught and reported).
- `cv-decision-gates.md` §5.3 and `cv-formatting.md`'s validation checklist
  both now point at the script instead of describing the checks only in prose.

### Reconciled / flagged (not silently merged)
- The other session's CV used materially different conventions (US Letter →
  A4, Calibri Light → plain Calibri, black-and-white → navy/grey colour,
  plain-text LinkedIn → hyperlinked, "Profile" → "Profile Summary", round →
  square primary bullets, ~90 → ~105-108 char budget). Rather than overwrite
  this repo's tested, production conventions with an untested one-off
  session's choices, added an explicit "Open question" callout in
  `cv-formatting.md` naming every discrepancy, so a future session doesn't
  silently pick a side either. See that file for the full list.
- The other session's standalone `hiranmanu/cv-tailoring-skill` repo, created
  in error instead of updating this one, has been deleted.

## [1.6.1] - 2026-09-17 (Post-Restructure QA Sweep)

After the v1.6.0 restructure (SKILL.md + references/), did a full per-file
read-through rather than trust the mechanical move. Found and fixed 5 stale
self-references the restructure left behind — the orchestrator was renamed
from `cv-tailoring.md` to `SKILL.md`, but four reference files
(`cv-config.md` x3, `cv-decision-gates.md`, `cv-market-research.md`,
`cv-tracker.md` x2) still called it by its old name in prose:
- `cv-config.md`: file-locations table, two decision-gate rows, and the
  "file modification notes" section all said `cv-tailoring.md`
- `cv-decision-gates.md`: the Render section pointed at `cv-tailoring.md`
- `cv-market-research.md`: the Quick-mode skip note pointed at
  `cv-tailoring.md`
- `cv-tracker.md`: two references (the tracker-location note and the
  logging-confirmation note) pointed at `cv-tailoring.md`

Verified after fixing: `grep` sweep for `cv-tailoring.md` across
`references/` returns nothing; every `Phase 4.x` / `5.x` mentioned anywhere
in the skill is actually defined somewhere (no orphaned references left);
`plugin.json` and `marketplace.json` parse as valid JSON and agree on name
(`cv-tailoring`) and version (`1.6.0`); `SKILL.md` is 315 lines (under the
500-line guidance) with a 66-word frontmatter description.

## [1.6.0] - 2026-09-17 (Real Plugin/Skill Structure)

Every prior version of this repo would **not have loaded as an installable
Claude Code skill**, verified against Claude Code's actual plugin reference
docs. The requirements: a skill must be a directory containing a file
literally named `SKILL.md`; a plugin needs `.claude-plugin/plugin.json`;
a marketplace's `source` field points at a plugin directory, not a bare
`.md` file. This repo had none of that — `cv-tailoring.md` sat in a flatly
named `cv-skill/` folder with no `plugin.json` anywhere, and
`.claude-plugin/marketplace.json`'s `source` pointed directly at the `.md`
file. It worked only because Claude was being told by hand, in chat, to go
read that file — not because `/plugin install` would have found it.

**Restructured to:**
```
hiran-skills/
├── .claude-plugin/marketplace.json
└── plugins/cv-tailoring/
    ├── .claude-plugin/plugin.json       (new — was missing entirely)
    └── skills/cv-tailoring/
        ├── SKILL.md                     (renamed from cv-tailoring.md)
        └── references/                  (all 9 supporting files moved here)
```

- `cv-tailoring.md` → `SKILL.md`, moved into a directory named to match the
  skill (`cv-tailoring/`), per the required `skill-name/SKILL.md` shape.
- All 9 reference files moved into `references/`, loaded on demand rather
  than sitting flat alongside the entrypoint — this is the documented
  progressive-disclosure pattern, not a workaround.
- Added `plugins/cv-tailoring/.claude-plugin/plugin.json`.
- Fixed `.claude-plugin/marketplace.json`'s `source` to point at the plugin
  directory (`./plugins/cv-tailoring`) instead of a bare file path.
- Every internal reference in `SKILL.md` updated from bare filenames
  (`cv-background.md`) to `references/cv-background.md`, since the
  reference files now sit one level below the entrypoint.
- `/plugin marketplace add hiranmanu/hiran-skills` and
  `/plugin install cv-tailoring@hiran-skills` (README's own documented
  install commands) should now actually resolve to something real.

### QA/validation reordering

Talent Acquisition and Hiring Manager lens checks (Phase 5.5, now 5.1) are
pure text review — keywords, ordering, numbers, title — and don't need a
rendered file. Only the format checks (em dashes, line wraps, `pdftotext`
extraction) genuinely require a render. Previously both ran after
rendering, meaning a content-only fix cost a full re-render to re-check.
Reordered: **Phase 5.1 (QA personas) now runs on draft text before
rendering; render happens once that passes; Phase 5.3 (format validation)
runs on the render.** A punctuation or line-length fix no longer requires
re-running the persona review; a keyword or wording fix does.

### Deduplication

`cv-decision-gates.md` and `cv-qa-personas.md` both contained the full HM/TA
checklists (same 5+5 checks, described twice). `cv-qa-personas.md` is now
the single source for the checklists themselves (with the reasoning and
red/green-flag detail); `cv-decision-gates.md` keeps only the pass/fail
loop-back logic and cross-references the checklist rather than restating it.

### Skills-section policy

Added a bounded "signature breadth" allowance to `cv-formatting.md`: up to
1-2 truthful, non-JD skills may appear at the *end* of the skills line if
genuinely differentiating for the role level — never ahead of a JD keyword,
never counted toward the ATS score, never anything not already confirmed in
`cv-background.md`. Addresses the risk that a fully JD-mirrored skills line
under-signals genuine breadth.

## [1.5.0] - 2026-09-17 (Speed Modes Operationalized)

README and SKILLS.md have described three workflow modes (Quick/Balanced/
Full Manual) since v1.2.0, but nothing in the actual skill files enforced
them — there was no mechanism to skip anything. This is why running the
skill always took the same time regardless of what was asked for.

- `cv-tailoring.md` Phase 0 now has an explicit table: for each mode, which
  phases run, which are skipped, and what's compressed. Phase 5.3
  validation never gets skipped in any mode — only research, discovery,
  and QA-persona review scale down.
- Quick mode is the default when a JD is pasted with no other instruction.
  Explicitly asking for the full workflow, or a JD that's clearly high-
  stakes, should still trigger Full Manual.
- `cv-market-research.md` and `cv-qa-personas.md` cross-reference the mode
  table so they don't give contradictory instructions if read on their own
  mid-workflow.
- Added an explicit edge case (`cv-tailoring.md` §Edge Cases) for Solution
  Architect / Enterprise Architect JDs — no template exists yet, and this
  was previously only flagged in a `cv-config.md` table, easy to miss
  mid-run.

## [1.4.0] - 2026-09-17 (Integrity Fix — Broken References & Contradictions)

The v1.3.0 "comprehensive audit" merged several files but never updated the
files that pointed at them, and left two other real contradictions in
place. This release fixes what actually broke a live run, not just style.

### Broken references fixed
- `cv-tailoring.md` Phase 0/2 and `cv-decision-gates.md` referenced
  `cv-job-context.md` and `cv-career-history-supplement.md` — both were
  merged into `cv-background.md` in v1.3.0, but the references were never
  updated. Both files also referenced `cv-formatting-rules.md`, which was
  merged into `cv-formatting.md` in the same release. All references now
  point at the real files.
- **Consequence of the bug:** Phase 2.5's experience-discovery interview had
  no file to write confirmed facts back to. This is now `cv-background.md`
  §2, explicitly documented as the append-only destination.

### Contradictions resolved
- **Scoring method.** `cv-tailoring.md` described weighted keyword-only
  scoring (hard skills 2x, title 1.5x, domain 1x); `cv-scoring.md` and
  `cv-semantic-clusters.md` described unweighted semantic-cluster scoring.
  `cv-scoring.md` is now the single source of truth for the method;
  `cv-semantic-clusters.md` holds cluster lookup data only.
- **Tracker location.** `cv-tracker.md` still described a local
  `Hiran_Applications_Tracker.xlsx` with "no cross-tool sync" — contradicting
  `cv-config.md` and `cv-tailoring.md`, both of which describe a Google
  Sheets tracker inside the GDrive `Interviews CV` folder. Rewrote
  `cv-tracker.md` to match; noted the discrepancy explicitly in case the
  GDrive assumption turns out to be the stale one instead.
- **Filename convention.** `cv-generation-and-qa.md` used
  `{FirstName}_{LastName}_{Company}_CV.docx`; every other file used
  `{YYYY-MM-DD}_{Company}_{Role}`. Resolved by deleting the orphaned file
  (see below) — the correct convention lives in `cv-formatting.md` and
  `cv-config.md` only, once.

### Phase numbering fixed
`cv-tailoring.md` had two separate `## Phase 6` headers (Summary Report,
then Tracker Sync) and an overlapping Phase 4/Phase 5 both titled
"Generation." `cv-decision-gates.md` referenced "Phase 5.3" and "Phase 5.5"
with no matching headers anywhere. Renumbered consistently: 0, 1, 2, 2.5,
3, 4 (with sub-steps 4.1-4.4, now defined and matching the loop targets
`cv-decision-gates.md` already used), 5 (5.3 validation, 5.5 QA personas),
6, 7 — applied across `cv-tailoring.md`, `cv-decision-gates.md`, and
`cv-qa-personas.md`.

### Files removed
- `cv-generation-and-qa.md` — orphaned from a pre-v1.3.0 generation (wrong
  filename convention, duplicate line-wrap-budget content). Its still-useful
  content (character-budget math, exact QA command sequence, metadata step)
  merged into `cv-formatting.md` and `cv-decision-gates.md` §5.3.
- `GOOD_TO_GREAT_PLAN.md` — a prior self-audit that proposed style/example
  additions but never caught the structural breakage above; superseded by
  this fix.
- Top-level `marketplace.json` — a redundant, non-standard duplicate of
  `.claude-plugin/marketplace.json` (the one Claude Code actually reads),
  with its own separately-stale file list and version number.

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

