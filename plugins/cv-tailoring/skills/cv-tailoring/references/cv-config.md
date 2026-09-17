# CV Tailoring Configuration

Centralized configuration for file paths, source CVs, GDrive locations, and template rules. Update this file once; reference it everywhere.

---

## File Locations

All skill-file paths are relative to `plugins/cv-tailoring/skills/cv-tailoring/` unless otherwise noted (so `cv-formatting.md` in this table means `references/cv-formatting.md` from `SKILL.md`'s perspective). CV library and GDrive paths are absolute/GDrive-native as shown.

| File | Path | Purpose |
|------|------|---------|
| CV Library (Product Template) | `/home/claude/cv-work/resumes/Hiran_Patel_CV_2Page_Product.md` | Source content for all Product Director/VP/CPO roles |
| CV Library (Data Architect Template) | `/home/claude/cv-work/resumes/Hiran_Patel_CV_2Page_DataArchitect.md` | Source content for all Data Architect/Engineer roles |
| Formatting Rules | `cv-formatting.md` | Hard constraints: font, layout, voice patterns, validation |
| Background Context | `cv-background.md` | Confirmed facts, template selection, title blending rules |
| Semantic Clusters | `cv-semantic-clusters.md` | ATS scoring methodology and role-type clusters |
| Market Research Prompts | `cv-market-research.md` | Company research, role benchmarking, JD parsing guidance |
| Scoring Methodology | `cv-scoring.md` | Keyword presence + semantic clustering logic (single source of truth for the method) |
| QA Personas | `cv-qa-personas.md` | Hiring Manager + Talent Acquisition review checklists |
| Tailoring Orchestrator | `cv-tailoring.md` | Main workflow: Phases 0-7, decision gates, edge cases |
| Tracker Schema | `cv-tracker.md` | Applications tracker structure and update rules |

---

## Source CVs (GDrive)

| Template | Filename | GDrive Folder | Purpose | LinkedIn URL? |
|----------|----------|---------------|---------|----------------|
| PRODUCT_CV | Hiran_Patel_CV_2Page.pdf | Interviews CV | Use for Product Director, VP of Product, CPO, Senior PM roles | Yes: `linkedin.com/in/hirankpatel` |
| DATA_ARCHITECT_CV | Hiran_Patel_CV_2Page_Data_Architect.pdf | Interviews CV | Use for Data Architect, Data Engineer, Analytics Engineer roles | No |

**GDrive Folder ID:** `1_bf1bZ0OCzbFFOftwZNjQQ1q6QeFEg9v`
**GDrive Path:** `Interviews CV/`

---

## Output Configuration

All generated CVs go to GDrive in timestamped folders.

| Setting | Value | Notes |
|---------|-------|-------|
| Output Base Path | `Interviews CV/claude-output/` | Parent folder for all tailored CV outputs |
| Folder Naming | `{YYYY.MM.DD}_{Company}_{Role}/` | Example: `2026.09.14_TalentInternational_ProductDirector/` |
| File Naming (DOCX/PDF) | `{YYYY-MM-DD}_{Company}_{Role}` | Example: `2026-09-14_TalentInternational_ProductDirector.docx` |
| Tracker Sheet ID | (stored in memory, see session context) | Applications tracking spreadsheet in Google Sheets |
| Tracker Sheet Name | Applications | Tab name within tracker spreadsheet |

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
- Font: Calibri Light 10.5pt
- Voice pattern: Action + Number + Method + Scale
- Layout rules: Date right-aligned, citizenship right-aligned, no em-dashes
- Formatting: Single-line bullets, rounded sub-bullets (○)

**PRODUCT_CV unique:**
- LinkedIn URL: Present, plain text format
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
| Decision Gate: Validation fails | Loop back to Phase 4.1 | See cv-tailoring.md for detailed logic |
| Decision Gate: QA Personas fail | Loop back to Phase 4.1 or 4.2 | See cv-tailoring.md for detailed logic |
| Recommendations Section | Remove for all roles | Never include in tailored output |
| Blended Titles | Max 1-2 per CV | Never blend more than 1-2 roles per CV |
| LinkedIn URL in output | Product roles only | Remove for Data Architect roles |

---

## File Modification Notes

- This file was last updated: 2026-09-17
- When adding new templates (e.g., Solution Architect), update this config first before creating new files
- When changing GDrive paths, update both this config and the orchestrator (cv-tailoring.md Phase 0)
- When adding new semantic clusters, update cv-semantic-clusters.md and the term-to-cluster mappings
