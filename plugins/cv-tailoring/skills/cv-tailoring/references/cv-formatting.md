# CV Formatting & Voice Guide

Hard constraints and voice patterns for all CV tailoring. This covers both formatting rules and the specific voice/tone that defines Hiran's CVs.

## Part 1: Hard Constraints

### Content Rules

- **No em dashes anywhere in generated CV text** — profile, bullets, role context lines, everything. Use a comma, colon, or semicolon instead, or split into two sentences. This matches the user's own writing register.
  - Example: "Won $28M — the largest AdTech deal ever closed" → "Won $28M, the largest AdTech deal ever closed"
- **No personality-trait bullets.** Never add "passionate about X" or "excited by Y." Facts only.
- **No en dashes either.** Same rule as em dashes, same reason. Date ranges
  use a plain hyphen: `Jan 2026 - present`, not `Jan 2026 – present`.
- **Single-line bullets only.** No wraps to a second line, ever — this is a
  hard rule, not a preference. Budget the character count *while writing*,
  not after export — catching a wrap after render is too late to feel
  reliable. At Calibri 10.5pt on an A4 page with the margins in this
  template (top/bottom 560 twips, left/right 680 twips), a bulleted line
  (glyph + indent) holds roughly 105-108 characters including spaces and
  punctuation. This is template-specific: it will shift if margins, font
  size, or font family ever change — re-derive it (render + measure) rather
  than assuming it still holds after a layout change. When a bullet
  genuinely doesn't fit, cut a weaker clause rather than shrinking font
  size or margins — those aren't available levers. This is a proactive
  budget, not a guarantee: still run `scripts/validate_cv.py` (§Validation
  below), since actual rendering also depends on kerning and any bold runs
  (company names, metrics), which render wider than plain text.
- **Career-history bullet marker is a small square (▪), not round.** Applies
  to primary bullets throughout the Career & Key Achievements section.
- **Blended titles (when appropriate).** When a past role's actual title undersold its real scope, prefix it with the functional title:
  - Format: `{Functional Title}, {Actual Title}`
  - Example: `Head of Product, Principal AdTech Consultant` (Amazon)
  - Example: `Senior Product Director, VP of Product` (OneAdvanced)
  - **Critical rule:** Only blend 1-2 roles maximum per CV. Don't blend every role. Choose roles where the scope-to-title mismatch is genuinely significant and relevant to the JD. Blending all roles looks manufactured and fake.
  - Rule: Only blend if the functional title genuinely matches the scope. Never manufacture a title that isn't true.
  - For JD-specific tailoring: If the JD calls for "Product Director," and you held "VP of Product," blend it as `Senior Product Director, VP of Product` to show direct relevance without fabrication.
- **Keyword placement in bullets.** When tailoring for a JD:
  - Lead with the keyword if possible: "Architected search and discovery infrastructure..." not "Built infrastructure for search and discovery..."
  - Reorder bullets to surface JD-relevant work first, even if it means moving older achievements up.
  - Never rewrite a bullet to force a keyword that isn't truthfully there.

### Font & Layout Rules

Confirmed as the house style (2026-09-17), superseding all earlier Calibri
Light / US Letter / black-and-white guidance in this file's history:

- **Font:** plain Calibri, 10.5pt, uniform across every section — Profile
  Summary, Key Skills, role titles/dates, company lines, and bullets all
  match. Not Calibri Light: tried it, a direct side-by-side PDF comparison
  came back preferring plain Calibri. Never let sizes drift apart across
  sections (e.g. Profile Summary at 10.5pt while bullets sit at 9.5pt reads
  as inconsistent — this happened once and was flagged as a mistake).
- **Page size:** A4, not US Letter. Margins: top/bottom 560 twips, left/right
  680 twips (tight, for 2-page density).
- **Colour scheme:** navy headings (`#1F3864`), near-black body text
  (`#222222`), mid-grey secondary text (`#555555`) — not black-and-white.
  Section headings get a thin navy bottom border/rule.
- **Line spacing:** 1.15 (line: 276, lineRule: auto) on paragraphs that may
  wrap (Profile Summary, Key Skills rows, bullets). Single-line elements
  (role title/date line, company/descriptor line) must NOT carry this
  multiplier — it inflates their height even though they never wrap, which
  visibly enlarges the gap between e.g. a role title and its company line
  below it. Leave those at default line spacing.
- **Bullet spacing:** zero extra space between bullets within the same role
  (spacing.after: 0) — the gap comes from line height alone. Save
  spacing.after for section/role breaks only.
- **Header layout:**
  - Name: left-aligned, bold, large, navy
  - Contact line: `London, UK | Phone | Email (hyperlinked, mailto:) | LinkedIn (hyperlinked)`
    — no parenthetical asides (e.g. don't add "(open to remote/global)")
  - Role dates: right-aligned via a tab stop, **not bold**, same size as
    everything else. Compute the tab position explicitly from this
    template's actual page width minus its margins — do NOT use docx-js's
    `TabStopPosition.MAX`, which is a fixed 9026-twip constant tuned for a
    different margin setup and undershoots the true right edge here (this
    caused a real "dates aren't flush right" bug). Also avoid `PositionalTab`
    (`w:ptab`) for this — it renders broken in LibreOffice (text runs into
    the date with no space), which is how this got caught. `roleHeader()`
    in `build_cv_reference.js` has the correct working tab-stop math; copy
    it rather than re-deriving from scratch.
  - Dual nationality: appears once only, at the bottom under
    Qualifications/Personal Details, right-aligned to the same tab stop as
    role dates (`Languages: ... [tab] Joint Nationality: British & American`)
    — never repeated in the Profile. A brief "markets covered" phrase can be
    folded into the end of the Profile Summary's second paragraph instead,
    in matching (non-italic, non-grey) formatting, not as a standalone aside.
  - LinkedIn URL: **Product roles only** (Product CV includes it, Data
    Architect CV does not) — hyperlinked (`mailto:` for email too), not
    plain text
- **Section heading:** "Profile Summary", not "Profile" (ATS-friendly)
- **Recommendations/References section:** Remove entirely for all roles —
  applies to either label ("Recommendations" or "References"), and to a
  placeholder line like "available on request" too. Don't add either
  heading, even empty.
- **Sections order:** Profile Summary, Key Skills & Competencies, Career & Key Achievements, Qualifications/Certifications/Personal Details
- **Document authenticity metadata:** every generated `.docx` must set
  `creator` and `lastModifiedBy` to `"Hiran Patel"` (plus a real `title`,
  e.g. `"Hiran Patel - CV"`), not left as a generic tool/library default —
  this carries through to the PDF's Author field on conversion (verified via
  `pdfinfo`). `scripts/validate_cv.py` checks this automatically (see
  Validation below).
- **Naming:** "dunnhumby" is always lowercase, in every position including
  at the start of a line/sentence.
- **Vague filler:** avoid phrases like "details available on request" for
  early-career entries — write out the actual substance instead, however
  brief.
- **Page-split protection:** each role (title + company line + all its
  bullets) must stay together and complete on a single page — never split
  across a page break. In docx-js terms: `keepNext`/`keepLines` on every
  paragraph in the role's block except the last.
- **Document length:** hard cap, never exceed 2 pages, whatever else a
  content pass adds.

A full reference implementation of every rule above (docx-js, Node) lives at
`scripts/build_cv_reference.js` in this skill — copy and adapt it per JD
rather than re-deriving the styling from prose each time.

### Output Format

- **DOCX is the deliverable; don't self-generate a PDF as the final
  artifact.** `soffice`/LibreOffice substitutes Carlito for Calibri, which
  is close but not metric-identical — it can under- or over-predict line
  wraps and page breaks versus real Word. Presenting a LibreOffice-rendered
  PDF as if its pagination is authoritative is how the 3-page/role-split
  bug happened: the DOCX looked correct against one renderer and wrong
  against the other. Ship the `.docx`; Hiran exports the PDF himself from
  real Word/Calibri when he needs one, which is the only render that
  actually reflects what a reader will see.
- **LibreOffice rendering is still fine as an internal structural
  gut-check** (page count sanity, does the numbering config parse, is text
  extractable) — just don't present that PDF to Hiran as a deliverable or
  cite its exact page/line breaks as proof of anything. Treat its output
  as "probably fine," not "verified."
- **Filename format still applies to the DOCX:**
  `{YYYY-MM-DD}_{Company}_{Role}.docx` (drop the `.pdf` half of the pair
  described below unless a PDF is separately requested).
  - Example: `2026-09-14_TalentInternational_ProductDirector.docx`
  - Use ISO date format (YYYY-MM-DD) in filenames, folder-date format (YYYY.MM.DD) for GDrive subfolder names.

### ATS Parsing Rules

- **pdftotext -layout must be readable.** This still needs *a* rendered PDF to check against (LibreOffice's is fine for this — text extraction and em-dash grepping don't depend on exact font metrics the way pagination does), just don't hand that PDF to Hiran as the deliverable. Spot-check 3-4 bullets parse as continuous text, not gibberish.
- **No em dashes in PDF text output.** Grep the PDF text extract for "—". Must be zero.

### Profile/Headline Rules

- **Mirror JD role title language in the headline.** If the JD calls for "Senior Product Director," start with "Senior Product Director" not "Product executive."
- **Front-load JD-relevant keywords in the first two sentences.** After the title, the next 30-40 words should hit 3-4 of the top keywords from the JD (search, discovery, recommendations, AI/LLMs, CRM, CDP, MarTech, etc.).
- **No widow/orphan lines.** Same principle as the Key Skills rows below,
  applied to Profile Summary's flowing prose: a paragraph must not wrap so
  its final line holds only 1-2 words. Check this by rendering and reading
  the actual wrap point, not by eyeballing sentence length — trim or
  extend the sentence so the last line carries a reasonable fraction of
  the line width. This applies to every paragraph in Profile Summary, not
  just the last one in the section.
- **Reflect hands-on IC positioning if the role requires it.** "Comfortable operating as a hands-on individual contributor" should appear if the JD emphasizes this.
- **Include integration/collaboration language.** "Working directly with Engineering," "GTM collaboration," "Sales partnership" — these are keywords worth surfacing early.

### Skills Section Rules

- **JD-priority ordering.** Top line: keywords from the JD's "must-have"
  section — this is what both the ATS parser and a skimming recruiter hit
  first, so it carries the keyword-density weight. Secondary lines:
  adjacent capabilities relevant to the role.
- **No speculative tech.** If the JD doesn't mention "Power BI" or "Looker,"
  don't list BI tools by name unless it's a truthful, differentiating
  addition per the rule below. Never invent a tech stack.
- **Don't include irrelevant domains** (e.g., "CPG, FMCG" if the JD is B2B
  SaaS with no retail mention) — this dilutes relevance, distinct from the
  differentiator case below, which is deliberate and bounded.
- **Signature breadth (optional, max 1-2 items, always last).** A CV that's
  100% JD-mirrored can read as narrower than the person actually is —
  losing the signal that they bring more than the minimum bar. Where a real,
  truthful skill exists that JD keywords don't cover but that's genuinely
  differentiating for this level of role (e.g., a Data Architect JD with no
  mention of executive stakeholder communication, and the person has real
  board-level reporting experience), it's fine to add up to 1-2 such items
  at the *end* of the skills line, after every JD keyword. Rules for this:
  - Never precedes a JD keyword in the line — density up front always wins.
  - Never counts toward, or displaces, the ATS coverage score in Phase 3 —
    it's for the human reader, not the parser.
  - Must be something `cv-background.md` or the CV library already
    confirms as true — this is never a place to test a claim.
  - If it would push the line over the character budget below, cut it
    before cutting a JD keyword.
- **Format:** exactly 3 rows, middle-dot (`\u00b7`) divider between items,
  each row deliberately wrapping to roughly 1.4-1.8 lines — never a 3rd
  line, and never a 2nd line with only 1-3 orphan words (that means the
  row is under-filled: add more keywords to that row rather than leaving
  a short spill). Balance by rendering and checking the actual wrap point
  after adding/removing an item, not by eyeballing source-string length —
  bold runs, punctuation density, and kerning all shift where it breaks.

### Validation Before Output

Run `python3 scripts/validate_cv.py <path> --max-pages 2` (see `cv-decision-gates.md`
§5.3) — it automates the five checks below marked ⚙ in one pass. The rest still need
a human look at the rendered page images.

- [ ] ⚙ No em dashes or en dashes (grep on PDF text extraction)
- [ ] ⚙ No bullet wraps to second line
- [ ] ⚙ No role split across a page boundary
- [ ] ⚙ Page count within cap (default 2)
- [ ] ⚙ DOCX/PDF Author metadata is "Hiran Patel", not a generic tool default
- [ ] pdftotext -layout is readable (spot-check 3-4 bullets) — not automated; garbled/reordered text needs a human read
- [ ] Filename format correct: `{YYYY-MM-DD}_{Company}_{Role}`
- [ ] Blended titles used only when truthfully justified
- [ ] Keywords from JD surfaced in profile, skills, and top bullets
- [ ] No keywords forced into bullets where they don't truthfully belong
- [ ] Square bullets (▪) used for primary career bullets
- [ ] LinkedIn URL present only for Product roles, hyperlinked, and reads
      `https://www.linkedin.com/in/hiran-patel/` exactly (confirmed URL —
      `cv-config.md`'s table is the source of truth; if the two ever
      disagree, `cv-config.md` is stale, not this line)
- [ ] Recommendations/References section removed (either label)
- [ ] Each Key Skills row wraps to ~1.4-1.8 lines, not a 3rd line and not
      a 2nd line with only 1-3 orphan words
- [ ] Profile Summary paragraphs don't wrap to a 1-2 word final line
- [ ] Deliverable is the `.docx` — no self-generated PDF presented as the
      final output or cited as pagination proof
- [ ] Phase 6 summary report delivered alongside the file, every time —
      see `SKILL.md` §Phase 6, no decision gate, never skipped

---

## Part 2: Voice & Tone

This CV has a specific voice: metric-driven, execution-focused, proof-point dense. Preserve it in all tailoring, regardless of which template (Product or Data Architect).

### The Voice Pattern: Action + Number + Method + Scale

**Examples:**
- "Won $28M in professional services and drove $138M in incremental media spend through AI-enhanced AdTech"
- "Built search and discovery ranking system serving 10+ networks, handling 500M+ daily queries, improving match rates by 34%"
- "Drove 40% annual revenue growth, achieved 85% client retention with 9.3 NPS, won 3 AdTech awards"

**Breaking it down:**
- **Action verb first:** Won, Drove, Built, Launched, Architected, Defined, Cut, Delivered, Directed
- **Specific number immediately:** $28M, 40%, 85%, £1M, 3 awards, 34% improvement
- **Method/approach:** via/through/using X
- **Scale marker:** teams of X, Y clients, Z networks, handling N queries

### What NOT to Say

❌ "Passionate about building great products"
❌ "Leveraged cross-functional collaboration"
❌ "Deep expertise in product strategy"
❌ "Responsible for product vision"
❌ "Helped the team achieve X"
❌ "Excited to partner with Engineering"

### When Tailoring, Preserve This Voice

**For search/discovery/ranking bullets:**
❌ "Architected search and discovery infrastructure for retail media platform"
✓ "Built search and discovery ranking system serving 10+ retail networks, handling 500M+ daily queries, improving merchant match rates by 34%"

**For AI/LLM work:**
❌ "Integrated AI/LLMs into product development"
✓ "Launched AI-powered recommendations engine using LLMs, increasing user engagement by 28% and generating £2M+ new revenue"

**For hands-on IC work:**
❌ "Worked directly with Engineering teams"
✓ "Directed daily product delivery cycles with Engineering, shipping 15+ features per sprint from discovery through launch"

**For GTM/Commercial work:**
❌ "Collaborated with GTM and Sales teams"
✓ "Drove GTM strategy and Sales enablement across 3 SaaS verticals, achieving 92% customer retention and £15M ARR"

**For data/architecture work (Data Architect template):**
❌ "Built data infrastructure"
✓ "Architected first-party data platform handling 500M+ daily events, achieving 99.99% uptime, reducing query latency by 45%"

### The Rule

Every bullet should make you think "what did this person actually *do* and what was the *impact*?" not "what did they manage or oversee?"

**Hierarchy:**
- Specific > Generic
- Numbers > Adjectives
- Outcome > Process
- Action > Description
