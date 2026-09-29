# 04 - ATS Scoring (Method + Cluster Data)

Owned by **step 04 (Score)** in `SKILL.md`. One file, one method: Part 1 is how
to score, Part 2 is the cluster lookup data the method reads from. (These were
two files, `cv-scoring.md` and `cv-semantic-clusters.md`, until v2.0.0; they
were merged so the method and its data can't drift apart.)

This is a **transparent, repeatable heuristic**, not a vendor algorithm. Workday,
Greenhouse, Taleo, etc. don't publish their methods, so this is a directional
coverage signal. This is the only place that caveat needs stating.

---

## Part 1: Method - Keyword Presence + Semantic Clustering

Real ATS systems don't just match exact keywords, they match semantic clusters.
When a JD mentions "MarTech," they also score for "marketing automation," "lead
scoring," "CDP," "CRM," etc.

**1. Extract keywords from the JD.** Pull the nouns, noun phrases and verb phrases
that describe required skills, tools, domains and capabilities. Include both
must-have and nice-to-have. Step 02 already sorted them into buckets, so reuse
that list rather than re-deriving it.

**2. Map keywords to clusters.** For each core keyword, pull its related cluster
(3-5 terms) from Part 2.

**3. Search the CV for exact matches or clear synonyms** (core keyword plus
cluster terms).
- Exact: "search" in JD, "search" in CV.
- Cluster: "MarTech" in JD, "Salesforce integrations for marketing automation" in CV (hits 2 cluster terms).
- Clear synonym: "ranking" ~ "rank", "personalization" ~ "personalisation".
- NOT a match: a loose thematic connection.

**4. Count and score.** (Keywords found in CV, including cluster hits) / (total
keywords + cluster terms) = coverage %. No weighting, simple presence/absence.
Example: core "MarTech" + 5 cluster terms; CV has Salesforce, marketing
automation and CDP, so 3/6 = 50% for that cluster.

**Worked example.** JD keywords: [product strategy, search, recommendations,
ranking, B2B SaaS, CRM, CDP, MarTech, hands-on IC, AI/LLMs, PRDs, UX workflows,
Engineering partnership, GTM, Sales]. CV contains all 15, so 15/15 = 100%.

### Before / after

- **Before (step 04):** coverage of an untailored CV built from the bank's default lines for this template: the `(P)`-tagged lines for PRODUCT_CV, the `(DA)`-tagged lines for DATA_ARCHITECT_CV, no JD-driven profile or skills.
- **After (step 06, once the review edits are applied):** the final tailored
  text. Report both; target 85%+.

### Rules

1. **Only count what's in the JD.** If the JD doesn't name "Salesforce" or
   "Power BI", don't score against them, and don't invent a tech stack.
2. **Reordering is free, invention is not.** Moving a bullet with "search +
   ranking" up raises visibility. Adding "built Elasticsearch clusters" that
   isn't in `03-background.md` is fabrication.
3. **Synonyms are fair game.** "Product ownership" ~ "owned the product
   strategy". If you'd accept it as a synonym in conversation, it counts.
4. **Honesty over optimisation.** A CV that scores 72% and survives interview
   beats one that scores 92% and overstates the fit. A real gap stays a gap.

### Keyword status table (goes in the step 08 report)

For each must-have, one of:

| Status | Meaning |
|---|---|
| covered | the JD's own term appears (verbatim or trivial inflection) |
| synonym-only | the concept is present under a different term; switch to the JD's term if it is truthfully applicable, since ATS matching is often literal |
| missing (have it) | `03-background.md` shows you genuinely have it but the CV never says it: add it, preferring a bullet (evidence) over the profile (claim) |
| missing (gap) | you don't have it: leave it out, list it as a gap, never stuff it |

---

## Part 2: Cluster Data (lookup only)

Scoring logic lives in Part 1. This part only says which terms belong to which
cluster.

### Role-type clusters

**Product Director / VP Product / Senior PM (Product Leadership)**
- Core: product strategy, vision, roadmap, product ownership, end-to-end ownership, leadership
- Cluster: product management, roadmap planning, vision setting, cross-functional alignment, product development, product leadership, product thinking, OKRs, strategic planning

**Discovery / Search / Recommendations**
- Core: search, discovery, recommendations, ranking, matching, personalization, information retrieval, user needs discovery
- Cluster: search functionality, discovery platform, recommendation engine, ranking algorithm, personalization engine, content discovery, user intent, information architecture, browse/search hybrid, relevance, matching algorithms, recommendation systems, personalized content

**CRM / CDP / MarTech**
- Core: CRM, CDP, MarTech, marketing automation, customer data, lead scoring
- CRM: Salesforce, HubSpot, Dynamics, CRM systems, customer relationship management, sales automation, contact management, pipeline management, customer data
- CDP: customer data platform, data unification, customer profiles, data activation, identity resolution, first-party data, customer identity
- MarTech: marketing automation, Marketo, Pardot, ActiveCampaign, email marketing, campaign management, lead nurturing, lead scoring, marketing workflows, customer journey
- Related: data integration, APIs, integrations, data flows, customer insights, customer segmentation

**B2B SaaS / Customer-facing / Data-rich platforms**
- Core: B2B SaaS, customer-facing, data-rich, platform, GTM, commercial
- Cluster: business software, SaaS products, recurring revenue, customer success, account management, enterprise software, platform design, scalability, data platform, analytics, metrics, customer acquisition, sales collaboration, GTM strategy, revenue growth, product-market fit

**Hands-on IC / Delivery / Engineering partnership**
- Core: hands-on, individual contributor, IC, PRDs, UX workflows, delivery, Engineering partnership, from discovery through delivery
- Cluster: hands-on product work, execution, project delivery, specification writing, wireframing, prototyping, UX design collaboration, engineering collaboration, technical product requirements, agile development, sprint planning, product delivery, launch execution

**AI / LLM / Prototyping**
- Core: AI, LLM, prototyping, Claude Code, Cursor, Lovable, experimentation
- Cluster: artificial intelligence, machine learning, large language models, generative AI, AI-powered features, AI tools, AI experimentation, rapid prototyping, no-code/low-code tools, AI-assisted development, prompt engineering, AI integration

**Data Architect / Data Engineer**
- Core: data architecture, data engineering, data infrastructure, data platform, data pipeline, ETL, data modeling, database design, data warehouse
- Cluster: infrastructure as code, cloud data platforms, Apache Spark, Airflow, dbt, Python, SQL, big data, distributed systems, data quality, data governance, schema design, dimensional modeling, OLAP, data lake, Snowflake, BigQuery, Redshift, Databricks, Kafka, streaming data, batch processing, real-time data

**Retail Media / First-Party Data (domain)**
- Core: first-party data, identity resolution, retail media, measurement, clean rooms, privacy & consent, data activation, customer data
- Cluster: customer identity platform, privacy-safe data, zero-party data, clean room technology, data unification, privacy compliance, GDPR, consent management, data anonymization, retail data network, advertiser outcomes, media measurement, attribution, brand safety, data marketplace, retail analytics, customer insights

**AdTech / Measurement (domain)**
- Core: AdTech, measurement, attribution, programmatic, ad-serving, RTB, impression tracking, conversion tracking, brand safety, campaign optimization
- Cluster: advertising technology, programmatic advertising, real-time bidding, attribution modeling, multi-touch attribution, campaign optimization, audience targeting, retargeting, cross-device tracking, viewability, measurement framework, marketing mix modeling, incrementality testing

**Enterprise / Internal Technology Product (added v2.0.0)**
- Core: product management function, business capability model, value stream, enterprise architecture, demand management, prioritisation, operating model, portfolio
- Cluster: capability roadmap, capability vision, product lifecycle management, technology roadmap, technology investment, business case, funding approval, change management, adoption, agile/lean/DevOps, KPIs, quality assurance, CIO/CTO stakeholder management, deputising

### Term-to-cluster lookup

If the JD mentions... look in the CV for:

- **MarTech:** marketing automation, Salesforce, HubSpot, Marketo, Pardot, ActiveCampaign, lead scoring, email marketing, campaign management, CDP, customer data, marketing workflows, lead nurturing
- **CDP:** customer data platform, data integration, customer profiles, identity resolution, first-party data, data activation, customer segmentation, Segment, mParticle, Tealium, Lytics
- **Search / Discovery / Recommendations:** search functionality, ranking, personalization, recommendation engine, user intent, information retrieval, algorithm, relevance, matching
- **Hands-on IC:** execution, delivery, from discovery through PRDs, specification writing, prototyping, direct Engineering partnership, sprint execution, launch, quality assurance
- **B2B SaaS:** SaaS, recurring revenue, customer success, enterprise software, platform, GTM, sales collaboration, product-market fit, scaling, customer acquisition
- **AI / LLM:** artificial intelligence, machine learning, generative AI, large language model, AI-powered, AI features, experimentation, prototyping, AI tools, prompt engineering
- **Data Architect / Data Engineering:** data architecture, data engineering, data infrastructure, pipeline, ETL, modeling, Spark, dbt, Airflow, Python, SQL, big data, Snowflake, BigQuery, Redshift, Databricks, Kafka, streaming, batch processing
- **First-Party Data / Privacy & Consent:** first-party data, identity resolution, customer identity, privacy-safe, clean room, consent management, GDPR, data anonymization, customer data, zero-party data, data activation
- **Retail Media / Measurement:** retail media, measurement, attribution, brand safety, advertiser outcomes, clean rooms, customer data, data activation, measurement framework, media network, retail analytics
- **Business capability model / Value stream:** capability model, value-stream alignment, capability vision and roadmap, enterprise architecture, process/technology/data components, portfolio
- **Demand management:** demand intake, prioritisation, business case, funding approval, investment priorities, revenue-aligned outcomes
