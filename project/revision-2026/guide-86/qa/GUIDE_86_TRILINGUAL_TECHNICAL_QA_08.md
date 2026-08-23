# Guide 86 — Trilingual Technical QA 08

**Guide:** 86 — Database Administrator  
**Controlled branch:** `revision/guide-00-100-2026`  
**Frozen English source:** `GUIDE_86_DATABASE_ADMINISTRATOR_ENGLISH_v2.md` — blob `ce3f8215c91230c15e1efdd702e6f73571c7ae18`  
**Spanish:** `GUIDE_86_ADMINISTRADOR_DE_BASES_DE_DATOS_ES419_v2.md`  
**Portuguese:** `GUIDE_86_ADMINISTRADOR_DE_BANCO_DE_DADOS_PTBR_v2.md`  
**Review date:** 2026-08-22

## Gate purpose

This gate checks occupation identity, numeric values, source links, technical meaning, authority boundaries, opportunity pathways, privacy/security, AI and accessibility parity across English, `es-419` and `pt-BR`.

## Occupation mapping parity — PASS

All three editions preserve:

- O*NET-SOC **15-1242.00 — Database Administrators**;
- Canada **NOC 21223 — Database analysts and data administrators**;
- Colombia **CUOC 25210 — Diseñadores y administradores de bases de datos**.

No edition uses the obsolete U.S. code 15-1141.00 or invents a different Colombia/Canada occupation.

## Wage and outlook parity — PASS

All editions preserve official U.S. 2025 wages:

- $60,230 / $28.96;
- $79,610 / $38.28;
- median $104,620 / $50.30;
- $135,460 / $65.13;
- $163,320 / $78.52.

All preserve the 2024–2034 outlook:

- 78,000 employment in 2024;
- 77,500 projected in 2034;
- **-1%** projected growth;
- **3,800** projected annual openings.

The editions explicitly state that total employment is projected to decline slightly and that annual openings include replacement/turnover. None converts openings into a growth claim.

## Current non-government market parity — PASS

All editions preserve the title-specific Indeed context as separate from official wages:

- approximately $110,414/year average;
- $73,876 low;
- $165,024 high;
- 2.1k observations from postings over 36 months;
- updated August 10, 2026.

It remains labeled non-government and non-guaranteed.

## Canada parity — PASS

All editions preserve:

- NOC 21223 scope;
- degree/college plus programming/related-experience expectations;
- current **not regulated in Canada** statement from Job Bank;
- C$25.00 / C$40.87 / C$61.03 national hourly wage values.

## Colombia and SENA parity — PASS

All editions preserve CUOC 25210 as the direct Colombian mapping and do not fabricate a representative national DBA salary.

All preserve:

- SENA Implementación y gestión de bases de datos — Tecnólogo — **3,984 hours/horas**;
- Bases de datos: generalidades y sistemas de gestión — **40 hours/horas**;
- Construcción de bases de datos con MySQL — **48 hours/horas**;
- live availability/admission/cohort/location caveats.

## Employer technology parity — PASS

The three editions preserve selected current O*NET employer-posting signals including SQL 62%, Python 42%, AWS 29%, Azure 25%, Snowflake 16%, Spark 13%, Power BI 12%, Java 12%, PostgreSQL 11%, Kafka 10%, major 9% technologies, Git/Linux/MySQL 8%, Oracle PL/SQL/Oracle Database 7%, UNIX 6% and selected 5% tools.

They are labeled posting signals rather than universal requirements.

## Reader-link and research-source parity — PASS

- The three reader-facing editions preserve the same **21 verification destinations**.
- The controlled research pack preserves **26 evidence URLs** for claim traceability.
- Reader curation does not replace the research evidence record.

No fabricated or AI-generated authority is introduced.

## Production authority and change-control parity — PASS

All editions retain the rule that technical capability does not equal organizational authority and preserve:

- target/environment verification;
- authorized change/ticket/window requirements where applicable;
- non-production testing;
- peer review where required;
- backup/restore or rollback readiness;
- validation before/after change;
- stop/escalation conditions;
- evidence retention.

## Backup/recovery parity — PASS

All editions preserve the high-consequence distinctions that:

- successful backup jobs do not prove recoverability;
- restore tests are required to establish practical recovery capability;
- RPO/RTO are organizational recovery objectives, not values the DBA invents;
- replication/high availability is not backup;
- failover should be tested;
- destructive production restoration requires explicit authorization and a controlled plan.

## Security/privacy parity — PASS

All editions retain:

- least privilege;
- role-based access;
- MFA where supported/required;
- credential/secrets controls;
- no curiosity browsing;
- privileged-action auditability;
- separation of duties where required;
- encryption/security controls within assigned responsibility;
- protected backup handling;
- privacy/retention/legal-hold boundaries;
- secure extracts and test-data controls;
- incident evidence preservation and escalation.

## Cloud and automation parity — PASS

All editions state that managed/cloud database services do not remove customer responsibility for identity/access, network exposure, data classification, configurable encryption, backup retention, logging, credentials, resilience, costs and change governance.

Automation retains version control, review, parameter/environment validation, secrets management, logging, rollback and limited automation identity permissions.

## Responsible-AI parity — PASS

All editions allow only policy-approved, low-risk assistance and explicitly prohibit:

- protected data, credentials, private schemas, connection strings or protected logs in unapproved AI tools;
- unreviewed AI-generated production SQL/scripts;
- autonomous production changes outside approved governance;
- treating AI output as incident evidence or vendor authority;
- skipping rollback/testing because AI output appears plausible.

Human accountability and validation remain mandatory.

## Accessibility and portfolio parity — PASS

All editions retain meaningful headings, readable contrast, structured tables, text descriptions for diagrams, non-color-only communication, keyboard-accessible considerations and clear incident/change steps. No automated check is described as legal accessibility certification.

Portfolio guidance remains restricted to public, licensed or synthetic data and excludes credentials, connection strings, production schemas/screenshots, real backups, private IPs/hostnames, proprietary configurations and unauthorized vulnerability details.

## Expanded opportunity parity — PASS

All editions preserve:

- CareerOneStop/American Job Center/WIOA discovery with eligibility caveats;
- O*NET-approved apprenticeship titles Database Administrator (Nof) and Database Technician, with live verification at Apprenticeship.gov;
- Canada training discovery;
- SENA long-form and supplemental pathways;
- OIT/Cinterfor regional locator;
- practical learning sequence;
- safe portfolio projects;
- four-week starter plan;
- job-title variants;
- employer due-diligence questions.

No funding, admission, apprenticeship seat, job or salary is guaranteed.

## Gate result

**PASS — Trilingual Technical QA**

**Blockers:** none.

Guide 86 is cleared to enter controlled Publication QA and Release Audit.
