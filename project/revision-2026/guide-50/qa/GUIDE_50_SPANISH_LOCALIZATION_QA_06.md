# Guide 50 — Spanish Localization QA 06

**Guide:** 50 — Phlebotomy Technician  
**Locale:** neutral Latin American Spanish (`es-419`)  
**Branch:** `revision/guide-00-100-2026`  
**Date:** August 19, 2026  
**Gate decision:** **PASS**

## Controlled input

Frozen English source:

`project/revision-2026/guide-50/working-masters/GUIDE_50_PHLEBOTOMY_TECHNICIAN_ENGLISH_v2.md`

Localized master:

`project/revision-2026/guide-50/working-masters/GUIDE_50_PHLEBOTOMY_TECHNICIAN_ES419_v2.md`

## QA checks

- Occupation identity preserved: Guide 50 / Phlebotomy Technician / técnico en flebotomía.
- Neutral Latin American Spanish used; no country-specific Spanish is presented as universally applicable.
- Structural sequence preserved from the frozen English source, including scope boundaries, education pathways, safety, funding, income, AI, cybersecurity/privacy, scam avoidance, current sources, and review note.
- U.S. O*NET occupation code **31-9097.00** preserved.
- Canadian grouping **NOC 33101** preserved and clearly described as broader than the standalone U.S. title.
- Colombia SENA pathway preserved as a **48-hour** in-person complementary course with restricted eligibility for `técnico o auxiliar en enfermería`; it is not represented as an open-entry beginner course.
- OSHA **29 CFR 1910.1030** and CDC Standard Precautions safety context preserved.
- Official U.S. wage controls preserved: **USD $21.75/hour**, **$45,230/year**, **$17.20 / $35,780**, **$28.26 / $58,780**, approximately **139,700** workers, **5%–6%** projected growth, approximately **18,400** annual openings, and BLS OOH May 2024 median **$43,660**.
- Supplementary non-government Salary.com estimate remains explicitly separated and labeled: approximately **USD $41,314/year / $20/hour** as of **August 1, 2026**, with **$38,353–$44,694** stated 25th–75th percentile range.
- Canadian Job Bank wage controls preserved: **CAD $19.18**, **$27.00**, and **$36.11** per hour.
- WIOA, Registered Apprenticeship, Canada student-aid, employer support, Colombia, and Latin America training/funding pathways preserved without implying guaranteed eligibility or funding.
- Clinical-safety boundary preserved: the guide is not a venipuncture procedure manual and does not authorize independent diagnosis, laboratory-result interpretation, treatment decisions, medication changes, or practice outside verified scope.
- Explicit prohibition on unsupervised venipuncture practice from written, video, or AI-generated instructions preserved.
- AI safety and protected-health-information controls preserved; AI is not presented as a replacement for approved protocols, clinical judgment, licensed supervision, specimen controls, infection-control rules, exposure response, or emergency escalation.
- Cybersecurity/privacy controls preserved, including minimum-necessary access, credential protection, approved devices/channels, and prohibition on unapproved public AI or consumer services for protected patient data.
- Exact source URL set from the frozen English source was retained in the Spanish source section, including O*NET, BLS, Apprenticeship.gov, CareerOneStop, OSHA, CDC, Canadian Job Bank, Canada student aid, SENA Betowa, OIT/Cinterfor, and Salary.com.
- No claim of independent human certification, clinical certification, professional accreditation, certified translation, legal review, financial advice, or guaranteed employment outcomes was introduced.
- UTF-8 accents and punctuation reviewed; no placeholder or translation-pending marker intentionally remains.

## Decision

**Spanish Localization Helper: PASS.**

The `es-419` master is suitable to advance to the Brazilian Portuguese localization gate. This is internal controlled QA, not independent human or certified translation review.