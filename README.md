# hiran-skills

Personal Claude Skills library for CV tailoring, interview prep, and job search workflows.

## Structure

Each skill gets its own folder with files organized for clarity and maintainability:

```
hiran-skills/                                  # marketplace root
├── .claude-plugin/
│   └── marketplace.json                       # marketplace manifest — points at plugins/
├── plugins/
│   └── cv-tailoring/                          # the plugin
│       ├── .claude-plugin/
│       │   └── plugin.json                    # plugin metadata
│       └── skills/
│           └── cv-tailoring/                  # the actual skill Claude loads
│               ├── SKILL.md                   # entrypoint — 9-phase orchestrator
│               ├── scripts/
│               │   ├── validate_cv.py          # automated Phase 5.3 checks
│               │   └── build_cv_reference.js   # reference docx-js house-style implementation
│               └── references/                # loaded on demand, not upfront
│                   ├── cv-background.md        # role facts, template selection — write target for Phase 2.5
│                   ├── cv-formatting.md        # hard constraints + voice patterns
│                   ├── cv-config.md            # centralized configuration
│                   ├── cv-decision-gates.md    # phase decision logic (loop targets)
│                   ├── cv-semantic-clusters.md # cluster lookup data only
│                   ├── cv-scoring.md           # ATS methodology (single source of truth)
│                   ├── cv-qa-personas.md       # HM + TA checklists (single source of truth)
│                   ├── cv-market-research.md   # research patterns
│                   └── cv-tracker.md           # tracker schema (GDrive/Sheets)
├── CHANGELOG.md
├── SKILLS.md
└── README.md
```

## Skills

See `SKILLS.md` for the current catalog.

### cv-tailoring (v1.11.1)

Tailors a CV to a job description for CPO/VP Product, Data Architect, Solution/Enterprise Architect, and related senior product/data roles.

**What it does (Phases 0-7, see `SKILL.md` for the full sequence):**
1. Intake — load CV library and reference files (Phase 0)
2. Researches the role and company signals (Phase 1)
3. Assesses gaps against JD requirements, checking `cv-background.md` first (Phase 2)
4. Runs a discovery interview for addressable gaps, writes confirmed facts back to `cv-background.md` (Phase 2.5)
5. Scores ATS keyword coverage before/after via semantic clustering, target 85%+ (Phase 3)
6. Rewrites profile, skills, and bullets to match the JD (Phase 4)
7. Reviews draft text via Hiring Manager + Talent Acquisition lenses before rendering (Phase 5.1), then validates the render's hard constraints (Phase 5.3)
8. Generates a summary report (Phase 6)
9. Logs the application to the Google Sheets tracker in GDrive (Phase 7)

**Recent Example:** TalentInternational Product Director role
- **Before:** 64% ATS coverage (18/28 keywords)
- **After:** 93% ATS coverage (26/28 keywords)
- **Profile rewrite:** "Senior Product Director" + search/discovery + hands-on IC + prototyping tools (Claude Code, Cursor, Lovable, Bolt)
- **Skills regenerated:** 5 lines of JD-only keywords, search/discovery front-loaded
- **Output:** Professional DOCX with all sub-bullets preserved (this
  example predates both the v1.8.0 navy/grey colour house style and the
  v1.10.0 DOCX-only deliverable change — see `cv-formatting.md` for the
  current spec)

**Installation in Claude Code:**
```bash
/plugin marketplace add hiranmanu/hiran-skills
/plugin install cv-tailoring@hiran-skills
```

## Workflow

Three speed modes, defined and enforced in `SKILL.md` Phase 0 (not
just described here — the orchestrator actually skips the right phases
per mode):

### Quick (1-2 min)
Paste JD → get PDF → done. Skips web research and the discovery interview;
never skips validation. Default when you just paste a JD with no other
instruction.

### Balanced (15-20 min)
Paste JD → 2-3 quick questions (only for gaps that move the ATS score) →
generate → review once → upload.

### Full Manual (90-135 min)
All 9 phases with full discovery interview, gap assessment, QA, decision
loops. Best for high-stakes roles or skill refinement.

## Using this from a plain claude.ai chat (no Claude Code)

A chat session without this repo mounted can't read these files directly,
so it's tempting to regenerate the house style from memory/prose rules
alone. That's how the TabStopPosition.MAX bug (dates not flush right) and
the PositionalTab/LibreOffice bug got introduced in September 2026 — a
chat session re-derived the docx-js layout from scratch instead of
starting from the tested reference. If a chat session has shell/git
access, it should `git clone` this repo first and copy
`scripts/build_cv_reference.js` as the literal starting point (see that
file's own header comment), rather than reimplementing `cv-formatting.md`'s
rules from prose each time.

## Updating

Push changes from Claude to GitHub:
```bash
git add -A
git commit -m "Update: <description>"
git push origin master
```

When Hiran confirms new facts about past roles, update `plugins/cv-tailoring/skills/cv-tailoring/references/cv-background.md` so the skill uses them without re-asking.

## Recent Updates

**v1.11.1 (Sep 18, 2026) — Skill audit: fix stale DOCX+PDF references, dedupe title blending, phase mislabel:**
- A full audit found the v1.10.0 "DOCX-only" change hadn't propagated
  everywhere: `SKILL.md`'s Render section, its own frontmatter, `plugin.json`,
  `marketplace.json`, and `cv-config.md` all still described a DOCX+PDF
  deliverable. Aligned all five to DOCX-only.
- Collapsed title-blending rules that were duplicated near-verbatim in
  `cv-background.md` and `cv-formatting.md` into one source of truth.
- Fixed `cv-tracker.md` referencing the wrong phase for GDrive output.
- This README and `SKILLS.md` were themselves found stale at v1.10.0 during
  the audit — fixed alongside this release, see `CHANGELOG.md`.

**v1.11.0 (Sep 18, 2026) — House-style sync: descriptor colon, LinkedIn hyperlink fix, References check automated:**
- Company/descriptor line rule (`City, UK: descriptor`, colon not dash)
  added to `cv-formatting.md` and `cv-config.md`.
- `validate_cv.py` now automates the References/Recommendations check.
- Fixed a `cv-config.md`/`cv-formatting.md` contradiction over whether the
  LinkedIn URL is plain text or hyperlinked (hyperlinked is correct).

**v1.10.0 (Sep 18, 2026) — Docx-only output, widow/orphan rule, Phase 6 enforcement:**
- DOCX made the sole deliverable — a chat session must not present a
  self-generated LibreOffice PDF as final output or pagination proof
  (Carlito vs. real Calibri metrics mismatch caused the v1.9.0 pagination
  bug); LibreOffice rendering stays an internal structural check only.
- Added the same widow/orphan rule Key Skills rows got in v1.9.0 to
  Profile Summary paragraphs.
- `SKILL.md` Phase 6 (Summary Report) now has an explicit "never skipped"
  callout.

**v1.9.0 (Sep 18, 2026) — Chat-session bug fixes + release backfill:**
- Fixed a wrong LinkedIn URL in `cv-config.md` (missing hyphen).
- Rewrote the Key Skills rule to match the confirmed 3-row/middle-dot style.
- Documented two real docx-js bugs (`TabStopPosition.MAX`, `PositionalTab`)
  hit by a chat session working without this repo mounted.
- Broadened the "remove Recommendations" rule to also cover "References".
- Backfilled GitHub Releases for v1.0.0-v1.6.1.

**v1.8.0 (Sep 17, 2026) — House style confirmed, authenticity metadata:**
- Hiran confirmed the separate chat session's conventions (flagged as an open
  question in v1.7.0) ARE the new house style. `cv-formatting.md`,
  `cv-config.md`, and `cv-background.md` rewritten accordingly: plain Calibri
  10.5pt uniform (not Calibri Light), A4 (not US Letter), navy/grey colour
  (not black-and-white), square ▪ primary bullets (not round), hyperlinked
  email/LinkedIn (not plain text), "Profile Summary" heading, ~105-108 char
  bullet budget, tab-aligned dual-nationality line, no more open question.
- Added a DOCX/PDF authenticity requirement: `creator`/`lastModifiedBy` must
  be set to "Hiran Patel" (not a generic tool default) on every generated
  file — verified to carry through to the PDF's Author field on conversion.
  `scripts/validate_cv.py` now checks this automatically.
- Added `scripts/build_cv_reference.js`, a full docx-js reference
  implementation of every rule in `cv-formatting.md` — copy and adapt per JD
  rather than re-deriving the styling from prose each time.

**v1.7.0 (Sep 17, 2026) — Automated Phase 5.3 validation + cross-session audit:**
- Added `scripts/validate_cv.py`, replacing the prose-only "run pdftotext and
  eyeball it" instructions with an actual script: page count, em/en dashes,
  bullet-wrap detection, and role-page-split detection, all in one pass, exit
  code gates the workflow. The last two checks previously had no tooling.
- A separate Claude chat session had been doing CV formatting work without
  knowing this skill existed, using different conventions. Rather than
  silently merge either direction, flagged every discrepancy for Hiran to
  confirm (resolved in v1.8.0 above).
- Deleted the other session's duplicate standalone repo
  (`hiranmanu/cv-tailoring-skill`), created in error instead of updating this
  one.

**v1.6.1 (Sep 17, 2026) — Post-restructure QA sweep:**
- Full per-file read-through after the v1.6.0 restructure rather than trusting the mechanical move; found and fixed 5 stale `cv-tailoring.md` self-references left over from the `SKILL.md` rename

**v1.6.0 (Sep 17, 2026) — Real plugin/skill structure:**
- Restructured into the shape Claude Code's plugin system actually requires (`plugins/cv-tailoring/skills/cv-tailoring/SKILL.md` + `.claude-plugin/plugin.json` + `references/`) — every prior version would not have loaded via `/plugin install`
- Reordered QA: persona review now runs pre-render on draft text, format validation runs post-render, so a content-only fix no longer needs a re-render
- Deduplicated the HM/TA checklists into one source of truth; added the bounded "signature breadth" allowance to the skills-section policy

**v1.5.0 (Sep 17, 2026) — Speed modes operationalized:**
- The three workflow modes (Quick/Balanced/Full Manual) were described in this README but never implemented anywhere executable. `cv-tailoring.md` Phase 0 now has an explicit table mapping each mode to exactly which phases/checkpoints it skips, and `cv-market-research.md` / `cv-qa-personas.md` cross-reference it so they don't contradict it if read standalone.
- Quick mode is now the default for a bare JD paste with no other instruction — skips company research and the discovery interview, never skips Phase 5.3 validation.
- Added an explicit edge case for Solution/Enterprise Architect JDs (no template exists yet) so it surfaces mid-workflow instead of staying buried in `cv-config.md`.

**v1.4.0 (Sep 17, 2026) — Integrity fix:**
- Fixed broken references: `cv-tailoring.md` and `cv-decision-gates.md` pointed at `cv-job-context.md` / `cv-career-history-supplement.md` / `cv-formatting-rules.md`, none of which existed post-v1.3.0 merge. Everything now points at the real files (`cv-background.md`, `cv-formatting.md`).
- Resolved two contradictory scoring methods (weighted keyword-only in `cv-tailoring.md` vs. semantic clustering in `cv-scoring.md`/`cv-semantic-clusters.md`) into one: `cv-scoring.md` is now the single source of truth for the method, `cv-semantic-clusters.md` holds lookup data only.
- Renumbered phases consistently (0, 1, 2, 2.5, 3, 4 with sub-steps 4.1-4.4, 5 with 5.3/5.5, 6, 7) across `cv-tailoring.md`, `cv-decision-gates.md`, and `cv-qa-personas.md` — previously had two conflicting `Phase 6` headers and phase references (5.3, 5.5) with no matching headers anywhere.
- Rewrote `cv-tracker.md`, which still described a local `Hiran_Applications_Tracker.xlsx` with no cross-tool sync, contradicting the GDrive/Google Sheets tracker described everywhere else.
- Deleted `cv-generation-and-qa.md` (orphaned from a prior generation, contained a contradictory filename convention); its still-useful content (character-budget math, QA command sequence, metadata step) merged into `cv-formatting.md` and `cv-decision-gates.md`.
- Deleted `GOOD_TO_GREAT_PLAN.md` — its structural findings are addressed by this fix; it never actually caught the broken references above.

**v1.3.0 (Sep 15, 2026):**
- File consolidation: merged formatting + voice guides, merged context + career history
- Centralized configuration in `cv-config.md` with GDrive folder IDs and workflow defaults
- Explicit decision gate logic in `cv-decision-gates.md` (Phase 2 gap paths, Phase 5 validation checks)
- Enhanced semantic clusters: added Data Architect, Retail Media/First-Party Data, AdTech/Measurement clusters
- Tested full manual workflow on TalentInternational Product Director role: 64% → 93% ATS score

**v1.2.0 (Sep 14, 2026):**
- Semantic clustering for ATS scoring, QA personas framework (Hiring Manager + Talent Acquisition lenses, Phase 5.5), voice guide, and a refined title-blending rule (only 1-2 roles max per CV)
- Added `cv-job-context.md`, `cv-semantic-clusters.md`, `cv-qa-personas.md`

**v1.1.0 (Sep 13/14, 2026):**
- First full end-to-end workflow test (Monzo Chief of Staff → CPO tailoring)
- Added `cv-career-history-supplement.md`, `cv-formatting-rules.md`, `cv-generation-and-qa.md`, `cv-market-research.md`, `cv-scoring.md`, `cv-tracker.md`
- ATS score on that test: 60% → 91%

**v1.0.0 (Sep 13, 2026) — Initial release:**
- `cv-tailoring.md` main skill doc (Phases 0-6), `cv-job-context.md` placeholder, three CV template variants (CPO/VP Product, Data Architect, Solution Architect), weighted-keyword ATS scoring, applications tracker workbook, GitHub repo initialized

See `CHANGELOG.md` for the full detailed history (every version back to
v1.0.0, with the specific files/bugs each one touched) and the repo's
[Releases page](https://github.com/hiranmanu/hiran-skills/releases) for
the same, one release per version.
