# Guide 02 — Neutral Latin American Spanish Detailed Parity QA 17

Date: 2026-08-07  
Branch: `revision/guide-00-100-2026`  
English frozen source: `project/revision-2026/guide-02/source/GUIDE_02_ENGLISH_WORKING_MASTER_v2.md`  
Spanish working master: `project/revision-2026/guide-02/source/GUIDE_02_SPANISH_LATAM_WORKING_MASTER_v2.md`

## Gate purpose

This record closes the detailed English↔neutral Latin American Spanish structural, high-impact numeric/date, source-destination, terminology-control, and claims-control review needed before Brazilian Portuguese production begins. It is a controlled project QA record, not professional translation certification, independent human review, accreditation, accessibility certification, legal review, medical review, or publication approval.

## Decision

**PASS — Spanish detailed parity gate closed for progression to Brazilian Portuguese production.**

The Spanish edition remains a working master, not a publication candidate. Sentence-level polishing can continue during trilingual QA, but no material structural, wage/date, credential-scope, regional-pathway, source-ledger, or assurance-boundary mismatch was identified in this gate.

## 1. Structural parity — PASS

Both controlled editions retain the same numbered Section 1 through Section 19 sequence and the same major functional coverage:

1. guide use;
2. role definition;
3. duties and realistic work cycles;
4. career fit, conditions, and safety;
5. ethics, boundaries, privacy, and escalation;
6. income, benefits, and outlook;
7. education and credentials;
8. free/low-cost training, funding, scholarships, and employer support;
9. apprenticeships/work-based learning and career ladders;
10. employer-supported learning and repayment agreements;
11. accessibility and inclusion;
12. privacy, cybersecurity, and ethical AI;
13. evidence of ability;
14. interview preparation;
15. first 30/60/90 days;
16. advancement, portability, and exit planning;
17. pre-enrollment/payment/signing controls;
18. twelve-week action plan; and
19. decision and cost worksheets.

The Spanish edition also retains the controlled source ledger and version/maintenance controls after Section 19.

## 2. High-impact numerical and date parity — PASS

The following material values remain equivalent in meaning across English and Spanish:

| Control | English source | Spanish edition |
|---|---|---|
| BLS official proxy median annual wage | `$51,030` | `US$51,030` |
| BLS proxy hourly wage | `$24.54/hour` | `US$24.54 por hora` |
| BLS projected growth | `11%` | `11%` |
| BLS projection period | `2024–2034` | `2024–2034` |
| ZipRecruiter annual market estimate | `$41,023/year` | `US$41,023/año` |
| ZipRecruiter hourly market estimate | `$19.72/hour` | `US$19.72/hora` |
| ZipRecruiter as-of date | `July 16, 2026` | `16 de julio de 2026` |
| Canada grouping | `NOC 42201` | `NOC 42201` |
| Canada national low/median/high | `C$19.00/C$26.00/C$36.06` | `C$19.00/C$26.00/C$36.06` |
| Job Bank summary date | `June 2, 2026` | `2 de junio de 2026` |
| Job Bank wage-table update | `November 19, 2025` | `19 de noviembre de 2025` |
| Job Bank reference period | `2023–2024` | `2023–2024` |
| SAMHSA page update date in ledger | `March 24, 2026` | `24 de marzo de 2026` |

The Spanish text preserves the distinction between official occupational data and non-government market estimates rather than collapsing them into one salary claim.

## 3. Income and source-label controls — PASS

The Spanish edition preserves all material qualifications:

- BLS Community Health Workers remains a clearly labeled **official occupational proxy**, not a dedicated Peer Support Specialist wage series.
- ZipRecruiter remains a clearly labeled **non-government market estimate** and is not described as an official statistic or guarantee.
- Canada Job Bank remains the broader **NOC 42201** grouping rather than an exact wage guarantee for every peer-support role.
- Colombia and the rest of Latin America retain the no-invented-wage rule where no directly comparable official occupational series has been verified.

## 4. Credential, scope, and portability controls — PASS

The Spanish edition preserves the following safety-critical meanings:

- SAMHSA core competencies are a practice framework, not a universal U.S. national license.
- State, Tribal, payer, program, and employer requirements must be verified locally.
- Canada NOC classification does not create one identical credential requirement for every peer-support job.
- Colombia community mental-health and mutual-help pathways do not establish a U.S.-style nationwide Certified Peer Support Specialist credential.
- WHO guidance is an international conceptual framework, not a portable occupational credential.
- Peer support does not become psychotherapy, diagnosis, medication management, licensed casework, legal advice, or emergency clinical practice unless a worker separately holds and acts within the required authorization.

## 5. Regional terminology review — PASS with controlled preferences

The edition is sufficiently neutral for Latin American use. Preferred terminology for the remaining trilingual cycle is:

- `peer support` → `apoyo entre pares`;
- `peer support specialist` → `especialista en apoyo entre pares`;
- `peer worker` → `persona trabajadora par` or a natural sentence-level equivalent;
- `self-disclosure` → `autorrevelación`;
- `recovery` → `recuperación` where the behavioral-health context is clear;
- `behavioral health` → `salud conductual`, while retaining official English institutional terms where needed;
- `work-based learning` → `aprendizaje basado en el trabajo` or a legally accurate local explanation;
- `Registered Apprenticeship` remains an official U.S. program term and must not be generalized as a legally identical Latin American apprenticeship category; and
- `scope` should use `alcance`, `límites de la función`, or `ámbito de actuación` according to context rather than mechanical one-word substitution.

No terminology choice in the reviewed master was found to create a materially broader clinical authority or credential claim than the English source.

## 6. Source-ledger destination parity — PASS for controlled source set

The Spanish ledger retains the same principal official/non-government destinations used by the frozen English source:

- SAMHSA core competencies;
- SAMHSA peer support workers;
- U.S. Bureau of Labor Statistics Community Health Workers;
- Apprenticeship.gov;
- CareerOneStop / American Job Centers;
- Federal Student Aid;
- ZipRecruiter Peer Support Specialist Salary;
- Government of Canada Job Bank summary and wage pages;
- Colombia Ministerio de Salud y Protección Social community mental-health and policy pages;
- SENA;
- Servicio Público de Empleo; and
- WHO peer-support mental-health-services publication.

A final live-link retest remains required after the Portuguese edition is complete and before artifact publication.

## 7. Accessibility, encoding, and assurance boundaries — PASS for source stage

The Spanish master retains hierarchical Markdown headings, short paragraphs, direct instructions, lists, explicit warnings, and readable table-free source text suitable for later DOCX/PDF production. No independent human certification, professional translation certification, accreditation, legal review, medical review, or accessibility certification is claimed.

Publication-level screen-reader behavior, DOCX style semantics, PDF tagging/reading order, rendered layout, embedded hyperlinks, metadata, and accessibility inspection remain future gates.

## 8. Reusable automation added

A deterministic checker was added at:

`scripts/guide02_translation_parity.py`

with workflow:

`.github/workflows/guide02-translation-parity.yml`

The checker fails closed on:

- missing or reordered Sections 1–19;
- UTF-8 BOM/replacement-character/non-LF defects;
- missing high-impact wage/date facts;
- source-URL-set divergence;
- loss of official-proxy/non-government-market labels;
- loss of key credential/portability limitations; and
- obvious unsupported certification, employment-guarantee, or salary-guarantee language.

The automated workflow result must be recorded separately when GitHub executes it; this QA record does not falsely represent a pending workflow as passed.

## Next controlled gate

Proceed to the **Brazilian Portuguese v2 working master** from the same frozen English source. After Portuguese production, run English↔Spanish↔Portuguese terminology, structural, numeric/date, source-ledger, and claims parity QA before DOCX/PDF generation.

## Controlled status

**Spanish detailed parity: PASS.**  
**Guide 02 publication status: HOLD — Portuguese and trilingual artifact QA remain incomplete.**
