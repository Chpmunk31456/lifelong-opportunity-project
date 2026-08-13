# Guide 39 — Brazilian Portuguese Localization QA

**Occupation:** Heavy Equipment Operator  
**Locale:** pt-BR  
**Date:** August 13, 2026  
**Gate:** Portuguese Localization  
**Result:** PASS

## Inputs reviewed

- Frozen English source: `project/revision-2026/guide-39/working-masters/GUIDE_39_HEAVY_EQUIPMENT_OPERATOR_ENGLISH_v2.md`
- Portuguese localization candidate: `project/revision-2026/guide-39/working-masters/GUIDE_39_HEAVY_EQUIPMENT_OPERATOR_PTBR_v2.md`
- Current-source evidence: `project/revision-2026/guide-39/research/GUIDE_39_CURRENT_SOURCE_EVIDENCE_02.md`

## Controlled checks

- **Scope parity — PASS.** The pt-BR edition remains specifically about heavy construction-equipment operation and preserves the distinction from crane/tower operation, forklifts/material-moving equipment, surface-mining equipment, and heavy-equipment mechanics.
- **Safety-critical meaning — PASS.** The localization retains the requirement for employer/site procedures, equipment-specific training, qualified supervision, inspection/defect reporting, PPE/access controls, signaling, utility/excavation controls, traffic/pedestrian separation, shutdown/maintenance authorization, and applicable occupational-safety rules. It does not convert career guidance into operating instruction.
- **Education/pathway parity — PASS.** U.S. O*NET occupation 47-2073.00, Canada NOC 73400, SENA's `Operación de maquinaria pesada para excavación`, Colombia's Sistema Nacional de Cualificaciones, OIT/Cinterfor, apprenticeship, public training, and employer/union/contractor pathways are preserved.
- **Funding/support parity — PASS.** American Job Centers/WIOA, Canada Student Grants and Loans, Colombia/Latin America public training, employer reimbursement, apprenticeship/trainee, union funds, and supervised qualification pathways remain present with the original eligibility and non-guarantee cautions.
- **Numeric parity — PASS.** U.S. official 2025 wage values ($28.78/hour; $59,850/year; 10th percentile $20.28/$42,190; 90th percentile $48.60/$101,090), 489,300 jobs, 3%–4% projected growth, 41,900 annual openings, private U.S. estimates, Canada CAD 24.00/32.50/45.00 wage points, the 2,208-hour SENA program, and relevant source dates are retained without changing their underlying values.
- **Official/private salary labeling — PASS.** O*NET/BLS and Canada Job Bank figures remain clearly separated from supplementary Indeed and Salary.com estimates.
- **Source-link parity — PASS.** The official/public and supplementary salary URLs from the frozen English source are retained in the pt-BR edition without localization-induced URL changes.
- **Terminology — PASS.** Brazilian Portuguese terminology is natural and occupation-appropriate, including `operador de máquinas pesadas`, `equipamentos de construção`, `escavadeira`, `trator de esteiras`, `pá-carregadeira`, `retroescavadeira`, `motoniveladora`, `EPI`, `terraplenagem`, `canteiro/obra`, `treinamento prático supervisionado`, and `segurança e saúde ocupacional`.
- **Accessibility/readability — PASS.** Headings, short paragraphs, ordered steps, bullet lists, explicit cautions, and plain-language explanations remain intact. No decorative formatting was introduced that would impair text-first reading.
- **Encoding — PASS.** The committed file is UTF-8 text and Portuguese diacritics render normally.
- **AI/privacy controls — PASS.** The pt-BR edition retains the prohibition on using AI as a substitute for safety-critical procedures and preserves protections for site plans, drawings, credentials, incident information, project/customer data, geolocation-sensitive infrastructure information, and other protected information.
- **Assurance boundary — PASS.** The localized guide does not claim independent human certification, professional accreditation, certified translation, legal review, financial advice, or guaranteed employment outcomes.

## Gate decision

The Brazilian Portuguese localization is faithful to the frozen English source, natural for a Brazilian Portuguese audience, and preserves occupation-specific, safety, opportunity, wage, source, and assurance controls. **Portuguese Localization: PASS.**

Technical QA, publication, and release audit remain fail-closed pending their own evidence.