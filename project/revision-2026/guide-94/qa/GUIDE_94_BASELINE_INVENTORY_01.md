# Guide 94 — Baseline Inventory

## Occupation
Civil Engineering Technician

## Controlled branch
`revision/guide-00-100-2026`

## Sequential predecessor
Guide 93 — Surveying and Mapping Technician — is fully closed through Publication PASS and Release Audit PASS before this workspace is initialized.

## Legacy publication baseline
The controlled branch contains the legacy Guide 94 publication at `94-civil-engineering-technician/` with a root README and separate English, Spanish, and Brazilian Portuguese edition directories.

The legacy English README identifies the edition as **Version 1.0**, published **July 2026**. These files are therefore the comparison baseline for the controlled 2026 revision, not current-source evidence by themselves.

### Legacy metadata and QA records
- Root README: `94-civil-engineering-technician/README.md` — blob `a14e69693fe6ebdeca1ea3ecb10688013aec080f`
- English README: `94-civil-engineering-technician/english/README.md` — blob `609f21b1cad85a3161db6468e32f936b8551a52d`
- English QC: `94-civil-engineering-technician/english/QC.md` — blob `f7343f80438fea501236691627c4753eb94a2bf5`; reports 7 pages and 23,157 searchable characters
- Spanish README: `94-civil-engineering-technician/spanish/README.md` — blob `dd0bd53491140c67d9acd87dd7849225fd6ddc34`
- Spanish QC: `94-civil-engineering-technician/spanish/QC.md` — blob `8067df7ac64d6908a74ed3cee7960431064d7a61`; reports 5 pages and labels the file a publication candidate pending owner review
- Brazilian Portuguese README: `94-civil-engineering-technician/portuguese/README.md` — blob `d1ded9dd49060f5ad7bb4734fbccbe260cb77c0d`
- Brazilian Portuguese QC: `94-civil-engineering-technician/portuguese/QC.md` — blob `d26549f85e0ce8bff837df35a1f103c64edf03a6`; reports 6 pages and labels the file a publication candidate pending owner review

### Legacy publication binaries
English:
- DOCX: `94-civil-engineering-technician/english/docx/Civil Engineering Technician.docx` — blob `81936879c617efd8c863d5a92b553bf373671fad` — 45,957 bytes
- PDF: `94-civil-engineering-technician/english/pdf/Civil Engineering Technician.pdf` — blob `48e55e065bad34aa5ff638d28eb80f77af7e41c3` — 192,405 bytes

Spanish (`es-419` target for controlled revision):
- DOCX: `94-civil-engineering-technician/spanish/docx/Guia_94_T_cnico_en_ingenier_a_civil.docx` — blob `96c776e8a724081f3bb62806e3a0afa1d476f466` — 43,114 bytes
- PDF: `94-civil-engineering-technician/spanish/pdf/Guia_94_T_cnico_en_ingenier_a_civil.pdf` — blob `17499e099cba96eba39c7c47f6958bc3ed75d3fb` — 122,394 bytes

Brazilian Portuguese (`pt-BR` target for controlled revision):
- DOCX: `94-civil-engineering-technician/portuguese/docx/Guia_94_T_cnico_em_Engenharia_Civil_PTBR.docx` — blob `72eb380f41bc8a8e3fbe07db1ceaff8c5e906bea` — 42,864 bytes
- PDF: `94-civil-engineering-technician/portuguese/pdf/Guia_94_T_cnico_em_Engenharia_Civil_PTBR.pdf` — blob `8ad6f38866f03990ecffc086cff1b2d9e5ce9596` — 128,464 bytes

## Baseline anomalies and controls
1. The root and English README files begin with a UTF-8 BOM; controlled Markdown working masters should be normalized to UTF-8 without an unnecessary BOM.
2. Spanish and Portuguese binary filenames visibly lost accented characters (`T_cnico`, `ingenier_a`). The controlled publication package must use stable ASCII-safe or correctly encoded normalized filenames and must not inherit this ambiguity.
3. Legacy page counts differ materially across editions (English 7, Spanish 5, Portuguese 6). This is not proof of translation error, but it requires structural and semantic parity review after the English source is rebuilt and frozen.
4. The Spanish and Portuguese QC records describe publication candidates pending owner review; they cannot be treated as evidence of certified translation or controlled trilingual equivalence.
5. The legacy package contains DOCX/PDF outputs and metadata/QC Markdown, but no frozen controlled Markdown source master for the guide body. The controlled revision therefore requires a new source-backed English Markdown master before localization.
6. Legacy files are evidence inputs only. They do not establish current factual accuracy, current wage/training information, exact trilingual equivalence, independent human review, accreditation, legal/engineering certification, or controlled 2026 publication readiness.

## Controlled-revision requirements
Guide 94 must be rebuilt sequentially under the expanded opportunity standard, including:

- current occupation/classification and labour-market evidence;
- official United States and Canadian wage/outlook evidence plus clearly labelled current non-government market estimates;
- United States, Canada, Latin America, and Colombia education, funding, scholarship, employer-support, and work-based-learning pathways where supportable;
- technician-versus-licensed-engineer scope boundaries and jurisdiction-specific professional-practice cautions;
- construction/site safety, field documentation, measurement, materials/testing, CAD/BIM/GIS/data handling, accessibility, privacy, cybersecurity, and responsible-AI controls as relevant;
- neutral Latin American Spanish and Brazilian Portuguese localization only after English source freeze;
- terminology, structural, links, DOCX, PDF, metadata, checksum, all-page rendering, publication, and release-audit QA;
- no unsupported claim of independent human certification, professional translation certification, accreditation, engineering/legal review, accessibility certification, funding approval, employment guarantee, or earnings guarantee.

## Gate result
**PASS — Baseline Inventory**

No blocker identified for current-source research.
