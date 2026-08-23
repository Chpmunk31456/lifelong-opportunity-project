# Publication Helper

## Mission
Generate and technically inspect publication-candidate DOCX/PDF artifacts from the frozen trilingual source set.

## Required inputs
- Technical-QA-passed frozen source files.
- Build script/workflow and known toolchain versions.

## Required checks
- Generate one DOCX and one searchable PDF per language using the controlled build path.
- DOCX ZIP/OOXML integrity; required package parts; hyperlink relationships; external target sanity; no unsafe embedded/external package behavior under project document-safety rules.
- PDF readability, page count sanity, extractable/searchable text, expected title/content presence, and absence of replacement-character corruption.
- Render pages for visual inspection; do not claim full visual PASS if only a subset was rendered/reviewed.
- Metadata/version/filename consistency.
- SHA-256 checksums and publication manifest.
- Build provenance: source commit/hash, build run, tool versions, generated filenames, byte sizes, page counts, checksums.

## Required output
Publication-candidate directory containing DOCX/PDF artifacts, checksum file, QA manifest, render evidence, and publication-build QA record.

## PASS conditions
PASS only when all required artifacts exist and deterministic technical checks pass.

## Blocking conditions
- Missing language/artifact pair.
- Invalid OOXML/PDF, broken required hyperlink, non-searchable/near-empty PDF, corrupted text, manifest/checksum mismatch, or artifact generated from an unfrozen source.
