# Available Skills

## cv-tailoring
Tailors a CV to a job description, scores ATS keyword coverage before/after, generates a DOCX + PDF, and logs the application to a tracker workbook.

**Files:**
- `cv-skill/cv-tailoring.md` — main skill definition
- `cv-skill/cv-career-history-supplement.md` — confirmed facts per role (board/investor, BI tools, Design)
- `cv-skill/cv-formatting-rules.md` — CV generation formatting constraints
- `cv-skill/cv-scoring.md` — ATS scoring methodology
- `cv-skill/cv-generation-and-qa.md` — output validation checklist
- `cv-skill/cv-market-research.md` — JD research patterns
- `cv-skill/cv-tracker.md` — application tracker schema

**Status:** v1.1.0 (production ready)
**ATS Coverage:** 60% → 91% on recent Monzo application

## Upcoming skills
- `interview-skill/` — interview prep (STAR format, Q&A, role-specific research)
- `linkedin-skill/` — LinkedIn profile optimization

---

**Installation in Claude Code:**
```bash
/plugin marketplace add hiranmanu/hiran-skills
/plugin install cv-tailoring@hiran-skills
```
