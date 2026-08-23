# Guide 47 — Portuguese Localization QA 07

**Guide:** 47 — Pharmacy Technician  
**Locale:** Brazilian Portuguese (`pt-BR`)  
**Branch:** `revision/guide-00-100-2026`  
**Date:** August 18, 2026  
**Result:** **PASS**

## Controlled source

Frozen English source:

`project/revision-2026/guide-47/working-masters/GUIDE_47_PHARMACY_TECHNICIAN_ENGLISH_v2.md`

Localized master:

`project/revision-2026/guide-47/working-masters/GUIDE_47_PHARMACY_TECHNICIAN_PTBR_v2.md`

The frozen English evidence base is unchanged.

## Scope and structural parity

The `pt-BR` edition preserves the full controlled guide sequence and the English safety/regulatory boundaries, including:

- occupation definition and O*NET/SOC anchor;
- jurisdiction-dependent technician support activities rather than universal authority;
- explicit prohibition on independent diagnosis, prescribing, therapy selection, medication/dose changes, pharmacist-only counseling, final clinical verification, unauthorized refills, controlled-substance safeguard bypass, or concealment of medication errors;
- patient-identification, barcode, product-selection, discrepancy, storage, recall, temperature, and inventory controls;
- nonsterile/sterile compounding and advanced-preparation boundaries without procedural instruction;
- hazardous-drug, sharps, exposure, spill, PPE, infection-prevention, and emergency-reporting boundaries;
- controlled-substance security, access, inventory, audit, witness, discrepancy, and diversion-prevention controls;
- privacy, cybersecurity, credential, protected-information, and public-AI restrictions;
- responsible-AI limits for live pharmacy decisions and records;
- U.S., Canada, Colombia, and Latin America education and entry pathways;
- free/low-cost learning, apprenticeship/work-based learning, funding, and employer support;
- official versus non-government wage labeling;
- practical starter plan, transferable experience, advancement, scam warnings, spending pause conditions, source list, and assurance boundary.

No Portuguese wording expands legal, clinical, dispensing, compounding, vaccination, or controlled-substance authority beyond the frozen English source.

## Controlled numeric and classification parity

Verified retained controlled values include:

- O*NET/SOC **29-2052.00**;
- Canada **NOC 32124**;
- Colombia **CNO 3315**;
- SENA Servicios Farmacéuticos **2,640 / 2.640 hours** and minimum age **16+**;
- U.S. official wages **USD $22.00/hour** and **USD $45,750 / $45.750 annual**;
- approximately **490,400 / 490.400 workers in 2024**, **6 percent** growth for **2024–2034**, and approximately **49,000 / 49.000 annual openings**;
- Indeed non-government estimate **USD $21.13/hour**, low **$14.84**, high **$30.07**, updated **July 27, 2026 / 27 de julho de 2026**;
- Canada official wages **CAD $17.50**, **$24.83**, and **$34.20 per hour**, with the November 19, 2025 update date preserved;
- research/review date **August 18, 2026 / 18 de agosto de 2026**.

Portuguese punctuation conventions do not alter the underlying controlled values.

## Source URL parity

The Portuguese `## Fontes atuais` section preserves the exact frozen English URL set. It includes the O*NET summary/wages/trends pages, BLS Pharmacy Technicians page, CareerOneStop licensing/certification/WIOA locators, Apprenticeship.gov, Federal Student Aid FAFSA guidance, three Government of Canada Job Bank pages, Canada Student Grants and Loans, SENA Observatorio, SENA Betowa, the Colombian pharmaceutical-service regulatory compilation, both OIT/Cinterfor links, and the supplementary Indeed salary page.

No localized substitute, alternate endpoint, shortened URL, or additional unsupported salary source was introduced.

## Terminology and language QA

The edition uses Brazilian Portuguese while retaining named foreign credentials and program titles where translation could imply a different regulatory status. `Registered Apprenticeship`, `Pharmacy Examining Board of Canada (PEBC)`, `NOC`, `CNO`, `SENA`, `WIOA`, `FAFSA`, and official source names remain identifiable.

Clinical and regulatory language remains conservative. Questions involving safety, interactions, dosing, side effects, therapy selection, final verification, or other clinical judgment are routed to the pharmacist or another authorized clinician rather than assigned to the technician.

## Accessibility, encoding, and readability

- UTF-8 Portuguese accents are used directly with no mojibake or replacement-character placeholders.
- Markdown heading and list hierarchy remains compatible with downstream DOCX/PDF generation.
- Regulatory terms are explained in context without implying Brazilian recognition of foreign credentials.
- No `TODO`, lorem ipsum, untranslated placeholder, or translation-pending marker remains.

## Assurance boundary

The closing note explicitly states that the controlled revision **does not claim** independent human certification, professional pharmacy or medical review, legal/regulatory review, professional certified translation, accessibility certification, accreditation, guaranteed licensing/registration, guaranteed funding, guaranteed employment, or guaranteed income.

This QA record is internal controlled localization evidence. It is not professional translation certification, pharmacy/medical review, regulator approval, accreditation, or independent human certification.

## Decision

**Portuguese Localization Helper: PASS.**

Guide 47 may advance to Trilingual Technical QA. That gate remains fail-closed and must independently validate trilingual structure, terminology, source URLs, controlled values, links, DOCX/PDF integrity, rendering, metadata, and checksums before publication.
