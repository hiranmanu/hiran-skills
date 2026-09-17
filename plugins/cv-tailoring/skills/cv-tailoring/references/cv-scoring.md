# ATS Scoring Methodology

This is a **transparent, repeatable heuristic**, not a vendor algorithm. Workday, Greenhouse, Taleo, etc. don't publish their methods, so this is a directional coverage signal — this is the only place that caveat needs stating; don't repeat it elsewhere.

**This is the single source of truth for the scoring method.** `cv-semantic-clusters.md` holds the cluster lookup data this method reads from — role-type clusters and term-to-cluster mappings — but the scoring logic itself lives only here.

## Method: Keyword Presence + Semantic Clustering Scoring

Real ATS systems don't just match exact keywords — they match semantic clusters. When a JD mentions "MarTech," they're also scoring for "marketing automation," "lead scoring," "CDP," "CRM," etc.

**Step 1: Extract keywords from the JD**
Pull all nouns, noun phrases, and verb phrases that describe required skills, tools, domains, and capabilities. Be comprehensive — include both "must-have" and "nice-to-have" sections.

**Step 2: Map keywords to semantic clusters**
For each core keyword, check `cv-semantic-clusters.md` and pull its related semantic cluster (3-5 related terms).

Example: JD mentions "MarTech" → cluster = marketing automation, lead scoring, CDP, CRM, customer data, Salesforce, HubSpot, etc.

**Step 3: Search the CV for exact matches or clear synonyms (across core keyword + cluster)**
- Exact match: "search" in JD, "search" in CV
- Cluster match: "MarTech" in JD, "Salesforce integrations for marketing automation" in CV (hits 2 cluster terms)
- Clear synonym: "ranking" ~ "rank", "personalization" ~ "personalisation"
- NOT a match: loose thematic connection

**Step 4: Count and score**
- (Keywords found in CV, including cluster hits) ÷ (total keywords + cluster terms) = coverage percentage
- No weighting — simple presence/absence across core + cluster
- Example:
  - Core: MarTech (1 keyword)
  - Cluster: marketing automation, Salesforce, lead scoring, CDP, CRM (5 terms)
  - CV has: Salesforce ✓, marketing automation ✓, CDP ✓
  - Found: 3 cluster hits + 0 core (core not in CV)
  - Score contribution for "MarTech" cluster: 3/6 = 50% for this cluster

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
