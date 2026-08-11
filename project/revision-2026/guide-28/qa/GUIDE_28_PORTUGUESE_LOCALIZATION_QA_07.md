# Guide 28 — Brazilian Portuguese Localization QA 07

**Gate:** Portuguese Localization Helper (`pt-BR`)  
**Date:** 2026-08-11  
**Result:** PASS

## Controlled inputs

- Frozen English source: `project/revision-2026/guide-28/publication-candidate/GUIDE_28_ENGLISH_v2.md`
- English source blob: `f1dad00b99ff639f8e70928f47896cfa5d723c35`
- Portuguese candidate: `project/revision-2026/guide-28/publication-candidate/GUIDE_28_PORTUGUESE_pt-BR_v2.md`
- Portuguese candidate blob: `eacf86a85fa99006359aa1aab656a73e2688cfc0`

## QA checks

### 1. Structural parity — PASS

The Brazilian Portuguese candidate preserves the controlled English structure: metadata and disclaimer; numbered Sections 1–18; hazardous-energy, machine-guarding, lifting/rigging, electrical/pressure, U.S. funding, Canada, Colombia, Latin America, AI, accessibility, 90-day plan, training-provider questions, employer questions, advancement, pause/reconsider, sources, and final decision rule. The 90-day plan preserves Days 1–15, 16–30, 31–60, and 61–90.

### 2. Numerical and compensation parity — PASS

Verified preservation and labeling of material figures and dates, including: 2024 employment about 538,300; May 2024 combined median US$63,510 / US$30.53 per hour; US$63,760 industrial machinery mechanics; US$60,500 machinery maintenance workers; US$65,170 millwrights; lower 10 percent below US$44,430; upper 10 percent above US$91,620; 13% projected growth for 2024–2034; about 54,200 annual openings; non-government Indeed estimate about US$30.05 per hour, approximately 5.8 thousand observations over 36 months, updated July 13, 2026; Section 127 limit US$5,250 for calendar year 2026; Canada NOC 72400 and C$37.00/hour; SENA duration 3,984 hours; 20–30 posting review; and revision/source-check date August 11, 2026.

Official statistics remain distinct from the clearly labeled non-government market estimate. No salary is presented as guaranteed.

### 3. Jurisdiction and credential boundaries — PASS

The localization preserves U.S.-specific OSHA/WIOA/IRS/Registered Apprenticeship scope, Canada NOC/Red Seal and provincial-territorial qualification boundaries, Colombia SENA/APE and CONTE-related caution, and the instruction not to transfer one jurisdiction's legal or credential assumptions to another Latin American country.

### 4. Safety terminology and escalation controls — PASS

Hazardous-energy control, `bloqueio/etiquetagem (lockout/tagout)`, machine guarding, lifting/rigging, confined-space, electrical, pressure-system, qualification/authorization, stop-and-escalate, and production-pressure safeguards remain explicit. The text does not provide bypass instructions or imply that a job title grants regulated authority.

### 5. Funding and opportunity coverage — PASS

The Portuguese edition retains paid apprenticeship, public/community-college or technical training, WIOA/American Job Center support, employer educational assistance, scholarships/grants, supportive services, Canada apprenticeship support, SENA pathways, APE vacancy-search terms, and the low-debt decision rule.

### 6. AI, privacy, accessibility, and evidence integrity — PASS

Responsible-AI controls preserve restrictions on confidential, customer, credential, proprietary, export-controlled, and sensitive machine information; technical verification against approved sources; human accountability; and prohibition on allowing AI to override safety requirements. Accessibility supports and the essential-safety-requirement boundary are preserved.

### 7. Link and source parity — PASS

The controlled source set is retained without changing destination URLs:

1. BLS Occupational Outlook Handbook.
2. Apprenticeship.gov career-seeker resources.
3. U.S. DOL WIOA TEGL 07-25.
4. IRS Section 127 guidance.
5. OSHA 29 CFR 1910.147.
6. OSHA lockout/tagout tutorial.
7. Government of Canada Job Bank NOC 72400.
8. Red Seal Industrial Mechanic (Millwright).
9. Government of Canada Apprenticeship Service.
10. SENA Betowa — Mantenimiento Mecánico Industrial.
11. SENA Agencia Pública de Empleo.
12. Indeed Industrial Mechanic salary page, explicitly separated as non-government market-pay evidence.

### 8. Language, encoding, and claims — PASS

The edition uses Brazilian Portuguese (`pt-BR`) with occupation-specific terminology while retaining official program/trade names where translation could blur legal or source identity. UTF-8 Portuguese diacritics and punctuation are intact. No independent human editorial certification, professional translation certification, accessibility certification, legal review, trade-licensing approval, accreditation, employment guarantee, or other unsupported certification is claimed.

## Gate decision

**PASS.** The Guide 28 Brazilian Portuguese localization is suitable to advance to the helper manifest as complete. This gate validates controlled localization parity; it does not substitute for later trilingual technical, link, DOCX, PDF, metadata, rendering, checksum, publication, or release-audit gates.