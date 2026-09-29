# Available Skills

Catalog of every skill in this marketplace. Each skill versions independently — see its own `README.md`/`CHANGELOG.md` for details, not this file.

| Skill | Version | Description | Docs |
|---|---|---|---|
| `cv-tailoring` | 2.0.0 | Tailors a CV to a job description in one 8-step workflow: intake, parse the JD, gap check (asks about anything addressable), ATS score, draft, independent review, render and validate, report. Master fact file, no modes, DOCX to a local output folder. | [README](plugins/cv-tailoring/README.md) · [CHANGELOG](plugins/cv-tailoring/CHANGELOG.md) |

> `interview-prep` moved to its own repository, [`hiranmanu/interview-prep`](https://github.com/hiranmanu/interview-prep), on 2026-09-29: it and CV tailoring are distinct jobs at different points in time.

## Installation

```bash
/plugin marketplace add hiranmanu/hiran-skills
/plugin install <skill-name>@hiran-skills
```

e.g. `/plugin install cv-tailoring@hiran-skills`.

## Upcoming Skills

- `linkedin-optimizer` — LinkedIn profile optimization (headline, summary, experience section)

Each will land as its own plugin under `plugins/`, with its own `plugin.json` version starting at `1.0.0`, independent of every other skill's version — see `CLAUDE.md` for the checklist to follow when adding one.
