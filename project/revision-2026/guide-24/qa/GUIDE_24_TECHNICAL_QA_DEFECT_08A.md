# Guide 24 — Technical QA defect record 08A

**Guide:** 24 — Facilities Coordinator and Building Operations Assistant  
**Date:** 2026-08-10  
**Stage:** Trilingual technical QA  
**Status:** **FAIL — localization gates reopened**

## Evidence

GitHub Actions workflow **Guide 24 controlled publication build**, run **31407371355**, failed closed at the trilingual structural, link, encoding, and source-control step before DOCX/PDF generation.

The validator confirmed that the English Version 2.0 source contains the current controlled evidence set, but the es-419 and pt-BR sources still reflect an earlier localization state.

### Material localization drift detected

Both localized editions were missing controlled current-source elements that are present in the frozen English source and Guide 24 evidence register, including:

- BLS May 2025 OEWS facilities-manager wage source;
- the current Indeed Facility Coordinator estimate used as the non-government coordinator-level comparison;
- the exact CareerOneStop WIOA training-finder URL;
- the Canada Job Bank Building Operator - Maintenance comparison under NOC 73201;
- the SENA Circular 282 de 2024 learner-support source; and
- the NOC 73201 controlled marker.

The automated comparison also found level-2 heading-count drift (`en: 17`, `es-419: 16`, `pt-BR: 16`) and URL-count drift (`en: 16`, `es-419: 12`, `pt-BR: 12`).

Manual inspection of the localized U.S. and Canada sections confirms this is substantive drift rather than a validator false positive: the localized files retain older Salary.com/PayScale compensation text and omit the newer controlled coordinator comparison and Building Operator NOC 73201 context.

## Required remediation

1. Reopen es-419 localization and align it to the frozen English Version 2.0 source while preserving natural neutral Latin American Spanish.
2. Reopen pt-BR localization and align it to the same frozen English source while preserving natural Brazilian Portuguese.
3. Refresh each localization QC record only after content, terminology, structure, warnings, figures, dates, and source URLs are reconciled.
4. Re-run the Guide 24 controlled publication workflow.
5. Technical QA must remain PENDING until a successful run produces and validates the trilingual DOCX/PDF publication candidates, rendering evidence, metadata manifest, and checksums.

## Assurance boundary

This defect record is internal controlled QA evidence. It is not independent human review, professional translation certification, accessibility certification, legal review, trade-licensing advice, accreditation, or an employment or earnings guarantee.
