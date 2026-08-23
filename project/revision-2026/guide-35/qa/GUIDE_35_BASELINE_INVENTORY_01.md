# Guide 35 Baseline Inventory 01

## Guide

- Number: 35
- Occupation: Production Planning and Expediting Clerk
- Controlled branch: `revision/guide-00-100-2026`
- Verified PR #17 head before this write: `05adda27a1761315fd1c7d7e12721df51e1e77eb`
- Inventory date: 2026-08-12

## Purpose

This record establishes the legacy artifact baseline for Guide 35 before controlled revision work begins. It is an inventory gate only. It does not certify the accuracy, currency, translation quality, accessibility, DOCX/PDF quality, or publication readiness of any legacy artifact.

## Legacy guide root

The live revision branch contains the legacy guide at:

`35-production-planning-and-expediting-clerk/`

The root contains:

- `README.md`
- `english/`
- `spanish/`
- `portuguese/`

The root README identifies the guide as **Production Planning and Expediting Clerk** and points to legacy English, Spanish (Latin America), and Brazilian Portuguese DOCX/PDF editions.

## English legacy inventory

`35-production-planning-and-expediting-clerk/english/` contains:

- `README.md`
- `docx/`
- `pdf/`
- `source/`

The English `source/` directory contains only:

- `qc.md`
- `sources.md`

No complete editable Markdown working master is present in the legacy English source directory. The legacy English DOCX/PDF therefore require controlled extraction/reconciliation rather than being treated as already-current source masters.

The root README labels the English DOCX/PDF as version `v1.0`.

## Spanish legacy inventory

`35-production-planning-and-expediting-clerk/spanish/` contains:

- `README.md`
- `QC.md`
- `docx/`
- `pdf/`

No complete editable Markdown source master is present in this locale directory.

The legacy Spanish filenames shown by the root README contain character-loss/underscore substitutions in words that should contain accented characters. These legacy filenames are evidence of an encoding/naming defect to be corrected during controlled publication work; they are not accepted as current controlled naming.

## Brazilian Portuguese legacy inventory

`35-production-planning-and-expediting-clerk/portuguese/` contains:

- `README.md`
- `QC.md`
- `docx/`
- `pdf/`

No complete editable Markdown source master is present in this locale directory.

The legacy Brazilian Portuguese filenames shown by the root README likewise contain character-loss/underscore substitutions where accented characters would normally appear. This is recorded as a legacy encoding/naming defect for later controlled correction.

## Encoding and metadata observations

The legacy root README begins with a UTF-8 BOM. Controlled Guide 35 working masters and QA evidence should use clean UTF-8 without an unnecessary BOM unless a downstream tool explicitly requires otherwise.

Legacy artifact existence does not establish:

- current factual accuracy;
- current wage or labor-market accuracy;
- source freshness;
- trilingual semantic parity;
- terminology quality;
- accessibility conformance;
- hyperlink health;
- DOCX structural integrity;
- searchable-PDF integrity;
- rendered-page quality;
- publication metadata accuracy; or
- independent human review/certification.

## Controlled revision state before initialization

Before this baseline record was created, `project/revision-2026/guide-35/` did not exist on the verified PR #17 head. Guide 34 was fully closed, making Guide 35 the next sequential controlled guide.

## Baseline result

**PASS — Baseline Inventory**

The legacy artifact set, source gap, locale directories, version signal, and known encoding/naming defects are sufficiently identified to begin current-source research and English reconstruction. This PASS applies only to the inventory gate.

## Next gate

**Research / Current Source Evidence — PENDING**

The next controlled step is to establish current official and clearly labeled non-government evidence for occupation scope, duties, education/training pathways, wages/income, funding and low-cost learning, employer-supported learning, apprenticeships/work-based learning, United States, Canada, Latin America, and Colombia-relevant pathways before revising the English master.
