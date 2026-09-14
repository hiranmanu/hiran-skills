# hiran-skills

Personal Claude Skills library for CV tailoring, interview prep, and job search workflows.

## Structure

Each skill gets its own folder with a `<skill>-` prefix on all internal files:

```
hiran-skills/
├── cv-skill/
│   ├── cv-tailoring.md                      # Main skill
│   ├── cv-career-history-supplement.md      # Confirmed role facts
│   ├── cv-formatting-rules.md               # Generation rules
│   ├── cv-scoring.md                        # ATS methodology
│   ├── cv-generation-and-qa.md              # QA checklist
│   ├── cv-market-research.md                # Research patterns
│   └── cv-tracker.md                        # Tracker schema
├── interview-skill/                         # (Upcoming)
├── linkedin-skill/                          # (Upcoming)
├── .claude-plugin/
│   └── marketplace.json                     # Claude Code manifest
├── SKILLS.md                                # Skill index
└── README.md
```

This structure scales cleanly — each skill folder is self-contained, all files prefixed with `<skill>-`, no nested subfolders, no cross-folder dependencies.

## Skills

See `SKILLS.md` for the current catalog.

### cv-tailoring (v1.1.0)

Tailors a CV to a job description for CPO/VP Product, Data Architect, Solution/Enterprise Architect, and related senior product/data roles.

**What it does:**
1. Extracts keywords from the job description
2. Scores ATS keyword coverage before (baseline) and after (target 85%+)
3. Checks `cv-skill/cv-career-history-supplement.md` for already-confirmed facts
4. Asks for gaps that are plausibly true but unconfirmed
5. Generates a tailored DOCX + PDF (no em dashes, single-line bullets)
6. Logs the application to `Hiran_Applications_Tracker.xlsx`

**Installation in Claude Code:**
```bash
/plugin marketplace add hiranmanu/hiran-skills
/plugin install cv-tailoring@hiran-skills
```

## Updating

Push changes from Claude to GitHub:
```bash
git add -A
git commit -m "Update: <description>"
git push origin master
```

When Hiran confirms new facts about past roles, update `cv-skill/cv-career-history-supplement.md` so the skill uses them without re-asking.
