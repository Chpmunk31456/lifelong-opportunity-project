# Guide 17 — English v2 technical pre-freeze QA

**Guide:** 17 — Bank Teller and Member Services Representative  
**QA date:** 2026-08-09  
**Target:** `references/english-v2-working-master.md`  
**Gate:** link/freshness, terminology, structure, and encoding  
**Result:** **FAIL CLOSED — freshness corrections required before English source freeze**

## Completed checks

- Confirmed the working master uses UTF-8 content and contains the controlled sections 1–19 in sequential order.
- Confirmed country-specific material is explicitly labeled for the United States, Canada, Latin America, and Colombia.
- Confirmed official and non-government income sources are separated rather than blended.
- Confirmed the guide retains the no-guarantee/no-certification disclaimers and does not claim independent human review, professional translation certification, accessibility certification, accreditation, legal review, regulator approval, or employment guarantees.
- Re-opened the principal official occupation, labor-market, funding, and apprenticeship references on 2026-08-09. O*NET 43-3071.00 remains current and marked Updated 2026; the BLS teller profile and May 2025 OEWS occupation structure remain reachable; Federal Student Aid FAFSA and scholarship guidance remain reachable; IRS Section 127 guidance remains reachable; and both Apprenticeship.gov teller/financial-services pages remain reachable.
- Re-opened the three current private U.S. salary sources and checked their live page state rather than relying on the prior audit snapshot.

## Freshness defects found

The working master must be corrected before source freeze because two private-market entries have advanced and one prior Salary.com snapshot is no longer supported by the currently retrievable page:

1. **Indeed** — current live page reports **$19.28/hour**, based on about **15.5k salaries** from job postings in the prior 36 months, **updated August 2, 2026**. The working master still states $19.25/hour, about 15.2k salaries, updated July 20, 2026.
2. **ZipRecruiter** — current live page still reports **$36,351/year / $17.48/hour**, but now states **As of August 8, 2026**. The working master still describes a July 27, 2026 page state.
3. **Salary.com** — the currently retrievable page reports **$37,559/year / approximately $18/hour**, **Last Updated June 01, 2026**. The working master currently states $37,554/year and `As of August 01, 2026`; that exact snapshot is not supported by the page retrieved during this gate.

These are private estimates, not government statistics. Their volatility is itself the reason this gate is fail-closed.

## Terminology and structural controls

**PASS subject to the freshness corrections above.**

- `Bank Teller`, `Credit Union Teller`, `Member Services Representative`, `Financial Services Representative`, and related titles are presented as examples rather than exact equivalents.
- `Registered Apprenticeship` is used cautiously and the conflict between the occupation listing and the financial-services industry page is explicitly disclosed.
- Regulated/restricted duties, fraud escalation, privacy, cybersecurity, and AI boundaries are expressed as employer/regulator-dependent controls rather than as authority granted by the guide.
- The 19-section structure is complete and ordered.
- No obvious mojibake, replacement-character artifacts, or leading-BOM artifact was observed in the retrieved UTF-8 master.

## Required next action

Correct the three private-income freshness entries in the English v2 working master, re-run the affected traceability/link checks, and only then create the frozen English localization source. Do **not** mark source freeze, localization, DOCX/PDF, metadata, publication, or release audit PASS from this record.

## Certification boundary

This is an internal controlled QA record. It is not independent human review, professional translation certification, accessibility certification, accreditation, legal review, regulator approval, or financial advice.
