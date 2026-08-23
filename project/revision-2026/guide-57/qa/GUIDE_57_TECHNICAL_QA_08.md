# Guide 57 — Technical QA 08

**Guide:** 57 — Medical Equipment Repairer  
**Result:** PASS  
**Date:** 2026-08-19

## Inputs

- Frozen English: `GUIDE_57_MEDICAL_EQUIPMENT_REPAIRER_ENGLISH_v2.md` — blob `961643b735d4ff085fe5a65eeaabccbaa77ef8aa`
- Spanish es-419: `GUIDE_57_MEDICAL_EQUIPMENT_REPAIRER_SPANISH_es-419_v1.md`
- Portuguese pt-BR: `GUIDE_57_MEDICAL_EQUIPMENT_REPAIRER_PORTUGUESE_pt-BR_v1.md`

## Technical QA controls

PASS — all three masters are UTF-8 text without replacement-character or BOM defects.

PASS — trilingual section coverage is complete and preserves the controlled source structure.

PASS — source URL parity is complete across English, Spanish, and Portuguese.

PASS — U.S. BLS controlled values are semantically preserved in all editions: 62,630; 30.11; 68,000; 76,800; 13%; 8,800; 7,300; 39,060; 99,290; 74,560; 66,640; 62,000; 61,030; 42,650.

PASS — Canada Job Bank values are semantically preserved: 24.04; 35.58; 55.34; November 19, 2025; 2023–2024 reference data.

PASS — Colombia controls are preserved: SENA `Mantenimiento de Equipo Biomédico`, Tecnólogo, 24 months, 2024 Caldas locator, INVIMA technovigilance.

PASS — FDA servicing-versus-remanufacturing boundary is present in all three languages and does not authorize improvised design changes.

PASS — safety, decontamination, return-to-service, traceability, privacy, cybersecurity, responsible-AI, credential-transfer, title-protection, scam, and escalation boundaries are present in all three languages.

PASS — no edition claims independent human certification, professional translation certification, accreditation, licensure approval, legal review, clinical approval, employment guarantee, or earnings guarantee.

## Publication controls required

The publication workflow must:

1. use Pandoc reader `gfm-tex_math_dollars` so USD/CAD dollar values cannot become TeX math;
2. validate controlled values by semantic representation and not force pt-BR punctuation onto source-reported wage figures;
3. verify URL parity before conversion;
4. generate three DOCX and three PDFs;
5. validate DOCX package integrity and searchable PDF text;
6. render and inspect every PDF page;
7. fail if any rendered page has an edge margin below 2 pixels;
8. reconcile PDF page counts with rendered-page counts;
9. generate publication metadata and SHA-256 checksums; and
10. update Publication and Release Audit to PASS only after every control succeeds.

## Gate decision

Technical QA: **PASS**.
