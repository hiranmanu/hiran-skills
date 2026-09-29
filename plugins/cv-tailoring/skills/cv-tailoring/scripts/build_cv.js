#!/usr/bin/env node
/**
 * build_cv.js - render a tailored CV from a JSON content file.
 *
 *   node build_cv.js content.json                 -> writes to the auto output path
 *   node build_cv.js content.json out.docx        -> writes to an explicit path
 *   node build_cv.js content.json --identity my.json
 *
 * The house style (fonts, sizes, colours, margins, spacing, keepNext/keepLines,
 * tab stops, document properties) lives HERE, once, and is implemented exactly
 * as references/03-formatting.md specifies. A run only writes CONTENT: the JSON
 * file (see example_content.json for every field). No code is copied or edited
 * per CV, which is what used to cause escaping and layout regressions.
 *
 * Identity (name, contact, output folder) comes from identity.json next to this
 * script (gitignored, local only); identity.example.json is the template. If
 * identity.json is missing the example is used and a warning is printed.
 *
 * Auto output path (when no out path is given):
 *   <identity.output_base>/<YYYY.MM.DD>_<meta.company>_<meta.role_folder>/
 *       Hiran_CV_<YYYY.MM.DD>_<meta.company>_<meta.brief_role>.docx
 * where the file prefix is identity.file_prefix. This removes the recurring
 * filename/date mistakes.
 *
 * Dependency: the `docx` npm package. Run `npm install` once in this folder.
 * After rendering, run validate_cv.py and word_layout_check.ps1 (SKILL.md step 05).
 */
const fs = require("fs");
const path = require("path");

let docx;
try {
  docx = require("docx");
} catch (e) {
  console.error("The 'docx' package is not installed. Run `npm install` once in " + __dirname);
  process.exit(2);
}
const {
  Document, Packer, Paragraph, TextRun, AlignmentType, BorderStyle,
  ExternalHyperlink, LevelFormat, convertInchesToTwip,
} = docx;

const NAVY = "1F3864";
const DARK = "222222";
const GREY = "555555";
const LINK = "1155CC";
const SZ = 21; // 10.5pt
const DATE_TAB = convertInchesToTwip(7.35); // right tab, flush to the true margin edge

// ------------------------------------------------------------------ helpers
const run = (text, o = {}) => new TextRun({ text, size: SZ, color: DARK, ...o });

const bulletNumbering = {
  config: [{
    reference: "bullet-list",
    levels: [{
      level: 0, format: LevelFormat.BULLET, text: "▪", alignment: AlignmentType.LEFT,
      style: { paragraph: { indent: { left: 300, hanging: 200 } } },
    }],
  }],
};

function bullet(text, keepNext = false) {
  return new Paragraph({
    numbering: { reference: "bullet-list", level: 0 },
    spacing: { after: 0, line: 276, lineRule: "auto" },
    keepNext, keepLines: true,
    children: [run(text)],
  });
}

function sectionHeading(text) {
  return new Paragraph({
    spacing: { before: 220, after: 90 },
    border: { bottom: { color: NAVY, space: 2, style: BorderStyle.SINGLE, size: 6 } },
    children: [new TextRun({ text, bold: true, size: 23, color: NAVY })],
  });
}

function dateLine(title, dates, keepNext = true, before = 150) {
  return new Paragraph({
    spacing: { before, after: 0 },
    keepNext,
    tabStops: [{ type: "right", position: DATE_TAB }],
    children: [
      new TextRun({ text: title, bold: true, size: SZ, color: DARK }),
      new TextRun({ text: "\t" + dates, size: SZ, color: GREY }),
    ],
  });
}

function companyLine(text) {
  return new Paragraph({
    spacing: { after: 40 }, keepNext: true,
    children: [new TextRun({ text, italics: true, size: SZ, color: GREY })],
  });
}

// header + company + bullets, keepNext chained so the whole role moves as one block
function roleBlock(r) {
  const out = [dateLine(r.title, r.dates), companyLine(r.company)];
  r.bullets.forEach((b, i) => out.push(bullet(b, i < r.bullets.length - 1)));
  return out;
}

function skillRow(row, last) {
  return new Paragraph({
    spacing: { after: last ? 0 : 50, line: 276, lineRule: "auto" },
    children: [run(row.label + ": ", { bold: true }), run(row.items.join("  ·  "))],
  });
}

// ------------------------------------------------------------------ input
function fail(msg) { console.error("build_cv.js: " + msg); process.exit(1); }

function loadJson(p, what) {
  try { return JSON.parse(fs.readFileSync(p, "utf-8").replace(/^﻿/, "")); }
  catch (e) { fail(`cannot read ${what} (${p}): ${e.message}`); }
}

function collectStrings(v, where, out) {
  if (typeof v === "string") out.push([where, v]);
  else if (Array.isArray(v)) v.forEach((x, i) => collectStrings(x, `${where}[${i}]`, out));
  else if (v && typeof v === "object") Object.entries(v).forEach(([k, x]) => collectStrings(x, where ? `${where}.${k}` : k, out));
}

function checkContent(c) {
  const need = (cond, msg) => { if (!cond) fail("content: " + msg); };
  need(c.profile && Array.isArray(c.profile.paragraphs) && c.profile.paragraphs.length >= 1 && c.profile.paragraphs.length <= 3, "profile.paragraphs must have 1-3 paragraphs (two is the house style)");
  need(typeof c.profile.lead === "string", "profile.lead (the bold opening words) is required");
  need(Array.isArray(c.skills) && c.skills.length === 3, "skills must have exactly 3 rows");
  c.skills.forEach((s, i) => need(s.label && Array.isArray(s.items) && s.items.length > 0, `skills[${i}] needs a label and items`));
  need(Array.isArray(c.roles) && c.roles.length > 0, "roles must have at least one role");
  c.roles.forEach((r, i) => need(r.title && r.dates && r.company && Array.isArray(r.bullets) && r.bullets.length > 0, `roles[${i}] needs title, dates, company and bullets`));
  need(c.qualifications && Array.isArray(c.qualifications.lines) && c.qualifications.lines.length > 0, "qualifications.lines is required");
  const strings = [];
  collectStrings(c, "", strings);
  strings.forEach(([w, s]) => { if (/[—–]/.test(s)) fail(`content: em/en dash in ${w}. Use a comma, colon or plain hyphen: "${s.slice(0, 60)}"`); });
}

function todayDots() {
  const d = new Date();
  const p = (n) => String(n).padStart(2, "0");
  return `${d.getFullYear()}.${p(d.getMonth() + 1)}.${p(d.getDate())}`;
}

// ------------------------------------------------------------------ main
const argv = process.argv.slice(2);
if (argv.length === 0 || argv[0] === "-h" || argv[0] === "--help") {
  console.log("usage: node build_cv.js content.json [out.docx] [--identity identity.json]");
  process.exit(argv.length === 0 ? 1 : 0);
}
let contentPath = null, outPath = null, identityPath = null;
for (let i = 0; i < argv.length; i++) {
  if (argv[i] === "--identity") identityPath = argv[++i];
  else if (!contentPath) contentPath = argv[i];
  else outPath = argv[i];
}
const content = loadJson(contentPath, "content file");
checkContent(content);

const localId = path.join(__dirname, "identity.json");
const exampleId = path.join(__dirname, "identity.example.json");
if (!identityPath) {
  if (fs.existsSync(localId)) identityPath = localId;
  else { identityPath = exampleId; console.error("warning: identity.json not found, using identity.example.json (placeholder identity)"); }
}
const id = loadJson(identityPath, "identity file");
const template = (content.template || "product").toLowerCase();

if (!outPath) {
  const m = content.meta || {};
  if (!m.company || !m.role_folder || !m.brief_role) fail("no out path given, so content.meta needs company, role_folder and brief_role for the auto output path");
  if (!id.output_base) fail("identity.output_base is not set");
  const date = m.date || todayDots();
  outPath = path.join(id.output_base, `${date}_${m.company}_${m.role_folder}`, `${id.file_prefix || "CV"}_${date}_${m.company}_${m.brief_role}.docx`);
}
fs.mkdirSync(path.dirname(path.resolve(outPath)), { recursive: true });

const contact = [
  new TextRun({ text: `${id.location}   |   ${id.phone}   |   `, size: SZ, color: GREY }),
  new ExternalHyperlink({ link: `mailto:${id.email}`, children: [new TextRun({ text: id.email, size: SZ, color: LINK, underline: {} })] }),
];
if (template === "product" && id.linkedin) {
  contact.push(new TextRun({ text: "   |   ", size: SZ, color: GREY }));
  contact.push(new ExternalHyperlink({ link: id.linkedin, children: [new TextRun({ text: "LinkedIn", size: SZ, color: LINK, underline: {} })] }));
}

const children = [
  new Paragraph({ spacing: { after: 20 }, children: [
    new TextRun({ text: id.name + " ", bold: true, size: 40, color: NAVY }),
    new TextRun({ text: id.credentials || "", size: 24, color: GREY }),
  ] }),
  new Paragraph({ spacing: { after: 170, line: 276, lineRule: "auto" }, children: contact }),

  sectionHeading("Profile Summary"),
];
content.profile.paragraphs.forEach((text, i, arr) => {
  const kids = i === 0 ? [run(content.profile.lead, { bold: true }), run(text)] : [run(text)];
  children.push(new Paragraph({ spacing: i < arr.length - 1 ? { after: 60, line: 276, lineRule: "auto" } : { line: 276, lineRule: "auto" }, children: kids }));
});

children.push(sectionHeading("Key Skills & Competencies"));
content.skills.forEach((row, i) => children.push(skillRow(row, i === content.skills.length - 1)));

children.push(sectionHeading("Career & Key Achievements to Date"));
content.roles.forEach((r) => children.push(...roleBlock(r)));
if (content.earlier_career && Array.isArray(content.earlier_career.bullets)) {
  const ec = content.earlier_career;
  children.push(dateLine("Earlier Career", ec.dates || "", true, 150));
  ec.bullets.forEach((b) => children.push(bullet(b)));
}

children.push(sectionHeading("Qualifications, Certifications & Personal Details"));
children.push(new Paragraph({
  spacing: { after: 40, line: 276, lineRule: "auto" },
  tabStops: [{ type: "right", position: DATE_TAB }],
  children: [run("Languages: ", { bold: true }), run(id.languages || ""), run("\tJoint Nationality: ", { bold: true }), run(id.nationality || "")],
}));
content.qualifications.lines.forEach((l) => children.push(bullet(l)));

const doc = new Document({
  creator: id.name, lastModifiedBy: id.name, title: `${id.name} - CV`,
  subject: "Curriculum Vitae", description: `Tailored CV for ${id.name}`,
  numbering: bulletNumbering,
  styles: { default: { document: { run: { font: "Calibri" } } } },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 560, bottom: 560, left: 680, right: 680 } } },
    children,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(outPath, buf);
  console.log(path.resolve(outPath));
});
