# Guide 02 English artifact divergence hold 04

- **Guide:** 02 — Peer Support Specialist
- **Date:** 2026-08-07
- **Workflow:** Guide 02 English artifact extraction QA
- **Workflow run:** `31146029169`
- **Job:** `92765541110` (`extract-and-compare`)
- **Branch:** `revision/guide-00-100-2026`
- **Control status:** **HOLD — authoritative English baseline not yet selected**
- **Scope:** Existing English v1.0 DOCX and PDF only
- **Nature of review:** Automated technical extraction and source-equivalence control. This is not independent human certification, accreditation, professional translation certification, accessibility certification, legal review, or factual validation.

## Reproduced artifact evidence

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `02-peer-support-specialist/english/docx/Lifelong_Opportunity_Peer_Support_Specialist_Guide_English_v1.0.docx` | 47,103 | `73a3c177c6ce0531f22483c75f76702b1d41ccaffa669dd4ce4d5dafcd2c827c` |
| `02-peer-support-specialist/english/pdf/Lifelong_Opportunity_Peer_Support_Specialist_Guide_English_v1.0.pdf` | 361,526 | `8086942769c1759af1695988032204b135ad7b8bae6f6d6b3955dd9bc61f50c1` |

## DOCX technical intake

- Required OOXML parts missing: **None**
- Extracted non-empty paragraphs: **295**
- External relationships: **0**
- Title metadata: `Lifelong Opportunity Peer Support Specialist Guide English v1.0`
- Creator metadata: `Alberto (Al) Leiva`
- DOCX normalized extracted characters: **19,004**

## PDF technical intake

- Pages: **10**
- Encrypted: **False**
- Strict parser: **pypdf strict mode passed**
- Extracted characters before normalization: **27,446**
- PDF normalized extracted characters: **26,999**
- Title metadata: `Lifelong Opportunity Peer Support Specialist Guide English v1.0`
- Author metadata: `Alberto (Al) Leiva`

## Source-equivalence result

- Normalized DOCX-to-PDF similarity ratio: **0.809991**
- Full normalized containment: **False**
- Required pass threshold: **0.970000**
- Result: **FAIL-CLOSED / HOLD**

The PDF contains approximately 7,995 more normalized extracted characters than the DOCX. This difference is material enough that the two files must not be treated as interchangeable source artifacts without further inspection.

## Controlled decision

1. Do **not** designate either v1.0 artifact as the authoritative English baseline yet.
2. Do **not** weaken the 0.97 source-equivalence threshold merely to force a pass.
3. Treat the DOCX and PDF as two divergent baseline candidates until their textual differences are characterized.
4. Preserve the already completed official-source, funding/training, apprenticeship, jurisdiction, and income research independently of this artifact hold.
5. Next gate: extract and compare the divergent sections, determine which content is unique to each artifact, then select or reconstruct the authoritative English baseline with an auditable rationale before substantive master revision.

## Provenance

The metrics above were emitted by GitHub Actions workflow run `31146029169`, job `92765541110`, after successful checkout, successful installation of the pinned PDF parser, successful DOCX/PDF structural extraction, and the fail-closed source-equivalence comparison. The workflow failed intentionally because similarity was below the controlled threshold.
