# Guide 00 Integration and QA Manifest — Batch 01

**Guide:** 00 — Lifelong Opportunity Foundation Guide  
**Branch:** `revision/guide-00-100-2026`  
**Prepared:** 2026-08-02  
**Status:** Completed controlled integration plan and source-to-section traceability record; not a publication certificate

## Purpose

This manifest converts the completed source-verification batches into an auditable assembly plan for the English, neutral Latin American Spanish, and Brazilian Portuguese editions of Guide 00. It identifies the exact source text, intended destination, terminology controls, and publication gates so that no verified evidence is lost or silently changed during assembly.

## Controlled source set

| Source file | Controlled use | Status |
|---|---|---|
| `00-foundation-guide/source/Lifelong_Opportunity_Foundation_Guide_English_v1.1_REVISED_MASTER.md` | Approved English structural master | Working master present |
| `project/revision-2026/guide-00/foundation-additions-trilingual.md` | Funding, apprenticeship, income-research, and editorial-control source text | Trilingual source prepared |
| `project/revision-2026/guide-00/LATIN_AMERICA_PATHWAYS_TRILINGUAL.md` | Mexico, Argentina, and Chile insertion text | Trilingual source prepared |
| `project/revision-2026/guide-00/OFFICIAL_SOURCE_VERIFICATION_REGISTER.md` | U.S., Canada, and Colombia primary-source traceability | Verified register |
| `project/revision-2026/guide-00/OFFICIAL_SOURCE_VERIFICATION_BATCH_02.md` | U.S. student aid, vocational rehabilitation, SNAP E&T, Canada labor and apprentice support, Colombia SNIES and ICETEX | Verified evidence batch |
| `project/revision-2026/guide-00/OFFICIAL_SOURCE_VERIFICATION_BATCH_03.md` | Colombia and Brazil pathways and terminology | Verified evidence batch |
| `project/revision-2026/guide-00/OFFICIAL_SOURCE_VERIFICATION_BATCH_04.md` | Mexico, Argentina, and Chile pathways and status controls | Verified evidence batch |

## English assembly map

### Existing Section 4 — Research pay, benefits, and outlook

Retain the current compensation-research method. During final editorial assembly:

- preserve the hierarchy of official labor statistics, employer postings, commercial or crowdsourced estimates, and union or public pay schedules;
- preserve the distinction between employee pay, contractor billing, self-employment revenue, and take-home income;
- retain the requirement to record geography, date checked, pay basis, and methodology limits;
- do not add occupation-specific wage figures to Guide 00 because it is a foundation guide rather than an occupational guide.

### Existing Section 7 — Funding, free or low-cost training, financial aid, and apprenticeship locator

Retain the existing United States, Canada, and Colombia foundation text and expand it in the following controlled order:

1. United States
2. Canada
3. Latin America overview
4. Colombia
5. Brazil
6. Mexico
7. Argentina
8. Chile

Insert the English portion of `LATIN_AMERICA_PATHWAYS_TRILINGUAL.md` after the Colombia subsection and before Section 8.

Add a concise Brazil subsection based on Batch 03 that distinguishes:

- QualificaPro and Caminho Digital free-training pathways;
- professional-apprenticeship age limits and the disability-related maximum-age exception;
- Prouni scholarships;
- Sisu as an admission route rather than a scholarship;
- FIES as repayable educational financing.

Do not duplicate long explanations already contained in Guide 00. Keep the foundation guide navigational and preserve detailed source controls in the verification records.

### Existing Section 17 — Sources, versioning, and maintenance

Add the following official starting sources to the final source list:

- Brazil Ministry of Labour and Employment professional-qualification portal
- Brazil Aprendizagem Profissional portal
- Prouni, Sisu, and FIES official services
- Mexico Jóvenes Construyendo el Futuro
- Argentina Progresar Trabajo / Formación Profesional
- ChileAtiende and SENCE

The final edition must use a last-verified date and must not describe a time-limited call as currently open without a fresh check.

## Spanish edition assembly controls

The neutral Latin American Spanish edition must be translated from the approved English structure, not assembled as an independent rewrite.

Required controls:

- preserve all 17 numbered sections and the closing section;
- preserve country-specific official names in their original language;
- use `aprendizaje remunerado`, `formación de aprendiz`, or the official country term according to context rather than forcing one regional term everywhere;
- distinguish `beca`, `subvención o ayuda no reembolsable`, `crédito educativo`, `apoyo educativo sujeto a condiciones`, and `apoyo económico para capacitación en el trabajo`;
- use `acreditación de alta calidad` only when the official record confirms that status;
- do not translate a stipend as `salario` or a completion record as a professional license;
- label the edition as machine-assisted and editorially reviewed only after the documented checks pass;
- do not claim certified translation or independent professional review.

Target filename:

`00-foundation-guide/source/Lifelong_Opportunity_Foundation_Guide_Spanish_es-419_v1.1_REVISED_MASTER.md`

## Brazilian Portuguese edition assembly controls

The Brazilian Portuguese edition must be translated from the approved English structure and reviewed against the trilingual terminology source.

Required controls:

- preserve all 17 numbered sections and the closing section;
- preserve official country-specific program names;
- use `aprendizagem profissional` for the Brazilian legal pathway and avoid applying that term inaccurately to every other country;
- distinguish `bolsa de estudos`, `auxílio não reembolsável`, `financiamento estudantil`, `apoio educacional sujeito a condições`, and `auxílio financeiro para capacitação no trabalho`;
- distinguish course-completion certificates from degrees, regulated credentials, and professional licenses;
- preserve the age limits and disability exception for Brazilian professional apprenticeship;
- do not describe Sisu as a scholarship or FIES as free aid;
- label the edition as machine-assisted and editorially reviewed only after the documented checks pass;
- do not claim certified translation or independent professional review.

Target filename:

`00-foundation-guide/source/Lifelong_Opportunity_Foundation_Guide_Portuguese_pt-BR_v1.1_REVISED_MASTER.md`

## Structural parity checklist

All three language editions must contain:

1. Title and subtitle
2. Author and mission statement
3. AI-assistance acknowledgment
4. Ethical and practical limits
5. Sections 1 through 17 in the same order
6. U.S., Canada, Latin America, Colombia, Brazil, Mexico, Argentina, and Chile pathway coverage
7. Compensation-research method
8. Funding-type distinctions
9. Employer-support safeguards
10. Accessibility and inclusion
11. Safety, privacy, and integrity controls
12. Ethical portfolio and application guidance
13. 30/60/90-day pathway
14. Required worksheet list
15. Source, versioning, and maintenance controls
16. Closing “one honest next step” section

## Link inventory for final automated and manual QA

The final assembled editions must test at least the following official domains and paths:

- `careeronestop.org`
- `apprenticeship.gov`
- `studentaid.gov`
- `rsa.ed.gov`
- `fns.usda.gov`
- `jobbank.gc.ca`
- `canada.ca`
- `red-seal.ca`
- `sena.edu.co`
- `serviciodeempleo.gov.co`
- `mineducacion.gov.co`
- `mintrabajo.gov.co`
- `icetex.gov.co` and `web.icetex.gov.co`
- `gov.br`
- `jovenesconstruyendoelfuturo.stps.gob.mx`
- `programasparaelbienestar.gob.mx`
- `argentina.gob.ar`
- `chileatiende.gob.cl`

For every failed or redirected link, record:

- source edition;
- original URL;
- HTTP or access result;
- redirect target where applicable;
- whether the destination remains authoritative;
- replacement action;
- date checked.

## DOCX and PDF publication controls

Before Guide 00 can become a publication candidate:

- generate DOCX from each approved Markdown source;
- generate searchable PDF from each approved DOCX or controlled source;
- confirm headings are represented as real heading styles;
- confirm lists are real lists rather than manually typed symbols;
- confirm URLs are clickable and visible;
- confirm tables do not overflow page margins;
- confirm Unicode punctuation and accented characters render correctly;
- confirm no page is blank, clipped, duplicated, or missing;
- inspect every rendered page visually;
- reconcile title, author, version, date, language, license, filename, and document metadata;
- create checksums for final publication files.

## Batch QA result

- Source-to-section traceability: **PASS**
- English insertion location defined: **PASS**
- Brazil integration requirements defined: **PASS**
- Spanish target structure and terminology controls: **PASS**
- Portuguese target structure and terminology controls: **PASS**
- Link inventory defined: **PASS**
- DOCX/PDF publication gate defined: **PASS**
- Independent certification claim check: **PASS — no such claim is made**

## Remaining Guide 00 work

1. Integrate the approved Latin America and Brazil text into the English master.
2. Complete the full neutral Latin American Spanish Markdown master.
3. Complete the full Brazilian Portuguese Markdown master.
4. Run structural and terminology comparison across all three editions.
5. Run live link QA.
6. Generate and inspect DOCX and searchable PDF files.
7. Reconcile metadata, versions, filenames, and checksums.
8. Keep PR #17 in draft pending publication-candidate review.
