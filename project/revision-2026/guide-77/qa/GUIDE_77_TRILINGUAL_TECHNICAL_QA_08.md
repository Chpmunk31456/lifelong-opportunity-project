# Guide 77 — Trilingual Technical QA 08

**Stage:** Trilingual Technical QA — **PASS**

English, neutral Latin American Spanish (`es-419`), and Brazilian Portuguese (`pt-BR`) masters were reviewed as one controlled set after the English source freeze and both localization gates.

## Controlled parity verified

- O*NET-SOC `27-1024.00`, Canada NOC `52120`, and Colombia OCUPACOL / CIUO 2166 comparison scope are preserved.
- WCAG 2.2 values `4.5:1`, `3:1`, and the SC 1.4.11 non-text contrast boundary are preserved without claiming automatic WCAG or legal accessibility conformance.
- Canada Job Bank values remain C$20.00 / C$31.25 / C$52.88 per hour with 2023–2024 national reference period and November 19, 2025 update context.
- SENA `Desarrollo de Medios Gráficos Visuales` remains identified as a Tecnólogo listing with 3,984 hours, with cohort/modality/seat verification required.
- U.S. official O*NET/BLS values remain $39,520 (10th percentile), $62,960 median / $30.27 per hour, and $104,910 (90th percentile).
- U.S. Indeed estimate remains approximately $23.41/hour with displayed $13.25–$41.36/hour range, August 2, 2026 update, about 6.1k observations and prior 36-month source window; it is explicitly labeled non-government market evidence.
- Colombia Indeed junior estimate remains COP 1,902,446/month, 26 reported salaries, July 29, 2026 update and explicit small-sample/title limitation.
- All 13 frozen source URLs are present in all three masters.

## Technical and assurance boundaries verified

The three editions preserve:

- graphic-design versus production-art versus prepress scope distinctions;
- print-production controls for bleed, trim, resolution, color, fonts, linked assets, packaging, proofing and version control;
- copyright, licensing, trademark, model/property release and provenance escalation boundaries;
- privacy, confidentiality, MFA, password, approved-storage, phishing/malware and file-sharing safeguards;
- responsible generative-AI limits, including no upload of protected information to unapproved services and mandatory authorized-human verification;
- accessibility-aware design guidance without claiming certification;
- funding/training/apprenticeship availability caveats;
- ethical portfolio rules and prohibition on misrepresenting authorship;
- repaired 30-day action plan and final-design checklist semantics;
- no employment, earnings, funding, licensing, certification, freelance-work or client-acquisition guarantee.

## Structural and localization QA

- No placeholder text, `TODO`, or translation-pending markers were introduced.
- Locale-specific prose is natural rather than mechanically literal while controlled technical terms, codes, source names, URLs, dates and numeric evidence retain the frozen meaning.
- Currency and decimal notation remain unambiguous.
- Source URLs remain verbatim so publication-link QA can validate one shared source set.
- No new factual claims were introduced by either localization.

**Result:** PASS.  
**Blockers:** none.

Publication remains fail-closed until the generated DOCX/PDF editions pass integrity, searchable-text, all-page rendering, page-count reconciliation, link, metadata and checksum controls.
