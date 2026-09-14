# hiran-claude-skills

Personal Claude Skills library for CV tailoring, interview prep, and job search workflows. Inspired by [ai-with-remy/team-skills](https://github.com/ai-with-remy/team-skills).

## Structure

- **skills/** — Claude SKILL.md definitions + inline references
- **content/** — Shared reference docs (career facts, formatting rules, ATS scoring methodology)
- **general/** — Skill index and general documentation
- **.claude-plugin/** — Claude Code plugin manifest + marketplace metadata
- **scripts/** — (Upcoming) automation scripts for batch processing, GitHub sync, etc.

## Skills

### cv-tailoring
Tailors a CV to a job description for CPO/VP Product, Data Architect, Solution/Enterprise Architect, and related senior product/data roles.

**What it does:**
1. Extracts keywords from the job description
2. Scores ATS keyword coverage before (baseline) and after (target 85%+)
3. Checks `content/career-history-supplement.md` for already-confirmed facts
4. Asks for gaps that are plausibly true but unconfirmed
5. Generates a tailored DOCX + PDF (no em dashes, single-line bullets)
6. Logs the application to `Hiran_Applications_Tracker.xlsx`

**Key files:**
- `skills/cv-tailoring.md` — the skill definition
- `skills/cv-tailoring-refs/` — supporting references (formatting, scoring, generation QA)
- `content/career-history-supplement.md` — per-role facts (board/investor, BI tools, Design ownership)

See `content/scoring.md` for how ATS coverage is computed.

## Installation in Claude Code

```bash
/plugin marketplace add ai-with-remy/hiran-claude-skills
/plugin install cv-tailoring@hiran-claude-skills
```

## Note on claude.ai

This repo follows Claude Code's plugin/marketplace format. Use in claude.ai Projects may require a separate publish step — check docs.claude.com/plugins for details.

## Updating

When Hiran confirms new facts about past roles (board/investor exposure, BI tools, Design involvement), add them to `content/career-history-supplement.md` so the skill can use them without re-asking.

## Roadmap

- [x] cv-tailoring skill + ATS scoring (v1.1.0)
- [ ] Interview prep skill (STAR format, role-specific research, Q&A)
- [ ] LinkedIn profile optimization skill
- [ ] Batch CV tailoring (multiple JDs in one pass)
- [ ] GitHub Actions workflow for syncing tracker + CVs
