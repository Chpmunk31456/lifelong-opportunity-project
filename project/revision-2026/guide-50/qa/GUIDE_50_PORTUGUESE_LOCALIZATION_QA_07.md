# Guide 50 — Portuguese Localization QA 07

**Guide:** 50 — Phlebotomy Technician  
**Locale:** Brazilian Portuguese (`pt-BR`)  
**Branch:** `revision/guide-00-100-2026`  
**Date:** August 19, 2026  
**Gate decision:** **PASS**

## Controlled input

Frozen English source:

`project/revision-2026/guide-50/working-masters/GUIDE_50_PHLEBOTOMY_TECHNICIAN_ENGLISH_v2.md`

Localized master:

`project/revision-2026/guide-50/working-masters/GUIDE_50_PHLEBOTOMY_TECHNICIAN_PTBR_v2.md`

## QA checks

- Occupation identity preserved: Guide 50 / Phlebotomy Technician / Técnico em Flebotomia.
- Brazilian Portuguese used consistently without presenting Brazil-specific terminology as a universal regulatory rule.
- Structural sequence preserved from the frozen English source, including scope boundaries, education pathways, safety, funding, income, AI, cybersecurity/privacy, scam avoidance, sources, and review note.
- U.S. O*NET occupation code **31-9097.00** preserved.
- Canadian occupational grouping **NOC 33101** preserved and clearly distinguished from the standalone U.S. occupation title.
- Colombia SENA pathway preserved as a **48-hour** in-person complementary course with restricted eligibility for `técnico o auxiliar en enfermería`; it is not presented as an open-entry beginner course.
- OSHA **29 CFR 1910.1030** and CDC Standard Precautions context preserved.
- Official U.S. wage controls preserved: **USD $21.75/hour**, **$45,230/year**, **$17.20 / $35,780**, **$28.26 / $58,780**, approximately **139,700** workers, **5%–6%** projected growth, approximately **18,400** annual openings, and BLS OOH May 2024 median **$43,660**.
- Supplementary Salary.com market estimate remains separately labeled as non-government: approximately **USD $41,314/year / $20/hour** as of **August 1, 2026**, with stated **$38,353–$44,694** 25th–75th percentile range.
- Canadian Job Bank wage controls preserved: **CAD $19.18**, **$27.00**, and **$36.11** per hour.
- WIOA, Registered Apprenticeship, Canada student-aid, employer support, Colombia, and Latin America training/funding pathways preserved without implying guaranteed funding or eligibility.
- Clinical-safety boundary preserved: the guide is not a venipuncture procedure manual and does not authorize independent diagnosis, interpretation of laboratory results, treatment decisions, medication changes, or work outside verified scope.
- Explicit prohibition on unsupervised venipuncture practice from written, video, or AI-generated instructions preserved.
- AI safety and protected-health-information controls preserved; AI is not presented as a substitute for approved protocols, clinical judgment, licensed supervision, specimen controls, infection control, exposure response, or emergency escalation.
- Cybersecurity/privacy controls preserved, including minimum-necessary access, credential protection, approved devices/channels, and prohibition on unapproved public AI or consumer services for protected patient data.
- Exact frozen-English source URL set retained in the Portuguese source section, including O*NET, BLS, Apprenticeship.gov, CareerOneStop, OSHA, CDC, Canadian Job Bank, Canada student aid, SENA Betowa, OIT/Cinterfor, and Salary.com.
- No claim of independent human certification, clinical certification, professional accreditation, certified translation, legal review, financial advice, or guaranteed employment outcomes was introduced.
- UTF-8 accents and punctuation reviewed; no placeholder or translation-pending marker intentionally remains.

## Decision

**Portuguese Localization Helper: PASS.**

The `pt-BR` master is suitable to advance to Trilingual Technical QA. This is internal controlled QA, not independent human or certified translation review.