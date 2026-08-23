# Guide 93 — Baseline Inventory 01

**Guide:** 93 — Surveying and Mapping Technician  
**Controlled branch:** `revision/guide-00-100-2026`  
**Baseline reviewed:** legacy `93-surveying-and-mapping-technician/` package on the live controlled branch  
**Review date:** 2026-08-22

## Legacy package verified

The legacy Guide 93 package contains English, neutral Latin American Spanish, and Brazilian Portuguese reader assets plus language-specific QC records.

### English
- `english/QC.md` — legacy QC reports 7 pages, 23,179 searchable characters, no broken fields, and 42 updated TOC entries.
- **Directory inversion confirmed:** `english/docx/Surveying and Mapping Technician.pdf` is the PDF binary (192,429 bytes; Git blob `9bd1f70059d4ef55b317117aa98bd269c45868c2`).
- **Directory inversion confirmed:** `english/pdf/Surveying and Mapping Technician.docx` is the DOCX binary (46,008 bytes; Git blob `5495ae0eda76d12d6c36b0d5c6f8849f08247a34`).

### Spanish (`es-419`)
- `spanish/docx/Guia_93_T_cnico_en_topograf_a_y_cartograf_a.docx` — 43,134 bytes; Git blob `59de4926ca6d705e5686cab6443d73299866061f`.
- `spanish/pdf/Guia_93_T_cnico_en_topograf_a_y_cartograf_a.pdf` — 122,701 bytes; Git blob `2014dc09973310236e8de26eb62ea9e085205f5e`.
- Legacy QC reports 5 final pages and explicitly labels the file set a publication candidate **pending owner review**.

### Portuguese (`pt-BR`)
- `portuguese/docx/Guia_93_T_cnico_em_Agrimensura_e_Mapeamento_PTBR.docx` — 42,845 bytes; Git blob `7d84ef3ca3392b0709e4f9ca85fa64caffa8c23a`.
- `portuguese/pdf/Guia_93_T_cnico_em_Agrimensura_e_Mapeamento_PTBR.pdf` — 128,659 bytes; Git blob `3bf3e684eef76776670558273d4d2fb21271dd82`.
- Legacy QC reports 6 pages and explicitly labels the file set a publication candidate **pending owner review**.

The legacy folder names and old QC records are inputs only. They do not satisfy the 2026 controlled research, editorial, traceability, localization, technical-QA, publication, or release-audit gates.

## Controlled-revision purpose

The 2026 revision must rebuild Guide 93 from current occupation, labour-market, training, safety, licensing/authority, drone, geospatial, accessibility, privacy/security and responsible-AI evidence. It must not inherit stale figures, ambiguous professional-scope claims, or the English binary-directory inversion.

## Required occupation-specific controls

The revised guide must:
- distinguish **Surveying and Mapping Technician** work from the legally regulated work of a licensed/professional land surveyor or other jurisdiction-specific authorized professional;
- preserve boundaries around legal property lines, cadastral certification, monumentation, signed/sealed survey products and other regulated outputs;
- explain field workflows involving total stations, GNSS/GPS, levels, data collectors, control points, traverses, topographic measurements and office reduction/checking;
- address coordinate systems, datums, units, calibration, tolerances, closure/error checks, metadata, provenance and false precision;
- cover CAD/GIS and current employer technology signals without presenting one vendor tool as universally required;
- address drone/RPA use only within applicable aviation, operator, airspace and organizational rules;
- include field safety for traffic, heat, weather, terrain, construction sites, lone work, PPE and emergency planning;
- protect sensitive coordinates, infrastructure, customer/property information, credentials and restricted imagery;
- constrain AI to approved assistance such as drafting, calculations/code explanation and documentation, with human validation and no invented legal boundaries, authoritative coordinates or survey-grade accuracy;
- include accessible map/report practices and safe synthetic/open-data portfolio options;
- preserve jurisdiction-specific labour-market and training limitations rather than implying wages, credentials, funding, licensing or demand transfer unchanged between countries.

## Gate result

**PASS — Baseline Inventory**

**Blockers:** none.

The English DOCX/PDF directory inversion is a documented legacy input defect, not a blocker, because the controlled revision will reconstruct publication outputs from verified sources rather than reusing folder semantics.

Guide 93 may proceed to Current-source Research.
