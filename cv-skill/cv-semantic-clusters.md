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

### Data Architect / Data Engineer (Role Type)
**Core keywords:** data architecture, data engineering, data infrastructure, data platform, data pipeline, ETL, data modeling, database design, data warehouse
**Semantic cluster:** data architecture, data engineering, infrastructure as code, cloud data platforms, Apache Spark, Airflow, dbt, Python, SQL, big data, distributed systems, data quality, data governance, schema design, data modeling, dimensional modeling, OLAP, data lake, data warehouse, Snowflake, BigQuery, Redshift, Databricks, Apache Kafka, streaming data, batch processing, real-time data

### Retail Media / First-Party Data (Domain)
**Core keywords:** first-party data, identity resolution, retail media, measurement, clean rooms, privacy & consent, data activation, customer data
**Semantic cluster:** first-party data, identity resolution, customer identity platform, privacy-safe data, zero-party data, clean room technology, data activation, customer data, data unification, privacy compliance, GDPR, consent management, data anonymization, retail data network, advertiser outcomes, media measurement, attribution, brand safety, data marketplace, retail analytics, customer insights

### AdTech / Measurement (Domain)
**Core keywords:** AdTech, measurement, attribution, programmatic, ad-serving, RTB, impression tracking, conversion tracking, brand safety, campaign optimization
**Semantic cluster:** AdTech, advertising technology, programmatic advertising, real-time bidding, ad-serving, impression tracking, conversion tracking, attribution modeling, multi-touch attribution, brand safety, campaign optimization, audience targeting, retargeting, cross-device tracking, viewability, measurement framework, marketing mix modeling, incrementality testing

**This file is lookup data only.** For the actual scoring method (how to
use these clusters to compute a coverage percentage), see `cv-scoring.md` —
don't duplicate that logic here; update it there and this file stays purely
about which terms belong to which cluster.

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

### If JD mentions "Data Architect" or "Data Engineering":
Look for: data architecture, data engineering, data infrastructure, pipeline, ETL, modeling, Spark, dbt, Airflow, Python, SQL, big data, Snowflake, BigQuery, Redshift, Databricks, Kafka, streaming, batch processing

### If JD mentions "First-Party Data" or "Privacy & Consent":
Look for: first-party data, identity resolution, customer identity, privacy-safe, clean room, consent management, GDPR, data anonymization, customer data, zero-party data, data activation

### If JD mentions "Retail Media" or "Measurement":
Look for: retail media, measurement, attribution, brand safety, advertiser outcomes, clean rooms, customer data, data activation, measurement framework, media network, retail analytics

See `cv-scoring.md` for how these clusters get turned into a coverage
score — the mechanics (point-counting, weighting, worked example) live
there so there's one method, not two.
