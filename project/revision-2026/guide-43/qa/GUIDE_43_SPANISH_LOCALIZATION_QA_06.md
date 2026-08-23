# Guide 43 — Spanish Localization QA 06

**Guide:** 43 — Solar Photovoltaic Installer  
**Language:** neutral Latin American Spanish (`es-419`)  
**Branch:** `revision/guide-00-100-2026`  
**Date:** 2026-08-16  
**Result:** PASS

## Controlled inputs

- Frozen English source: `project/revision-2026/guide-43/working-masters/GUIDE_43_SOLAR_PHOTOVOLTAIC_INSTALLER_ENGLISH_v2.md`
- Spanish master: `project/revision-2026/guide-43/working-masters/GUIDE_43_SOLAR_PHOTOVOLTAIC_INSTALLER_ES419_v2.md`
- English source freeze evidence: `project/revision-2026/guide-43/qa/GUIDE_43_ENGLISH_SOURCE_FREEZE_05.md`

## Localization controls reviewed

1. **Structure:** All substantive English sections are represented in the Spanish edition in the same sequence, including occupation scope, permitted work, work environment, safety, falls/roof access, energized-PV boundaries, skills, U.S./Canada/Colombia/LATAM pathways, free-first learning, apprenticeships, funding, compensation, 12-week plan, transferable experience, advancement, AI, cybersecurity/privacy, scam controls, spending pause, sources, and limitations.
2. **Occupation and regulated-work boundary:** The Spanish text preserves the distinction between mechanical module/racking installation and regulated electrical design, connection, commissioning, energization, inspection, interconnection, engineering, and licensed/qualified-person work. No universal electrical authorization is implied.
3. **Safety:** Stop-work and escalation language remains explicit for electrical state, supervision, training/scope, roof integrity, fall protection, weather, damaged components, mismatched drawings/ratings, permits/inspection/utility authorization, and production pressure. The illuminated-module hazard and disconnect/isolation caution are preserved.
4. **Controlled numerics and dates:** SOC `47-2231`; NOC `73200`; Construction Electrician NOC `72200`; SENA `2,200 hours` and `96 hours`; OSHA `29 CFR 1926.501`, `6 feet (1.8 m)`; BLS `$51,860`, `$24.93`, `$39,070`, `$80,150`, `28,600`, `40,600`, `42% (12,000 jobs)`, `4,100`; Indeed `$26.12`, `$16.37`, `$41.68`, approximately `2,900`, `36 months`, `$7,500`, July 17, 2026; Canada `CAD $18.65`, `CAD $26.00`, `CAD $40.00`, November 19, 2025; and the `12-week` plan are preserved without conversion or reinterpretation.
5. **Official vs non-government compensation:** BLS and Government of Canada Job Bank remain identified as official/public sources. Indeed remains explicitly labeled a non-government market supplement and is not presented as guaranteed pay.
6. **Source URLs:** The complete controlled source URL set from the frozen English master is retained unchanged in the Spanish source section, including BLS, O*NET, OSHA, Apprenticeship.gov, Federal Student Aid, DOL/WIOA, Canada Job Bank, Red Seal, both SENA/Betowa entries, Colombia Ministry RETIE, both OIT/Cinterfor entries, and Indeed.
7. **Colombia/RETIE qualifier:** The Spanish edition preserves the English source's cautious handling of the Ministry page's inconsistent year information for Resolution 40284 and does not invent or resolve the disputed year.
8. **AI/privacy/cybersecurity:** AI is limited to non-authoritative support and cannot replace site, structural, electrical, code, fall-protection, isolation, commissioning, inspection, interconnection, manufacturer, or authorized-person decisions. Customer/site/utility/credential data protections are retained.
9. **Assurance boundaries:** The edition does not claim independent human certification, professional translation certification, accessibility certification, legal review, engineering approval, electrical-code approval, licensing determination, accreditation, guaranteed employment, or guaranteed earnings.
10. **Language quality:** Spanish is neutral Latin American Spanish, uses natural reader-facing phrasing, and avoids region-specific legal assumptions beyond explicitly named jurisdictional material. English proper names, occupational codes, program names, and official source labels are retained where translation could reduce traceability.
11. **Encoding/placeholders:** UTF-8 text is used; no intentional placeholder, TODO, or unsupported certification marker was introduced.

## Disposition

**Spanish Localization: PASS.** The controlled `es-419` master may be used as an input to Portuguese localization and later trilingual Technical QA.

This QA record is internal controlled evidence. It does not constitute independent human translation certification, legal review, electrical or engineering approval, accessibility certification, licensing determination, accreditation, or a guarantee of employment or earnings.