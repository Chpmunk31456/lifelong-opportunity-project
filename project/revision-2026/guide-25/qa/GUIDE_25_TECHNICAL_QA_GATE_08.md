# Guide 25 — Technical QA gate 08

**Guide:** 25 — General Maintenance and Repair Worker / Building Maintenance Technician  
**Date:** 2026-08-10  
**Stage:** Trilingual technical QA  
**Status:** **PASS**

## Evidence

GitHub Actions workflow `Guide 25 controlled publication build` run **31432309599** completed successfully after the fail-closed version-marker defect recorded during the first build attempt was corrected without weakening the remaining controls.

The successful run verified all three controlled source editions for:

- trilingual structural parity;
- required source URLs and URL syntax;
- controlled BLS, Indeed, Canada Job Bank NOC 73201, WIOA/American Job Center, Apprenticeship.gov, SENA/Betowa, Servicio Público de Empleo, accessibility, privacy, responsible-AI, and safety/licensing boundary markers;
- UTF-8/BOM controls and placeholder scan;
- DOCX ZIP integrity;
- valid searchable PDFs with substantial extractable text;
- all-page PDF raster rendering;
- metadata manifest generation; and
- SHA-256 checksum generation.

The generated publication QA manifest records **PASS** for English, `es-419`, and `pt-BR`. Each PDF contains 10 pages. Extractable text counts are 19,733 characters for English, 22,887 for `es-419`, and 22,568 for `pt-BR`.

## Assurance boundary

This is controlled internal automated QA. It is not independent human review, professional translation certification, accessibility certification, legal review, trade-licensing advice, accreditation, or an employment or earnings guarantee.
