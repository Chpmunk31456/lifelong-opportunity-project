# Guide 42 — Portuguese Localization QA Gate 07

**Guide:** 42 — Painter and Coating Worker  
**Locale:** Brazilian Portuguese (`pt-BR`)  
**Branch:** `revision/guide-00-100-2026`  
**Source master:** `project/revision-2026/guide-42/working-masters/GUIDE_42_PAINTER_AND_COATING_WORKER_ENGLISH_v2.md`  
**Localized master:** `project/revision-2026/guide-42/working-masters/GUIDE_42_PAINTER_AND_COATING_WORKER_PTBR_v2.md`  
**Gate result:** **PASS**

## QA scope

The Brazilian Portuguese edition was reviewed against the frozen English source after the English and Spanish controlled gates had passed. The review was fail-closed and focused on factual, structural, terminology, safety, jurisdiction, compensation, source, and non-guarantee parity.

## Controls reviewed

- **Occupational scope parity — PASS.** Construction/maintenance painting remains distinct from industrial coating/painting. Training, hazards, machinery, wages, and credential expectations are not blended.
- **Structure and sequencing — PASS.** The edition preserves the substantive order and coverage of occupation scope, duties, physical demands, safety, hazardous legacy coatings, spray finishing, respiratory protection, skills, entry pathways, jurisdictional pathways, funding, compensation, starter plan, transferable experience, advancement, AI, cybersecurity/privacy, scams, spending cautions, sources, and limitations.
- **Safety boundary parity — PASS.** Stop-and-escalate controls remain explicit for unknown lead/asbestos or other hazardous legacy materials, ventilation, respirators, grounding, ignition sources, work at height, confined/enclosed spaces, incompatible materials, and unauthorized equipment/processes.
- **Regulatory references — PASS.** OSHA references remain unchanged and jurisdiction-limited: 29 CFR 1926.62, 29 CFR 1910.107, and 29 CFR 1910.134.
- **Jurisdiction qualifiers — PASS.** U.S., Canada, Colombia, and Latin America/Caribbean pathways remain separated. Red Seal remains an interprovincial framework rather than a universal license. SENA/OCUPACOL references retain current-availability and jurisdiction qualifiers.
- **Numeric/date/currency parity — PASS.** Controlled SOC/NOC/CIUO identifiers, U.S. BLS/O*NET figures, Canada Job Bank CAD wage figures, years, growth rates, occupational counts, openings, and 12-week plan values are preserved.
- **Compensation evidence boundary — PASS.** Compensation remains source-tied and explicitly non-guaranteed; the edition does not convert national statistics or individual vacancy evidence into promised starting pay.
- **Credential/non-guarantee controls — PASS.** The edition does not imply that short training creates licensure, Red Seal status, respirator qualification, confined-space authorization, hazardous-material authorization, inspection authority, or guaranteed employment/earnings.
- **AI/privacy/cybersecurity boundary parity — PASS.** AI remains limited to low-risk assistance and cannot replace SDS/TDS, exposure assessments, respirator selection/fit testing, ventilation engineering, fall protection, confined-space procedures, hazardous-material determinations, coating specifications, inspection criteria, or employer-approved work instructions. Confidential-data restrictions remain explicit.
- **Source/URL set integrity — PASS.** The controlled official/public URL set is preserved for BLS, O*NET, OSHA, Red Seal, Canada Job Bank, OCUPACOL, SENA, OIT/Cinterfor, and SENCE.
- **Encoding and placeholder review — PASS.** Brazilian Portuguese diacritics and punctuation are UTF-8 readable. No replacement-character corruption, TODO markers, translation placeholders, or unresolved template tokens were introduced.
- **Natural readability — PASS.** The language is professional, direct Brazilian Portuguese rather than a literal word-for-word rendering, while technical names, codes, URLs, legal/regulatory labels, dates, figures, and evidence boundaries remain intact.
- **Assurance boundary — PASS.** The edition does not claim independent human certification, professional translation certification, accessibility certification, legal review, environmental approval, accreditation, guaranteed employment, or guaranteed earnings.

## Release decision

**Portuguese Localization: PASS.**

The `pt-BR` master is approved to proceed to trilingual Technical QA. Publication is not approved by this localization gate; trilingual structural/source/numeric/link/encoding controls, DOCX/PDF build validation, rendering, checksums, Publication, and Release Audit remain separate fail-closed gates.
