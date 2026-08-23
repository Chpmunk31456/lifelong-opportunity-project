# Guide 01 — Brazilian Portuguese Sentence-Level Editorial QA 02

**Guide:** Agente comunitário de saúde  
**Language:** Brazilian Portuguese (`pt-BR`)  
**Branch:** `revision/guide-00-100-2026`  
**Review date:** August 6, 2026  
**Status:** Completed controlled sentence-level editorial review; corrections approved for exact application; not publication certification

## Scope

This review compares the opening occupation, suitability, safety, training, and regional-pathway sections of the Brazilian Portuguese working master against the controlled English master and the approved trilingual terminology controls. The review checks natural Brazilian Portuguese, plain-language readability, preservation of safety meaning, role boundaries, and avoidance of literal English-derived phrasing.

This record does not certify the translation, accessibility conformance, legal compliance, professional accreditation, medical accuracy, or independent human review. Publication remains on hold pending completion of all controlled QA gates.

## Files reviewed

- `working-masters/GUIDE_01_AGENTE_COMUNITARIO_DE_SAUDE_PTBR_WORKING_MASTER.md`
- `working-masters/GUIDE_01_COMMUNITY_HEALTH_WORKER_ENGLISH_WORKING_MASTER.md`
- `TRILINGUAL_TERMINOLOGY_AND_TRANSLATION_CONTROL_01.md`
- `TRILINGUAL_STRUCTURAL_PARITY_QA_01.md`

## Approved editorial corrections

The following exact replacements improve natural Brazilian Portuguese while preserving the controlled meaning.

| No. | Current pt-BR text | Approved replacement | Reason |
|---:|---|---|---|
| 1 | `desescalada de conflitos` | `capacidade de reduzir tensões e lidar com conflitos com segurança` | Avoids an uncommon literal calque and states the practical skill in clear language. |
| 2 | `rotas de escalonamento` | `procedimentos claros para encaminhar situações que excedam as atribuições do trabalhador` | Removes corporate or technical jargon and preserves the worker-safety and scope-of-practice control. |
| 3 | `treinamento de curto prazo no trabalho` | `treinamento de curta duração oferecido no local de trabalho` | Produces more natural Brazilian Portuguese without changing the Bureau of Labor Statistics concept of short-term on-the-job training. |
| 4 | `ações de alcance` | `ações de aproximação e atendimento comunitário` | Replaces a literal rendering of “outreach” with wording that is more readily understood in Brazilian community-health contexts. |

## Safety-meaning reconciliation

The approved replacements preserve these controls:

- urgent clinical, safeguarding, and privacy concerns must be referred to qualified personnel;
- the worker must remain within duties authorized by the employer, program, training, supervision, and local law;
- employers should provide supervision, safety procedures, referral mechanisms, and support for difficult cases;
- short workplace training does not override state, employer, occupational, or professional requirements;
- course completion does not guarantee employment, certification, registration, licensure, promotion, or income.

No correction expands clinical authority, creates a professional license, equates a certificate of completion with regulated certification, or implies guaranteed employment or earnings.

## Controlled application requirements

Before these corrections are considered applied:

1. verify that each current phrase occurs exactly once in the pt-BR working master;
2. apply only the four approved replacements;
3. require strict UTF-8 encoding without a byte-order mark;
4. run Markdown whitespace and heading checks;
5. confirm that no English, es-419, source-register, or workflow file changed in the correction commit;
6. record the resulting commit and workflow identifiers;
7. repeat the safety-meaning check after application.

Any missing, duplicate, or already-divergent source phrase must fail closed and be reviewed rather than replaced approximately.

## QA conclusion

**Sentence-level pt-BR editorial review: PASS WITH FOUR CONTROLLED CORRECTIONS PENDING APPLICATION.**

The reviewed sections are substantively aligned with the English master, but the four phrases above should be corrected before the Brazilian Portuguese editorial freeze. The remaining document must still pass final terminology, structural, live-link, DOCX, PDF, metadata, checksum, rendering, and publication QA.