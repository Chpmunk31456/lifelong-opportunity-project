# Guide 29 — Brazilian Portuguese Localization QA 07

**Gate:** Portuguese Localization Helper (`pt-BR`)  
**Date:** 2026-08-11  
**Result:** PASS

## Controlled inputs

- Frozen English source: `project/revision-2026/guide-29/publication-candidate/GUIDE_29_ENGLISH_v2.md`
- English source blob: `f7e5180058c7a8264b8204b0e1a1f8fde4de1499`
- Portuguese candidate: `project/revision-2026/guide-29/publication-candidate/GUIDE_29_PORTUGUESE_pt-BR_v2.md`
- Portuguese candidate blob: `9a53cb4d787bfed3f90732af601871f5640eaf79`

## QA checks

### 1. Structural parity — PASS

The Brazilian Portuguese candidate preserves the controlled English structure: metadata and disclaimer; numbered Sections 1–18; work scope; safety/environment/task boundaries; U.S. refrigerant requirements; entry routes; U.S. labor-market evidence; free/low-cost pathways; apprenticeship/work-based learning; Canada; Colombia; Latin America; deliberate skill building; evidence of competence; digital tools/AI/privacy/cybersecurity; 12-week plan; training-provider questions; sources; and final decision rule. The 12-week plan preserves Weeks 1–2, 3–4, 5–6, 7–8, 9–10, and 11–12.

### 2. Numerical and compensation parity — PASS

Verified preservation and labeling of material figures and dates, including: BLS 2024 employment about 425,200; May 2024 median US$59,810 / US$28.75 per hour; lower 10 percent below US$39,130; upper 10 percent above US$91,020; 8% projected growth for 2024–2034; about 40,100 annual openings; non-government Indeed estimate about US$30.38 per hour based on roughly 56,000 observations over 36 months and updated July 20, 2026; Section 127 limit US$5,250 for calendar year 2026; Canada NOC 72402 with C$22.00 low, C$37.50 median, and C$56.00 high; and SENA program duration 2,208 hours.

Official statistics remain distinct from the clearly labeled non-government estimate. No wage is presented as guaranteed.

### 3. Jurisdiction and credential boundaries — PASS

The localization preserves U.S.-specific EPA Section 608, OSHA, WIOA, IRS and Registered Apprenticeship boundaries; Canada NOC 72402, Red Seal and provincial/territorial controls; Colombia SENA/APE pathways; and the direction not to transfer one jurisdiction's licensing, refrigerant, safety, tax, apprenticeship or credential assumptions to another Latin American country.

### 4. Safety, refrigerant, and escalation controls — PASS

Hazardous-energy control, electrical and pressure hazards, refrigerant recovery/charging boundaries, combustion, work at height, confined/restricted spaces, PPE, manufacturer instructions, qualified supervision and stop-and-escalate safeguards remain explicit. The localization does not provide bypass instructions or imply that a job title or credential authorizes regulated work outside local requirements.

### 5. Funding and opportunity coverage — PASS

The Portuguese edition retains public/technical training, paid trainee routes, employer-supported training, scholarships, FAFSA/Pell, American Job Centers/WIOA, employer Section 127 educational assistance, apprenticeship verification, Canada apprenticeship/Red Seal pathways, SENA technical training and APE, and the free-first/low-debt decision rule.

### 6. AI, privacy, cybersecurity, and evidence integrity — PASS

Responsible-AI controls preserve technical verification against manufacturer and authorized sources, restrictions on using AI as authority for hazardous work, privacy protections for customer/building data, and cybersecurity restrictions for connected HVAC/building-control systems. Portfolio examples remain sanitized and do not encourage disclosure of customer, credential, network, proprietary or access information.

### 7. Link and source parity — PASS

The controlled source set is retained without changing destination URLs: BLS; EPA Section 608 certification and related refrigerant pages; OSHA 29 CFR 1910.147; Federal Student Aid FAFSA/Pell resources; U.S. DOL WIOA TEGL 07-25; Apprenticeship.gov; IRS Section 127 guidance; Government of Canada Job Bank NOC 72402; Red Seal Refrigeration and Air Conditioning Mechanic and harmonization guidance; SENA Betowa; SENA Agencia Pública de Empleo; and Indeed's HVAC Technician salary page as explicitly non-government market evidence.

### 8. Language, encoding, accessibility, and unsupported-claim control — PASS

The edition uses natural Brazilian Portuguese (`pt-BR`) and occupation-specific terminology while retaining official program, regulatory and trade names where translation could blur source identity. UTF-8 diacritics, punctuation, headings, lists and link text are intact and readable. No independent human editorial certification, professional translation certification, accessibility certification, legal review, regulatory approval, trade licensure, accreditation, guaranteed funding, guaranteed employment or guaranteed earnings is claimed.

## Gate decision

**PASS.** Guide 29 Brazilian Portuguese localization is suitable to advance to the helper manifest as complete. This gate validates controlled localization parity; it does not substitute for later trilingual technical, link, DOCX, PDF, metadata, rendering, checksum, publication, or release-audit gates.