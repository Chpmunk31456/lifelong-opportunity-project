# Guide 46 — Trilingual Technical QA Gate 08

**Guide:** 46 — Environmental Field Technician  
**Branch:** `revision/guide-00-100-2026`  
**Date:** August 18, 2026  
**Controlled publication workflow source:** `bc15353a063d7b5825d427b22406c5b230dfed45`  
**Publication-candidate commit:** `0002ff2fe7c4c3577a903205a3212dc0432eb7f9`  
**Gate result:** **PASS**

## Preconditions

Baseline Inventory, Current-source Research, English Editorial, Evidence/Traceability, English Source Freeze, Spanish Localization (`es-419`), and Portuguese Localization (`pt-BR`) are PASS. Spanish corrective history remains preserved in QA 06 and 06B rather than hidden.

## Deterministic trilingual source controls

`GUIDE_46_AUTOMATED_SOURCE_DIAGNOSTIC.json` reports overall **PASS** with no failures:

- English: 24 H2 sections, 26 direct source URLs, no missing required markers, no missing controlled numeric values, at least two controlled 2,208-hour references, and no encoding/legacy defects.
- Spanish (`es-419`): 24 H2 sections, 26 direct source URLs, no missing required markers, no missing controlled numeric values, no URL differences from English, at least two controlled 2,208-hour references, and no encoding/localization defects.
- Portuguese (`pt-BR`): 24 H2 sections, 26 direct source URLs, no missing required markers, no missing controlled numeric values, no URL differences from English, at least two controlled 2,208-hour references, and no encoding/localization defects.

Controlled occupational and pathway values include SOC `19-4042`, O*NET `19-4042.00`, NOC `22300`, U.S. `49,490 / 23.79 / 36,130 / 85,630 / 40,400 / 42,100 / +1,600 / +4 / 5,600`, Canada `22.00 / 33.89 / 51.10`, and SENA `2,208 / 2,208 / 2,112` hour controls.

## Live-link behavior

The controlled link diagnostic checked all 26 English-source URLs and recorded:

- total URLs: 26;
- explicit broken 404/410 results: **0**;
- unverified responses: 3;
- two BLS pages returned HTTP 403 to the automated probe and were correctly classified as access-controlled/unverified rather than broken or content-verified; and
- SUIN-Juriscol timed out at transport level and was correctly classified as transport-unverified.

The gate therefore preserves the project's verification boundary: an access or transport limitation is not falsely represented as content verification, while explicit 404/410 would fail the link gate.

## Controlled build and artifact QA

The workflow-produced commit `0002ff2fe7c4c3577a903205a3212dc0432eb7f9` has commit message `Build and validate Guide 46 publication candidates` and created the controlled publication-candidate package.

`GUIDE_46_PUBLICATION_QA_MANIFEST.json` reports overall **PASS** and edition-level PASS:

- English: DOCX 28,352 bytes; PDF 238,402 bytes; 16 PDF pages / 16 rendered pages.
- Spanish (`es-419`): DOCX 29,744 bytes; PDF 242,989 bytes; 17 PDF pages / 17 rendered pages.
- Portuguese (`pt-BR`): DOCX 29,645 bytes; PDF 243,487 bytes; 17 PDF pages / 17 rendered pages.

The workflow generated three DOCX files and three searchable PDFs, validated DOCX structure, validated searchable PDF text and Unicode integrity, rendered every PDF page, checked for malformed/blank/clipped pages, required exact PDF/render page-count agreement, generated the publication manifest, and generated SHA-256 checksums.

`SHA256SUMS.txt` contains six hashes, one for each DOCX/PDF artifact.

## Safety, environmental-data, and AI controls

Technical QA preserves the frozen-source boundaries that:

- HAZWOPER is conditional and is not represented as universal qualification;
- PPE and required respirator use remain employer/program controlled;
- confined-space entry/rescue and other specialized high-risk work are not taught or authorized;
- field sampling remains governed by the approved project plan/SOP/method, laboratory/client requirements, and applicable rules;
- sample identity, chain of custody, contemporaneous observations, instrument/calibration records, anomaly handling, and documented corrections remain protected;
- fabricated, backfilled, silently normalized, substituted, or concealed environmental data is prohibited;
- AI may not make real sampling-method, PPE/respirator, safety, compliance, or field-data decisions; and
- confidential client, site, laboratory, geolocation, access, security, and investigation data remains protected from unauthorized AI/cloud use.

## Decision

**Trilingual Technical QA: PASS.** Guide 46 may proceed to Controlled Publication.

This is internal automated project QA. It does not claim independent human review, professional translation certification, accessibility certification, legal or environmental review, laboratory or engineering approval, industrial-hygiene or medical review, hazardous-waste qualification, respiratory-protection qualification, confined-space or rescue qualification, sampling-method approval, regulatory/licensing determination, accreditation, guaranteed funding, employment, or earnings.
