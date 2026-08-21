# Guide 73 — Spanish Localization QA 07

**Occupation:** Sales Support and Account Coordinator  
**Locale:** neutral Latin American Spanish (`es-419`)  
**Review date:** 2026-08-21  
**Gate:** Spanish Localization — PASS

## Controlled source

The Spanish Version 2 working master was localized from the frozen English master:

`project/revision-2026/guide-73/working-masters/GUIDE_73_SALES_SUPPORT_AND_ACCOUNT_COORDINATOR_ENGLISH_v3.md`

Frozen English blob:

`7396ad017d9e5415b056d8d4b50340f7315238b6`

Spanish master reviewed:

`project/revision-2026/guide-73/working-masters/GUIDE_73_SALES_SUPPORT_AND_ACCOUNT_COORDINATOR_ES419_v2.md`

Spanish master blob at review:

`1cc95f06d49db7493a4045fe7decd1bcf1c69977`

No public translation service or external translation API was used.

## Structural and semantic parity

PASS. The Spanish master preserves the frozen English sequence and substantive coverage for:

- occupation definition and title variability;
- opportunity framing and workload realities;
- responsibilities and explicit authority limits;
- communication, organization, commercial-administration, and digital-tool skills;
- intake, preparation, verification, handoff, follow-up, and closure workflow;
- CRM/data-quality controls;
- privacy, cybersecurity, fraud-prevention, and incident-reporting controls;
- responsible-AI restrictions and human verification;
- U.S., Canada, Colombia, and Latin America pathways;
- free/low-cost training, WIOA, scholarships, workforce services, and work-based learning;
- official and non-government compensation distinctions;
- fictional portfolio guidance, truthful resume/interview preparation, 30-day learning plan, advancement paths, sources, and assurance boundary.

No material English section was intentionally omitted or broadened into unsupported authority.

## Identifier, wage, date, and market-estimate parity

PASS. The Spanish master preserves the controlled meaning of:

- O*NET `41-3091.00`;
- Canada NOC `64101`;
- Colombia CUOC `33220`;
- U.S. official 2025 median wages: `$33.65/hour` and `$69,990/year`;
- U.S. employment/outlook: `1,226,700`, `3% to 4%`, `2024 to 2034`, and approximately `123,000` projected openings;
- Canada official wages: `C$19.23`, `C$31.50`, and `C$56.23` per hour, updated November 19, 2025;
- Indeed Account Coordinator estimate: approximately `$53,849/year`, about `1.6k` salary observations from postings, updated August 2, 2026, range approximately `$38,645–$75,035/year`;
- Indeed Sales Support Representative estimate: approximately `$21.10/hour`, about `4.2k` salary observations from postings, updated August 3, 2026, range approximately `$14.98–$29.71/hour`.

Official occupational benchmarks remain clearly separated from non-government market estimates. No unsupported Colombia salary benchmark was introduced.

## Controlled source/link parity

PASS. The Spanish master retains the frozen English destinations for O*NET, CareerOneStop WIOA training, Government of Canada training, Canada Job Bank, OCUPACOL, SENA Betowa, Colombia Public Employment Service, OIT/Cinterfor, CISA Secure Our World, NIST AI RMF, and both Indeed salary pages. URLs were not intentionally localized or rewritten.

## Authority and safety-of-information boundaries

PASS. The localization preserves that a coordinator does not automatically have authority to change prices, discounts, commissions, credit terms, contract language, delivery commitments, refunds, write-offs, bank details, regulated advice, or final approvals. It also preserves prohibitions against fabricating purchase orders, signatures, invoices, consent, pipeline activity, or sales results.

Customer/company confidentiality, approved-system use, least-necessary access, MFA, password controls, independent verification of bank/payment changes, recipient verification, retention/deletion, incident reporting, and protection against phishing/fraud remain explicit.

## Responsible-AI boundary

PASS. AI is limited to employer-approved, low-risk assistance. Human verification remains required for consequential commercial content. Confidential contracts, credentials, payment data, private customer records, account strategy, non-public pricing, and other protected information must not be placed in unapproved AI systems. The NIST AI Risk Management Framework remains described as a risk-management reference, not as product/workflow certification.

## Language and encoding review

PASS. The master uses neutral Latin American Spanish suitable for a broad regional audience. Official names and identifiers remain intact where precision matters. Diacritics and UTF-8 text render normally; no obvious mojibake or placeholder translation text was identified.

## Assurance boundary

PASS. The Spanish master does not claim independent human linguistic certification, professional translation certification, legal/tax/financial/cybersecurity advice, accreditation, accessibility certification, funding approval, employment, income, admission, apprenticeship placement, certification, or promotion guarantees.

## Result

**PASS.** Guide 73 Spanish localization has sufficient structural, factual, terminology, link, numeric, authority, privacy, cybersecurity, AI, and assurance parity with the frozen English master to close the `spanish_localization` gate.

This is an internal machine-assisted controlled-project localization review; it is not independent human linguistic certification or professional translation certification.
