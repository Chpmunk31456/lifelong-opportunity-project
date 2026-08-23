# Guide 69 — Trilingual Technical QA 08

**Guide:** 69 — Hotel Front Desk and Guest Services  
**Date:** 2026-08-21  
**Result:** PASS

## Frozen source set

- English: `GUIDE_69_HOTEL_FRONT_DESK_AND_GUEST_SERVICES_ENGLISH_v2.md` — blob `a75e6e8015fcd4afb4bdefc9f52264d4ffb0ad3a`
- Spanish es-419: `GUIDE_69_RECEPCION_DE_HOTEL_Y_SERVICIOS_AL_HUESPED_ES419_v2.md` — blob `af25143c35d230ab84617ef6954a6e6b0fb823bd`
- Portuguese pt-BR: `GUIDE_69_RECEPCAO_DE_HOTEL_E_SERVICOS_AO_HOSPEDE_PTBR_v2.md` — blob `604c732bc4e0e9486df365f2ab9c1c0a94652007`

## Technical parity checks

- All three editions identify O*NET-SOC `43-4081.00` as the U.S. occupational benchmark and NOC `64314` as the Canada comparison.
- All three editions preserve the same 13 controlled current-source URLs.
- The official BLS May 2025 benchmark is semantically identical across locales: employment `261,420`; mean hourly `USD $17.09`; mean annual `USD $35,550`; median hourly `USD $16.86`. Locale-specific thousands/decimal punctuation does not alter the underlying values.
- The O*NET/BLS distribution is preserved: median annual `USD $35,070`; annual 10th/90th percentiles `USD $27,120` / `USD $45,470`; hourly 10th/90th percentiles `USD $13.04` / `USD $21.86`.
- Salary.com remains clearly labeled as a current **non-government market estimate** in all three editions and preserves the August 1, 2026 values.
- Canada Job Bank low/median/high values remain `CAD $15.00`, `$18.00`, and `$26.50` per hour.
- SENA durations remain `2,208` hours for `SERVICIO DE RECEPCION HOTELERA` Técnico and `3,984` hours for `COORDINACION DE SERVICIOS HOTELEROS` Tecnólogo.
- U.S. funding and free/low-cost pathways, employer-supported training, Registered Apprenticeship discovery, Canada Training Credit qualification language, Colombia pathways, and Latin America/Caribbean discovery remain present.
- Privacy, key issuance, identity verification, payment security, fraud/social engineering, password/MFA, least privilege, cybersecurity, responsible AI, accessibility, conflict/safety, night-audit, and professional-boundary controls remain materially equivalent.
- No edition claims that this internal QA is independent human certification, professional translation certification, accreditation, accessibility certification, legal review, financial advice, or security certification.

## Encoding and structural checks

- Markdown sources are UTF-8 and display expected Spanish and Brazilian Portuguese diacritics.
- No replacement-character (`�`) defect is present in the reviewed source text.
- Headings, numbered lists, bullets, source links, wage tables expressed as lists, warning sections, verification checklist, final perspective, and assurance boundary remain readable and semantically aligned.
- URLs remain literal and are not localized or rewritten.
- Version is `2.0` and review date is `2026-08-21` across the controlled editions.

## Publication readiness decision

**PASS.** The trilingual Markdown source set is technically ready for publication-candidate generation and downstream DOCX/PDF, metadata, checksum, rendering, and release-audit gates.

This PASS is an internal controlled QA determination, not independent human linguistic, accessibility, legal, security, or professional certification.
