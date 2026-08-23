# Guide 96 — Spanish Localization QA

## Locale
Neutral Latin American Spanish (`es-419`)

## QA date
2026-08-22

## Frozen English source
`GUIDE_96_ELECTRICAL_AND_ELECTRONIC_ENGINEERING_TECHNICIAN_ENGLISH_v2.md`

Frozen English blob:
`8a29c6130e2e38327e2faaadc12d2b3fdc28281e`

## Spanish master
`project/revision-2026/guide-96/working-masters/GUIDE_96_TECNICO_EN_INGENIERIA_ELECTRICA_Y_ELECTRONICA_ES419_v2.md`

Spanish blob:
`7a4d943acd8e6406cca659d791ee3c555a3bc319`

## Localization checks

### Structure — PASS
- Full reader-facing guide retained rather than a summary.
- Major section sequence preserves the English learning flow.
- Six-step action plan and four-week schedule retained.
- Lists/checklists remain accessible and readable.

### Occupation identifiers — PASS
- O*NET-SOC 17-3023.00 retained.
- Canada NOC 22310 retained.
- Colombia CUOC 31141 retained.
- Colombia title rendered naturally as `Técnicos en electrónica`.

### U.S. controlled values — PASS
2025 O*NET/BLS values retained exactly:
- $49,510 / $23.80;
- $61,610 / $29.62;
- $78,190 / $37.59;
- $97,650 / $46.95;
- $115,700 / $55.62.

BLS OOH context retained separately:
- $77,180 median, May 2024;
- 1% growth 2024–2034;
- about 8,400 openings/year;
- associate degree typical entry education.

### Canada values — PASS
- C$24.04 low;
- C$35.58 median;
- C$55.34 high;
- technologist versus technician program-duration distinction retained;
- provincial certification/title caveat retained.

### Colombia/SENA values — PASS
- CUOC 31141 competence-level context retained.
- `Mantenimiento electrónico e instrumental industrial` retained as a Tecnólogo pathway.
- Current reviewed SENA duration retained as **24 months**.
- 11th-grade/selection and live-cohort caveats retained.
- `Electrónica básica` remains explicitly complementary only.

### Brazil/Peru/regional pathways — PASS
- OIT/Cinterfor locator retained.
- SENAI Técnico em Eletrônica retained at **1,200 hours**.
- SENATI remains a current-program locator with no unsupported current-seat guarantee.

### Current non-government market context — PASS
- Electrical Technician: about $30.67/hour, ~9,000 observations, updated 2026-08-10.
- Electronics Technician: about $27.58/hour, ~8,400 observations, updated 2026-08-09.
- Colombia Técnico/a electrónico/a: about COP 1,711,841/month, 187 observations, updated 2026-07-31.
- All remain clearly labeled non-government estimates.

### Electrical-safety semantics — PASS
Spanish text preserves:
- deenergization-first rule;
- lockout/tagout awareness;
- stored-energy/capacitor awareness;
- qualified-person verification boundary;
- qualified-person test-work boundary;
- test-equipment inspection/rating concept;
- prohibition on treating the guide as permission for live mains/industrial-panel probing.

No unsafe operational detail was introduced in translation.

### Professional-scope semantics — PASS
The translation preserves distinctions among technician support, licensed engineering, electrician/installation authority, inspection/certification authority, calibration authority and qualified-person electrical testing.

### Cybersecurity and AI — PASS
- Password/MFA/update/phishing/change-control concepts retained.
- AI remains limited to low-risk assistance.
- AI is explicitly not measurement, calibration, protection-setting, engineering-approval or energized-work authority.

### Accessibility — PASS
Neutral, readable Spanish is used; checklists, milestones, simulation/deenergized-learning alternatives and essential-safety boundaries remain intact.

### Source parity — PASS
All 23 reader-verification URLs from the frozen English master are preserved in the Spanish edition.

### Claims/disclaimers — PASS
No independent human certification, certified translation, accreditation, legal review, licensed-engineering review, electrical-safety certification, accessibility certification or outcome guarantee is claimed.

## QA result
**PASS — Spanish Localization (`es-419`)**

The Spanish master is eligible for trilingual parity once Portuguese localization passes.
