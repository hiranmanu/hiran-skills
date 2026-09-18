# Changelog — marketplace

Changes to the marketplace itself: new skills added or removed, shared
tooling (`scripts/`), manifest schema, and repo-wide conventions. This file
does **not** track individual skills' changes — each plugin has its own
`CHANGELOG.md` (e.g. [`plugins/cv-tailoring/CHANGELOG.md`](plugins/cv-tailoring/CHANGELOG.md))
and versions independently.

Entries here are dated, not semver-tagged to a single number — there's no
one "marketplace version" that means much on its own now that skills
version independently. `marketplace.json`'s top-level `version` bumps on
structural changes only (a new skill added, schema change), not on every
skill release.

## 2026-09-18 — Repository restructure: independent per-plugin versioning

The marketplace is about to grow beyond one skill (`cv-tailoring`), so
moved from one shared version number for the whole repo to each plugin
versioning independently.

- This `CHANGELOG.md` used to document `cv-tailoring` exclusively (it was
  the only skill). That full history moved to
  `plugins/cv-tailoring/CHANGELOG.md`, which is now the source of truth for
  that plugin's version history.
- `README.md` (root) thinned to a marketplace-level index; the detailed
  cv-tailoring writeup moved to `plugins/cv-tailoring/README.md`.
- `SKILLS.md` thinned to a catalog table (skill, version, one-liner, links)
  instead of embedding each skill's full version history — that was a
  third copy of the same content already in each plugin's own `CHANGELOG.md`.
- `scripts/check_release_consistency.py` rewritten to loop over every
  `plugins/*/` and check each plugin's version independently, rather than
  being hardcoded to `cv-tailoring`.
- `marketplace.json`'s top-level `version` decoupled from any single
  plugin's version — bumped to `1.12.0` to mark this structural change;
  going forward it moves only when the marketplace/catalog structure
  itself changes.
- New convention: future git tags use `<plugin-name>-vX.Y.Z` (e.g.
  `cv-tailoring-v1.11.2`) instead of bare `vX.Y.Z`, so a second plugin's
  tags can't collide with the first's. Existing bare tags (`v1.0.0`
  through `v1.11.1`) predate this and are left as-is — unambiguous today
  since `cv-tailoring` was the only plugin at the time.

See [`CLAUDE.md`](CLAUDE.md) for the updated release checklist this
restructure introduces.
