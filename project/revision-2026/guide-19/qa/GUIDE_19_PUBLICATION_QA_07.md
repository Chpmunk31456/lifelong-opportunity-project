# Guide 19 — Publication QA 07

**Guide:** 19 — Paralegal and Legal Assistant  
**Date:** 2026-08-09  
**Status:** **PASS**

## Automated build evidence

GitHub Actions workflow: `Guide 19 controlled publication build`  
Successful run: **31345260933** (run #2)  
Result: **SUCCESS**

The first run failed closed at the structural/source gate because the validator required the English spelling `California` in all language editions. The Portuguese source correctly used `Califórnia`. The validator was corrected to use locale-aware jurisdiction-marker matching; no substantive content control was removed.

## Publication artifacts

The successful controlled build generated and committed:

- `GUIDE_19_ENGLISH_v2.docx`
- `GUIDE_19_ENGLISH_v2.pdf`
- `GUIDE_19_SPANISH_LATAM_v2.docx`
- `GUIDE_19_SPANISH_LATAM_v2.pdf`
- `GUIDE_19_PORTUGUESE_BR_v2.docx`
- `GUIDE_19_PORTUGUESE_BR_v2.pdf`
- `GUIDE_19_PUBLICATION_QA_MANIFEST.json`
- `SHA256SUMS.txt`

under `project/revision-2026/guide-19/publication-candidate/`.

## Machine controls passed

The successful action passed all of the following before committing publication candidates:

- 19-section trilingual structural sequence;
- locale-aware controlled numerical values;
- locale-aware jurisdiction markers;
- required authoritative/source URLs;
- DOCX ZIP integrity and presence of `word/document.xml`;
- PDF readability through `pdfinfo`;
- searchable/extractable PDF text through `pdftotext`;
- all-page PDF raster rendering;
- SHA-256 checksum generation;
- rebase-safe publication commit.

## Manifest results

Automated manifest status: **PASS**.

| Edition | DOCX bytes | PDF bytes | PDF pages | Extractable PDF characters | Status |
|---|---:|---:|---:|---:|---|
| English | 30,218 | 360,646 | 20 | 38,115 | PASS |
| Spanish (es-419) | 30,873 | 362,518 | 20 | 40,434 | PASS |
| Portuguese (pt-BR) | 30,919 | 363,900 | 20 | 39,892 | PASS |

All six binary publication artifacts have recorded SHA-256 checksums in the committed checksum file.

## Publication decision

**PASS.** Guide 19 has a complete, machine-validated trilingual DOCX/PDF publication package and may proceed to final release audit.

## Assurance boundary

This is internal project publication QA. It is not independent legal review, professional translation certification, accessibility certification, accreditation, regulator approval, or an employment guarantee.