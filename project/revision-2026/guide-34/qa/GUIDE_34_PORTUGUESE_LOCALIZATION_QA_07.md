# Guide 34 — Brazilian Portuguese Localization QA 07

**Guide:** 34 — Quality Control Inspector and Manufacturing Technician  
**Locale:** Portuguese (Brazil), `pt-BR`  
**Candidate:** `project/revision-2026/guide-34/publication-candidate/GUIDE_34_PORTUGUESE_pt-BR_v2.md`  
**Authoritative English source:** `project/revision-2026/guide-34/publication-candidate/GUIDE_34_ENGLISH_v2.md`  
**Frozen English blob:** `3acc14cf631834904a1c41f54d5767d85c3c6025`  
**QA date:** 2026-08-12  
**Result:** **PASS**

## Controlled localization checks

| Control | Result | Evidence / note |
|---|---|---|
| Locale and version metadata | PASS | Candidate identifies Brazilian Portuguese (`pt-BR`), Version 2.0 controlled revision, and 12 August 2026 revision date. |
| Structural parity | PASS | All 22 numbered English sections are represented in the same sequence; subsection intent is retained. |
| Career-scope parity | PASS | Inspector, quality technician, manufacturing technician, production/test/metrology and quality-assurance distinctions remain explicit; no engineering, audit, calibration, regulatory or product-release authority is implied. |
| Safety parity | PASS | Machine guarding, interlocks, stored energy, PPE/EPI, normal-production versus servicing distinction, and stop/escalate conditions are retained. `lockout/tagout` is localized as `bloqueio e etiquetagem` while preserving the English term once for traceability. |
| Numerical parity — U.S. official data | PASS | BLS values preserved: May 2024 median US$47,460; lower 10% US$34,590; upper 10% US$75,510; manufacturing median US$48,170; 2024–2034 ≈0%; ≈69,900 annual openings. Portuguese uses locale-appropriate separators without changing values. |
| Numerical parity — private market estimate | PASS | Indeed date 20 July 2026 and approximately US$22.97/hour preserved and explicitly labeled non-government; Salary.com remains a separate private estimate. |
| Credential parity | PASS | ASQ CQI/CQT names remain proper credential names; CQI US$460 fee and three-year full-time paid experience requirement are preserved with change-warning language and no license/equivalence claim. |
| U.S. funding and apprenticeship | PASS | Employer reimbursement/support, WIOA, American Job Centers, CareerOneStop Scholarship Finder, public colleges, and Registered Apprenticeship boundaries are retained. |
| Canada jurisdiction and wage parity | PASS | Sector-first NOC warning retained. NOC 94212 plastic-products example preserves C$17.77 / C$21.91 / C$30.00 low/median/high figures with locale-appropriate separators and no cross-sector generalization. |
| Colombia pathway parity | PASS | SENA/Betowa, Agencia Pública de Empleo and free-offer caution retained; 3,984-hour Gestión de la Producción Industrial and 2,208-hour Control de Calidad en Confección Industrial figures preserved. |
| Brazil / Latin America parity | PASS | SENAI-SP Inspetor de Qualidade 160-hour example retained; country-by-country verification and non-equivalence boundaries preserved. |
| Training and cost controls | PASS | Free-first/low-cost sequencing, employer support, scholarships, apprenticeships, public technical education, written reimbursement terms, and predatory-program warning signs retained. |
| Measurement / metrology boundaries | PASS | Instrument suitability, calibration-status checks, approved method, inch/metric error risk, and limits on claiming calibration competence retained. |
| Ethics and records | PASS | Traceability, revision control, nonconformance segregation, no backdating/fabrication, and escalation of falsification pressure retained. |
| AI controls | PASS | AI is limited to learning/low-risk support; it is not final authority for product disposition, controlled specifications, safety/LOTO, regulation, legal/compliance or sensitive production data. |
| Cybersecurity/privacy | PASS | MFA, removable media, personal devices, cloud/file-sharing, vendor access, controlled technical data and prohibited convenience transfers to personal AI/cloud/messaging are retained. |
| Accessibility | PASS | Disability-inclusive framing, possible accommodations, essential-function/safety limits and jurisdiction-specific legal framing retained; no accessibility certification is claimed. |
| 12-week plan parity | PASS | Weeks 1–12 remain grouped as 1–2, 3–4, 5–6, 7–8, 9–10 and 11–12 with the same progression and evidence-building intent. |
| Portfolio and truthfulness | PASS | Simulated work must be labeled; proprietary/customer/regulated data exclusions and truthful-scope requirements are retained. |
| Source-map parity | PASS | All 14 controlled source URLs from the English source map are present and unchanged. |
| Encoding / readability | PASS | UTF-8 Portuguese diacritics render correctly in Markdown; prose is natural Brazilian Portuguese rather than word-for-word machine syntax. |
| Assurance boundary | PASS | Candidate explicitly disclaims independent human certification, professional translation certification, accessibility certification, accreditation, legal review, safety approval and employment-placement validation unless separately documented. |

## Focused terminology review

Approved usage in this candidate includes:

- `inspetor de controle de qualidade` / `inspetor de qualidade` according to context;
- `técnico de manufatura` for the manufacturing-technician role family;
- `controle da qualidade`, `garantia da qualidade` and `engenharia da qualidade` as distinct concepts;
- `equipamento de proteção individual (EPI)` for PPE;
- `bloqueio e etiquetagem (lockout/tagout)` for the OSHA hazardous-energy control term;
- `não conformidade`, `rastreabilidade`, `metrologia`, `calibração`, `controle estatístico de processo` and `carta de controle` in standard Brazilian technical usage;
- official program and credential names (BLS, OSHA, WIOA, Registered Apprenticeship, ASQ CQI/CQT, Job Bank/NOC, SENA/Betowa, SENAI) kept recognizable rather than translated into misleading local equivalents.

## QA conclusion

The Brazilian Portuguese Version 2.0 candidate maintains the frozen English guide's substantive claims, safety controls, numerical evidence, jurisdictional distinctions, funding and training pathways, source map and assurance limits while reading naturally for a Brazilian audience. No unsupported credential, accreditation, licensing, translation-certification, employment, wage or safety claim was introduced.

**Portuguese Localization QA: PASS.**
