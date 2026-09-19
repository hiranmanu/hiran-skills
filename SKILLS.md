# Available Skills

Catalog of every skill in this marketplace. Each skill versions independently — see its own `README.md`/`CHANGELOG.md` for details, not this file.

| Skill | Version | Description | Docs |
|---|---|---|---|
| `cv-tailoring` | 1.14.0 | Tailors a CV to a job description using an 8-phase workflow: intake → research → gap assessment → discovery → ATS scoring → generation → validation/QA → summary. Saves DOCX to a local output folder; no cloud sync. | [README](plugins/cv-tailoring/README.md) · [CHANGELOG](plugins/cv-tailoring/CHANGELOG.md) |
| `interview-prep` | 1.2.0 | Builds interview intel from a JD + company: research (incl. named interviewers, filings, hiring signals), STAR answers, smart questions, intro, engagement-type-aware HR-screen basics. Multi-round aware; builds the presentation itself when a round requires one. Scales from a 10-minute rapid brief to a full dossier. | [README](plugins/interview-prep/README.md) · [CHANGELOG](plugins/interview-prep/CHANGELOG.md) |

## Installation

```bash
/plugin marketplace add hiranmanu/hiran-skills
/plugin install <skill-name>@hiran-skills
```

e.g. `/plugin install cv-tailoring@hiran-skills`.

## Upcoming Skills

- `linkedin-optimizer` — LinkedIn profile optimization (headline, summary, experience section)

Each will land as its own plugin under `plugins/`, with its own `plugin.json` version starting at `1.0.0`, independent of every other skill's version — see `CLAUDE.md` for the checklist to follow when adding one.
