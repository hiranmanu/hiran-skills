# Available Skills

## cv-tailoring (v1.8.0)

Tailors a CV to a job description using a 9-phase workflow: intake → research → gap assessment → discovery → ATS scoring → generation → validation/QA → summary → tracker sync.

**Core Files:**
- `plugins/cv-tailoring/skills/cv-tailoring/SKILL.md` — main orchestrator, Phases 0-7
- `plugins/cv-tailoring/skills/cv-tailoring/references/cv-background.md` — role facts, template selection, title blending rules; also the write target for Phase 2.5 discovery findings
- `plugins/cv-tailoring/skills/cv-tailoring/references/cv-formatting.md` — hard constraints (font, em-dashes, layout, character budgets, voice pattern)
- `plugins/cv-tailoring/skills/cv-tailoring/references/cv-config.md` — centralized configuration (file paths, GDrive IDs, workflow defaults)
- `plugins/cv-tailoring/skills/cv-tailoring/references/cv-decision-gates.md` — explicit phase decision logic and loop targets (authority on when to ask, when to skip, QA gates)
- `plugins/cv-tailoring/skills/cv-tailoring/references/cv-semantic-clusters.md` — keyword clustering lookup data (term mappings only — see cv-scoring.md for the method)
- `plugins/cv-tailoring/skills/cv-tailoring/references/cv-scoring.md` — ATS scoring method (single source of truth)
- `plugins/cv-tailoring/skills/cv-tailoring/references/cv-qa-personas.md` — Hiring Manager + Talent Acquisition review checklists
- `plugins/cv-tailoring/skills/cv-tailoring/references/cv-market-research.md` — JD research and company signal patterns
- `plugins/cv-tailoring/skills/cv-tailoring/references/cv-tracker.md` — application tracker schema (Google Sheets, in GDrive)
- `plugins/cv-tailoring/skills/cv-tailoring/scripts/validate_cv.py` — automated Phase 5.3 checks (page count, em/en dashes, bullet wraps, role-page-splits, Author metadata)
- `plugins/cv-tailoring/skills/cv-tailoring/scripts/build_cv_reference.js` — reference docx-js implementation of the full house style

**Recent Results:**
- **Monzo Chief of Staff to CPO:** 60% → 91% ATS coverage
- **TalentInternational Product Director:** 64% → 93% ATS coverage (search/discovery/hands-on IC emphasis)

**Workflow Modes:**
1. **Quick (1-2 min):** Paste JD → generate → done. No questions, no gates.
2. **Balanced (15-20 min):** Paste JD → 2-3 quick questions → generate → review once → upload.
3. **Full Manual (90-135 min):** All 9 phases with discovery interview, gap assessment, multi-loop QA.

**Output:**
- Tailored DOCX (editable) + PDF (for submission)
- Professional black-and-white formatting: Calibri font, section underlines, proper bullet hierarchy
- No LinkedIn URL for agency postings (configurable per JD source)
- All sub-bullets preserved; no em-dashes; proper spacing and alignment

**Installation in Claude Code:**
```bash
/plugin marketplace add hiranmanu/hiran-skills
/plugin install cv-tailoring@hiran-skills
```

---

## Upcoming Skills

- `interview-skill/` — Interview prep (STAR format, Q&A, role-specific research, mock interviews)
- `linkedin-skill/` — LinkedIn profile optimization (headline, summary, experience section)

---

## Version History

**v1.8.0 (Sep 17, 2026):**
- House style confirmed: plain Calibri 10.5pt uniform, A4, navy/grey colour,
  square bullets, hyperlinked contact details, "Profile Summary" heading —
  supersedes all earlier Calibri Light / US Letter / black-and-white / round
  bullet guidance. No more open question from v1.7.0.
- Added DOCX/PDF authenticity metadata requirement (Author = "Hiran Patel")
  with an automated check in `validate_cv.py` (5th check, tested both ways)
- Added `scripts/build_cv_reference.js`, a working reference implementation
  of the full house style

**v1.7.0 (Sep 17, 2026):**
- Added `scripts/validate_cv.py`: automated Phase 5.3 validation (page count,
  em/en dashes, bullet-wrap detection, role-page-split detection) — previously
  the last two had no tooling at all, only manual eyeballing
- Audited against a separate chat session's CV work; reconciled what was an
  unambiguous improvement, flagged the rest (font, page size, colour, bullet
  shape) as an open question in `cv-formatting.md` rather than silently merging
- Deleted a duplicate standalone repo (`hiranmanu/cv-tailoring-skill`) that the
  other session created in error instead of updating this one

**v1.6.1 (Sep 17, 2026):**
- Full per-file QA sweep after the v1.6.0 restructure: found and fixed 5 stale `cv-tailoring.md` self-references left over from the SKILL.md rename

**v1.6.0 (Sep 17, 2026):**
- Restructured into the real Claude Code plugin/skill format: `plugins/cv-tailoring/skills/cv-tailoring/SKILL.md` + `references/` — previous versions would not have loaded via `/plugin install`
- Reordered QA: persona review (5.1) now runs pre-render on draft text; format validation (5.3) runs post-render — avoids re-rendering for content-only fixes
- Deduplicated HM/TA checklists (`cv-qa-personas.md` is now the single source)
- Added bounded "signature breadth" allowance to the skills-section policy

**v1.5.0 (Sep 17, 2026):**
- Operationalized the Quick/Balanced/Full Manual speed modes in `cv-tailoring.md` Phase 0 (previously only described in README/SKILLS, never enforced)
- Quick mode now the default for a bare JD paste — skips research and discovery, never skips validation
- Added Solution/Enterprise Architect as an explicit edge case (template gap was buried in `cv-config.md` only)

**v1.4.0 (Sep 17, 2026):**
- Fixed broken file references left behind by the v1.3.0 merge (`cv-job-context.md`, `cv-career-history-supplement.md`, `cv-formatting-rules.md` no longer exist; all references now point at `cv-background.md` / `cv-formatting.md`)
- Consolidated ATS scoring into one method (was two contradictory descriptions across `cv-tailoring.md` and `cv-scoring.md`)
- Renumbered phases consistently everywhere (was two conflicting `Phase 6` headers, and `Phase 5.3`/`5.5` referenced with no matching sections)
- Rewrote `cv-tracker.md` (was describing a local xlsx file, contradicting the GDrive/Sheets tracker described everywhere else)
- Deleted `cv-generation-and-qa.md` (orphaned, wrong filename convention) and `GOOD_TO_GREAT_PLAN.md` (superseded); useful content merged into `cv-formatting.md` and `cv-decision-gates.md`

**v1.3.0 (Sep 15, 2026):**
- File consolidation: merged 12 files → 11 files (formatting + voice guides merged; context + career history merged)
- Centralized configuration in `cv-config.md` (GDrive folder IDs, source CV locations, output folder, workflow defaults)
- Explicit decision gate logic in `cv-decision-gates.md` (Phase 2 gap path detection, Phase 5 validation gates, Phase 5.5 QA lenses)
- Enhanced semantic clusters: Data Architect, Retail Media/First-Party Data, AdTech/Measurement clusters added
- Good to Great improvement plan (14-18 hours): before/after examples, expanded role details, scoring examples with real JDs
- Tested full manual (Phase 0-7) workflow on TalentInternational Product Director: 64% → 93% ATS score

**v1.2.0 (Sep 14, 2026):**
- Workflow redesign: three speed options (Quick/Balanced/Full Manual) to fit delivery timelines
- Decision gates and rewrite loops clarified per cv-decision-gates.md
- All confirmed facts captured in cv-background.md (templates, Design ownership, BI tools, MarTech/CRM)

**v1.1.0 (Sep 13, 2026):**
- Initial release: 9-phase CV tailoring workflow
- ATS scoring methodology with semantic cluster matching
- Professional DOCX/PDF generation with formatting constraints
- Application tracker integration
