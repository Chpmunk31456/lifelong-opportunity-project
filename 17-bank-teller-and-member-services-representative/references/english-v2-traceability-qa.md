# Guide 17 — English v2 Claim-to-Source Traceability QA

**Guide:** 17 — Bank Teller and Member Services Representative  
**Date:** 2026-08-09  
**Artifact reviewed:** `references/english-v2-working-master.md`  
**Evidence base:** `references/guide-17-v2-current-source-ledger.md` plus live source re-verification  
**Gate:** Claim-to-source traceability and freshness  
**Decision:** **FAIL — CORRECTION REQUIRED BEFORE SOURCE FREEZE**

This is a fail-closed QA record. It does not claim independent human review, legal review, professional translation certification, accessibility certification, accreditation, regulator approval, or publication approval.

## Executive finding

The English v2 working master is substantively traceable to the controlled evidence ledger, but one current non-government salary claim failed freshness verification on 2026-08-09. The source-freeze gate therefore remains closed.

### Required correction

The working master currently states:

- `Salary.com: $37,557/year average; page state reviewed July 1, 2026.`

Live re-verification of the cited Salary.com page on 2026-08-09 instead showed:

- **Average: $37,559/year**
- **Last Updated: June 01, 2026**
- **Average hourly presentation: $18/hour**

Source: https://www.salary.com/research/salary/opening/bank-teller-salary

The master must be corrected to the live source state before this traceability gate can be marked PASS. The difference is small, but controlled revision does not knowingly freeze stale or mismatched provenance.

## 1. U.S. occupational mapping — PASS

**Claim:** O*NET 43-3071.00 is the primary U.S. teller mapping; sample titles include Bank Teller, Credit Union Teller, Member Services Representative, Financial Services Representative, and related titles.  
**Source:** https://www.onetonline.org/link/details/43-3071.00  
**Re-verification:** PASS. O*NET showed `Updated 2026`, code 43-3071.00, and the cited title family.

## 2. U.S. entry requirements — PASS

**Claim:** Tellers typically need a high school diploma or equivalent and receive short-term on-the-job training; an employer may require a background check.  
**Source:** https://www.bls.gov/ooh/office-and-administrative-support/tellers.htm  
**Re-verification:** PASS.

## 3. U.S. official wage and outlook — PASS

**Claims:**

- May 2024 median wage: **$39,340/year**;
- equivalent median hourly pay: **$18.91/hour**;
- projected employment change: **-13% from 2024 to 2034**;
- about **29,800 openings per year on average**, primarily replacement openings.

**Source:** https://www.bls.gov/ooh/office-and-administrative-support/tellers.htm  
**Re-verification:** PASS.

The working master appropriately does not treat replacement openings as occupational growth.

## 4. May 2025 BLS handling — PASS

**Claim treatment:** the master states that the May 2025 OEWS structure contains 43-3071 Tellers but deliberately does not publish a May 2025 teller wage as a directly captured official occupation-table figure.  
**Source:** https://www.bls.gov/oes/2025/may/oes_stru.htm  
**Decision:** PASS. This is conservative and preserves provenance integrity.

## 5. U.S. private income estimates

### Indeed — PASS

**Claim:** **$19.25/hour** average base salary, updated **July 20, 2026**, based on approximately **15.2k salaries from job postings over the prior 36 months**.  
**Source:** https://www.indeed.com/career/teller/salaries  
**Re-verification:** PASS on 2026-08-09.

### ZipRecruiter — PASS

**Claim:** **$36,351/year**, approximately **$17.48/hour**, with the cited page showing a current July 2026 estimate and a central range around $32,000-$40,000.  
**Source:** https://www.ziprecruiter.com/Salaries/Bank-Teller-Salary  
**Re-verification:** PASS. The live page reported the same annual and hourly averages and a July 27, 2026 as-of date.

### Salary.com — FAIL / CORRECTION REQUIRED

**Working-master claim:** $37,557/year; July 1, 2026.  
**Live source state:** $37,559/year; last updated June 1, 2026.  
**Source:** https://www.salary.com/research/salary/opening/bank-teller-salary  
**Decision:** FAIL until corrected in the English working master.

Private estimates remain clearly labeled as non-government research and are not averaged together or represented as official statistics.

## 6. Canada occupation and wages — PASS

**Occupational mapping:** NOC/OaSIS 64400 — Customer services representatives - financial institutions.  
**Official source:** https://noc.esdc.gc.ca/Structure/NOCProfile?GoCTemplateCulture=en-CA&code=64400&version=2021.0&wbdisable=true  
**Current OaSIS corroboration:** occupation 64400.00 remains mapped to financial-institution customer service and indicates secondary-school-level preparation or several weeks of on-the-job training.

**Wage claim:** Canada **C$18.00/hour low, C$22.50/hour median, C$30.67/hour high**; wages updated November 19, 2025 from the 2023-2024 Labour Force Survey reference period.  
**Source:** https://www.jobbank.gc.ca/marketreport/wages-occupation/14136/ca  
**Re-verification:** PASS on 2026-08-09.

## 7. FAFSA and federal student aid — PASS

**Claim:** the 2026-27 FAFSA can provide access, subject to eligibility and participating programs, to federal grants, Federal Work-Study, and federal student loans; states, schools, and some private aid providers also use FAFSA information.  
**Source:** https://studentaid.gov/articles/fafsa-student-steps/  
**Re-verification:** PASS.

The master correctly avoids implying that a short teller course is automatically Title IV eligible.

## 8. WIOA training support — PASS

**Claim:** WIOA can support eligible forms of occupational skills training, on-the-job training, incumbent-worker training, workplace training with related instruction, skill upgrading/retraining, and customized training, subject to eligibility and local/provider rules.  
**Source:** https://www.dol.gov/agencies/eta/advisories/training-and-employment-guidance-letter-no-08-19  
**Re-verification:** PASS.

The master correctly directs readers to verify a specific program/provider with an American Job Center before paying.

## 9. Employer educational assistance — PASS

**Claim:** under a compliant IRC Section 127 educational-assistance program, up to **$5,250** of qualifying employer-provided educational assistance can be excluded from employee gross income for calendar years 2025 and 2026, subject to rules and plan terms.  
**Source:** https://www.irs.gov/newsroom/irs-updates-frequently-asked-questions-about-section-127-educational-assistance-programs  
**Re-verification:** PASS. IRS update IR-2026-55 is dated April 20, 2026.

The master correctly avoids implying that every employer provides the benefit or that every course/employee qualifies.

## 10. Apprenticeship status — PASS AS A DISCLOSED DISCREPANCY

The master does not collapse conflicting federal signals into a false categorical statement.

**Occupation Finder:** https://www.apprenticeship.gov/apprenticeship-occupations/listings?occupationCode=43-3071.00  
Live re-verification states that Tellers 43-3071.00 is **not currently approved for use in a Registered Apprenticeship Program**.

**Financial Services industry page:** https://www.apprenticeship.gov/apprenticeship-industries/financial-services  
Live re-verification still lists **Bank Teller** under `High-Demand Apprenticeship Occupations` and reports more than **6,248 apprentices served in financial services in 2024**.

**Decision:** PASS for the master’s cautious wording. A claimed teller Registered Apprenticeship must be verified by exact sponsor, program, registered occupation, and responsible state/federal office.

## 11. Colombia / SENA — PASS WITH PUBLICATION-TIME RECHECK REQUIRED

The controlled ledger records current SENA Betowa financial-services examples and the master describes them as dynamic offerings rather than permanent entitlements. The exact enrollment state must be rechecked again before publication because Betowa availability and program state can change.

Controlled sources:

- https://betowa.sena.edu.co/oferta/suministro-de-informacion-y-asesoria-para-el-consumidor-financiero?location=57011001&modality=V&offertype=company&programId=63571
- https://betowa.sena.edu.co/oferta/registro-contable-de-operaciones-comerciales?location=57011001&modality=V&offertype=company&programId=228684
- https://betowa.sena.edu.co/oferta/ingresos-y-gastos-personales?location=57011001&modality=V&offertype=company&programId=69801

**Decision:** PASS for claim framing; mandatory freshness recheck remains at publication QA.

## 12. Geographic and regulatory boundaries — PASS

The master correctly states that Latin America does not share one teller credential, wage standard, licensing system, or training pathway. It tells readers to verify country-specific requirements and does not treat the teller/member-service title as automatic authority to approve credit, originate regulated mortgages, provide investment/legal/tax advice, or override fraud, privacy, authentication, sanctions, or anti-money-laundering controls.

These statements are framed as risk/authority boundaries and verification requirements rather than as jurisdiction-specific legal advice.

## 13. Privacy, cybersecurity, accessibility, and responsible AI — PASS AT CONTENT LEVEL

The master:

- prohibits use of real customer/confidential institution data in public AI tools;
- requires employer-approved systems and human verification for customer-impacting work;
- emphasizes authentication, privacy, fraud escalation, and secure-system behavior;
- uses descriptive headings and plain-language warnings;
- does not promise a particular workplace accommodation;
- reserves final DOCX/PDF accessibility and rendering checks for downstream artifact QA.

## Gate conclusion

**Claim-to-source traceability gate: FAIL — one factual freshness correction is required.**

Before the gate can be changed to PASS:

1. correct the Salary.com figure from **$37,557/year** to **$37,559/year**;
2. correct the Salary.com source-state date from **July 1, 2026** to **June 1, 2026**;
3. re-run the affected income paragraph check;
4. then continue with exhaustive link/freshness, terminology, structural, encoding, and English source-freeze QA.

No downstream localization or publication PASS should be recorded while this gate is failed.