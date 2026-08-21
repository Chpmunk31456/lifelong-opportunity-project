# Guide 73 — Brazilian Portuguese Localization QA 08

**Occupation:** Sales Support and Account Coordinator  
**Locale:** Brazilian Portuguese (`pt-BR`)  
**Review date:** 2026-08-21  
**Gate:** Portuguese Localization — PASS

## Controlled source

The Portuguese Version 2 working master was localized from the frozen English master:

`project/revision-2026/guide-73/working-masters/GUIDE_73_SALES_SUPPORT_AND_ACCOUNT_COORDINATOR_ENGLISH_v3.md`

Frozen English blob:

`7396ad017d9e5415b056d8d4b50340f7315238b6`

Portuguese master reviewed:

`project/revision-2026/guide-73/working-masters/GUIDE_73_SALES_SUPPORT_AND_ACCOUNT_COORDINATOR_PTBR_v2.md`

Portuguese master blob at review:

`4e200fcbe499c5aa1723438ce2ea28626ce73bcf`

No public translation service or external translation API was used.

## Structural and semantic parity

PASS. The Portuguese master preserves the frozen English sequence and substantive coverage for occupation definition, role variability, opportunity framing, responsibilities, authority limits, communication/organization/commercial administration/digital tools, account-support workflow, CRM/data quality, privacy/cybersecurity/fraud controls, responsible AI, U.S./Canada/Colombia/Latin America pathways, free-first training and workforce funding discovery, official and non-government compensation distinctions, fictional portfolio examples, truthful resume/interview preparation, 30-day learning plan, advancement paths, source notes, and assurance boundary.

No substantive English section was intentionally omitted or expanded into unsupported commercial authority.

## Identifier, wage, date, and estimate parity

PASS. Controlled meaning is preserved for:

- O*NET `41-3091.00`;
- Canada NOC `64101`;
- Colombia CUOC `33220`;
- U.S. official 2025 median wages `$33.65/hour` and `$69,990/year`;
- approximately `1,226,700` workers in 2024, `3% to 4%` growth from 2024 to 2034, and approximately `123,000` projected openings;
- Canada official values `C$19.23`, `C$31.50`, and `C$56.23` per hour, updated November 19, 2025;
- Indeed Account Coordinator estimate approximately `$53,849/year`, approximately `1.6k` salary observations from postings, updated August 2, 2026, with displayed range approximately `$38,645–$75,035/year`;
- Indeed Sales Support Representative estimate approximately `$21.10/hour`, approximately `4.2k` salary observations from postings, updated August 3, 2026, with displayed range approximately `$14.98–$29.71/hour`.

Official benchmark wages remain separate from non-government estimates. No unsupported national Colombia salary benchmark was introduced.

## Controlled link parity

PASS. The Portuguese master preserves the frozen English destinations for O*NET, CareerOneStop WIOA training, Government of Canada training, Job Bank, OCUPACOL, SENA Betowa, Colombia Public Employment Service, OIT/Cinterfor, CISA Secure Our World, NIST AI RMF, and the two Indeed salary pages. URLs were not intentionally localized or rewritten.

## Authority, privacy, cybersecurity, fraud, and AI boundaries

PASS. The localization preserves that a coordinator does not automatically have authority over pricing, discounts, commissions, credit terms, contract language, delivery commitments, refunds/write-offs, bank details, regulated advice, or final approvals. Fabricated purchase orders, signatures, invoices, consent, pipeline activity, and sales results remain prohibited.

Employer-approved systems, least-necessary access, MFA, strong password practices, independent verification of payment/bank changes, recipient verification, retention/deletion controls, and incident reporting remain explicit.

AI remains limited to employer-approved, low-risk support. Human verification remains required for consequential commercial content. Confidential contracts, credentials, payment data, private customer records, account strategy, non-public pricing, and other protected information must not be entered into unapproved AI systems. NIST AI RMF remains a risk-management reference rather than a certification claim.

## Language and encoding review

PASS. The master uses natural Brazilian Portuguese suitable for a general audience. Official classification names, product names, and formal program/resource names remain in their original form where precision matters. Accents and UTF-8 characters render normally; no obvious mojibake or placeholder translation text was identified.

## Assurance boundary

PASS. The Portuguese master does not claim independent human linguistic certification, professional translation certification, legal/tax/financial/cybersecurity advice, accreditation, accessibility certification, funding approval, employment, income, admission, apprenticeship placement, certification, or promotion guarantees.

## Result

**PASS.** Guide 73 Brazilian Portuguese localization has sufficient structural, factual, terminology, link, numeric, authority, privacy, cybersecurity, AI, and assurance parity with the frozen English master to close the `portuguese_localization` gate.

This is an internal machine-assisted controlled-project localization review; it is not independent human linguistic certification or professional translation certification.
