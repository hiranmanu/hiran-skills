# ATS Scoring Methodology

This is a **transparent, repeatable heuristic**, not a vendor algorithm. Workday, Greenhouse, Taleo, etc. don't publish their methods, so this is a directional coverage signal.

## Method: Keyword Presence Scoring

**Step 1: Extract keywords from the JD**
Pull all nouns, noun phrases, and verb phrases that describe required skills, tools, domains, and capabilities. Be comprehensive — include both "must-have" and "nice-to-have" sections.

**Step 2: Search the CV for exact matches or clear synonyms**
- Exact match: "search" in JD, "search" in CV
- Clear synonym: "ranking" ~ "rank", "personalization" ~ "personalisation", "end-to-end" ~ "from 0-to-1"
- NOT a match: loose thematic connection ("discovery" in JD, "platform strategy" in CV with no mention of discovery)

**Step 3: Count and score**
- Keywords found in CV ÷ total keywords in JD = coverage percentage
- No weighting (2x/1.5x/1x weights were invented heuristics, not grounded in actual ATS behavior)
- Simple presence/absence, same weight for all

**Step 4: Report**
> ATS coverage: {before}% → {after}%
> Found: {count} of {total} keywords
> Still missing: {keyword 1}, {keyword 2}

## Example

JD keywords: [product strategy, search, recommendations, ranking, B2B SaaS, CRM, CDP, MarTech, hands-on IC, AI/LLMs, PRDs, UX workflows, Engineering partnership, GTM, Sales]

CV text: "product strategy" ✓, "search" ✓, "recommendations" ✓, "ranking" ✓, "B2B SaaS" ✓, "CRM" ✓, "CDP" ✓, "MarTech" ✓, "hands-on" ✓, "AI" ✓, "PRDs" ✓, "UX" ✓, "Engineering" ✓, "GTM" ✓, "Sales" ✓

Result: 15/15 = 100%

## Important rules

1. **Only count what's actually in the JD.** If the JD doesn't mention "Salesforce" or "Power BI" by name, don't score against those tools. Don't invent a tech stack for a company you haven't researched.

2. **Reordering is free, invention is not.** You can move a bullet with "search + ranking" to the top to increase keyword visibility. You cannot add "built Elasticsearch clusters" if that wasn't in your background.

3. **Synonyms are fair game.** "Product ownership" ~ "owned the product strategy", "direct Engineering partnership" ~ "worked closely with Engineering teams". Use judgment — if you'd accept it as a synonym in a conversation, it counts.

4. **The score is before/after, one CV at a time.** Before: your base CV as-is. After: the same CV with bullets reordered and the profile/skills section tailored to this specific JD.

5. **Honesty over optimization.** A CV that scores 72% and survives an interview is better than one that scores 92% and gets rejected for overstating your fit. If a gap is real, say so.
