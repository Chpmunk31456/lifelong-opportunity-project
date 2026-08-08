# Guide 06 — Legacy English Extraction and Reconciliation 02

Date: 2026-08-08
Branch: `revision/guide-00-100-2026`
Guide: 06 — Administrative Assistant and Office Coordinator

## Gate purpose

Deterministically extract the legacy English DOCX and searchable PDF, preserve both text extractions as audit evidence, and measure whether one artifact can safely be treated as the sole source for the 2026 reconstruction. This is a source-reconciliation control, not factual revalidation, legal or financial advice, publication approval, independent human review, certification, accreditation, or accessibility certification.

## Artifact fingerprints

- DOCX Git blob SHA: `733d8d64ff30b726b905242d479a8e2ebbd73f99`
- PDF Git blob SHA: `2c3b64a0c92f78e6dbe3bbf3e87a6387a76b3d91`
- DOCX SHA-256: `b156079226aa5590e4afa8bf106ed65866037b63fe41e4ac1f459d30b8f11645`
- PDF SHA-256: `e58e6c139f735740fce627d9a14f38433a59a6f85e9081d08d99ff9e5533ffc3`
- DOCX extracted non-empty blocks: 258
- PDF pages: 10
- DOCX extracted characters: 19,483
- PDF extracted characters: 27,792

## Deterministic comparison

- Normalized character-sequence similarity: **0.7314**
- Normalized unique-token Jaccard similarity: **0.9694**
- Material token/fact set only in DOCX: `none detected`
- Material token/fact set only in PDF: `0, 4.0`
- Automated classification: **RECONCILE**

The character score is deliberately sensitive to pagination, line wrapping, and repeated PDF headers. The token score is more tolerant of layout noise. Neither score by itself proves substantive equivalence.

## DOCX heading inventory

- Why I Created This Guide
- Acknowledgment of AI Assistance
- Ethical and Practical Limits
- How This Guide Relates to the Foundation Guide
- Table of Contents
- 1. How to Use This Guide
- Decision rules
- 2. What the Work Is
- Definition, titles, and settings
- 3. Duties, Tools, and Work Cycles
- Core duties
- A realistic work cycle
- 4. Fit, Conditions, and Safety
- Career-fit questions
- Who should pause
- 5. Ethics, Boundaries, and Escalation
- Scope and stop-work rules
- 6. Pay, Benefits, and Outlook
- National context
- Local wage research
- 7. Education and Credentials
- Free-first pathway
- School and credential verification
- 8. Employer-Supported Learning
- Tuition benefits and repayment
- Internships, apprenticeships, and career ladders
- 9. Accessibility and Inclusion
- Accommodations across the pathway
- 10. Privacy, Cybersecurity, and Ethical AI
- Responsible information use
- 11. Build Evidence of Ability
- Portfolio projects and résumé evidence
- 12. Interview Preparation
- Questions and answer guidance
- 13. First 30, 60, and 90 Days
- Entry plan
- 14. Advancement, Portability, and Exit Planning
- Career movement and retained value
- 15. Before You Enroll or Sign
- Verification checklist
- 16. Is This Career Right for Me?
- Decision scorecard
- 17. Twelve-Week Action Plan
- Sequential plan
- 18. Worksheets
- Cost and agreement worksheets
- 19. Sources, Versioning, and Maintenance
- Official sources and review policy

## Evidence files

- `project/revision-2026/guide-06/qa/evidence/guide06_legacy_docx_extract.txt`
- `project/revision-2026/guide-06/qa/evidence/guide06_legacy_pdf_extract.txt`

## Controlled decision

**HOLD for substantive reconciliation.** The extracted evidence is deterministic and auditable, but the 2026 English working master must not be frozen from an automated similarity score alone. Review substantive sections, identify PDF-only or DOCX-only material, and record the composite-source decision before drafting the revised master.
