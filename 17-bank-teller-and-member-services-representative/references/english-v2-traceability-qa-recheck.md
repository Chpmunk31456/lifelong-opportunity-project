# Guide 17 — English v2 Claim-to-Source Traceability QA Recheck

**Guide:** 17 — Bank Teller and Member Services Representative  
**Date:** 2026-08-09  
**Artifact reviewed:** `references/english-v2-working-master.md`  
**Prior gate record:** `references/english-v2-traceability-qa.md`  
**Evidence base:** controlled source ledger plus live source re-verification  
**Gate:** Claim-to-source traceability and freshness recheck  
**Decision:** **PASS**

This record closes the single failed freshness item identified in the prior fail-closed QA record. It does not claim independent human review, legal review, professional translation certification, accessibility certification, accreditation, regulator approval, or publication approval.

## Corrected private-income claim

The English v2 working master now states:

- **Salary.com:** **$37,554/year average**, approximately **$18/hour**, with the source stating **As of August 01, 2026**.

Live source re-verification on 2026-08-09 confirmed the Salary.com Bank Teller page reports an average U.S. salary of **$37,554/year** and **$18/hour** as of **August 01, 2026**.

Source: https://www.salary.com/research/salary/opening/bank-teller-salary

The previous intermediate June 2026 figure was not frozen because a fresh check showed it had already been superseded. This record intentionally preserves that audit history rather than rewriting the earlier failed QA record.

## Other non-government estimates rechecked

- **Indeed:** **$19.25/hour** average base salary; page updated **July 20, 2026**, based on approximately **15.2k salaries** from job postings over the prior 36 months.  
  Source: https://www.indeed.com/career/teller/salaries
- **ZipRecruiter:** **$36,351/year** average and approximately **$17.48/hour**; live page reviewed during this gate reported **As of July 27, 2026** and a majority range of approximately **$32,000-$40,000**.  
  Source: https://www.ziprecruiter.com/Salaries/Bank-Teller-Salary

These remain clearly labeled as non-government market estimates and are not averaged together or represented as official statistics.

## Prior PASS findings retained

The prior QA record already passed the following controlled claims and no conflicting evidence was introduced by this correction:

- O*NET 43-3071.00 occupational mapping;
- BLS teller entry requirements;
- BLS May 2024 median wage and 2024-2034 outlook framing;
- conservative handling of May 2025 OEWS occupation structure;
- Canada NOC 64400 and Job Bank wage framing;
- FAFSA and federal student-aid boundaries;
- WIOA training-support framing;
- IRC Section 127 employer educational-assistance limit and caveats;
- disclosed Apprenticeship.gov teller-status discrepancy;
- Colombia/SENA dynamic-offering caveats;
- jurisdictional and regulatory boundaries;
- privacy, cybersecurity, accessibility-content, fraud-escalation, and responsible-AI controls.

## Gate conclusion

**Claim-to-source traceability and freshness gate: PASS.**

The English v2 working master may advance to exhaustive link, terminology, structural, and encoding QA. It is **not yet source-frozen** and no localization or publication PASS is implied by this record.