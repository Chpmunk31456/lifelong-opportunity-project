# Guide 17 — Publication QA 09

**Guide:** 17 — Bank Teller and Member Services Representative  
**Date:** 2026-08-09  
**Status:** **PASS — controlled publication package**

## Build result

GitHub Actions controlled publication run `31342505793` completed successfully after the publication workflow was hardened for locale-aware numerical validation and rebase-safe artifact publishing.

## Publication artifacts

The controlled publication-candidate directory contains:

- English DOCX and searchable PDF
- neutral Latin American Spanish DOCX and searchable PDF
- Brazilian Portuguese DOCX and searchable PDF
- `GUIDE_17_PUBLICATION_QA_MANIFEST.json`
- `SHA256SUMS.txt`

The Markdown sources used for the build are retained in the same controlled directory for traceability.

## Automated controls passed

The publication manifest records PASS for:

- 19-section trilingual structure;
- locale-aware preservation of controlled numerical values;
- required source URLs;
- DOCX ZIP/package integrity;
- PDF readability;
- searchable/extractable PDF text;
- SHA-256 checksum generation;
- all-page raster rendering.

## Edition results

- English: 20-page PDF; 38,831 extractable characters; PASS.
- es-419: 21-page PDF; 44,051 extractable characters; PASS.
- pt-BR: 21-page PDF; 43,342 extractable characters; PASS.

## Rendering boundary

All PDF pages were raster-rendered successfully by the controlled workflow and uploaded as a workflow artifact. This record does not convert automated raster-generation success into a claim of independent human visual inspection or accessibility certification.

## Gate decision

**PASS.** Guide 17 publication requirements are satisfied for the controlled 2026 revision program and the guide may proceed to the Release Auditor stage.

## Assurance boundary

This is internal project QA. It does not claim independent human review, professional translation certification, accessibility certification, legal review, regulator approval, accreditation, or guaranteed employment, wages, funding, training, promotion, or apprenticeship status.
