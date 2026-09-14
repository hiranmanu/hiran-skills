# hiran-claude-skills

Personal Claude Skills / plugins library.

## Plugins

- **cv-tailoring** — tailors a CV to a job description, scores ATS keyword
  coverage before/after, generates a DOCX + PDF, and logs the application
  to `Hiran_Applications_Tracker.xlsx`. See `plugins/cv-tailoring/SKILL.md`.

## Install in Claude Code

    /plugin marketplace add <your-github-username>/hiran-claude-skills
    /plugin install cv-tailoring@hiran-claude-skills

## Note on claude.ai

This repo follows Claude Code's documented plugin/marketplace format. It is
not yet confirmed whether claude.ai's own plugin catalog (the one your
Projects can install from) reads directly from a GitHub marketplace like
this one, or requires a separate admin/publishing step — check
docs.claude.com or support.claude.com before assuming this repo alone
makes the skill available inside claude.ai chats.

## Updating

The `career-history-supplement.md` file under
`plugins/cv-tailoring/references/` holds facts Hiran has confirmed that
supplement the base CV (board/investor exposure, BI tools used, Design
ownership per role). Keep it current — the skill checks it before asking
about ATS gaps it might already have an answer for.
