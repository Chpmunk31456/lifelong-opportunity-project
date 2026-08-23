# Guide 80 — Portuguese Localization QA 07

**Language:** Brazilian Portuguese (`pt-BR`)  
**Localized master:** `project/revision-2026/guide-80/working-masters/GUIDE_80_ESPECIALISTA_EM_ENTRADA_DE_DADOS_E_REGISTROS_PTBR_v2.md`  
**Frozen English source:** blob `8318127b1f14e7f7e20110ed315b4741c048be34`  
**Review date:** 2026-08-21

## Language/register — PASS

The edition uses natural Brazilian Portuguese. International technical terms that are common in records/data operations (OCR, CSV, MFA, data steward, legal hold, SLA) are retained or explained in context rather than translated into unnatural terminology.

## Occupation-code parity — PASS

Preserved:

- O*NET-SOC **43-9021.00**;
- Canada NOC **14111**;
- Colombia CUOC **41321**;
- Colombia CUOC **44150**.

The text preserves the two-part Colombia mapping: capture/digitalization versus archive/records operations.

## Numeric parity — PASS

Preserved:

- U.S. wage percentiles $31,200/$15.00; $35,760/$17.19; $41,340/$19.88; $48,410/$23.27; $58,790/$28.26;
- **141,600** employment in 2024;
- **104,900** projected employment in 2034;
- **-26%** projected change;
- **9,500 projected annual openings**;
- software signals **24% / 20% / 9% / 7%**;
- Canada **C$17.00 / C$23.50 / C$32.60 per hour**;
- Colombia Indeed approximately **COP 1,327,533/month**, **72 salaries**, updated **July 30, 2026**;
- SENA **3,984 / 40 / 48 hours**.

## Colombia wage-boundary parity — PASS

The Portuguese edition preserves the warning that OCUPACOL's CUOC 41321 salary display lacks statistical representativeness and is not a representative national wage benchmark.

## Professional-boundary parity — PASS

Preserved:

- transcription correction versus source-fact correction;
- ambiguity escalation;
- no fabrication/backdating/suppression;
- no independent retention/destruction/legal-hold decisions;
- access does not equal permission to disclose;
- accounting/clinical/legal/HR/privacy/security decisions remain outside the role unless separately authorized;
- audit and segregation-of-duties controls;
- no confidential production data in portfolios or unapproved AI/cloud services.

## Data/OCR/AI/security/accessibility parity — PASS

The localized edition maintains spreadsheet/database validation, OCR exception handling, import controls, privacy/security practices, phishing/MFA awareness, human verification of AI/automation output, accessibility and dysgraphia-friendly workflow guidance, and ergonomic caveats.

## Career-tool parity — PASS

The Portuguese edition includes:

- U.S./Canada/Colombia/Latin America pathways;
- honest automation/outlook discussion;
- training/funding caveats;
- synthetic-data portfolio;
- resume/interview/employer questions;
- scam warning;
- first-30-day and 90-day plans;
- data-entry, records and OCR/import checklists.

## URL parity — PASS

All **21 frozen URLs** from the English traceability record are preserved unchanged.

## Assurance boundary — PASS

The edition does not claim independent human certification, certified translation, legal/regulatory/privacy/records-management review, accessibility certification, cybersecurity certification, funding approval, employment guarantee or earnings guarantee.

## Gate decision

**PASS — Portuguese Localization**

The `pt-BR` edition is cleared for Trilingual Technical QA.

**Blockers:** none.
