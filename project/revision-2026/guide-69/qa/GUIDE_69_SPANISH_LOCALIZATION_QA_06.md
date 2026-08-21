# Guide 69 — Spanish Localization QA 06

**Guide:** 69 — Hotel Front Desk and Guest Services  
**Locale:** es-419 — neutral Latin American Spanish  
**Date:** 2026-08-21  
**Source:** `project/revision-2026/guide-69/working-masters/GUIDE_69_HOTEL_FRONT_DESK_AND_GUEST_SERVICES_ENGLISH_v2.md`  
**Frozen English blob:** `a75e6e8015fcd4afb4bdefc9f52264d4ffb0ad3a`  
**Spanish master:** `project/revision-2026/guide-69/working-masters/GUIDE_69_RECEPCION_DE_HOTEL_Y_SERVICIOS_AL_HUESPED_ES419_v2.md`

## Controlled review

The Spanish edition was localized only after the English source-freeze gate passed. The localization preserves the occupational scope and deliberately does not expand delegated authority.

Checks completed:

- PASS — neutral Latin American Spanish used; Colombia-specific SENA program names remain as official source titles.
- PASS — O*NET-SOC `43-4081.00`, Canada NOC `64314`, TEER 4, and the Hotel Associate Registered Apprenticeship reference are preserved.
- PASS — United States, Canada, Colombia, and Latin America/Caribbean pathways remain present.
- PASS — free-first training, WIOA, American Job Centers, employer-supported development, apprenticeship, funding, and scholarship discovery language remains qualified and non-guaranteed.
- PASS — SENA program durations remain `2,208` hours and `3,984` hours in the underlying controlled values; Spanish typography renders these as `2.208` and `3.984` hours without changing the quantities.
- PASS — BLS/O*NET U.S. controlled wage values are preserved: employment `261,420`; mean hourly `USD $17.09`; mean annual `USD $35,550`; median hourly `USD $16.86`; median annual `USD $35,070`; annual 10th/90th percentiles `USD $27,120` / `USD $45,470`; hourly 10th/90th percentiles `USD $13.04` / `USD $21.86`.
- PASS — Salary.com is explicitly labeled a current **non-government market estimate**, preserving `USD $34,841`, approximately `$17/hour`, and the stated `$32,261–$37,181` 25th-to-75th percentile range.
- PASS — Canada Job Bank controlled values remain `CAD $15.00`, `CAD $18.00`, and `CAD $26.50` per hour.
- PASS — privacy, guest-location confidentiality, identity verification, replacement-key controls, payment security, fraud/social-engineering controls, least privilege, password/MFA boundaries, and incident escalation remain explicit.
- PASS — responsible-AI restrictions preserve the prohibition on placing payment-card data, identity data, credentials, room/access data, confidential reservations, incident reports, employee data, surveillance data, and internal hotel information into unauthorized public AI systems.
- PASS — human review remains required for AI-assisted guest communications, translations, recommendations, itineraries, schedules, training material, summaries, and operational suggestions.
- PASS — accessibility language avoids claiming legal expertise or accessibility certification and requires verification before promising accessibility.
- PASS — night-audit boundaries do not convert the role into professional accounting authority.
- PASS — the assurance boundary continues to deny guarantees of employment, income, admission, funding, apprenticeship placement, promotion, licensing, certification, legal compliance, or other outcomes.
- PASS — no claim of independent human certification, professional hospitality certification, professional translation certification, legal review, accessibility certification, accreditation, financial advice, or security certification was introduced.
- PASS — the 13-item controlled source set is preserved textually, including the 12 official/public-sector sources and the separately labeled Salary.com market source.

## Link and source handling

This localization gate verifies preservation of the frozen source URLs and claim-to-source relationships. It does not claim a fresh independent live-link crawl. Live link behavior, generated DOCX/PDF hyperlinks, metadata, rendering, and publication artifacts remain subject to the later Technical QA and Publication gates.

## Result

**SPANISH LOCALIZATION: PASS**

The es-419 master is eligible to become the predecessor for Brazilian Portuguese localization. This is controlled machine-assisted localization and editorial QA under the author's direction; it is not professional translation certification or independent human linguistic certification.
