/**
 * build_cv_reference.js — reference implementation of every rule in
 * ../references/cv-formatting.md (house style confirmed 2026-09-17).
 *
 * This is a WORKING EXAMPLE, not a generic template engine: the content
 * below (Profile Summary, Key Skills rows, per-role bullets) is the actual
 * text from a real tailored CV (SVP Product / AI-native role). For a new
 * JD, copy this file, keep every styling helper and layout constant
 * (fonts, sizes, colours, spacing, margins, keepNext/keepLines wiring,
 * document properties) exactly as-is, and only rewrite the *content*
 * passed into roleBlock(), the Profile Summary paragraphs, and the Key
 * Skills rows to match the target role — reusing real facts from the CV
 * library, never inventing achievements (per SKILL.md's core principle).
 *
 * After running this (`node <file>.js`), always run
 * `python3 scripts/validate_cv.py <output>.docx --max-pages 2` before
 * calling it done — see cv-decision-gates.md §5.3.
 */
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  BorderStyle, Spacing, Table, TableRow, TableCell, WidthType,
  ExternalHyperlink, LevelFormat, convertInchesToTwip
} = require("docx");

const NAVY = "1F3864";
const DARK = "222222";
const GREY = "555555";

const bulletNumbering = {
  config: [
    {
      reference: "bullet-list",
      levels: [
        {
          level: 0,
          format: LevelFormat.BULLET,
          text: "\u25AA",
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 300, hanging: 200 } } },
        },
      ],
    },
  ],
};

function bullet(text, opts = {}) {
  return new Paragraph({
    numbering: { reference: "bullet-list", level: 0 },
    spacing: { after: 0, line: 276, lineRule: "auto" },
    children: [new TextRun({ text, size: 21, color: DARK, ...opts })],
  });
}

function sectionHeading(text) {
  return new Paragraph({
    spacing: { before: 220, after: 90 },
    border: { bottom: { color: NAVY, space: 2, style: BorderStyle.SINGLE, size: 6 } },
    children: [new TextRun({ text, bold: true, size: 23, color: NAVY, allCaps: false })],
  });
}

function roleHeader(title, dates, keepNext = true) {
  return new Paragraph({
    spacing: { before: 150, after: 0 },
    keepNext,
    tabStops: [{ type: "right", position: convertInchesToTwip(7.35) }],
    children: [
      new TextRun({ text: title, bold: true, size: 21, color: DARK }),
      new TextRun({ text: "\t" + dates, bold: false, size: 21, color: GREY }),
    ],
  });
}

function companyLine(text, keepNext = true) {
  return new Paragraph({
    spacing: { after: 40 },
    keepNext,
    children: [new TextRun({ text, italics: true, size: 21, color: GREY })],
  });
}

// Builds a full role block (header + company + bullets) with keepNext chained
// through every paragraph except the last bullet, so the whole role moves
// together as one unit if it doesn't fit on the current page.
function roleBlock(title, dates, company, bulletTexts) {
  const paras = [
    roleHeader(title, dates, true),
    companyLine(company, true),
  ];
  bulletTexts.forEach((t, i) => {
    const isLast = i === bulletTexts.length - 1;
    paras.push(
      new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        spacing: { after: 0, line: 276, lineRule: "auto" },
        keepNext: !isLast,
        keepLines: true,
        children: [new TextRun({ text: t, size: 21, color: DARK })],
      })
    );
  });
  return paras;
}

const doc = new Document({
  creator: "Hiran Patel",
  lastModifiedBy: "Hiran Patel",
  title: "Hiran Patel - CV",
  subject: "Curriculum Vitae",
  description: "Tailored CV for Hiran Patel",
  numbering: bulletNumbering,
  styles: {
    default: {
      document: { run: { font: "Calibri" } },
    },
  },
  sections: [
    {
      properties: {
        page: {
          size: { width: 11906, height: 16838 }, // A4
          margin: { top: 560, bottom: 560, left: 680, right: 680 },
        },
      },
      children: [
        // Name
        new Paragraph({
          spacing: { after: 20 },
          children: [
            new TextRun({ text: "Hiran Patel ", bold: true, size: 40, color: NAVY }),
            new TextRun({ text: "BSc, MBA", size: 24, color: GREY }),
          ],
        }),
        new Paragraph({
          spacing: { after: 170, line: 276, lineRule: "auto" },
          children: [
            new TextRun({ text: "London, UK   |   +44 [redacted-phone]   |   ", size: 21, color: GREY }),
            new ExternalHyperlink({
              link: "mailto:[redacted-email]",
              children: [new TextRun({ text: "[redacted-email]", size: 21, color: "1155CC", underline: {} })],
            }),
            new TextRun({ text: "   |   ", size: 21, color: GREY }),
            new ExternalHyperlink({
              link: "https://www.linkedin.com/in/hiran-patel/",
              children: [new TextRun({ text: "LinkedIn", size: 21, color: "1155CC", underline: {} })],
            }),
          ],
        }),

        sectionHeading("Profile Summary"),
        new Paragraph({
          spacing: { after: 90, line: 276, lineRule: "auto" },
          children: [
            new TextRun({ text: "Product executive ", bold: true, size: 21, color: DARK }),
            new TextRun({
              text: "with 15+ years leading product organisations across B2B SaaS, retail media, AdTech, and enterprise data platforms, most recently defining AI/agentic product strategy at CEO and board level. Builds and scales product functions from 0-to-1 to \u00a3100M+ ARR, embedding AI/ML into core commercial products and converting investment into measurable business outcomes: $28M won in professional services, $138M in incremental revenue, and \u00a352M delivered at 520% ROI.",
              size: 21, color: DARK,
            }),
          ],
        }),
        new Paragraph({
          spacing: { line: 276, lineRule: "auto" },
          children: [
            new TextRun({
              text: "Owns full product portfolios end-to-end - vision, multi-year roadmap, organisation design, hiring, P&L, and vendor/build-vs-buy decisions - while remaining hands-on across discovery, data, and delivery. Regularly partners with CEO, CMO and CTO advisory boards, leads global on/off-shore teams of 30+, and has driven two company exits including post-merger product integration, across the UK/EU, USA & APAC.",
              size: 21, color: DARK,
            }),
          ],
        }),

        sectionHeading("Key Skills & Competencies"),
        new Paragraph({ spacing: { after: 50, line: 276, lineRule: "auto" }, children: [new TextRun({
          text: "AI/ML & Agentic Product Strategy  \u00b7  Product Vision, Multi-Year Roadmaps & Portfolio Ownership  \u00b7  Executive & Board-Level Stakeholder Management (CEO, CMO, CTO)  \u00b7  Product Organisation Design, Hiring & Talent Strategy",
          size: 21, color: DARK,
        })]}),
        new Paragraph({ spacing: { after: 50, line: 276, lineRule: "auto" }, children: [new TextRun({
          text: "P&L Management & Commercial Monetisation  \u00b7  Platform Build (0-to-1) & API/Integration Architecture  \u00b7  Data Architecture, Clean Rooms & First-Party Data  \u00b7  Vendor Selection & Build-vs-Buy Analysis",
          size: 21, color: DARK,
        })]}),
        new Paragraph({ spacing: { line: 276, lineRule: "auto" }, children: [new TextRun({
          text: "GTM Strategy & Revenue Growth  \u00b7  M&A Due Diligence & Integration  \u00b7  Cross-Functional & Global Team Leadership  \u00b7  Cloud (AWS, GCP)  \u00b7  B2B / B2B2C / Enterprise SaaS  \u00b7  CPG & FMCG",
          size: 21, color: DARK,
        })]}),

        sectionHeading("Career & Key Achievements to Date"),

        ...roleBlock(
          "Interim Director of Product, Data & Technology (contract)",
          "Jan 2026 - present",
          "dunnhumby / Tesco, London, UK: Retail Media SaaS, Data Science, AI/Agentic",
          [
            "Own the \u00a3200M+ multi-year AI-enabled product strategy and vision for a retail media aggregator platform",
            "Secured \u00a310M+ investment and built a 20+ person multi-partner product, engineering and data science org",
            "Led discovery with CPG advertisers, agency holdcos, and retail partners to validate the GTM proposition",
            "Owned the roadmap and led 4x vendor selections spanning data clean rooms, ad-serving, and external engineering",
            "Architected the UK's largest first-party data and measurement strategy across 10+ media networks and channels",
          ]
        ),

        ...roleBlock(
          "VP of Product (contract)",
          "Jul 2024 - Jan 2025",
          "OneAdvanced, London & Birmingham, UK: PE-backed SaaS Leader",
          [
            "Spearheaded the \u00a3100M ARR B2B SaaS portfolio in workforce management & financial solutions, integrating AI",
            "Drove a 25% uplift in customer satisfaction and retention through new product OKRs and a performance framework",
            "Led market-driven product roadmap, GTM sales strategy, and M&A target evaluation across 3 vertical SaaS categories",
            "Defined the AI and data strategy for the product org, shaping investment priorities and build-vs-buy decisions",
          ]
        ),

        ...roleBlock(
          "Head of Product, Principal AdTech Consultant",
          "Dec 2021 - Nov 2023",
          "Amazon, London, UK: Global AdTech & Media Measurement",
          [
            "Won $28M in professional services and drove $138M in incremental media spend through AI-enhanced AdTech",
            "Built a global team co-building 3-year AdTech strategy & AI-innovation roadmaps with 82 enterprise clients",
            "Directed the CMO/CTO advisory board to drive investment via proof-of-value projects with P&G, Mars, HP, LG & Sony",
            "Drove a 45% win rate across measurement, attribution, and clean room consulting engagements, lead to closed-won",
          ]
        ),

        ...roleBlock(
          "Chief Product Officer",
          "Apr 2019 - Aug 2021",
          "Hybrid Theory (acquired by Azerion), London, UK: Digital Marketing Agency",
          [
            "Drove 40% annual revenue growth, achieved 85% client retention with 9.3 NPS, and won 3 AdTech awards for AI",
            "Launched AI-powered contextual and first-party data advertising products that generated \u00a31M in new revenue",
            "Led M&A investment strategy, secured \u00a33M for a social AI acquisition, and oversaw the merger, leading squads of 20+",
            "Engineered a cultural & operational turnaround, transforming the business into a market leader pre-acquisition",
          ]
        ),

        ...roleBlock(
          "Senior Product Director (contract)",
          "Mar 2018 - Apr 2019",
          "Dentsu, London, UK: Global Marketing Agency",
          [
            "Contracted to develop & launch a B2B SaaS media hub product for clients to analyse marketing effectiveness",
            "Managed on-shore and off-shore teams of 30 specialists, including data scientists, across international locations",
            "Directed strategy, roadmaps, resources and revenues, liaising with major data stakeholders like Intel and Microsoft",
            "Delivered the product to specification and deadline, retaining \u00a33M in billings and saving \u00a31M in resources",
          ]
        ),

        ...roleBlock(
          "Managing Partner",
          "Feb 2017 - Feb 2018",
          "Patel Hospitality Group, Alabama, USA: Hotel Hospitality",
          [
            "Managed a $15M hotel portfolio and an 80-strong team across 4 locations in Alabama, with full P&L accountability",
            "Negotiated stringent renovation contracts to reduce costs by 25% ($500K saved), lifting profits 20% in 3 months",
          ]
        ),

        ...roleBlock(
          "Product Director (contract)",
          "Jan 2016 - Feb 2017",
          "Sage, London, UK: Multinational Enterprise Software Company",
          [
            "Integrated diverse data and technology in C-level reports for sales, HR, marketing & finance, saving \u00a310M",
            "Led the \u00a33M business case for an agile product strategy and a centre of excellence for data architecture insights",
          ]
        ),

        ...roleBlock(
          "Senior Product Manager, Senior Consultant & Senior Data Analyst",
          "Jun 2010 - Dec 2015",
          "dunnhumby, London UK / Chicago & Cincinnati, USA: Marketing Data Science, AI/ML",
          [
            "Led a 10-person team on a 2-year, \u00a31M PoC for Tesco, Coca-Cola, Facebook, P&G & Twitter measuring ad impact",
            "Delivered a \u00a310M big-data pricing tool for Tesco: cut deployment time 40%, \u00a352M (520% ROI)",
            "Additional: Macy's ($3M data solution, $2M pipeline) and Kroger ($15M delivery, $2M savings)",
          ]
        ),

        new Paragraph({
          spacing: { before: 120, after: 50 },
          keepNext: true,
          children: [new TextRun({ text: "Earlier Career", bold: true, size: 21, color: DARK })],
        }),
        bullet("Senior Consultant, Accenture, Atlanta: saving $13M in costs per year via a governance framework (2010)"),
        bullet("Product Analyst, Walmart: information security upgrades across 8K stores, 1.8M employees, 21 countries (2009-2010)"),
        bullet("Product Manager, University of Alabama: led $100K revenue and teams deploying public Wi-Fi to 15K users (2009)"),
        bullet("Founder, Editor & Partner: football fan-community network, three sites, millions of downloads (2002-2009)"),

        sectionHeading("Qualifications, Certifications & Personal Details"),
        new Paragraph({
          spacing: { after: 40, line: 276, lineRule: "auto" },
          tabStops: [{ type: "right", position: convertInchesToTwip(7.35) }],
          children: [
            new TextRun({ text: "Languages: ", bold: true, size: 21, color: DARK }),
            new TextRun({ text: "Fluent English & Gujarati", size: 21, color: DARK }),
            new TextRun({ text: "\tJoint Nationality: ", bold: true, size: 21, color: DARK }),
            new TextRun({ text: "British & American", size: 21, color: DARK }),
          ],
        }),
        bullet("Executive MBA, Quantic School of Business and Technology, Washington DC, USA"),
        bullet("BSc Management Information Systems & Computer Science, The University of Alabama, USA"),
        bullet("Selected Certifications: Agile, Scrum Master, International Product Owner, Six Sigma, Snowflake, Marketing"),
        bullet("Amazon: Web Services Cloud Practitioner. Advertising: Campaign Planning, DSP Campaigns, Sponsored Ads, Retail"),
      ],
    },
  ],
});

Packer.toBuffer(doc).then((buf) => {
  // Adjust output path/filename per SKILL.md's naming convention: {YYYY-MM-DD}_{Company}_{Role}.docx
  require("fs").writeFileSync("./output.docx", buf);
  console.log("written");
});
