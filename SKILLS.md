# Available Skills

Catalog of every skill in this marketplace. Each skill versions independently — see its own `README.md`/`CHANGELOG.md` for details, not this file.

| Skill | Version | Description | Docs |
|---|---|---|---|
| `cv-tailoring` | 1.11.2 | Tailors a CV to a job description using a 9-phase workflow: intake → research → gap assessment → discovery → ATS scoring → generation → validation/QA → summary → tracker sync. | [README](plugins/cv-tailoring/README.md) · [CHANGELOG](plugins/cv-tailoring/CHANGELOG.md) |

## Installation

```bash
/plugin marketplace add hiranmanu/hiran-skills
/plugin install <skill-name>@hiran-skills
```

e.g. `/plugin install cv-tailoring@hiran-skills`.

## Upcoming Skills

- `interview-prep` — Interview prep (STAR format, Q&A, role-specific research, mock interviews)
- `linkedin-optimizer` — LinkedIn profile optimization (headline, summary, experience section)

Each will land as its own plugin under `plugins/`, with its own `plugin.json` version starting at `1.0.0`, independent of `cv-tailoring`'s version — see `CLAUDE.md` for the checklist to follow when adding one.
