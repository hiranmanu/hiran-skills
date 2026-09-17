# CV Formatting & Voice Guide

Hard constraints and voice patterns for all CV tailoring. This covers both formatting rules and the specific voice/tone that defines Hiran's CVs.

## Part 1: Hard Constraints

### Content Rules

- **No em dashes anywhere in generated CV text** — profile, bullets, role context lines, everything. Use a comma, colon, or semicolon instead, or split into two sentences. This matches the user's own writing register.
  - Example: "Won $28M — the largest AdTech deal ever closed" → "Won $28M, the largest AdTech deal ever closed"
- **No personality-trait bullets.** Never add "passionate about X" or "excited by Y." Facts only.
- **Single-line bullets only.** No wraps to a second line. Budget the
  character count *while writing*, not after export — catching a wrap after
  render is too late to feel reliable. At Calibri 10.5pt on a US Letter page
  with ~1" margins and a ~6.5" text width, a bulleted line (glyph + indent)
  holds roughly 90-100 characters including spaces and punctuation; Aptos
  11pt is slightly wider, so budget closer to 85-95 there. Treat 90 as the
  safe target regardless of which font is confirmed. When a bullet
  genuinely doesn't fit, cut a weaker clause rather than shrinking font
  size or margins — those aren't available levers. This is a proactive
  budget, not a guarantee: still run the QA sequence in
  `cv-decision-gates.md` §5.3, since actual rendering also depends on
  kerning and any bold runs (company names, metrics), which render wider
  than plain text.
- **Sub-bullets use rounded hole bullets (○), not em-dashes.** Replace em-dashes with ○ for secondary points (e.g., 2010-2015 Dunnhumby section).
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

- **Font:** Calibri Light 10.5pt (or Aptos Light as alternative). Not Calibri Regular.
- **Line spacing:** Tight (good for ATS parsing)
- **Header layout:**
  - Name: left-aligned
  - Date: right-aligned
  - Citizenship/Nationality: right-aligned (aligned with date)
  - LinkedIn URL: **Product roles only** (Product CV includes it, Data Architect CV does not)
- **LinkedIn URL format:** `linkedin.com/in/{handle}` (plain text, not clickable link)
- **Recommendations section:** Remove entirely for all roles
- **Sections order:** Profile, Key Skills & Competencies, Career & Key Achievements

### ATS Parsing Rules

- **pdftotext -layout must be readable.** After generating PDF, run pdftotext and spot-check 3-4 bullets. They should parse as continuous text, not gibberish.
- **No em dashes in PDF text output.** Grep the PDF text extract for "—". Must be zero.
- **Exact filename format:** `{YYYY-MM-DD}_{Company}_{Role}.docx` and `.pdf`
  - Example: `2026-09-14_TalentInternational_ProductDirector.docx`
  - Use ISO date format (YYYY-MM-DD) in filenames, folder-date format (YYYY.MM.DD) for GDrive subfolder names.

### Profile/Headline Rules

- **Mirror JD role title language in the headline.** If the JD calls for "Senior Product Director," start with "Senior Product Director" not "Product executive."
- **Front-load JD-relevant keywords in the first two sentences.** After the title, the next 30-40 words should hit 3-4 of the top keywords from the JD (search, discovery, recommendations, AI/LLMs, CRM, CDP, MarTech, etc.).
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
- **Format:** Dot-separated single line, no wraps. ~80-90 char budget per line.

### Validation Before Output

Run `python3 scripts/validate_cv.py <path> --max-pages 2` (see `cv-decision-gates.md`
§5.3) — it automates the four checks below marked ⚙ in one pass. The rest still need
a human look at the rendered page images.

- [ ] ⚙ No em dashes or en dashes (was: grep "—" on PDF text — script now also catches "–")
- [ ] ⚙ No bullet wraps to second line (was: visual PDF check only)
- [ ] ⚙ No role split across a page boundary
- [ ] ⚙ Page count within cap (default 2)
- [ ] pdftotext -layout is readable (spot-check 3-4 bullets) — not automated; garbled/reordered text needs a human read
- [ ] Filename format correct: `{YYYY-MM-DD}_{Company}_{Role}`
- [ ] Blended titles used only when truthfully justified
- [ ] Keywords from JD surfaced in profile, skills, and top bullets
- [ ] No keywords forced into bullets where they don't truthfully belong
- [ ] Rounded hole bullets (○) used for sub-bullets, not em-dashes
- [ ] LinkedIn URL present only for Product roles
- [ ] Recommendations section removed
- [ ] DOCX/PDF core properties (Author) set to the user's own name, not left as a generic tool default

> **Open question — not yet reconciled:** a separate Claude chat session (not this
> Claude Code skill) built a one-off "SVP Product / AI" branded CV using different
> conventions than this file specifies: US Letter → A4, Calibri Light → plain Calibri,
> black-and-white → navy/grey colour scheme, plain-text LinkedIn → hyperlinked
> email+LinkedIn, "Profile" → "Profile Summary" heading, ~90 char bullet budget →
> ~105-108 (different page/margins/font), round bullets → small square (▪) for
> primary bullets. That session's rules are written up in that session's own
> `CV_STYLE_GUIDE.md` (see `hiran-skills` — that repo has since been deleted per
> instruction; the content is now only in that chat's project memory). Nobody has
> confirmed whether that's meant to become the new house style here, a distinct
> "branded" variant kept alongside this one, or a one-off that shouldn't propagate.
> Until Hiran confirms, treat *this* file (Calibri Light, US Letter, black-and-white,
> ~90 char budget) as the authoritative convention for anything generated by this
> skill — don't silently adopt the other session's choices.

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
