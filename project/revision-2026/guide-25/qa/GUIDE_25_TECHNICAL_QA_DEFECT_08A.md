# Guide 25 — Technical QA defect 08A

**Guide:** 25 — General Maintenance and Repair Worker / Building Maintenance Technician  
**Date:** 2026-08-10  
**Stage:** Trilingual technical QA  
**Status:** **FAIL-CLOSED / REMEDIATION REQUIRED**

## Trigger

GitHub Actions workflow `Guide 25 controlled publication build` run **31432144501** failed during `Trilingual structural, link, encoding, and source controls` before DOCX/PDF generation.

## Finding

The three controlled source editions use Markdown metadata formatted as `**Version:** 2.0 controlled revision` (and localized equivalents). The initial workflow marker expected a plain `Version 2.0` / `Versión 2.0` / `Versão 2.0` sequence and therefore reported the version marker missing in all three languages.

This is a QA-rule defect rather than source-content drift: the controlled version metadata is present, but the regular expression did not account for the colon and Markdown bold delimiters.

## Required remediation

Adjust only the version-marker expression so it recognizes the controlled Markdown metadata form while preserving all other fail-closed structural, source URL, encoding, placeholder, document-integrity, searchable-PDF, rendering, metadata, and checksum controls. Re-run the complete workflow. Do not advance technical QA or publication to PASS unless the corrected run succeeds.

## Assurance boundary

This defect record documents internal automated QA behavior. It is not independent human review, professional translation certification, accessibility certification, legal review, trade-licensing advice, accreditation, or an employment or earnings guarantee.
