# Semantic Clustering for ATS Scoring

Real ATS systems don't just match exact keywords — they match semantic clusters. When a JD mentions "MarTech," they're looking for the ecosystem around it: marketing automation, lead scoring, CDP, CRM, customer data platforms, email, campaigns, etc.

This file maps role types and key terms to their semantic clusters so we can score comprehensively, not just on exact matches.

## Role Type Clusters

### Product Director / VP Product / Senior PM (Product Leadership)
**Core keywords:** product strategy, vision, roadmap, product ownership, end-to-end ownership, leadership
**Semantic cluster:** product management, product strategy, roadmap planning, vision setting, cross-functional alignment, product development, product leadership, product thinking, OKRs, strategic planning

### Discovery / Search / Recommendations focus
**Core keywords:** search, discovery, recommendations, ranking, matching, personalization, information retrieval, user needs discovery
**Semantic cluster:** search functionality, discovery platform, recommendation engine, ranking algorithm, personalization engine, content discovery, user intent, information architecture, browse/search hybrid, relevance, ranking systems, matching algorithms, recommendation systems, personalized content, user experience discovery

### CRM / CDP / MarTech integration focus
**Core keywords:** CRM, CDP, MarTech, marketing automation, customer data, lead scoring
**Semantic cluster:** 
- **CRM:** Salesforce, HubSpot, Dynamics, CRM systems, customer relationship management, sales automation, contact management, pipeline management, customer data
- **CDP:** customer data platform, data unification, customer profiles, data activation, identity resolution, first-party data, customer identity
- **MarTech:** marketing automation, Marketo, Pardot, ActiveCampaign, email marketing, campaign management, lead nurturing, lead scoring, marketing workflows, customer journey
- **Related:** customer data, data integration, APIs, integrations, data flows, customer insights, customer segmentation

### B2B SaaS / Customer-facing / Data-rich platforms
**Core keywords:** B2B SaaS, customer-facing, data-rich, platform, GTM, commercial
**Semantic cluster:** business software, SaaS products, recurring revenue, customer success, account management, enterprise software, platform design, scalability, data platform, analytics, metrics, customer acquisition, sales collaboration, GTM strategy, revenue growth, product-market fit

### Hands-on IC / Delivery / Engineering partnership
**Core keywords:** hands-on, individual contributor, IC, PRDs, UX workflows, delivery, Engineering partnership, from discovery through delivery
**Semantic cluster:** hands-on product work, individual contributor, non-management, execution, project delivery, specification writing, wireframing, prototyping, UX design collaboration, engineering collaboration, technical product requirements, agile development, sprint planning, product delivery, launch execution, quality assurance

### AI / LLM / Prototyping
**Core keywords:** AI, LLM, prototyping, Claude Code, Cursor, Lovable, experimentation
**Semantic cluster:** artificial intelligence, machine learning, large language models, generative AI, AI-powered features, AI tools, AI experimentation, rapid prototyping, no-code tools, low-code tools, developer tools, AI-assisted development, prompt engineering, AI product features, AI integration

## Term-to-Cluster Mapping (for scoring)

When scoring a CV against a JD, if the JD mentions a key term, search the CV for:

### If JD mentions "MarTech":
Look for: marketing automation, Salesforce, HubSpot, Marketo, Pardot, ActiveCampaign, lead scoring, email marketing, campaign management, CDP, customer data, marketing workflows, lead nurturing

### If JD mentions "CDP":
Look for: customer data platform, data integration, customer profiles, identity resolution, first-party data, data activation, customer segmentation, Segment, mParticle, Tealium, Lytics

### If JD mentions "Search/Discovery/Recommendations":
Look for: search functionality, ranking, personalization, recommendation engine, user intent, information retrieval, algorithm, relevance, user experience, matching

### If JD mentions "Hands-on IC" or "Individual Contributor":
Look for: execution, delivery, from discovery through PRDs, specification writing, prototyping, direct Engineering partnership, sprint execution, launch, quality assurance

### If JD mentions "B2B SaaS":
Look for: SaaS, recurring revenue, customer success, enterprise software, platform, GTM, sales collaboration, product-market fit, scaling, customer acquisition

### If JD mentions "AI/LLM":
Look for: artificial intelligence, machine learning, generative AI, large language model, AI-powered, AI features, experimentation, prototyping, AI tools, prompt engineering

## Scoring rule for semantic clusters

1. Extract core keywords from JD
2. For each core keyword, pull its semantic cluster (use this file)
3. Count CV text matches against **core keyword + full cluster**
4. Example:
   - Core keyword: "MarTech" (1 point)
   - Cluster matches: "marketing automation" + "Salesforce" + "lead scoring" (3 points)
   - Total: 4 points found for the "MarTech" cluster
5. Aggregate across all clusters
6. Score = (total cluster points found) / (total possible cluster points)

This catches "Salesforce integrations for marketing automation" in the CV even though it doesn't use the exact word "MarTech."
