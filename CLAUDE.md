# Working in this repo

This is a Claude Code plugin marketplace (`hiran-skills`). One plugin
(`cv-tailoring`) lives under `plugins/cv-tailoring/`.

## Release checklist — every version bump

This repo has a documented history of version-number drift: `marketplace.json`
sat stale at 1.4.0 until v1.9.0 caught it; `README.md`/`SKILLS.md` sat stale
at v1.10.0 until a manual audit in v1.11.1 caught that. Both happened because
a version was bumped in the "primary" files without touching every place
that also declares it.

**Every file below states the current version or must be updated on release.
Bump all of them in the same commit — not just the ones that feel primary:**

| File | What to update |
|---|---|
| `plugins/cv-tailoring/.claude-plugin/plugin.json` | `version` field |
| `.claude-plugin/marketplace.json` | top-level `version` AND the `cv-tailoring` plugin entry's `version` |
| `plugins/cv-tailoring/skills/cv-tailoring/references/cv-config.md` | "File Modification Notes" → "last updated" date |
| `README.md` | `### cv-tailoring (vX.Y.Z)` header, plus a new entry under "Recent Updates" |
| `SKILLS.md` | `## cv-tailoring (vX.Y.Z)` header, plus a new entry under "Version History" |
| `CHANGELOG.md` | new `## [X.Y.Z] - <date>` entry at the top, in the existing Added/Fixed/Housekeeping style |
| git tag | `git tag -a vX.Y.Z -m "..."` and `git push origin vX.Y.Z` |
| GitHub Release | one release per version tag (create via `gh release create` or the web UI — this repo's convention, see CHANGELOG's v1.9.0 backfill note) |

**Before calling a version bump done, run:**
```bash
python3 scripts/check_release_consistency.py
```
It fails loudly on any mismatch instead of relying on someone remembering
to grep manually — treat a failing run the same as a failing test, not an
FYI.

## Other conventions

- Cross-reference, don't duplicate: reference files that describe the same
  logic from two places (e.g. scoring method vs. cluster lookup data) must
  say explicitly which one is the single source of truth. See
  `cv-scoring.md` / `cv-semantic-clusters.md` for the pattern to copy.
- When a rule changes in `cv-formatting.md`, check whether `cv-config.md`
  or `cv-background.md` state the same rule elsewhere — that's exactly how
  the DOCX+PDF drift and title-blending duplication (fixed in v1.11.1)
  happened.
