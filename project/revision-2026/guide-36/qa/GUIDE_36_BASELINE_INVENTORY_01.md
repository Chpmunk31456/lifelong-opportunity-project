# Guide 36 Baseline Inventory 01

## Guide

- Number: 36
- Occupation: Warehouse and Inventory Control Specialist
- Controlled branch: `revision/guide-00-100-2026`
- Verified PR #17 head before this write: `a7e36a1a69cbef3782b9aec418842a0204932ce1`
- Inventory date: 2026-08-12

## Purpose

This record establishes the legacy artifact baseline for Guide 36 before controlled revision work begins. It is an inventory gate only. It does not certify the accuracy, currency, translation quality, accessibility, DOCX/PDF quality, or publication readiness of any legacy artifact.

## Legacy guide root

The live revision branch contains the legacy guide at:

`36-warehouse-and-inventory-control-specialist/`

The root contains:

- `README.md`
- `english/`
- `spanish/`
- `portuguese/`

The root README identifies the guide as **Warehouse and Inventory Control Specialist** and points to legacy English, Spanish (Latin America), and Brazilian Portuguese DOCX/PDF editions.

## English legacy inventory

`36-warehouse-and-inventory-control-specialist/english/` contains:

- `README.md`
- `docx/`
- `pdf/`
- `source/`

The English `source/` directory contains only:

- `qc.md`
- `sources.md`

No complete editable Markdown working master is present in the legacy English source directory. The legacy English DOCX/PDF therefore require controlled extraction/reconciliation rather than being treated as already-current source masters.

The English README labels the publication edition as version `1.0`, published in July 2026.

The legacy source summary is U.S.-centric. It identifies the U.S. Bureau of Labor Statistics occupation family **Shipping, Receiving, and Inventory Clerks**, uses a May 2024 national median pay figure of **$43,190**, and explicitly notes that apprenticeship, education, accessibility, labor, safety, and other jurisdiction-specific statements require current official verification. That source note is useful historical evidence, but it is not sufficient for the expanded 2026 controlled-revision standard.

## Spanish legacy inventory

`36-warehouse-and-inventory-control-specialist/spanish/` contains:

- `README.md`
- `docx/`
- `pdf/`

No locale-level QC file or complete editable Markdown source master was surfaced in the verified legacy Spanish directory.

The legacy Spanish filenames shown by the root README contain character-loss/underscore substitution in `Almac_n`, where an accented character would normally appear. This is recorded as a legacy encoding/naming defect to be corrected during controlled publication work; the filename is not accepted as current controlled naming.

## Brazilian Portuguese legacy inventory

`36-warehouse-and-inventory-control-specialist/portuguese/` contains:

- `README.md`
- `QC.md`
- `docx/`
- `pdf/`

No complete editable Markdown source master is present in this locale directory.

The legacy Brazilian Portuguese filenames shown by the root README contain character-loss/underscore substitution in `Armaz_m`, where an accented character would normally appear. This is recorded as a legacy encoding/naming defect for later controlled correction.

## Encoding and metadata observations

The legacy root README begins with a UTF-8 BOM. Controlled Guide 36 working masters and QA evidence should use clean UTF-8 without an unnecessary BOM unless a downstream tool explicitly requires otherwise.

Legacy artifact existence does not establish:

- current factual accuracy;
- current wage or labor-market accuracy;
- source freshness;
- United States, Canada, Latin America, or Colombia pathway completeness;
- current free/low-cost training, funding, scholarship, employer-support, apprenticeship, or work-based-learning availability;
- separation of official wage evidence from current non-government estimates;
- trilingual semantic parity;
- terminology quality;
- accessibility conformance;
- hyperlink health;
- DOCX structural integrity;
- searchable-PDF integrity;
- rendered-page quality;
- publication metadata accuracy; or
- independent human review, certification, translation certification, accreditation, legal review, or financial advice.

## Controlled revision state before initialization

Before this baseline record was created, `project/revision-2026/guide-36/` did not exist on the verified PR #17 head. Guide 35 had completed its controlled release-audit gate, making Guide 36 the next sequential controlled guide.

## Baseline result

**PASS — Baseline Inventory**

The legacy artifact set, source gap, locale directories, version signal, known encoding/naming defects, and limitations of the legacy source summary are sufficiently identified to begin current-source research and English reconstruction. This PASS applies only to the inventory gate.

## Next gate

**Research / Current Source Evidence — PENDING**

The next controlled step is to establish current official and clearly labeled non-government evidence for occupation scope, duties, education/training pathways, wages/income, funding and free/low-cost learning, scholarships, employer-supported learning, apprenticeships/work-based learning, United States, Canada, Latin America, and Colombia-relevant pathways before revising the English master.
