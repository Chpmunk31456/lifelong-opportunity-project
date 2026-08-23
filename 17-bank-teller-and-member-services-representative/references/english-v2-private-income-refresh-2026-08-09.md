# Guide 17 — English v2 private-income freshness refresh

**Guide:** 17 — Bank Teller and Member Services Representative  
**QA date:** 2026-08-09  
**Target:** `references/english-v2-working-master.md`  
**Gate:** current non-government U.S. income estimates  
**Result:** **VERIFIED — one working-master correction required before source freeze**

## Purpose

This record preserves a fresh, source-specific snapshot of the three private U.S. salary pages used in Guide 17. These figures are non-government estimates and are intentionally kept separate from official BLS wage statistics. They are volatile and must not be averaged together or described as guaranteed pay.

A previous refresh captured later-looking values that were not reproducible on the currently retrievable source pages. This record corrects that evidence fail-closed: publication uses the values that can be independently re-opened and verified now, not the earlier unreproducible snapshot.

## Live verification

### Indeed — Teller

Live page rechecked 2026-08-09:

- average base salary: **$19.25/hour**;
- low/high display: **$15.18–$24.42/hour**;
- sample statement: approximately **15.2k salaries** from job postings in the prior 36 months;
- page states **updated July 20, 2026**.

Source: https://www.indeed.com/career/teller/salaries

**Working-master delta:** none. The current working master already matches this reproducible source state.

### ZipRecruiter — Bank Teller

Live page rechecked 2026-08-09:

- average annual pay: **$36,351/year**;
- approximate hourly equivalent: **$17.48/hour**;
- page states **As of Jul 27, 2026**;
- displayed 25th/75th percentile range is approximately **$32,000–$40,000/year**.

Source: https://www.ziprecruiter.com/Salaries/Bank-Teller-Salary

**Working-master delta:** none. The amount, hourly equivalent, range, and July 27, 2026 source-state date remain supported by the retrievable page.

### Salary.com — Bank Teller

Live page rechecked 2026-08-09:

- average annual salary: **$37,557/year**;
- approximate hourly rate: **$18/hour**;
- current retrievable page identifies the benchmark **As of July 01, 2026** and shows **Last Updated on July 01, 2026**.

Source: https://www.salary.com/research/salary/opening/bank-teller-salary

**Working-master delta:** the current working master states $37,554/year and August 1, 2026. Replace that entry with the reproducible $37,557/year, approximately $18/hour, As of July 01, 2026 snapshot.

## Controlled correction set

Only this working-master change is authorized from this refresh:

1. Salary.com: `$37,554/year average, approximately $18/hour; source states **As of August 01, 2026**.` → `$37,557/year average, approximately $18/hour; source states **As of July 01, 2026**.`

Do not change the official BLS figures, the currently supported Indeed or ZipRecruiter entries, Canada figures, regional pathways, or other guide claims based on this record.

## Gate consequence

English source freeze remains **NOT PASSED** until the Salary.com working-master line is patched and the affected traceability/link check is rerun. The earlier unreproducible Indeed/ZipRecruiter/Salary.com snapshot is superseded by this corrected evidence record but remains visible in repository history for auditability.

## Certification boundary

This is an internal controlled QA record. It is not independent human review, professional translation certification, accessibility certification, accreditation, legal review, regulator approval, financial advice, or an income guarantee.
