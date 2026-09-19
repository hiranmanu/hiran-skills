# CV Tailoring Configuration

Centralized configuration for file paths, source CVs, and template rules. Update this file once; reference it everywhere.

---

## File Locations

All skill-file paths are relative to `plugins/cv-tailoring/skills/cv-tailoring/` unless otherwise noted (so `cv-formatting.md` in this table means `references/cv-formatting.md` from `SKILL.md`'s perspective). CV library and output paths are local absolute paths as shown.

| File | Path | Purpose |
|------|------|---------|
| CV Library (Product Template) | `C:\Users\hiran\Downloads\Hiran_Patel_CV_2Page.pdf` | Source content for all Product Director/VP/CPO roles |
| CV Library (Data Architect Template) | `C:\Users\hiran\Downloads\Hiran_Patel_CV_2Page_Data_Architect.pdf` | Source content for all Data Architect/Engineer roles |
| Formatting Rules | `cv-formatting.md` | Hard constraints: font, layout, voice patterns, validation |
| Background Context | `cv-background.md` | Confirmed facts, template selection, title blending rules |
| Semantic Clusters | `cv-semantic-clusters.md` | ATS scoring methodology and role-type clusters |
| Market Research Prompts | `cv-market-research.md` | Company research, role benchmarking, JD parsing guidance |
| Scoring Methodology | `cv-scoring.md` | Keyword presence + semantic clustering logic (single source of truth for the method) |
| QA Personas | `cv-qa-personas.md` | Hiring Manager + Talent Acquisition review checklists |
| Tailoring Orchestrator | `SKILL.md` (not in `references/` — sits one level up) | Main workflow: Phases 0-6, decision gates, edge cases |

---

## Source CVs (Local)

| Template | Filename | Purpose | LinkedIn URL? |
|----------|----------|---------|----------------|
| PRODUCT_CV | Hiran_Patel_CV_2Page.pdf | Use for Product Director, VP of Product, CPO, Senior PM roles | Yes: `linkedin.com/in/hiran-patel/` |
| DATA_ARCHITECT_CV | Hiran_Patel_CV_2Page_Data_Architect.pdf | Use for Data Architect, Data Engineer, Analytics Engineer roles | No |

Source CVs live directly in `C:\Users\hiran\Downloads\` (not a subfolder,
not GDrive) — that's where the two PDFs above always are.

---

## Output Configuration

All generated CVs are saved locally — nothing is uploaded to GDrive or any
other cloud location. This is a fixed folder; don't pick a different
location per session.

| Setting | Value | Notes |
|---------|-------|-------|
| Output Base Path | `C:\Users\hiran\Downloads\CV Output\` | Parent folder for all tailored CV outputs. Outside the git repo — never commit generated CVs. |
| Folder Naming | `{YYYY.MM.DD}_{Company}_{Role}\` | Example: `2026.09.14_TalentInternational_ProductDirector\` |
| File Naming (DOCX only) | `Hiran_CV_{YYYY.MM.DD}_{Company}_{BriefRole}.docx` | Example: `Hiran_CV_2026.09.19_Citi_PMGenAI.docx` (confirmed 2026-09-19) — DOCX is the only deliverable, see `cv-formatting.md` "Output Format" for the full naming rules (current date, company always present, short role slug) |

There is no applications tracker — the skill does not log applications
anywhere. Track applications however you already do outside this skill.

---

## Template Selection Rules

Use this decision tree to select which CV template to reference (for voice, formatting, and content patterns):

```
What is the target role type?
├─ Product Director, VP of Product, CPO, Head of Product, Senior Product Manager
│  └─ Use PRODUCT_CV
│
├─ Data Architect, Data Engineer, Analytics Engineer, Data Scientist, ML Engineer
│  └─ Use DATA_ARCHITECT_CV
│
├─ Solution Architect, Enterprise Architect
│  └─ Not yet templated (document new variant when needed)
│
└─ Other
   └─ Ask user which template to use as reference
```

**Both templates share:**
- Font: plain Calibri, 10.5pt uniform across every section
- Colour scheme: navy/grey (not black-and-white) — see `cv-formatting.md`
- Voice pattern: Action + Number + Method + Scale
- Layout rules: A4, date right-aligned (not bold, flush on the true page
  margin edge), citizenship/nationality right-aligned to the same tab stop
  at the bottom, no em-dashes or en-dashes anywhere including date ranges
- Company/descriptor lines: colon divider (`City, UK: descriptor`), not a dash
- Formatting: single-line bullets only, square (▪) primary bullets
- Authenticity: DOCX/PDF Author metadata set to "Hiran Patel"

**PRODUCT_CV unique:**
- LinkedIn URL: Present, hyperlinked (not plain text)
- Sections: Profile, Key Skills & Competencies, Career & Key Achievements
- Sections: No Recommendations section

**DATA_ARCHITECT_CV unique:**
- LinkedIn URL: Absent
- Sections: Profile, Key Skills & Competencies, Career & Key Achievements
- Sections: No Recommendations section

---

## Workflow Execution Defaults

| Parameter | Default | Override When |
|-----------|---------|-----------------|
| ATS Target Score | 85%+ | JD complexity requires higher score (aim 90%+) |
| Rewrite Loops | 2 iterations max per phase | Complex role requires 3+ iterations |
| Decision Gate: Format validation fails (5.3) | Loop back to Phase 4.x, re-render | See `cv-decision-gates.md` for detailed logic |
| Decision Gate: QA Personas fail (5.1) | Loop back to Phase 4.1 or 4.2, re-run 5.1 (no render yet) | See `cv-decision-gates.md` for detailed logic |
| Recommendations Section | Remove for all roles | Never include in tailored output |
| Blended Titles | Max 1-2 per CV | Never blend more than 1-2 roles per CV |
| LinkedIn URL in output | Product roles only | Remove for Data Architect roles |

---

## File Modification Notes

- This file was last updated: 2026-09-19
- When adding new templates (e.g., Solution Architect), update this config first before creating new files
- When changing the local output path, update both this config and the orchestrator (`SKILL.md` Phase 0 and the Render section)
- When adding new semantic clusters, update cv-semantic-clusters.md and the term-to-cluster mappings
