# Guide 41 — Technical QA corrective diagnosis 08A

**Guide:** 41 — Carpenter and Cabinetmaking Technician  
**Branch:** `revision/guide-00-100-2026`  
**Date:** August 14, 2026  
**Controlled publication run:** `31786641340`  
**Gate status after diagnosis:** **PENDING — corrective repair required**

## Failure location

The controlled publication workflow failed in `Run trilingual structural source numeric and terminology controls`. The workflow correctly stopped before link validation, DOCX/PDF generation, rendering, metadata, checksums, or publication commit.

## Confirmed defects

### 1. Spanish source-URL parity drift

The frozen English master is authoritative. The `es-419` master does not currently preserve the exact frozen English source set. The failed control reported missing English URLs for the SENA Betowa program, Apprenticeship.gov, Canadian Job Bank requirements/wages, Canadian skilled-trades/apprenticeship support pages, and the Salary.com Cabinet Maker source, while the Spanish edition contains alternate or additional endpoints.

This is a genuine localization/source-parity defect. The repair must update the Spanish source list to the exact URLs present in the frozen English master rather than weakening the parity control.

### 2. Portuguese missing WIOA source URL

The `pt-BR` master is missing the frozen English CareerOneStop WIOA training-resource URL:

`https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx`

The Portuguese source list must add that exact URL.

### 3. Assurance-marker validator is Markdown-brittle

The frozen English master contains the required assurance boundary as `does **not** claim independent human certification...`. The validator searches the folded text for the contiguous phrase `does not claim independent human certification`; Markdown emphasis interrupts that literal substring. Equivalent localized assurance language is affected for the same reason.

This is a validator defect, not an assurance-content defect. The repair should normalize Markdown emphasis before marker comparison or use an equivalently strong robust marker. The assurance boundary must not be weakened.

### 4. 60-hour regex does not accept the frozen English form

The frozen English master states that the SENA program is a `60-hour` in-person complementary program. The current controlled regex is `60\s*(?:hour|hora)`, which accepts whitespace but not the hyphen in `60-hour`.

The controlled repair should accept both hyphenated English and localized whitespace forms, for example `60[-\s]*(?:hour|hora)`, while continuing to require the numeric value 60.

## Controls that must remain fail-closed

The corrective repair must not bypass or weaken:

- trilingual structural parity;
- exact frozen-English source-URL parity;
- controlled occupational/classification and wage values;
- apprenticeship, Red Seal, Canada, Colombia, funding, AI/privacy, and assurance terminology;
- UTF-8 and placeholder checks;
- live source-link behavior;
- DOCX and searchable-PDF integrity;
- all-page rendering QA;
- publication metadata and SHA-256 checksums.

## Decision

**Corrective diagnosis: PASS. Technical QA gate: PENDING.**

The failure is understood and bounded. Repair the two localization source-parity defects and the two validator defects, then rerun the full controlled publication workflow. Do not advance `technical_qa` in `GUIDE_41_HELPER_STATUS.json` until a complete replacement run passes all required controls.
