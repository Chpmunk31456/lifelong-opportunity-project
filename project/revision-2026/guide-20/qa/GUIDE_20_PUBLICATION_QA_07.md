# Guide 20 — Publication QA 07

**Guide:** 20 — Court Clerk and Judicial Services Assistant  
**Date:** 2026-08-09  
**Status:** **PASS**

## Automated build evidence

GitHub Actions workflow: `Guide 20 controlled publication build`  
Successful run: **31345686654**  
Result: **SUCCESS**

The controlled workflow completed every build and validation step before committing publication candidates.

## Publication artifacts

The successful build generated and committed:

- `GUIDE_20_ENGLISH_v2.docx`
- `GUIDE_20_ENGLISH_v2.pdf`
- `GUIDE_20_SPANISH_LATAM_v2.docx`
- `GUIDE_20_SPANISH_LATAM_v2.pdf`
- `GUIDE_20_PORTUGUESE_BR_v2.docx`
- `GUIDE_20_PORTUGUESE_BR_v2.pdf`
- `GUIDE_20_PUBLICATION_QA_MANIFEST.json`
- `SHA256SUMS.txt`

under `project/revision-2026/guide-20/publication-candidate/`.

## Machine controls passed

- 19-section trilingual structure;
- controlled numerical values;
- required jurisdiction/source markers;
- required authoritative/source URLs;
- DOCX ZIP integrity and `word/document.xml` presence;
- PDF readability;
- searchable/extractable PDF text;
- all-page raster rendering;
- SHA-256 checksum generation;
- rebase-safe publication commit.

## Manifest results

Automated manifest status: **PASS**.

| Edition | DOCX bytes | PDF bytes | PDF pages | Extractable PDF characters | Status |
|---|---:|---:|---:|---:|---|
| English | 28,184 | 364,866 | 19 | 33,576 | PASS |
| Spanish (es-419) | 27,888 | 360,942 | 19 | 32,420 | PASS |
| Portuguese (pt-BR) | 27,792 | 361,091 | 19 | 31,729 | PASS |

All six binary publication artifacts have recorded SHA-256 checksums in the committed checksum file.

## Publication decision

**PASS.** Guide 20 has a complete machine-validated trilingual DOCX/PDF publication package and may proceed to final release audit.

## Assurance boundary

This is internal project publication QA. It is not independent legal review, court approval, professional translation certification, accessibility certification, civil-service determination, accreditation, licensing approval, or an employment guarantee.