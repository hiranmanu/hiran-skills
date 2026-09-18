# hiran-skills

Personal Claude Skills marketplace for CV tailoring, interview prep, and job search workflows. Each skill is a separate plugin with its own independent version, README, and changelog — see [`CLAUDE.md`](CLAUDE.md) for the conventions this repo follows as it grows.

## Structure

```
hiran-skills/                                  # marketplace root
├── .claude-plugin/
│   └── marketplace.json                       # marketplace manifest — lists every plugin + its current version
├── plugins/
│   ├── cv-tailoring/                          # a plugin (= one skill), independently versioned
│   │   ├── .claude-plugin/plugin.json         # this plugin's own version
│   │   ├── README.md                          # this plugin's own writeup
│   │   ├── CHANGELOG.md                       # this plugin's own version history
│   │   └── skills/cv-tailoring/               # the actual skill Claude loads
│   └── <next-skill>/                          # future skills follow the same shape
├── CLAUDE.md                                  # release checklist + repo conventions
├── CHANGELOG.md                               # marketplace-level changes only (new skills, shared tooling, schema)
├── SKILLS.md                                  # thin catalog — one row per skill, links to each plugin's own docs
├── scripts/
│   └── check_release_consistency.py           # verifies every plugin's version is consistent everywhere it's declared
└── README.md                                  # this file
```

## Skills

See [`SKILLS.md`](SKILLS.md) for the current catalog. Each skill's detailed writeup, workflow, and full version history live in its own `plugins/<skill>/README.md` and `plugins/<skill>/CHANGELOG.md` — not duplicated here.

## Installation in Claude Code

```bash
/plugin marketplace add hiranmanu/hiran-skills
/plugin install <skill-name>@hiran-skills
```

See each skill's own README (linked from `SKILLS.md`) for its exact install name.

## Updating

Push changes from Claude to GitHub:
```bash
git add -A
git commit -m "Update: <description>"
git push origin master
```

Before considering a version bump for any skill done, follow [`CLAUDE.md`](CLAUDE.md)'s release checklist and run:
```bash
python3 scripts/check_release_consistency.py
```
It checks every plugin's version is consistent across `plugin.json`, `marketplace.json`, that plugin's own `README.md`/`CHANGELOG.md`, and its row in `SKILLS.md` — and fails loudly if not.

## Recent marketplace-level changes

See [`CHANGELOG.md`](CHANGELOG.md) for changes to the marketplace itself (new skills added, shared tooling, manifest schema). Per-skill changes live in that skill's own `plugins/<skill>/CHANGELOG.md`.
