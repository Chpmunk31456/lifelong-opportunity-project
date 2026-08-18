# Guide 47 — Technical QA publication preflight 08A

**Guide:** 47 — Pharmacy Technician  
**Branch:** `revision/guide-00-100-2026`  
**Date:** August 18, 2026  
**Authoritative branch head at preflight start:** `95da3cc39a6c1a81003c6be579571c51a18e0367`  
**Gate status after this preflight:** **PENDING — full controlled publication build still required**

## Purpose

This preflight records the controls verified before advancing Guide 47 into the full trilingual technical/publication workflow. It does not substitute for DOCX/PDF generation, rendered-page inspection, metadata checks, checksums, or final publication/release gates.

## Live-state reconciliation

- PR #17 is open, Draft, and unmerged.
- The active branch is `revision/guide-00-100-2026`.
- `GUIDE_47_HELPER_STATUS.json` records Baseline Inventory, Research, English Editorial, Evidence/Traceability, English Source Freeze, Spanish Localization, and Portuguese Localization as **PASS**.
- `technical_qa`, `publication`, and `release_audit` remain **PENDING**.
- No `publication-candidate` directory was present on the live branch at the start of this preflight, so no downstream gate is inferred from uncommitted or unavailable workflow artifacts.

## Trilingual source-set preflight

The frozen English, `es-419`, and `pt-BR` working masters were inspected at the live branch head. Their **Current sources** sections preserve the same controlled URL set, including:

- O*NET occupation, wage, and employment-trend sources;
- U.S. Bureau of Labor Statistics Pharmacy Technicians;
- CareerOneStop licensing, certification, and WIOA locators;
- Apprenticeship.gov;
- Federal Student Aid FAFSA guidance;
- Government of Canada Job Bank summary, requirements, and wages;
- Canada Student Grants and Loans;
- SENA occupational and Betowa pharmacy-services sources;
- Colombia pharmaceutical-service regulatory compilation;
- OIT/Cinterfor and its institutional network; and
- the clearly labeled non-government Indeed salary source.

No alternate localized endpoints were observed in the inspected source sections. Exact set equality remains enforced by the controlled publication workflow and must pass there before Technical QA can close.

## Controlled numeric/classification preflight

The frozen English master visibly contains the controlled anchors used by the publication validator, including:

- O*NET/SOC `29-2052.00`;
- U.S. official median `USD $22.00/hour` and `USD $45,750/year`;
- approximately `490,400` workers in 2024, `6 percent` projected growth, and about `49,000` annual openings;
- non-government Indeed estimate `USD $21.13/hour`;
- Canada NOC `32124` and national wages `CAD $17.50 / $24.83 / $34.20` per hour;
- Colombia CNO `3315`;
- SENA Técnico en Servicios Farmacéuticos duration `2,640 hours`; and
- minimum age `16+`.

The Spanish and Portuguese masters preserve the same substantive values using locale-appropriate thousands separators where applicable. The publication workflow remains fail-closed on those values.

## Regulated-scope and safety controls

The frozen English source explicitly states that pharmacy technicians work under pharmacist direction/supervision and that legal scope varies by jurisdiction. It prohibits treating this guide as pharmacy-practice instruction, medical/prescribing advice, controlled-substance procedure, or authorization to perform regulated acts.

The trilingual masters retain controls covering:

- pharmacist supervision and escalation of clinical questions;
- patient/product identification and verification;
- controlled-substance security and diversion prevention;
- compounding and advanced-preparation boundaries;
- hazardous-drug/sharps exposure controls;
- privacy, cybersecurity, and protected pharmacy data;
- responsible AI use that does not replace authorized pharmacy systems or pharmacist review; and
- explicit non-claims for independent human certification, professional pharmacy/medical review, legal/regulatory review, professional translation certification, accessibility certification, accreditation, guaranteed licensure/registration, employment, funding, or earnings.

## Workflow review

`.github/workflows/guide47-publication-build.yml` is configured to:

1. freeze the three validated working masters as publication candidates;
2. run trilingual structural, exact source-set, numeric, terminology, UTF-8, placeholder, and regulated-scope controls;
3. probe live source-link behavior while failing on explicit HTTP 404/410 responses;
4. generate DOCX and PDF editions;
5. validate DOCX integrity and searchable PDF text;
6. render and inspect every PDF page for blank pages and edge clipping;
7. create publication metadata and SHA-256 checksums;
8. upload rendered-page QA evidence; and
9. commit controlled publication candidates only after all prior steps pass.

These controls are materially aligned with the established controlled-publication pattern used by preceding guides.

## Decision

**Preflight evidence: PASS. Technical QA gate: PENDING.**

The content/source preflight found no reason to weaken or bypass the existing controlled workflow. Guide 47 must remain at Trilingual Technical QA until a complete publication build produces committed candidates and all document/render/metadata/checksum controls pass. Only then may `technical_qa` be advanced in `GUIDE_47_HELPER_STATUS.json`.