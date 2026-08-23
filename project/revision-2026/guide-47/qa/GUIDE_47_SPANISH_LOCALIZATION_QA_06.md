# Guide 47 — Spanish Localization QA 06

**Guide:** 47 — Pharmacy Technician  
**Locale:** neutral Latin American Spanish (`es-419`)  
**Branch:** `revision/guide-00-100-2026`  
**Date:** August 18, 2026  
**Result:** **PASS**

## Controlled source

Frozen English source:

`project/revision-2026/guide-47/working-masters/GUIDE_47_PHARMACY_TECHNICIAN_ENGLISH_v2.md`

Localized master:

`project/revision-2026/guide-47/working-masters/GUIDE_47_PHARMACY_TECHNICIAN_ES419_v2.md`

The English source was already frozen under `GUIDE_47_ENGLISH_SOURCE_FREEZE_05.md`; this localization does not change the English evidence base.

## Scope and structural parity

The Spanish edition preserves the English guide's substantive sequence and safety boundaries, including:

- occupation definition and O*NET/SOC anchor;
- permitted technician-support activities as jurisdiction-dependent examples rather than universal authority;
- explicit boundaries against independent diagnosis, prescribing, therapy selection, pharmacist-only counseling, final clinical verification, unauthorized refills, or controlled-substance safeguard bypass;
- patient-identification, product-selection, barcode, discrepancy, recall, temperature, storage, and inventory escalation controls;
- nonsterile/sterile compounding boundary and explicit statement that the guide does not teach compounding or specialized preparation procedures;
- hazardous-drug, sharps, spill, exposure, PPE, infection-prevention, and emergency-reporting boundaries;
- controlled-substance security, access, inventory, audit-trail, discrepancy, witness, and diversion-prevention boundaries;
- privacy, cybersecurity, protected-information, credential, and public-AI restrictions;
- responsible-AI limitations for live pharmacy operations;
- U.S., Canada, Colombia, and Latin America education and entry pathways;
- free/low-cost learning, apprenticeships/work-based learning, funding, and employer-support sections;
- official versus non-government income labeling;
- starter plan, transferable experience, advancement, scam warnings, spending pause conditions, current sources, and assurance boundary.

No Spanish text expands the legal or clinical scope beyond the frozen English source.

## Controlled numeric and classification parity

Verified retained values and classifications include:

- O*NET/SOC **29-2052.00**;
- Canada **NOC 32124**;
- Colombia **CNO 3315**;
- SENA Servicios Farmacéuticos **2,640 / 2.640 hours** and minimum age **16+**;
- U.S. official wage values **USD $22.00/hour** and **USD $45,750 / $45.750 annual**;
- U.S. employment **490,400 / 490.400 workers in 2024**, **6 percent** projected growth for **2024–2034**, and approximately **49,000 / 49.000 annual openings**;
- Indeed non-government estimate **USD $21.13/hour**, low **$14.84**, high **$30.07**, updated **July 27, 2026 / 27 de julio de 2026**;
- Canada official wages **CAD $17.50**, **$24.83**, and **$34.20 per hour**, with the November 19, 2025 update date retained;
- research/review date **August 18, 2026 / 18 de agosto de 2026**.

Spanish punctuation conventions do not change the underlying values.

## Source URL parity

The Spanish `## Fuentes actuales` section preserves the exact frozen English URL set, including all official/public sources and the supplementary Indeed salary source. Controlled URLs preserved include O*NET summary/wages/trends, BLS, CareerOneStop licensing/certification/WIOA locators, Apprenticeship.gov, Federal Student Aid, three Government of Canada Job Bank pages, Canada Student Grants and Loans, SENA Observatorio, SENA Betowa, the Colombian pharmaceutical-service regulatory compilation, both OIT/Cinterfor links, and Indeed.

No substitute, shortened, translated, or alternate endpoint was introduced.

## Terminology and language QA

The localization uses neutral Latin American Spanish and retains named programs or foreign credential titles when translating them could create regulatory ambiguity. Terms such as `Registered Apprenticeship`, `Pharmacy Examining Board of Canada (PEBC)`, `NOC`, `CNO`, `SENA`, `WIOA`, `FAFSA`, and official English source titles remain identifiable.

Medication-safety wording is conservative. The edition consistently uses escalation to the pharmacist or authorized clinician rather than implying independent clinical judgment.

## Accessibility, encoding, and readability

- UTF-8 Spanish accents and punctuation are used directly; no mojibake or replacement-character placeholders were introduced.
- Headings and list structure remain Markdown-readable and compatible with downstream DOCX/PDF generation.
- Acronyms are introduced in context where practical.
- Long regulatory concepts are split into readable paragraphs and lists rather than dense blocks.
- No `TODO`, untranslated placeholder, lorem ipsum, or translation-pending marker remains.

## Assurance boundary

The localized closing note explicitly states that the controlled revision **does not claim** independent human certification, professional pharmacy or medical review, legal/regulatory review, professional certified translation, accessibility certification, accreditation, guaranteed licensing/registration, guaranteed funding, guaranteed employment, or guaranteed earnings.

This QA record is an internal controlled localization review. It is not professional translation certification, pharmacy/medical review, regulatory approval, accreditation, or independent human certification.

## Decision

**Spanish Localization Helper: PASS.**

Guide 47 may advance to Brazilian Portuguese (`pt-BR`) localization. Downstream Technical QA remains fail-closed and must independently validate trilingual structure, terminology, URLs, controlled values, DOCX/PDF artifacts, rendering, metadata, and checksums before publication.
