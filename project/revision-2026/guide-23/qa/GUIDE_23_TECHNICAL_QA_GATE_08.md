# Guide 23 — Technical QA gate 08

**Guide:** 23 — Property Manager and Community Association Manager  
**Date:** 2026-08-10  
**Stage:** Trilingual technical QA  
**Status:** **PASS**

## Evidence

GitHub Actions workflow `Guide 23 controlled publication build` run **31382045579** completed successfully after the publication validator was corrected to use the exact CareerOneStop and Government of Canada Job Bank URLs contained in the frozen trilingual source set.

The successful run verified all three controlled source editions for:

- level-2 structural parity;
- required U.S., Canada, Colombia, WIOA, apprenticeship, wage, licensing, and source URLs;
- required WIOA, SENA, Apprenticeship.gov, Ley 675 de 2001, NOC 13101, and AI/IA markers;
- UTF-8 encoding controls, absence of replacement characters, and absence of placeholder text;
- DOCX ZIP integrity and required document payload;
- valid searchable PDFs with substantial extractable text;
- all-page PDF raster rendering;
- metadata manifest and SHA-256 checksum generation.

The generated manifest records **PASS** for English, `es-419`, and `pt-BR`, with 11, 8, and 8 PDF pages respectively.

## Assurance boundary

This is controlled internal automated QA. It is not independent human review, professional translation certification, accessibility certification, legal review, property-management licensing advice, accreditation, or an employment or earnings guarantee.
