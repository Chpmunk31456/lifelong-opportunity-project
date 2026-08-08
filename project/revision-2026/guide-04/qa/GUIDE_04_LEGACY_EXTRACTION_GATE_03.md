# Guide 04 — Legacy English Extraction Gate 03

**Guide:** 04 — Project Coordinator  
**Branch:** `revision/guide-00-100-2026`  
**Status:** HOLD — deterministic content extraction/reconciliation not yet complete  
**Scope:** legacy English DOCX/PDF only

## Purpose

This gate records the verified repository state and the remaining extraction constraint before any revised 2026 English master is constructed or frozen. It is intentionally fail-closed: repository presence, file size, or binary retrievability alone do not count as substantive content reconciliation.

## Verified repository evidence

### DOCX

- Path: `04-project-coordinator/english/docx/Lifelong_Opportunity_Project_Coordinator_Guide_English_v1.0.docx`
- Git blob SHA: `6fe21ac155c8962d65b6a13d389239dc6b710cbd`
- Size: `47,473` bytes
- GitHub Contents API confirms the file on `revision/guide-00-100-2026`.
- A connector-backed base64 retrieval begins with the expected ZIP/OOXML signature (`UEsDB...`), confirming that the object is a DOCX-compatible ZIP container rather than an empty placeholder.

### PDF

- Path: `04-project-coordinator/english/pdf/Lifelong_Opportunity_Project_Coordinator_Guide_English_v1.0.pdf`
- Git blob SHA: `f1119a0b8a2ee680d7bec3acd67d8844e8508fc8`
- Size: `362,133` bytes
- GitHub Contents API confirms the file on `revision/guide-00-100-2026`.

## Workflow evidence

The previously referenced extraction workflow run `31234518136` cannot currently be resolved through the GitHub Actions REST endpoint; the endpoint returns HTTP 404. Therefore no extraction result, job log, or reconciliation artifact from that run is accepted as evidence of PASS.

## Reclassification of the prior blocker

The earlier statement that the GitHub connector could not expose the legacy binary objects was too broad. The connector can retrieve the DOCX as base64 and can resolve both binary objects by path and blob SHA. The actual remaining constraint is narrower: the automation runtime has not yet produced a complete, independently auditable text extraction from those binaries because the connector response is truncated before the full base64 payload can be decoded locally, and the prior Actions run is unavailable.

## Gate decision

**HOLD.** Do not:

- treat the legacy DOCX and PDF as textually reconciled;
- construct or freeze the Guide 04 revised English master from assumed equivalence;
- claim that the prior extraction workflow passed;
- advance to translation or publication QA on the basis of file presence alone.

## Required evidence to clear this gate

At least one auditable path must succeed:

1. a GitHub Actions extraction job that checks out the branch, extracts DOCX XML text and searchable PDF text, records hashes and paragraph/text counts, compares the two legacy sources, and commits or uploads its reconciliation report; or
2. a complete binary download into a local/runtime workspace followed by deterministic DOCX/PDF extraction and a committed reconciliation report.

After extraction, the reconciliation report must identify substantive legacy sections, material DOCX/PDF differences if any, encoding or hyperlink anomalies, and the content that must be retained, corrected, replaced, or expanded in the 2026 English master.

## QA integrity note

This gate makes no claim of independent human certification, professional translation certification, accessibility certification, accreditation, legal review, or financial advice.
