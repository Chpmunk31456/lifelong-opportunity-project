# Guide 53 — Baseline Inventory 01

**Guide:** 53 — Physical Therapist Assistant  
**Branch:** `revision/guide-00-100-2026`  
**Date:** August 19, 2026  
**Status:** **PASS**

## Legacy package present

The repository contains the published Guide 53 package at `53-physical-therapist-assistant/` with separate English, Spanish, and Portuguese trees.

The English edition currently includes:

- `english/README.md` identifying Guide 53 as **Physical Therapist Assistant**, version 1.0, July 2026;
- an editable DOCX under `english/docx/`;
- a searchable PDF under `english/pdf/`; and
- `english/QC.md` recording an eight-page release candidate.

## Baseline defects and controlled-revision needs

1. **No editable source master is present in the legacy English tree.** The current package exposes README/QC plus DOCX/PDF artifacts, so Version 2 must be reconstructed into an auditable Markdown working master rather than editing the publication binary as the source of truth.
2. **The English README begins with a UTF-8 BOM.** Version 2 source files should be normalized to plain UTF-8 without a BOM or replacement characters.
3. **Legacy QA is incomplete for the 2026 revision standard.** The QC record covers rendering/searchability and selected layout checks, but it does not provide current-source traceability, jurisdiction-specific scope/licensure controls, trilingual structural/source parity, controlled wage/funding evidence, all-page publication QA, metadata, or SHA-256 sealing.
4. **Clinical scope requires stronger fail-closed wording.** Physical therapist assistants work under the direction and supervision of licensed physical therapists in the United States; Version 2 must not imply independent diagnosis, treatment-plan creation, unsupervised practice, or authority that belongs to a licensed physical therapist or another regulated professional.
5. **Cross-jurisdiction title equivalence must not be assumed.** Canada and Colombia may use assistant/rehabilitation-support titles and regulatory structures that are not equivalent to the U.S. PTA credential. Research must distinguish them explicitly before localization.
6. **Current-source refresh is required.** Education/accreditation, licensing/examination, wages/outlook, funding, employer support, and Colombia/Latin America pathways must be reverified with current authoritative sources before English reconstruction.

## Baseline decision

**PASS.** Guide 53 is suitable for controlled reconstruction, but the legacy DOCX/PDF package is not sufficient as the authoritative Version 2 source. Proceed to current-source Research before English Editorial.
