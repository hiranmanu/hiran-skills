# Formatting and positioning rules

These came out of many prior editing sessions with this user. They are
constraints, not preferences — don't relitigate them per JD.

## Hard layout constraints

- **Every bullet fits on a single line. No wrapping.** This is the single
  most-repeated instruction across every past session. See
  `generation-and-qa.md` for the character-budget mechanics that enforce it
  while writing, not just after.
- **Skills section is a single flowing line, never a two-column grid.**
  Grid/table layouts are the single biggest cause of ATS misparses — many
  systems read tables left-to-right across rows rather than column by
  column, which scrambles keywords into nonsense.
- **Section header: "Key Skills & Competencies"**, not "Core Expertise" —
  the safer, more commonly-parsed header across older ATS platforms, even
  though "Core Expertise" reads cleaner.
- One page under ~5 years' relevant experience shown, two pages beyond —
  same convention as this user's existing variants.
- Font: Calibri Regular 10.5pt body (Calibri Light was tried and dropped —
  too thin at export resolution), or Aptos 11pt if the user asks for a
  change. Don't introduce a third option unprompted.

## Content rules

- **No em dashes anywhere in generated CV text** — profile, bullets, role
  context lines, everything. Use a comma, colon, or semicolon instead, or
  split into two sentences. This matches this user's own writing register
  and is a hard rule, not a style nudge — check with a `grep "—"` pass on
  the draft before rendering, the same way bullet length gets checked.
- **No personality-trait bullets.** "Charismatic, empowering leader" and
  similar self-awarded traits get cut on sight, not softened. Every line
  must be provable from the career bullets, never a personality claim.
- **AI/ML claims are anchored to shipped outcomes only.** Don't add "AI/ML"
  as a keyword unless a real shipped result backs it — this user has
  explicitly flagged this as a line not to cross even under keyword
  pressure from a JD.
- Keep the summary to 3-5 lines: years of experience, scope, one signature
  number, aimed at the target seniority (CPO / VP / Director of Product).
- Company-context line per role: one line on what the company is, its
  scale, and what was owned there — this is the differentiator most peer
  CVs skip.

## Keyword and title rules (ATS + recruiter behaviour)

- **LinkedIn Recruiter and most ATS title-matching scan the title field,
  not the description** — so title framing carries more weight than body
  keyword density. Get the title line right first.
- **"Interim" leads over "Fractional"** in any title field.
- **CPTO sits alongside CPO** as a live search term — don't drop one for
  the other.
- **VP Product** and **Data Architect** are both deliberately retained as
  live search terms across variants, even on CVs primarily positioned
  around one of them — don't strip the other out to "focus" the CV.
- **Adjacent-word phrase matching favours contiguous paired terms** — e.g.
  keep "Product Strategy" together rather than splitting it across a
  sentence, since some ATS keyword matchers look for the exact phrase.
- Headline fields (title, LinkedIn headline) are read on a **~70-character
  mobile preview window** — don't bury the load-bearing keyword past that
  point.

## Blended/functional titles

- When a past role's actual title undersold its real scope (e.g. "Principal
  AdTech Consultant" undersold work that was genuinely Head-of-Product
  level), prefix the real title with a truthful functional descriptor:
  "Head of Product, Principal AdTech Consultant". The real title stays
  visible, never gets replaced.
- Never blend in a title whose scope the person didn't actually hold. If
  every past role had them as the principal decision-maker, don't
  manufacture a deputy/support title (e.g. "Chief of Staff") just to chase
  a JD's title field — that's fabrication, not positioning. Check per role:
  was the scope really equivalent, not just adjacent.

## Profile opening: mirror register, not titles

- When the JD's title matches the person's own real function (CPO, VP
  Product, Head of Product), lead the profile with that language directly
  — it's true, say it plainly.
- When it doesn't (Chief of Staff, COO, etc.), keep their real functional
  identity as the sentence's subject, and mirror the JD's own descriptive
  phrasing elsewhere in the sentence instead of borrowing the title. E.g.
  a JD asking for someone to "bridge Product, Engineering, Design, Data and
  senior leadership" earns "...bridging Product, Engineering, Data and
  senior leadership" in the profile — same register, no false title claim.

## The three live variants

Base template selection in Phase 2 should map to one of these unless the
JD clearly calls for something else:

1. **CPO / VP Product** — retail media, AdTech, B2B SaaS positioning.
2. **Data Architect** — first-party data, clean rooms, identity resolution,
   data governance framing.
3. **Solution / Enterprise Architect** — platform build, integration
   architecture, legacy modernisation framing.

If the JD spans two (common for platform/data-heavy product roles), lead
with whichever the title field most directly matches, and pull supporting
keywords from the other rather than blending both openers.
