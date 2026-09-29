# 02 - Background: Master Fact File

**The single source of truth for every claim on a tailored CV.** Owned by **step 02
(Gap Check & Confirm)** in `SKILL.md`; read at step 01 (Intake) and step 03 (Draft).

- **Section 1, Master Bullet Bank:** atomic facts per role. Bullets are drawn from here.
- **Section 2, Cross-Role Facts & Guardrails:** capabilities spanning several roles, with the JD words that trigger them and any framing limit. Check it before flagging a gap.
- **Section 3, Notable Absences:** genuine gaps. Keep them as gaps if the JD stresses them.
- **Sections 4-6:** template selection, title blending, JD term synonyms.

If a claim isn't in this file it isn't a fact yet: ask the user at step 02, then record the answer (below) before drafting. A fact that only lives in chat is treated as unsupported next session.

**Tags:** `(P)` product source CV, `(DA)` data-architect source CV, `(C date)` confirmed with the user on that date. Compose bullets by joining lines with "and". Never turn two facts into a cause-and-effect claim ("by", "through", "resulting in") unless a line says so.

## Adding facts safely (several runs at once)

**During a run this file is read-only.** Runs may be going in parallel, so nothing edits it directly. Instead:
1. **Read** the master file **and** the pending facts from other runs: `python scripts/background_inbox.py pending`.
2. **Record** a newly confirmed fact with `python scripts/background_inbox.py add --role "dunnhumby/Tesco" --text "..."` (role facts; `list-roles` shows valid names) or `add-cross --title "..." --text "..."` (cross-role facts). Each call writes its own uniquely named inbox file, so two runs never touch the same file.
3. **Merge** at the end of the run (or the batch): `python scripts/background_inbox.py merge`. It takes a lock, folds pending facts into the right place here, skips duplicates, and archives the inbox files. Safe to call from several runs at once.

---

## Section 1: Master Bullet Bank

Titles below are the titles actually held. The Data Architect template (Section 2) uses the alternate title shown as `DA title`.

### dunnhumby/Tesco - Interim Director of Product, Data & Technology (contract), Jan 2026 - Sep 2026
London, UK: Retail Media SaaS Data Science AI/Agentic
- Defined the £200M+ multi-year product strategy and vision for a retail media aggregator solving advertiser outcomes (P)
- Secured £10M+ investment (P)
- Built the multi-partner operating model of a 20+ person product, engineering and data science org (P)
- Drove discovery with CPG advertisers, agency holdcos and retail partners to validate the GTM proposition and shape live pilots (P). Related workstream to the £10M raise: may be joined to it with "and" or kept separate (C 2026-09-29)
- Owned the strategic roadmap (P)
- Led 4x vendor selections spanning data clean rooms, ad-serving, external engineering (P)
- Architected the UK's largest first-party data strategy and measurement framework across 10+ media networks and channels (P)
- Owned the dunnhumby Network Alliance (multi-retailer network product), including onboarding Kingfisher Group as a retailer partner; frame as retailer onboarding plus product/platform ownership, not a standalone commercial-negotiation claim (C 2026-09-24)
- Ran the PM operating cadence (quarterly/roadmap reviews) and structured PM growth paths; don't overstate team size or a formal promotion-committee structure (C 2026-09-19)
- Ran demand intake and prioritisation of engineering work, aligned to revenue and business-capability outcomes (C 2026-09-29)
- Wrote business cases and secured funded approval for AI, data clean rooms and identity graphs, among other investments (C 2026-09-29)
- Owned the business capability model and value-stream alignment (C 2026-09-28)
- Managed CIO/CTO-level stakeholder relationships and deputised for them (C 2026-09-28)
- Board-level product strategy presentations and investor roadshows (C)
- Owned the AI tooling and agentic product roadmap at strategy level, incl. build-vs-buy evaluation for AI infrastructure; never hands-on engineering (don't imply building RAG pipelines or agent frameworks) (C)
- Drove adoption of internal AI tooling across the product, engineering and data science org (C)
- Direct exposure to venture, strategic investors and corporate venture capital during the £10M+ raise (C)
- Partnered with Design on retail media UX and synthesised product-market research with design insights (C)

### OneAdvanced - VP of Product (contract), Jul 2024 - Jan 2025
London & Birmingham, UK: SaaS Leader PE-backed
- Spearheaded the £100M ARR B2B SaaS portfolio in workforce management & financial solutions, integrating AI capabilities (P)
- Drove a 25% uplift in customer satisfaction and retention through new product OKRs and a performance framework (P)
- Led the market-driven product roadmap, GTM sales strategy and M&A target evaluation across 3 vertical SaaS categories (P)
- Defined the AI and data strategy for the product organisation, shaping investment priorities and build-vs-buy decisions (P)
- Pricing and packaging work on the portfolio (C)
- Regular board-level updates to PE investors on roadmap and P&L (C)
- Drove internal AI tooling adoption across the SaaS portfolio (C)
- Presented to PE investors and portfolio-optimisation forums; involved in M&A evaluation (C)
- Worked across Design on the SaaS portfolio redesign and design-system alignment (C)

### Aviva - Enterprise Data Architect (contract), Aug 2024 - Jul 2026
UK: Global, Corporate, Specialty Insurance. Appears on the DATA_ARCHITECT template by default; on a Product CV only as profile proof or, when the JD stresses regulated/financial services, as a title-blended extra role (Section 4).
- Owned vendor relationships and the technical roadmap for a £90M programme (Guidewire, AWS, Snowflake, Collibra) (P/DA)
- Built delivery blueprints and RACI governance, accelerating delivery 30% (DA)
- Led data mesh architecture delivering £10M savings across Guidewire, SEND, hx pricing, AWS, Snowflake and Collibra (DA)
- Built AWS EventBridge/MSK event patterns, creating analytics products that improved underwriting accuracy 25% (DA)
- Moved SEND from daily batches to 15-minute micro-batches, enabling real-time decisioning for underwriting workflows (DA)
- Regulated insurance environment; GDPR/data-privacy exposure on first-party data work (C)
- On a Product CV keep the plain (contract) suffix: the dates overlap OneAdvanced (~6 months) and dunnhumby (~7 months), confirmed fine 2026-09-19, so add no 'concurrent contract' clarifier (C 2026-09-19)
- On a Product CV pull it in as an extra title-blended role (e.g. Technical Product Owner, Enterprise Data Architect) only when the JD stresses FinTech/financial services/regulated environments, reframed toward delivery, roadmap and vendor management (C)

### Amazon - Head of Product, Principal AdTech Consultant, Dec 2021 - Nov 2023
London, UK. DA title: Data Solutions Architect
- Won $28M in professional services and drove $138M in incremental media spend through AI-enhanced AdTech solutions (P/DA)
- Built a global team co-building 3-year AdTech strategy and AI-innovation roadmaps with 82 enterprise clients (P/DA)
- Directed the CMO/CTO advisory board to drive investments via proof-of-value projects with P&G, Mars, HP, LG and Sony (P/DA)
- Drove a 45% win rate across measurement, attribution and clean room consulting engagements, lead to closed-won (P)
- Personally owned pricing and proposal writing for the engagements; negotiated scope and terms directly with enterprise clients (C)
- Owned solution architecture and build-vs-buy analysis of data platform layers, aligning migration to enterprise standards (DA)
- Led development of data measurement solutions using Amazon's AdTech, APIs, data clean rooms and AWS technologies (DA)
- Directed design partnerships with enterprise clients and helped structure design review boards (C)
- Pricing and packaging on the AdTech consulting engagements (C 2026-09-19)

### Hybrid Theory (acquired by Azerion) - Chief Product Officer, Apr 2019 - Aug 2021
London, UK: Digital Marketing Agency. DA title: Data Product Architect
- Drove 40% annual revenue growth, 85% client retention and 9.3 NPS, and won 3 AdTech awards for AI products (P)
- Launched AI-powered contextual and first-party data advertising products generating £1M in new revenue (P/DA)
- Led M&A investment strategy, secured £3M for a social AI acquisition and oversaw the Azerion merger, leading squads of 20+ (P)
- Engineered a cultural and operational turnaround, transforming Hybrid Theory into a market leader, acquired by Azerion (P)
- Owned the Design function from scratch and hired and led the Head of Design (C 2026-09-29)
- Presented to the board pre-acquisition; investor updates (C)
- Spoke at IAB UK's Digital Trust Forum (2021) on "trust by design" and privacy-by-design; publicly documented via IAB UK's event coverage (C)
- Owned solution architecture across engineering for B2B data products, partnerships and privacy requirements (DA)
- Assessed a data estate of 10M events per day; led data architecture and technology-acquisition due diligence with risk assessments and integration plans (DA)
- Developed a leading position on data protection, ensuring security for 1B+ users per month (DA)
- Investor updates and M&A negotiations with Azerion; led M&A due diligence and investment strategy for the £3M social AI acquisition (C)
- Pricing and packaging on the AI-powered contextual and first-party data advertising products (C 2026-09-19)

### Dentsu - Senior Product Director (contract), Mar 2018 - Apr 2019
London, UK: Global Marketing Agency. DA title: Solutions Architect
- Contracted to develop and launch a B2B SaaS media hub product for clients to analyse marketing effectiveness (P)
- Managed on-shore and off-shore teams of 30 specialists, including data scientists, across multiple international locations (P)
- Directed strategy, roadmaps, resources and revenues, liaising with major data stakeholders such as Intel and Microsoft (P)
- Delivered to specification and deadline, retaining £3M in billings and saving £1M in resources (P)
- Led the architecture of the data ETL, governance and data visualisation components into BI reporting; aligned data solutions to enterprise data roadmaps (DA)
- Managed international design teams on-shore and off-shore for the media hub product (C)

### Patel Hospitality Group - Managing Partner, Feb 2017 - Feb 2018
Alabama, USA: Hotel Hospitality
- Managed a $15M hotel portfolio and an 80-strong team across 4 locations, with full P&L accountability (P/DA)
- Negotiated stringent renovation contracts and timeframes to reduce costs 25% ($500K saved) (P/DA)
- Introduced a hotel standard operating model that lifted profits 20% in 3 months, with a 4.2 TripAdvisor rating (P/DA)

### Sage - Product Director (contract), Jan 2016 - Feb 2017
London, UK: Multinational Enterprise Software Company. DA title: Data Solution Architect
- Integrated diverse data and technology in C-level reports for sales, HR, marketing & finance, saving £10M CapEx & OpEx (P/DA)
- Led the £3M business case for an agile product strategy and a centre of excellence delivering data architecture insights (P/DA)
- Defined data solution architecture, enterprise data standards and data roadmaps across functions (DA)
- Design-product integration for the C-suite reporting and data architecture work (C)

### dunnhumby - Senior Product Manager, Senior Consultant & Senior Data Analyst, Jun 2010 - Dec 2015
London UK, Chicago USA & Cincinnati USA: Marketing Data Science AI/ML. DA title: Sr. Data Manager, Data Consultant & Data Analyst
- Senior Product Manager for a 2-year £1M agile proof-of-concept for Tesco, Coca-Cola, Facebook, P&G and Twitter; led a 10-strong team building the first go-to-market product measuring digital ad impact through retail sales; roadmap delivered a £5M sales growth opportunity (P)
- Manager for a 10-month £7M B2C portfolio of data products across digital, legal, marketing, partnerships and stores; built the business roadmap and led retail media teams on offline & online measurement using Tesco customer data (P)
- Senior Product Manager for a 10-month £10M B2C big-data price & promotions optimisation tool for Tesco internationally: cut customer deployment time 40% through a common architecture approach and delivered £52M (520% ROI) (P/DA)
- Senior Consultant for Macy's overseeing a $3M data solution and $5M sales pipeline for retail & QSR; delivered a $2M sales pipeline of RFPs in 14 months (P/DA)
- Senior Data Analyst managing Kroger's $15M delivery of omnichannel campaigns across 65M US households; standardised direct mail across 14 retail subsidiaries, saving $2M (P/DA)

### Earlier Career, Feb 2002 - Jun 2010
- Senior Consultant, Accenture, Atlanta: saved $13M costs per year via a governance framework (Jan-Jun 2010)
- Product Analyst, information security upgrades to 8K Walmart stores, 1.8M employees, 21 countries (2009-10)
- Product Manager, University of Alabama: led $100K revenue and teams deploying public Wi-Fi to 15K users (Jan-May 2009)
- MD, Editor and Partner for three websites serving thousands of football fan forums and millions of video downloads (2002-09)

### Education, certifications, awards, languages
- Executive MBA, Quantic School of Business and Technology, Washington DC, USA. BSc Management Information Systems & Computer Science, The University of Alabama, USA
- Certifications: Agile, Scrum Master, International Product Owner, Six Sigma, Snowflake, UCloud, Marketing, Trading; AWS Cloud Practitioner; Amazon Advertising (Campaign Planning, DSP Campaigns, Sponsored Ads, Retail)
- Awards: 3 AdTech awards for AI products (Hybrid Theory, 2019-2021); Speaker, IAB UK Digital Trust Forum (2021)
- Languages: fluent English and Gujarati. Joint nationality: British & American

---

## Section 2: Cross-Role Facts & Guardrails

Each entry: the JD words that trigger it, where the evidence sits, and the limit on how to frame it. Role-specific facts live once in Section 1. A match here means **not a gap**.

- **Board, investor and PE exposure** (JD: investor relations, board reporting, quarterly business reviews, strategic planning for stakeholders). Hybrid Theory, OneAdvanced, dunnhumby (Section 1). Direct match.
- **BI / analytics tools, hands-on** (JD: Looker, Power BI, analytics tools). Excel, Power BI, Tableau, Looker, MicroStrategy, QuickSight, Google Data Studio, used for revenue reporting, product-metrics dashboards, customer analytics, competitive analysis, forecasting, data exploration and executive reporting. Direct match.
- **Governance and delivery tools** (JD: Jira, Confluence). Hands-on daily use across roles for delivery tracking, backlog/roadmap governance and documentation (C 2026-09-19). Direct match.
- **Design function** (JD: design partnership, UX/product alignment, design leadership). Owned at Hybrid Theory; partnered at dunnhumby, OneAdvanced, Amazon, Dentsu and Sage (Section 1). Almost certainly covered.
- **CRM, CDP, MarTech** (JD: CRM, CDP, martech, marketing automation, lead scoring). HubSpot, Salesforce, Marketo and Pardot evaluated and integrated with product platforms; CDP work on data architecture and customer-data integration; MarTech integrations, lead-scoring workflows and marketing-automation connectors. Context: primarily through AdTech/retail media work. Covered.
- **Regulated environments** (JD: regulator-facing, compliance, financial/healthcare/telecom regulation). GDPR/data-privacy compliance on first-party data strategies (dunnhumby, Amazon); Aviva is a regulated insurance environment. **Guardrail:** insurance, not banking. Banking/fintech regulation (PRA/FCA, AML/KYC), healthcare compliance, securities and formal regulatory affairs are genuine gaps.
- **AI coding assistants / agentic tooling, hands-on** (JD: coding assistants, AI-native mindset, leveraging Claude/AI tools). Daily use of Claude Code, Claude, OpenClaw, Hermes and other assistants in real workflow; this skill is itself built and run through Claude Code. Direct match.
- **AI platform ownership** (JD: Agent Hub, RAG, AI gateways, internal AI tooling adoption, AI platform roadmap, build-vs-buy for AI infrastructure). dunnhumby and OneAdvanced (Section 1). **Guardrail:** roadmap/ownership level only; frame as roadmap ownership, vendor evaluation and adoption-driving, never as personally building RAG pipelines or agent frameworks.
- **Commercial ownership** (JD: pricing, proposals, commercial negotiation, P&L/budget/margin, protecting project margin). Amazon: personally owned pricing and proposals and negotiated scope and terms directly. Formal budget/cost-base/margin-against-target accountability at Amazon, dunnhumby and OneAdvanced, plus full P&L at Patel Hospitality: distinct from top-line growth ownership. Direct match.
- **Pricing & packaging** (JD: pricing, packaging, monetisation). OneAdvanced, Hybrid Theory, Amazon (Section 1). **Guardrail:** don't invent pricing models or revenue-impact numbers beyond what is recorded.
- **Full-funnel conversion optimisation** (JD: conversion funnel, digital booking journey, funnel optimisation, checkout/enquiry flow). dunnhumby, Amazon, Dentsu, Hybrid Theory: owned full-funnel campaign setup and optimisation from audience selection to conversion across intent, product/detail page, enquiry and checkout, using funnel metrics (C 2026-09-19). **Guardrail:** campaign-level funnel ownership, not building or running a transactional booking system.
- **Personalisation, A/B testing, experimentation** (JD: personalisation, A/B testing, experimentation, recommendations engine). dunnhumby, Amazon, Dentsu, Hybrid Theory ran A/B tests on creatives, messaging, offers and recommendations-engine outputs to optimise personalisation and conversion (C 2026-09-19). **Guardrail:** no named experimentation platform (Optimizely, VWO) was confirmed: say "A/B testing" or "experimentation" only.
- **Two-sided marketplace / platform dynamics** (JD: two-sided marketplace, platform business, supply-demand, network effects). Amazon Ads (publisher supply against advertiser demand: owned demand-side client relationships, 82 enterprise clients, $28M services, $138M incremental spend); programmatic AdTech at Hybrid Theory (supply vs demand with real network effects); dunnhumby's aggregator (retailers, advertisers and agency holdcos on one platform). **Guardrail (C 2026-09-21):** hands-on ownership was demand-side; supply-side dynamics were understood and factored into strategy but not owned end to end. Frame as "marketplace/platform experience, supply-demand balancing, network effects", never as personal ownership of supply acquisition or onboarding.
- **Business capability model / value streams / enterprise architecture alignment** (JD: business capability model, value stream, capability vision and roadmap, enterprise architecture alignment). Confirmed across Hybrid Theory, Amazon, OneAdvanced, dunnhumby and Sage: connecting business capabilities and process/technology/data components to product roadmaps. Sage's £3M business case is the documented anchor, and the same approach applied in the other roles (C 2026-09-28). Don't limit it to Sage.
- **CIO/CTO relationships and deputising** (JD: reports to the CIO, senior technology leadership team, deputise for the CIO). Across Hybrid Theory, Amazon, OneAdvanced, dunnhumby and Sage: managed CIO/CTO-level relationships and acted as deputy/proxy for that function (C 2026-09-28). **Guardrail:** not a single named direct-reporting line unless one is confirmed.
- **Demand management, business cases, funded approvals** (JD: demand management, prioritisation methodology, investment cases, business case, funding approval, intake process, technology investment priorities). dunnhumby (Section 1). Confirmed 2026-09-29 as a pattern not specific to one role: apply it where the JD's scope calls for it, with Sage's £3M business case as the anchor elsewhere. **Guardrail:** the named programmes (AI, data clean rooms, identity graphs) belong to dunnhumby only.
- **CEO-level stakeholders** (JD: CEO, executive leadership team, engage stakeholders at all levels). Confirmed 2026-09-29; employer(s) not specified. **Guardrail:** keep it generic ("Board & C-suite stakeholders incl. CEO") and don't attribute it to a role.

---

## Section 3: Notable Absences (genuine gaps)

- No C-level title held above CPO (CPO is the highest; chief-of-staff is a different role type: support, not decision-maker).
- No CFO/finance operations experience (P&L management yes, financial operations no).
- No sales leadership (enterprise sales strategy yes, quota-carrying teams no).
- No HR/talent operations (team building yes, structured HR systems no).
- No direct legal/compliance background.
- Banking/fintech regulation, healthcare compliance, securities, formal regulatory affairs (see Regulated environments above).

These stay flagged as gaps if the JD emphasises them.

---

## Section 4: Template Selection

Pick by target role type. Both templates draw every fact from Section 1; the template only changes emphasis, ordering and titles.

- **PRODUCT_CV:** Product Director, VP of Product, CPO, Senior Product Manager, Head of Product. Uses the titles actually held. Includes the LinkedIn URL. Leads with product/commercial evidence.
- **DATA_ARCHITECT_CV:** Data Architect, Data Engineer, Analytics Engineer, Data Science. Uses the `DA title` shown in Section 1 and the `(DA)`-tagged lines first. No LinkedIn URL. Leads with data/architecture evidence.

Anything else: ask which template to use. Both share the layout and voice rules in `03-formatting.md`. The two original source-CV PDFs in `Source CVs/` are archival only.

---

## Section 5: Title Blending Strategy (When Tailoring for Specific JDs)

**This section is the single source of truth for title-blending rules.**
`03-formatting.md` only points here — don't duplicate the rules or examples
back into that file.

When a JD calls for a specific role title (e.g., "Product Director," "Senior Product Manager," "Solution Architect"), and prior experience includes related but differently-titled roles, use title blending in the "Career & Key Achievements" section.

**Format:** `{Functional Title}, {Actual Title}`

### Examples from Hiran's Background

- JD calls for "Product Director" → Past role was "VP of Product" (OneAdvanced)
  - Blended: `Senior Product Director, VP of Product`
  - Justification: VP is director-level scope, hands-on IC work matches the JD's emphasis

- JD calls for "Head of Product" → Past role was "Principal AdTech Consultant" (Amazon)
  - Blended: `Head of Product, Principal AdTech Consultant`
  - Justification: Scope was head-of-product level (82 clients, $138M impact, strategy/roadmap), title was consultant-level

- JD calls for "Senior Product Manager" → Past role was "Senior Product Director" (Dentsu)
  - May not need blending (title is higher)
  - Or blend downward if emphasizing hands-on IC: `Senior Product Manager, Senior Product Director`

### Rules for Title Blending

1. **Only blend when the scope genuinely matches.** Don't invent seniority.
2. **Functional title comes first** — it's what the JD sees first and what they're looking for.
3. **Actual title comes second** — it maintains truthfulness and verifiability.
4. **Use sparingly.** Only for roles where the scope-to-title mismatch is real and relevant to this JD.
5. **Never blend toward a title you never held.** "Product Director" blending is fine if you were VP or Head of Product; "Chief Product Officer" blending is not if you were only VP.

### When NOT to Blend

- The actual title is already higher than what the JD asks for (VP blending for Senior Manager role — unnecessary)
- The scope doesn't match (you were a consultant, don't blend to "Product Manager" unless you actually managed products)
- The JD doesn't emphasize title; it emphasizes skills (focus on skills section instead)

---

## Section 6: JD Term Synonyms (for matching)

When the JD uses a term below, these are the CV words that count as the same thing (synonym-only matches should be switched to the JD's own term where truthful).

- **MarTech:** marketing automation, Salesforce, HubSpot, Marketo, Pardot, lead scoring, campaign management, CDP, marketing workflows
- **CDP / first-party data:** customer data platform, customer profiles, identity resolution, data activation, segmentation, privacy-safe, clean room, consent management, GDPR
- **Search / discovery / recommendations:** ranking, personalisation, recommendation engine, relevance, matching, user intent
- **Hands-on IC:** execution, delivery, PRDs, specification writing, prototyping, Engineering partnership, sprint execution, launch
- **B2B SaaS:** SaaS, recurring revenue, customer success, enterprise software, platform, GTM, product-market fit
- **AI / LLM:** machine learning, generative AI, AI-powered, AI features, experimentation, prompt engineering
- **Data architecture / engineering:** data platform, pipeline, ETL, modelling, data governance, Snowflake, Databricks, Kafka, streaming, batch
- **Retail media / measurement / AdTech:** attribution, advertiser outcomes, clean rooms, measurement framework, programmatic, ad-serving, brand safety
- **Business capability / value stream:** capability model, value-stream alignment, capability roadmap, enterprise architecture, portfolio
- **Demand management:** demand intake, prioritisation, business case, funding approval, investment priorities
