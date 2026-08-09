# Guide 17 — English v2 private-income freshness refresh

**Guide:** 17 — Bank Teller and Member Services Representative  
**QA date:** 2026-08-09  
**Target:** `references/english-v2-working-master.md`  
**Gate:** current non-government U.S. income estimates  
**Result:** **VERIFIED — working-master corrections required before source freeze**

## Purpose

This record preserves a fresh, source-specific snapshot of the three private U.S. salary pages used in Guide 17. These figures are non-government estimates and are intentionally kept separate from official BLS wage statistics. They are volatile and must not be averaged together or described as guaranteed pay.

## Live verification

### Indeed — Teller

Live page checked 2026-08-09:

- average base salary: **$19.28/hour**;
- low/high display: **$15.22–$24.42/hour**;
- sample statement: approximately **15.5k salaries** from job postings in the prior 36 months;
- page states **updated August 2, 2026**.

Source: https://www.indeed.com/career/teller/salaries

**Working-master delta:** the current master still states $19.25/hour, approximately 15.2k salaries, updated July 20, 2026. Replace that snapshot with the verified values above.

### ZipRecruiter — Bank Teller

Live page checked 2026-08-09:

- average annual pay: **$36,351/year**;
- approximate hourly equivalent: **$17.48/hour**;
- page states **As of Aug 9, 2026**;
- displayed 25th/75th percentile range is approximately **$32,000–$40,000/year**.

Source: https://www.ziprecruiter.com/Salaries/Bank-Teller-Salary

**Working-master delta:** the amount and hourly equivalent remain supported, but the master’s July 27, 2026 page-state date is stale. Update the date to August 9, 2026.

### Salary.com — Bank Teller

Live current page checked during this gate:

- average annual salary: **$37,554/year**;
- approximate hourly rate: **$18/hour**;
- current page identifies the benchmark **As of August 01, 2026**.

Source: https://www.salary.com/research/salary/opening/bank-teller-salary

**Working-master delta:** none. The existing $37,554/year, approximately $18/hour, As of August 01, 2026 entry remains supported.

## Controlled correction set

Only these working-master changes are authorized from this refresh:

1. Indeed: `$19.25/hour` → `$19.28/hour`.
2. Indeed sample: `approximately 15.2k salaries` → `approximately 15.5k salaries`.
3. Indeed update date: `July 20, 2026` → `August 2, 2026`.
4. ZipRecruiter page-state date: `July 27, 2026` → `August 9, 2026`.
5. Salary.com: **no content change**.

Do not alter the official BLS figures, Canada figures, regional pathways, or other guide claims based on this record.

## Gate consequence

This refresh resolves the ambiguity created by the earlier fail-closed pre-freeze check and provides the exact current correction set. English source freeze remains **NOT PASSED** until the working master is patched and the affected traceability/link check is rerun.

## Certification boundary

This is an internal controlled QA record. It is not independent human review, professional translation certification, accessibility certification, accreditation, legal review, regulator approval, financial advice, or an income guarantee.
