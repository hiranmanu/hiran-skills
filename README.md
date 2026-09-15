# hiran-skills

Personal Claude Skills library for CV tailoring, interview prep, and job search workflows.

## Structure

Each skill gets its own folder with files organized for clarity and maintainability:

```
hiran-skills/
├── cv-skill/
│   ├── cv-tailoring.md                      # Main 9-phase workflow
│   ├── cv-background.md                     # Role facts + template selection
│   ├── cv-formatting.md                     # Hard constraints + voice patterns
│   ├── cv-config.md                         # Centralized configuration
│   ├── cv-decision-gates.md                 # Phase decision logic
│   ├── cv-semantic-clusters.md              # Keyword clustering + scoring
│   ├── cv-scoring.md                        # ATS methodology
│   ├── cv-generation-and-qa.md              # QA checklist
│   ├── cv-market-research.md                # Research patterns
│   └── cv-tracker.md                        # Tracker schema
├── interview-skill/                         # (Upcoming)
├── linkedin-skill/                          # (Upcoming)
├── marketplace.json                         # Claude marketplace manifest
├── CHANGELOG.md                             # Version history
├── GOOD_TO_GREAT_PLAN.md                    # Improvement roadmap
├── SKILLS.md                                # Skill index
└── README.md
```

## Skills

See `SKILLS.md` for the current catalog.

### cv-tailoring (v1.3.0)

Tailors a CV to a job description for CPO/VP Product, Data Architect, Solution/Enterprise Architect, and related senior product/data roles.

**What it does:**
1. Researches the role and company signals (Phase 1)
2. Assesses gaps against JD requirements (Phase 2)
3. Scores ATS keyword coverage before (baseline) and after (target 85%+) (Phase 3)
4. Rewrites profile, skills, and bullets to match JD (Phase 4)
5. Generates a tailored DOCX + PDF with proper formatting (Phase 5)
6. Validates output against hard constraints and voice patterns (Phase 5)
7. Generates QA checklist and application summary (Phase 6)
8. Logs the application to `Hiran_Applications_Tracker.xlsx` (Phase 6)
9. Uploads tailored files to GDrive (Phase 7)

**Recent Example:** TalentInternational Product Director role
- **Before:** 64% ATS coverage (18/28 keywords)
- **After:** 93% ATS coverage (26/28 keywords)
- **Profile rewrite:** "Senior Product Director" + search/discovery + hands-on IC + prototyping tools (Claude Code, Cursor, Lovable, Bolt)
- **Skills regenerated:** 5 lines of JD-only keywords, search/discovery front-loaded
- **Output:** Professional black-and-white DOCX/PDF with all sub-bullets preserved

**Installation in Claude Code:**
```bash
/plugin marketplace add hiranmanu/hiran-skills
/plugin install cv-tailoring@hiran-skills
```

## Workflow

### Quick (1-2 min)
Fire & forget: Paste JD → get PDF → done. No gates, no review.

### Balanced (15-20 min)
Paste JD → 2-3 quick questions → generate → review once → upload. Recommended.

### Full Manual (90-135 min)
All 9 phases with discovery interview, gap assessment, QA, decision loops. Best for high-stakes roles or skill refinement.

## Updating

Push changes from Claude to GitHub:
```bash
git add -A
git commit -m "Update: <description>"
git push origin master
```

When Hiran confirms new facts about past roles, update `cv-skill/cv-background.md` so the skill uses them without re-asking.

## Recent Updates

**v1.3.0 (Sep 15, 2026):**
- File consolidation: merged formatting + voice guides, merged context + career history
- Centralized configuration in `cv-config.md` with GDrive folder IDs and workflow defaults
- Explicit decision gate logic in `cv-decision-gates.md` (Phase 2 gap paths, Phase 5 validation checks)
- Enhanced semantic clusters: added Data Architect, Retail Media/First-Party Data, AdTech/Measurement clusters
- Good to Great improvement plan with 14-18 hours of enhancement work (prioritized)
- Tested full manual workflow on TalentInternational Product Director role: 64% → 93% ATS score
