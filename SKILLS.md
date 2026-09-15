# Available Skills

## cv-tailoring (v1.3.0)

Tailors a CV to a job description using a 9-phase workflow: research → gap assessment → ATS scoring → tailoring → generation → validation → QA → logging → uploading.

**Core Files:**
- `cv-skill/cv-tailoring.md` — main 9-phase workflow definition
- `cv-skill/cv-background.md` — role facts, template selection, title blending rules
- `cv-skill/cv-formatting.md` — hard constraints (font, em-dashes, layout, voice pattern)
- `cv-skill/cv-config.md` — centralized configuration (file paths, GDrive IDs, workflow defaults)
- `cv-skill/cv-decision-gates.md` — explicit phase decision logic (when to ask, when to skip, QA gates)
- `cv-skill/cv-semantic-clusters.md` — keyword clustering, scoring methodology, term mappings
- `cv-skill/cv-scoring.md` — ATS scoring baseline and methodology
- `cv-skill/cv-generation-and-qa.md` — output validation checklist
- `cv-skill/cv-market-research.md` — JD research and company signal patterns
- `cv-skill/cv-tracker.md` — application tracker workbook schema

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
