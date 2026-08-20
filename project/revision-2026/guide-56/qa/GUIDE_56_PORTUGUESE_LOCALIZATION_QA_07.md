# Guide 56 — Brazilian Portuguese Localization QA 07

**Guide:** 56 — Nursing Assistant and Patient Care Technician  
**Locale:** `pt-BR`  
**Branch:** `revision/guide-00-100-2026`  
**Date:** August 19, 2026  
**Gate:** Portuguese Localization  
**Status:** **PASS**

## Files reviewed

- Frozen English source: `project/revision-2026/guide-56/working-masters/GUIDE_56_NURSING_ASSISTANT_AND_PATIENT_CARE_TECHNICIAN_ENGLISH_v2.md`
- Brazilian Portuguese master: `project/revision-2026/guide-56/working-masters/GUIDE_56_NURSING_ASSISTANT_AND_PATIENT_CARE_TECHNICIAN_PTBR_v2.md`
- Current-source evidence: `project/revision-2026/guide-56/research/GUIDE_56_CURRENT_SOURCE_EVIDENCE_02.md`

## Localization controls

### Occupation and scope

PASS. The Portuguese edition preserves the distinction between nursing-assistant work and the non-standardized Patient Care Technician (PCT) title. It does not imply that the title itself authorizes phlebotomy, electrocardiography, specimen handling, medication activity, invasive procedures, or any other clinical task.

PASS. The localized scope continues to require applicable training, authorization, delegation where required, employer policy, jurisdiction rules, and supervision.

### Clinical safety boundary

PASS. The Portuguese edition retains the fail-closed patient-safety rules. It explicitly prohibits independent diagnosis, prescribing or medication-treatment decisions, unauthorized invasive/clinical procedures, falsification of care data, unsafe mobility/infection-control practices, and use of generative AI as a substitute for licensed clinical judgment or patient-specific orders.

PASS. The localized text preserves escalation requirements for material changes in condition, falls, suspected abuse or neglect, medication discrepancies, infection-control breaches, equipment problems, and other safety concerns.

### U.S. pathway and controlled values

PASS. The Portuguese edition preserves the state-approved training/competency-exam qualification boundary, CMS NATCEP/CEP clarification context, WIOA/American Job Center funding locators, and employer-support options without presenting funding or employment as guaranteed.

Controlled U.S. values preserved:

- USD $39,530 nursing-assistant median annual wage (May 2024)
- USD $37,700 orderly median annual wage (May 2024)
- 2% projected combined employment growth, 2024–2034
- approximately 211,800 openings per year
- Salary.com secondary estimate: USD $34,701/year / $17/hour
- Salary.com 25th–75th percentile range: USD $31,120–$36,431

PASS. The Salary.com figure remains clearly labeled non-governmental and methodologically separate from BLS.

### Canada pathway and controlled values

PASS. `NOC 33102` is preserved with the correct warning that a U.S. CNA credential does not automatically transfer to Canada.

Controlled Canadian wage values preserved:

- CAD $19.00/hour low
- CAD $24.00/hour median
- CAD $28.84/hour high

### Colombia pathway

PASS. The Portuguese edition preserves SENA `CNO 3311`, the broader regulated `Auxiliares en enfermería` pathway, the **2,640-hour** SENA Betowa Enfermería technical program, delegation/supervision language, and the ReTHUS verification requirement.

PASS. It does not represent a short private course as authorization to practise an auxiliary nursing occupation.

### Latin America and Caribbean coverage

PASS. Red Saber Cuidar and OIT/Cinterfor remain institutional/policy locators rather than licences or credentials, and the reader is directed to verify the national health authority, vocational-training institution, competency body, and employer requirements.

### Privacy, cybersecurity, and AI

PASS. Patient information, photographs, clinical records, identifiers, credentials, schedules, proprietary care documents, and other protected/confidential health information remain prohibited from public or unapproved AI systems.

PASS. The Portuguese edition preserves the instruction that AI must not replace licensed clinical judgment, patient-specific orders, emergency escalation, approved training, employer policy, or current legal/regulatory guidance.

### Source URL parity

PASS. The Portuguese master preserves the frozen English source set:

1. BLS Nursing Assistants and Orderlies
2. CMS QSO-26-08-NH
3. CareerOneStop WIOA-Eligible Training Program Finder
4. CareerOneStop American Job Center Finder
5. Government of Canada Job Bank NOC 33102 summary
6. Government of Canada Job Bank NOC 33102 wages
7. SENA Observatorio CNO 3311 occupation
8. SENA Observatorio CNO 3311 functions/norms
9. SENA Betowa Enfermería program 113535
10. Ministerio de Salud y Protección Social ReTHUS
11. OIT/Cinterfor Red Saber Cuidar
12. OIT/Cinterfor 2026 regional care qualifications initiative
13. Salary.com Certified Nursing Assistant Salary

No localized alternate endpoint was substituted for an authoritative frozen-English URL.

### Language and encoding

PASS. The text uses natural Brazilian Portuguese rather than literal word-for-word translation, while retaining necessary English credential/title names where they are formal U.S./Canadian labels.

PASS. UTF-8 text is clean, headings are readable, no translation placeholders remain, and the assurance boundary does not claim independent human certification, accreditation, certified translation, legal review, clinical approval, financial advice, or guaranteed employment.

## Decision

**Portuguese Localization: PASS.**

Guide 56 may advance to Trilingual Technical QA. Technical QA, Publication, and Release Audit remain fail-closed until their dedicated evidence and publication artifacts pass.