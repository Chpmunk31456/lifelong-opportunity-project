# Guide 63 — Portuguese Localization QA

**Occupation:** Library Assistant and Library Technician  
**Locale:** Brazilian Portuguese (`pt-BR`)  
**Review date:** 2026-08-20  
**Gate:** Portuguese Localization — PASS

## Source control

Portuguese was localized directly and independently from the frozen English Version 2 master:

`project/revision-2026/guide-63/working-masters/GUIDE_63_LIBRARY_ASSISTANT_AND_LIBRARY_TECHNICIAN_ENGLISH_v2.md`

Frozen English Git content/blob identity:

`73d877f8903bfc85cb8c17a7257250ec8f3cc30d`

The Spanish localization was not used as the source text.

## Parity checks

- Top-level section order and controlled meaning: PASS
- Exact official-source URL parity: **11/11**
- UTF-8 readability: PASS
- Replacement characters: none observed
- U.S. occupational codes preserved exactly:
  - SOC 25-4031
  - SOC 43-4121
- Canada occupational codes preserved exactly:
  - NOC 52100
  - NOC 14300
- Colombia classification preserved exactly:
  - CNO 1351
- U.S. wage/outlook values preserved:
  - $19.22/hour technician median
  - $17.31/hour assistant median
  - $18.05/hour / $37,540 combined median
  - 7% decline from 2024 to 2034
  - about 25,800 openings per year
- Canada wage values preserved:
  - C$28.00/hour technician median
  - C$23.17/hour assistant median
  - C$15.80 / C$23.17 / C$34.00 published range
- Education distinctions preserved: PASS
- Canada non-regulated language remains qualified as Job Bank's current record, not a universal legal conclusion: PASS
- Colombia assistant-level pathway is not represented as professional bibliotecólogo authority: PASS
- Copyright Section 108 remains conditional and non-legal-advice: PASS
- Patron privacy/confidentiality boundaries preserved: PASS
- Accessibility authority limits preserved: PASS
- AI protected-data restrictions preserved: PASS
- Cybersecurity escalation and no out-of-scope investigation boundary preserved: PASS
- Physical-work guidance remains non-procedural and employer-training dependent: PASS
- No guaranteed employment, earnings, funding, licensing, certification, accreditation, or professional status introduced: PASS

## Language quality

The edition uses Brazilian Portuguese with controlled occupation identifiers and official classification labels retained where translating them could alter source meaning. Colombian official terms such as `Auxiliares de biblioteca` and `bibliotecólogo` remain in their relevant jurisdictional context.

## Assurance boundary

This QA is internal machine-assisted controlled-project review. It does not claim independent human linguistic certification, professional translation certification, legal review, accessibility certification, or accreditation.

**Result: PASS.** Portuguese localization is suitable to advance the controlled sequence to Trilingual Technical QA.