# Guide 07 — Legacy English Extraction and Reconciliation 02

Date: 2026-08-08  
Branch: `revision/guide-00-100-2026`  
Guide: 07 — Customer Service Specialist

## Gate purpose

Deterministically extract the legacy English DOCX and searchable PDF, preserve both text extractions as audit evidence, and measure whether one artifact can safely be treated as the sole source for the 2026 reconstruction. This is a source-reconciliation control, not factual revalidation, publication approval, independent human review, certification, accreditation, or accessibility certification.

## Artifact fingerprints

- DOCX Git blob SHA: `3f78d7f6b78769372403230b83e0e75ef3e13535`
- PDF Git blob SHA: `3a9faaca6757997b511c5cb73e21eb48b5ecc0e1`
- DOCX SHA-256: `855dc8039107ff76a827dbaa2a9745dd1bca99a0f1ea532cad25d7c91811670a`
- PDF SHA-256: `b4e7c6e232cc8e8cc9c74786cfd6b4bb45a6c8f17869e373ceda6f66c4bb9d42`
- DOCX extracted non-empty blocks: 258
- PDF pages: 10
- DOCX extracted characters: 19,286
- PDF extracted characters: 27,390

## Deterministic comparison

- Normalized character-sequence similarity: **0.7311**
- Normalized unique-token Jaccard similarity: **0.9660**
- Material token/fact set only in DOCX: `2024.`
- Material token/fact set only in PDF: `0, 4.0`
- Automated classification: **RECONCILE**

The lower character score is substantially affected by PDF pagination, repeated running headers/footers, layout text, and the embedded license string. The high token Jaccard score indicates close substantive overlap but does not itself prove equivalence.

## DOCX heading inventory

The DOCX contains the complete controlled narrative structure from introductory limits through sections 1–19, including work definition, duties, fit, ethics, pay/outlook, education/credentials, employer-supported learning, accessibility, privacy/cybersecurity/AI, portfolio evidence, interviews, 30/60/90-day planning, advancement, enrollment verification, decision scorecard, twelve-week plan, worksheets, and sources/versioning.

## Preserved extraction evidence

GitHub Actions workflow run `31256539953` completed successfully and uploaded artifact `guide07-legacy-extraction-evidence` (artifact ID `9021537977`, SHA-256 digest `39d0ff980a5168e62892741352af2fd18faf03889245d9407cdbbb4747913636`). The artifact contains the deterministic DOCX extraction, PDF extraction, and generated reconciliation report used for this decision.

## Controlled decision

**PASS to composite-source selection.** The DOCX is the stronger textual spine because it preserves the narrative cleanly without repeated PDF layout text. The PDF remains a secondary reconciliation/layout artifact. The apparent PDF-only `4.0` token is from the CC BY-NC-SA 4.0 running header/license string; the apparent DOCX-only `2024.` token is punctuation-tokenization around the BLS May 2024 statement, not a substantive contradiction. No material PDF-only occupational, wage, funding, accessibility, education, privacy, or career-path fact was identified in this reconciliation pass.

The 2026 English v2 master must still be re-researched and rewritten from current authoritative evidence. Legacy wage, outlook, education, tax/funding, credential, apprenticeship, accessibility, Canada, Latin America, Colombia, privacy/cybersecurity, and AI claims are not treated as current solely because they appear in both legacy artifacts.
