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

### cv-tailoring (v1.6.1)

Tailors a CV to a job description for CPO/VP Product, Data Architect, Solution/Enterprise Architect, and related senior product/data roles.

**What it does (Phases 0-7, see `cv-tailoring.md` for the full sequence):**
1. Intake — load CV library and reference files (Phase 0)
2. Researches the role and company signals (Phase 1)
3. Assesses gaps against JD requirements, checking `cv-background.md` first (Phase 2)
4. Runs a discovery interview for addressable gaps, writes confirmed facts back to `cv-background.md` (Phase 2.5)
5. Scores ATS keyword coverage before/after via semantic clustering, target 85%+ (Phase 3)
6. Rewrites profile, skills, and bullets to match the JD (Phase 4)
7. Validates hard constraints (Phase 5.3) and reviews via Hiring Manager + Talent Acquisition lenses (Phase 5.5)
8. Generates a summary report (Phase 6)
9. Logs the application to the Google Sheets tracker in GDrive (Phase 7)

**Recent Example:** TalentInternational Product Director role
- **Before:** 64% ATS coverage (18/28 keywords)
- **After:** 93% ATS coverage (26/28 keywords)
- **Profile rewrite:** "Senior Product Director" + search/discovery + hands-on IC + prototyping tools (Claude Code, Cursor, Lovable, Bolt)
- **Skills regenerated:** 5 lines of JD-only keywords, search/discovery front-loaded
- **Output:** Professional black-and-white DOCX/PDF with all sub-bullets preserved

**Installation in Claude Code:**
```bash
/plugin marketplace add hiranmanu/hiran-skills
/plugin install cv-tailoring@hiran-skills
```

## Workflow

Three speed modes, defined and enforced in `cv-tailoring.md` Phase 0 (not
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

## Updating

Push changes from Claude to GitHub:
```bash
git add -A
git commit -m "Update: <description>"
git push origin master
```

When Hiran confirms new facts about past roles, update `plugins/cv-tailoring/skills/cv-tailoring/references/cv-background.md` so the skill uses them without re-asking.

## Recent Updates

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
