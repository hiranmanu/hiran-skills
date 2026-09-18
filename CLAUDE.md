# Working in this repo

This is a Claude Code plugin marketplace (`hiran-skills`). Each skill is
its own plugin under `plugins/<skill-name>/`, versioned independently.
Today that's `cv-tailoring`; more (job-prep, LinkedIn optimization, etc.)
are coming — see `SKILLS.md` "Upcoming Skills".

## Release checklist — bumping an existing skill's version

Every file below states that plugin's version. Bump all of them **for that
plugin only** in the same commit — don't touch other plugins' files, and
don't bump `marketplace.json`'s top-level version for this (see below).

| File | What to update |
|---|---|
| `plugins/<skill>/.claude-plugin/plugin.json` | `version` field |
| `.claude-plugin/marketplace.json` | that plugin's entry `version` only — **not** the top-level `version` |
| `plugins/<skill>/CHANGELOG.md` | new `## [X.Y.Z] - <date>` entry at the top |
| `plugins/<skill>/README.md` | `# <skill> (vX.Y.Z)` header, plus a line under "Recent Updates" |
| `SKILLS.md` (root) | that skill's row in the catalog table — version + description if changed |
| git tag | `git tag -a <skill>-vX.Y.Z -m "..."` and `git push origin <skill>-vX.Y.Z` |
| GitHub Release | one release per tag (`gh release create <skill>-vX.Y.Z` or the web UI) |

Skill-internal reference files (e.g. `cv-config.md`'s "last updated" date)
are that skill's own concern — check its own `SKILL.md`/references for
anything else it says must be touched on a change.

**Before calling a version bump done, run:**
```bash
python3 scripts/check_release_consistency.py
```
It loops over every plugin and fails loudly on any mismatch — treat a
failing run the same as a failing test, not an FYI. This has already
caught real drift twice before it existed (see
`plugins/cv-tailoring/CHANGELOG.md`'s v1.9.0 and v1.11.1 entries) — don't
skip it because the change "looks small."

`.github/workflows/release-consistency.yml` also runs this on every push
and PR to `master`, so a mismatch that slips past a local run still gets
caught before/at merge — don't rely on that as the only check, but it's
the backstop for when running it locally gets forgotten under time
pressure, which is exactly how the drift happened before.

## Checklist — adding a brand-new skill

1. Create `plugins/<skill-name>/` with the same shape as `cv-tailoring`:
   `.claude-plugin/plugin.json`, `README.md`, `CHANGELOG.md`,
   `skills/<skill-name>/SKILL.md` (+ `references/`, `scripts/` as needed).
   `plugin.json`'s `version` starts at `1.0.0`, independent of every other
   plugin.
2. Add an entry to `.claude-plugin/marketplace.json`'s `plugins` array.
3. Add a row to the root `SKILLS.md` catalog table, and move it out of
   "Upcoming Skills" if it was listed there.
4. Bump `marketplace.json`'s **top-level** `version` (this is the one case
   where that bumps — a new skill is a structural change to the
   marketplace itself) and add an entry to the root `CHANGELOG.md`
   (marketplace-level, not the new skill's own).
5. Run `python3 scripts/check_release_consistency.py` — it will pick up
   the new plugin automatically (it discovers plugins by globbing
   `plugins/*/.claude-plugin/plugin.json`, nothing to register manually).
6. Tag it `<skill-name>-v1.0.0`.

## Two-changelog model — don't confuse them

- **Root `CHANGELOG.md`**: marketplace-level only. New skill added/removed,
  shared `scripts/` tooling, `marketplace.json` schema changes. Its entries
  are dated, not tied to a single semver — there's no one "marketplace
  version" that means anything once skills version independently.
- **`plugins/<skill>/CHANGELOG.md`**: that skill's full history, semver-tagged,
  matching its `plugin.json` version. This is where 95% of day-to-day work
  gets logged.

If you're not sure which one an entry belongs in: does it change what a
skill *does*, or how it's packaged/generated/rendered? → that skill's own
changelog. Does it change the shape of the repo itself? → root changelog.

## Plugin self-containment — don't reach across plugin folders

Claude Code installs each plugin independently (`/plugin install
<skill>@hiran-skills` only pulls that plugin's subtree). A skill's
`SKILL.md`/references must **never** point at a file in a different
plugin's folder — it won't exist for someone who only installed this one
skill.

If two skills genuinely need the same underlying facts (e.g. a future
`interview-prep` skill wanting the same confirmed-role facts
`cv-tailoring`'s `cv-background.md` already has), the options are, in
order of preference:
1. **Duplicate deliberately**, with an explicit note in both files saying
   where the other copy lives and that they need to be kept in sync by
   hand (same pattern already used for cross-references within
   cv-tailoring — see `cv-scoring.md` / `cv-semantic-clusters.md`).
2. Don't build a shared/common `plugins/_shared/` folder and reference it
   from multiple plugins' `SKILL.md` — it'll work for you locally (mounted
   as one repo) but silently break for anyone who installs only one of the
   two plugins.

## Other conventions

- Cross-reference, don't duplicate within a single skill: reference files
  that describe the same logic from two places (e.g. scoring method vs.
  cluster lookup data) must say explicitly which one is the single source
  of truth. See `cv-scoring.md` / `cv-semantic-clusters.md` for the pattern
  to copy.
- When a rule changes in one reference file, check whether a sibling file
  states the same rule elsewhere — that's exactly how the DOCX+PDF drift
  and title-blending duplication (fixed in cv-tailoring v1.11.1) happened.
- Watch for hardcoded, environment-specific absolute paths in a skill's
  config file (e.g. `cv-config.md`'s `/home/claude/cv-work/...`) — flagged
  once as a portability risk, not yet resolved. Don't introduce the same
  pattern in a new skill's config without at least documenting the
  assumption explicitly.
