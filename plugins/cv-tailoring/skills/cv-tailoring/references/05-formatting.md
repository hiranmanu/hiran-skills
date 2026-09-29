# 05 - Formatting, Voice & Validation

Owned by **step 05 (Draft)** and **step 07 (Render & Validate)** in `SKILL.md`.
Hard constraints and voice for every tailored CV. This is the single home for
format rules: the old decision-gates and QA-persona files were folded in here
and into `SKILL.md` in v2.0.0, so a rule should exist in one place only.

---

## Part 1: Hard constraints

### Content rules

- **No em dashes or en dashes anywhere** (profile, bullets, role lines, dates). Use a comma, colon or semicolon, or split the sentence. Date ranges use a plain hyphen: `Jan 2026 - present`.
- **No personality-trait filler** ("passionate about", "excited by"). Facts only.
- **"dunnhumby" is always lowercase**, including at the start of a line.
- **No vague filler** ("details on request") for early-career entries: write the actual substance, however brief.
- **Blended titles:** rules and examples live in `03-background.md` Section 4 (single source of truth). Format `{Functional Title}, {Actual Title}`, max 1-2 per CV, never a title never held.
- **Recommendations / References section: removed entirely**, including an "available on request" line.
- **Every claim traces to `03-background.md`.** Combine facts with "and"; never turn two facts into cause-and-effect ("by", "through", "resulting in") unless the bank line says so.

### Bullets

The rule depends on where the role sits:

| Where | Length | Notes |
|---|---|---|
| **Page-1 roles** (the most recent 3-4 roles) | 1-2 lines, up to about 210 characters | A complete, tight one-liner is fine. If it wraps, the second line must be **40-80% full**: no orphan word, and never a third line |
| **Page-2 roles, Earlier Career** | Single line, about 105 characters | Keeps page 2 dense and page 1 free for richer bullets |
| **Qualifications / Certifications lines** | Single line, cap each at 4-5 items | These wrapped most often in practice: don't list every certification |

- Budget characters **while writing**, not after render. Calibri 10.5pt, A4, margins top/bottom 560 twips, left/right 680: a bulleted line holds about 105-108 characters. This shifts if margins, size or font change: re-measure rather than assume.
- When a page-1 bullet doesn't fit, cut a weaker clause. Font size and margins are never levers.
- Bullet marker is a small square (▪).
- Lead with the JD's keyword where it is truthfully there; reorder to surface JD-relevant work first; never rewrite a bullet to force a keyword that isn't there.

### Profile Summary

- **Two short paragraphs, 7 lines maximum in total.** Heading is "Profile Summary".
  - **Paragraph 1:** who you are, mirroring the JD's title language, with the headline proof. The first two sentences carry 3-4 of the JD's top keywords.
  - **Paragraph 2:** governance, board/C-suite, commercial or adjacent-role proof (for example the £90M Aviva programme as evidence of vendor-governance rigour), then the fit statement.
- **Every claim is paired with its proof.** A claim with no evidence in the same paragraph gets cut or backed.
- **Role outside your home domain:** open paragraph 1 with the domain-transfer argument, the one sentence connecting your background to their problem.
- Include hands-on IC positioning and Engineering/GTM collaboration language only if the JD emphasises them.
- **No orphan lines:** no paragraph may wrap so its last line holds only 1-2 words. Read the actual wrap points after every render, not just the first.
- Dual nationality never appears in the profile (see Header layout). A short "markets covered" phrase may close paragraph 2, in normal (non-italic, non-grey) formatting.

### Key Skills & Competencies

- **Exactly 3 rows**, each with a **bold, JD-mirrored label** followed by keywords separated by a middle dot (`·`). Example labels: "Product & Portfolio Leadership", "Data, Architecture & Vendors", "Leadership & Change".
- Each row wraps to about **1.4-1.8 lines**: never a third line, never a second line of 1-3 orphan words (add another true, relevant keyword instead of leaving a spill). Check by rendering.
- **What may appear:** a keyword goes in only if (a) the JD uses it or it is a close synonym, and (b) `03-background.md` supports it. A JD keyword with no evidence is **not added**: it is reported as a gap in step 08.
- **Repetition is intended, and skills need proof.** Each must-have JD keyword appears in the profile or skills **and** in at least one bullet as evidence; the top 3-5 appear in all three. **A keyword in the skills rows must also be evidenced in a bullet:** if the master file has no bullet evidence for it, it doesn't go in skills. ATS and human readers both look for the repeat. The only ban is a verbatim duplicate **inside one list** (for example "OKRs" twice in the skills rows).
- No speculative tech: don't name a tool the JD doesn't mention unless it is a truthful differentiator. Don't include irrelevant domains.
- **Signature breadth** (optional, max 1-2 items, always last): a real skill the JD doesn't cover that is genuinely differentiating. It never precedes a JD keyword, never counts toward the ATS score, and must already be in `03-background.md`. Cut it before cutting a JD keyword.

### Page rules

- **Hard cap: 2 pages.**
- **Most recent 3-4 roles on page 1.** Each role (title + company line + all bullets) stays together on one page: `keepNext`/`keepLines` on every paragraph of the block except the last.
- **If page 1 doesn't fit four roles, trim by relevance-weighted cutting**, lowest score first, wherever the line sits. Score each candidate line on (a) relevance to this JD's keywords and duties, (b) uniqueness (the only place the claim appears), (c) load (something else depends on it). Typical order: a low-relevance bullet in the oldest page-1 role; the profile's last clause; a low-relevance skills keyword; then bullets of the middle roles. Never reduce font, margins or line spacing, and never shorten dates.
- Rough page-1 budget that fits: profile 6-7 lines, skills 6 lines, then 4 bullets for the most recent role, 3 for the next, 3 for the third, 2-3 for the fourth.

### Font & layout (house style confirmed 2026-09-17)

- **Font:** plain Calibri (not Calibri Light), 10.5pt, uniform in every section. Never let sizes drift between sections.
- **Page:** A4. Margins top/bottom 560 twips, left/right 680.
- **Colours:** navy headings `#1F3864`, near-black body `#222222`, mid-grey secondary `#555555`. Section headings get a thin navy bottom rule.
- **Line spacing:** 1.15 (`line: 276, lineRule: auto`) on paragraphs that may wrap (profile, skills rows, bullets). Single-line elements (role title/date line, company line) stay at default: the multiplier inflates their height and visibly widens the gap under a role title.
- **Bullet spacing:** `spacing.after: 0` between bullets in a role; use `after` only for section and role breaks.
- **Sections, in order:** Profile Summary, Key Skills & Competencies, Career & Key Achievements to Date, Qualifications/Certifications/Personal Details.

### Header layout

- Name: left-aligned, bold, large, navy. Contact line: `London, UK | Phone | Email | LinkedIn`, pipe dividers, no parenthetical asides. Email and LinkedIn are live hyperlinks (`mailto:` for email), and the **email is also printed as literal text** so an ATS can read it.
- Company/descriptor line uses a colon: `London, UK: Global media technology consultancy`, not a dash.
- **Role dates:** right-aligned via a tab stop, not bold, same size, flush on the true page margin. Compute the tab position from this template's real page width minus margins. Do **not** use docx-js `TabStopPosition.MAX` (9026 twips, undershoots here) or `PositionalTab` (breaks in LibreOffice). Copy `roleHeader()` from `scripts/build_cv_reference.js`.
- **Dual nationality:** once only, at the bottom under Personal Details, right-aligned to the same tab stop as role dates (`Languages: ... [tab] Joint Nationality: British & American`).
- **LinkedIn URL:** Product roles only, `https://www.linkedin.com/in/hiran-patel/` exactly. `01-config.md` is authoritative if they ever differ.
- **Document metadata:** `creator` and `lastModifiedBy` = `"Hiran Patel"`, real `title` (`"Hiran Patel - CV"`).

### Output format

- **DOCX is the only deliverable.** No PDF is ever shipped. The page-fit check may export a temporary PDF from **real Word** to read pagination, then discards it. Never trust a LibreOffice/Carlito render: it substitutes for Calibri and paginates differently, which is how the 3-page/role-split bug happened.
- **Filename:** `Hiran_CV_{YYYY.MM.DD}_{Company}_{BriefRole}.docx`, dots not dashes in the date, the actual current date checked fresh, company always included, role as a 1-3 word slug (`PMGenAI`, not `ProductManagerGenAI`). Folder date format is the same `YYYY.MM.DD`.

### ATS parsing rules

- No em/en dashes (checked by script).
- **Dates:** every role has a start **and** an end (or "present") joined by an ASCII hyphen. A bare year or an en dash can drop the date on import (a Workday import lost dates this way).
- **Contact:** email and phone present as literal text.
- **Readable extraction:** spot-check 3-4 bullets read as continuous text when the DOCX text is extracted.

---

## Part 2: Voice

Metric-driven, evidence-first, execution-focused. Every bullet should answer "what did this person actually do, and what was the impact?", not "what did they oversee?".

**Pattern: Action + what/scope + how + outcome.** Put a number in when a real one exists; never invent one.

(Until v2.0.0 the pattern was "Action + Number + Method + Scale", number first. That forced truncation to about 105 characters and stripped the *how*. The number now follows the substance instead of leading it.)

**Compose, don't compress.** Combine 2-3 related bank lines into one sentence with "and":
- Weak: "Built a 20+ person org, securing £10M+ funding"
- Better: "Defined the £200M+ multi-year product strategy for a retail media aggregator and built the multi-partner operating model for a 20+ person product, engineering and data science org"

**Rewriting is fine; changing facts is not.** Stronger verbs, dropped repetition and reordered clauses are craft. Adding a cause, a scope, a client or a metric that the bank doesn't hold is fabrication.

**Hierarchy:** specific > generic; numbers > adjectives; outcome > process; action > description.

**What not to say:** "passionate about", "leveraged cross-functional collaboration", "deep expertise in", "responsible for", "helped the team achieve", "excited to partner with".

---

## Part 3: Validation checklist (step 07)

Automated (`python3 scripts/validate_cv.py <docx> --keywords-file <must-haves.txt>`):
- [ ] No em/en dashes
- [ ] No References/Recommendations heading or placeholder
- [ ] Author metadata is "Hiran Patel"
- [ ] Every role date is an ASCII-hyphen range with start and end
- [ ] Email present as literal text
- [ ] No verbatim duplicate keyword within the skills rows
- [ ] Every must-have appears, and each one in the profile or skills is also evidenced in a bullet (fails if not; warns if it is only in bullets)
- [ ] Bullets near the length ceiling flagged (warn)

Word check (`scripts/word_layout_check.ps1 <docx>`, Windows + Word):
- [ ] 2 pages
- [ ] Most recent 3-4 roles fully on page 1; no role split across a page break
- [ ] No section heading stranded at the bottom of a page

Manual (open the rendered DOCX):
- [ ] No bullet wraps to a third line, or leaves a one-word second line
- [ ] Skills rows each ~1.4-1.8 lines, no orphan spill
- [ ] Profile paragraphs have no 1-2 word last line
- [ ] Filename and output folder correct
- [ ] Square bullets; company lines use a colon; LinkedIn only on Product roles

On any failure, `SKILL.md` "Loops" says which step to return to.
