# Guide 69 — Brazilian Portuguese Localization QA 07

**Guide:** 69 — Hotel Front Desk and Guest Services  
**Locale:** pt-BR  
**Date:** 2026-08-21  
**Source-of-truth English blob:** `a75e6e8015fcd4afb4bdefc9f52264d4ffb0ad3a`  
**Portuguese master commit:** `c57bc2886a754bcee9dca272870dd66136257f47`  
**Result:** PASS

## Controlled checks

- Brazilian Portuguese is natural and occupationally appropriate rather than a literal machine gloss.
- O*NET-SOC `43-4081.00` and Canada NOC `64314` are preserved.
- U.S. BLS May 2025 values are preserved: employment `261,420`, mean hourly `USD $17.09`, mean annual `USD $35,550`, median hourly `USD $16.86`.
- O*NET/BLS 2025 values are preserved: median annual `USD $35,070`, annual 10th/90th percentiles `USD $27,120` / `USD $45,470`, hourly 10th/90th percentiles `USD $13.04` / `USD $21.86`.
- Salary.com is explicitly labeled a non-government market estimate and preserves the August 1, 2026 values: approximately `USD $34,841/year`, about `$17/hour`, and `USD $32,261–$37,181` 25th–75th percentile range.
- Canada Job Bank national wage values are preserved: `CAD $15.00`, `CAD $18.00`, and `CAD $26.50` per hour.
- Colombia SENA pathways are preserved: `SERVICIO DE RECEPCION HOTELERA` Técnico, `2,208` hours; `COORDINACION DE SERVICIOS HOTELEROS` Tecnólogo, `3,984` hours.
- United States funding/training pathways remain present: CareerOneStop Find Training, WIOA-Eligible Training Program Finder, American Job Centers, employer-supported development, and Registered Apprenticeship discovery.
- Canada Training Credit remains described as eligibility-dependent rather than guaranteed funding.
- Latin America/Caribbean discovery through ILO/Cinterfor remains qualified as a locator, not evidence of a specific opening.
- Privacy, replacement-key identity verification, least privilege, payment security, social-engineering, MFA/password, cybersecurity, AI, accessibility, complaint/safety, night-audit, and professional-boundary controls are retained.
- The Portuguese edition does not claim independent human certification, professional translation certification, legal review, accessibility certification, accreditation, financial advice, or security certification.
- All 13 controlled current-source URLs from the frozen English master are retained unchanged.
- UTF-8 Portuguese diacritics render correctly in the Markdown source; no replacement-character defect was introduced.

## Editorial notes

Established hotel-industry terms that are commonly used in Brazilian workplaces, including `front office`, `check-in`, `check-out`, `property management system`, `revenue management`, `handoff`, and `Registered Apprenticeship`, are retained where translating them would reduce precision. Explanatory Portuguese context is supplied around them.

## Gate decision

**PASS.** Guide 69 may advance to trilingual technical QA. This is an internal controlled QA determination only; it is not independent professional translation certification or human linguistic certification.
