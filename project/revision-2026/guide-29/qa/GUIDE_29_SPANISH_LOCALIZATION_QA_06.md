# Guide 29 — Spanish Localization QA 06

**Gate:** Spanish Localization Helper (`es-419`)  
**Date:** 2026-08-11  
**Result:** PASS

## Controlled inputs

- Frozen English source: `project/revision-2026/guide-29/publication-candidate/GUIDE_29_ENGLISH_v2.md`
- English source blob: `f7e5180058c7a8264b8204b0e1a1f8fde4de1499`
- Spanish candidate: `project/revision-2026/guide-29/publication-candidate/GUIDE_29_SPANISH_es-419_v2.md`
- Spanish candidate blob: `25390d06bdf24f0643230517f724bb158007518f`

## QA checks

### 1. Structural parity — PASS

The Spanish candidate preserves the controlled English structure: metadata and educational disclaimer; numbered Sections 1–18; occupation overview; task boundaries; hazardous-energy, electrical, pressure, refrigerant, combustion, working-at-height, and confined-space controls; U.S. Section 608 requirements; entry routes; labor-market evidence; free/low-cost pathways; apprenticeship verification; Canada; Colombia; Latin America; skills; evidence of competence; AI/privacy/cybersecurity; 12-week plan; training-provider questions; source list; final decision rule; authorship statement; and licensing statement.

### 2. Numerical and compensation parity — PASS

Verified preservation and localization of material figures and dates, including: 2024 employment about 425,200; May 2024 median pay US$59,810/year and US$28.75/hour; lower 10 percent below US$39,130; upper 10 percent above US$91,020; 8% projected growth for 2024–2034; about 40,100 annual openings; programs of approximately 6 months to 2 years; non-government Indeed estimate about US$30.38/hour based on roughly 56,000 observations over 36 months and updated July 20, 2026; Section 127 limit US$5,250 for calendar year 2026; Canada NOC 72402 wages C$22.00/C$37.50/C$56.00 per hour; SENA duration 2,208 hours; and revision date August 11, 2026.

Official statistics remain distinct from the clearly labeled non-government market estimate. No salary is presented as guaranteed.

### 3. Refrigerant, jurisdiction, and credential boundaries — PASS

The localization preserves EPA Section 608 certification scope and explicitly states that it does not replace state/local contractor, trade, business, electrical, gas, permit, or employer authorization requirements. It also preserves U.S.-specific OSHA/WIOA/IRS/Apprenticeship.gov boundaries, Canada NOC/Red Seal and provincial-territorial controls, Colombia SENA/APE pathways, and the instruction not to transfer one country's licensing, tax, environmental, safety, or credential assumptions to another Latin American jurisdiction.

### 4. Safety terminology and escalation controls — PASS

Hazardous-energy control, bloqueo/etiquetado context, electrical hazards, pressure, refrigerant handling, combustion, work at height, confined/restricted spaces, PPE/EPP, authorized scope, stop-and-escalate criteria, and anti-bypass safeguards remain explicit. The Spanish text does not imply that a job title, course, apprenticeship label, or certification grants broader regulated authority than the source supports.

### 5. Funding and opportunity coverage — PASS

The Spanish edition retains public technical/community-college routes, paid helper/trainee roles, employer-supported learning, union/association options, FAFSA/Pell, scholarships, American Job Centers/WIOA, supportive services, Section 127 employer educational assistance, apprenticeship verification, Canada apprenticeship/Red Seal pathways, Colombia SENA Betowa and APE, and the low-cost-first decision rule.

### 6. AI, privacy, cybersecurity, accessibility, and evidence integrity — PASS

The localization preserves AI as a secondary support tool rather than an authority for hazardous work; prohibitions on relying on AI for refrigerant identity, electrical/combustion safety, pressure limits, lockout/tagout, code compliance, charging, leak repair, legal scope, or bypass decisions; confidentiality controls for customer/building/network information; and cybersecurity escalation to responsible IT/OT/facilities/controls personnel. The text retains clear, scannable headings, short paragraphs, lists, explicit cautions, and plain-language escalation instructions. Portfolio examples preserve privacy and truthful-credential boundaries.

### 7. Link and source parity — PASS

The controlled source set is retained without changing destination URLs:

1. U.S. Bureau of Labor Statistics Occupational Outlook Handbook.
2. EPA Section 608 Technician Certification Requirements.
3. EPA Section 608 hub.
4. EPA Refrigerant Sales Restriction.
5. EPA Refrigerant Recovery and Recycling Equipment Certification.
6. OSHA 29 CFR 1910.147.
7. Federal Student Aid FAFSA information.
8. Federal Student Aid Pell information.
9. U.S. Department of Labor WIOA TEGL 07-25.
10. Apprenticeship.gov.
11. IRS Section 127 educational-assistance update dated April 20, 2026.
12. Government of Canada Job Bank NOC 72402 wage report.
13. Red Seal Refrigeration and Air Conditioning Mechanic.
14. Red Seal apprenticeship harmonization.
15. SENA Betowa — Mantenimiento de equipos de aire acondicionado y refrigeración.
16. SENA Agencia Pública de Empleo.
17. Indeed HVAC Technician salary page, explicitly separated as non-government market-pay evidence.

### 8. Language, encoding, and claims — PASS

The edition uses neutral Latin American Spanish (`es-419`) with HVAC/R terminology understandable across the region while retaining official program, agency, credential, trade, and regulatory names where translation could blur source identity. UTF-8 Spanish diacritics and punctuation are intact. Colombia-specific terminology is confined to the Colombia pathway. No independent human editorial certification, professional translation certification, accessibility certification, legal review, environmental-regulatory approval, trade-licensing approval, accreditation, funding guarantee, employment guarantee, or earnings guarantee is claimed.

## Gate decision

**PASS.** The Guide 29 Spanish localization is suitable to advance to the helper manifest as complete. This gate validates controlled localization parity; it does not substitute for later Brazilian Portuguese localization, trilingual technical/link QA, DOCX/PDF generation and inspection, metadata, rendering, checksum, publication, or release-audit gates.