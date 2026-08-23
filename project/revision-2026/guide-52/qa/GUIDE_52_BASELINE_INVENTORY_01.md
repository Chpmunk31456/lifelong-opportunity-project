# Guide 52 — Baseline Inventory 01

**Guide:** 52 — Surgical Technologist  
**Branch:** `revision/guide-00-100-2026`  
**Date:** August 19, 2026  
**Gate:** Baseline Inventory  
**Status:** **PASS**

## Legacy package inventory

The repository contains the legacy Guide 52 package at `52-surgical-technologist/` with English, Spanish, and Portuguese publication trees. The English tree contains a README, QC note, DOCX directory, and PDF directory. Equivalent language-package trees are present for Spanish and Portuguese.

The legacy English README identifies the edition as Version 1.0, published July 2026, with DOCX and searchable PDF availability. It also states that exact source equivalence and independent human linguistic review should not be assumed unless separately documented.

## Controlled-revision findings

1. No Guide 52 controlled revision workspace or fail-closed helper-status manifest existed under `project/revision-2026/guide-52/` before this gate.
2. The legacy package does not provide a controlled editable English Version 2 master suitable for the current sequential revision workflow; the canonical content is embodied in the publication package and must be reconstructed under current-source controls before localization.
3. The English README begins with a UTF-8 byte-order-mark representation at the document start. Encoding normalization is therefore a required editorial control for the reconstructed master.
4. Existing Spanish and Portuguese editions are legacy publication editions. They are not treated as proof of current source parity, terminology parity, or controlled localization against a newly frozen English source.
5. Surgical technology is regulated/supervised clinical operating-room work. Scope, credential expectations, sterile-technique boundaries, state/provincial or national regulation, and training pathways must be revalidated from current sources before editorial reconstruction.
6. Cross-country title equivalence must not be assumed. In particular, Colombia's `instrumentación quirúrgica` pathway may represent a broader professional scope than a U.S. surgical technologist role and requires separate jurisdiction-specific treatment.
7. Current-source research must distinguish official wage data from any supplementary non-government market estimates and must verify funding, apprenticeship/work-based learning, public/low-cost training, Canada, Latin America, and Colombia pathways before the English source is frozen.
8. No claim of independent human certification, professional translation certification, accessibility certification, accreditation, legal review, or guaranteed employment/income may be introduced without separate evidence.

## Required controlled sequence

The first incomplete gate after this inventory is **Current-source Research**. Subsequent gates remain fail-closed until their own evidence exists:

- English Editorial / Version 2 reconstruction
- Evidence / Traceability QA
- English Source Freeze
- Spanish Localization (`es-419`)
- Portuguese Localization (`pt-BR`)
- Trilingual Technical QA
- Publication
- Release Audit

## Decision

**Baseline Inventory: PASS.** The legacy package has been identified and bounded, known encoding/source-control limitations are documented, and Guide 52 is ready for current-source research. No downstream gate is advanced by this inventory.