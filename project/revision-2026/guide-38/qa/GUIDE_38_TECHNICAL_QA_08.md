# Guide 38 Technical QA — Gate 08

**Guide:** 38 — Dispatcher and Transportation Coordinator  
**Date:** 2026-08-13  
**Stage:** Technical QA Helper  
**Result:** PASS

## Evidence basis

The controlled Guide 38 publication workflow completed successfully in GitHub Actions run `31699219661` after the assurance-claim validator was narrowed so legitimate disclaimer language such as “certified translation” is not misclassified as a positive certification claim.

The successful run executed fail-closed controls across the English, neutral Latin American Spanish (`es-419`), and Brazilian Portuguese (`pt-BR`) editions for:

- trilingual structural parity;
- source URL and required-domain controls;
- controlled numerical-value checks;
- locale-aware terminology controls;
- UTF-8/encoding and placeholder scans;
- DOCX generation and package integrity;
- searchable PDF generation and text extraction;
- all-page PDF raster rendering;
- metadata-manifest generation; and
- SHA-256 checksum generation.

All workflow steps completed successfully. The generated trilingual publication candidates and publication QA outputs were committed to the controlled revision branch in commit `9d3fec78a2bd0f10f35bc943fad1aa735c82e505` (`Build and validate Guide 38 publication candidates`).

## Assurance boundary

This PASS records internal automated technical/publication QA evidence only. It is not independent human certification, professional translation certification, accessibility certification, legal review, certification-body approval, accreditation, or an employment or earnings guarantee.
