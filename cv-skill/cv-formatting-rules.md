# CV Formatting Rules

Hard constraints on CV generation. Violating any of these is a bug, not a style choice.

## Content rules

- **No em dashes anywhere in generated CV text** — profile, bullets, role context lines, everything. Use a comma, colon, or semicolon instead, or split into two sentences. This matches the user's own writing register.
- **No personality-trait bullets.** Never add "passionate about X" or "excited by Y." Facts only.
- **Single-line bullets only.** No wraps to a second line. Character budget: ~100-105 chars including spaces. Check lengths before rendering.
- **Blended titles (when appropriate).** When a past role's actual title undersold its real scope, prefix it with the functional title:
  - Format: `{Functional Title}, {Actual Title}`
  - Example: `Head of Product, Principal AdTech Consultant` (Amazon)
  - Example: `Senior Product Director, VP of Product` (OneAdvanced)
  - Rule: Only blend if the functional title genuinely matches the scope. Never manufacture a title that isn't true.
  - For JD-specific tailoring: If the JD calls for "Product Director," and you held "VP of Product," blend it as `Senior Product Director, VP of Product` to show direct relevance without fabrication.
- **Keyword placement in bullets.** When tailoring for a JD:
  - Lead with the keyword if possible: "Architected search and discovery infrastructure..." not "Built infrastructure for search and discovery..."
  - Reorder bullets to surface JD-relevant work first, even if it means moving older achievements up.
  - Never rewrite a bullet to force a keyword that isn't truthfully there.

## ATS parsing rules

- **pdftotext -layout must be readable.** After generating PDF, run pdftotext and spot-check 3-4 bullets. They should parse as continuous text, not gibberish.
- **No em dashes in PDF text output.** Grep the PDF text extract for "—". Must be zero.
- **Exact filename format:** `{YYYY-MM-DD}_{Company}_{Role}.docx` and `.pdf`
  - Example: `2026-09-14_TalentInternational_ProductDirector.docx`
  - Use ISO date format (YYYY-MM-DD) in filenames, folder-date format (YYYY.MM.DD) for GDrive subfolder names.

## Profile/headline rules

- **Mirror JD role title language in the headline.** If the JD calls for "Senior Product Director," start with "Senior Product Director" not "Product executive."
- **Front-load JD-relevant keywords in the first two sentences.** After the title, the next 30-40 words should hit 3-4 of the top keywords from the JD (search, discovery, recommendations, AI/LLMs, CRM, CDP, MarTech, etc.).
- **Reflect hands-on IC positioning if the role requires it.** "Comfortable operating as a hands-on individual contributor" should appear if the JD emphasizes this.
- **Include integration/collaboration language.** "Working directly with Engineering," "GTM collaboration," "Sales partnership" — these are keywords worth surfacing early.

## Skills section rules

- **JD-only keywords, nothing speculative.** If the JD doesn't mention "Power BI" or "Looker," don't list BI tools by name. If the JD doesn't mention specific tech, don't invent a tech stack.
- **Organize by relevance to the JD.** Top line: keywords from the JD's "must-have" section. Secondary lines: adjacent capabilities. Don't include irrelevant domains (e.g., "CPG, FMCG" if the JD is B2B SaaS with no retail mention).
- **Format:** Dot-separated single line, no wraps. ~80-90 char budget per line.

## Validation before output

- [ ] No em dashes (grep "—" on PDF text)
- [ ] No bullet wraps to second line (visual PDF check)
- [ ] pdftotext -layout is readable (spot-check 3-4 bullets)
- [ ] Filename format correct: `{YYYY-MM-DD}_{Company}_{Role}`
- [ ] Blended titles used only when truthfully justified
- [ ] Keywords from JD surfaced in profile, skills, and top bullets
- [ ] No keywords forced into bullets where they don't truthfully belong
