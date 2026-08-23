# Guide 01 — Direct Status Reconciliation Precheck 02

**Guide:** 01 — Community Health Worker  
**Branch:** `revision/guide-00-100-2026`  
**Control date:** 2026-08-05  
**Gate:** fail closed

## Purpose

Record the exact repository state before applying the trilingual working-master status reconciliation. This record is evidence for the controlled revision process; it is not a publication approval.

## Verified repository state

- Draft PR #17 remains open and intentionally unmerged.
- The branch head inspected for this precheck was `04a8ccb4bfdb7c6248f56b4d54a0df6546783fb6`.
- The English working master still contained the stale review date `August 3, 2026` and the stale status statement saying translation and final link validation remained pending.
- The controlled reconciliation script exists at `scripts/guide01_reconcile_working_master_status.py` with blob SHA `50b2af4cf5b6d80a4602631a8eaed99ae355c86f`.
- The script is fail closed: it requires exactly one controlled match, rejects unexpected UTF-8 BOMs and replacement-character encoding defects, and does not declare Guide 01 publication-ready.

## Required replacements before publication packaging

### English

Replace the stale status with language that accurately records completed trilingual integration, structural-parity review, terminology normalization, market-income reconciliation, and controlled link review, while keeping final editorial freeze, final live-link validation, DOCX/PDF generation, metadata, checksums, and publication QA pending.

### Neutral Latin American Spanish

Replace the stale status with the equivalent es-419 control statement. Do not describe automated QA as professional translation certification, accreditation review, accessibility certification, legal review, or independent human certification.

### Brazilian Portuguese

Replace the stale status with the equivalent pt-BR control statement. Preserve the same publication hold and non-certification restrictions.

## Acceptance criteria

The reconciliation gate passes only when all of the following are true:

1. All three working masters contain the updated status wording exactly once.
2. All three files remain valid UTF-8 without BOM or replacement characters.
3. The review dates are synchronized to the controlled revision date.
4. No text states or implies that Guide 01 is a completed publication candidate.
5. Sentence-level translation review and final live-link validation remain explicitly pending.
6. The resulting commit and any workflow run identifiers are recorded in a subsequent execution-QA record.

## Current disposition

**HOLD.** The precheck is complete, but the trilingual status replacements had not yet been verified as applied at the time of this record. Guide 01 remains in working-master status and must not advance to DOCX/PDF publication packaging until this gate passes.
