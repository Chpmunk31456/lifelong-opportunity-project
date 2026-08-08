# Guide 05 — Legacy English Extraction and Reconciliation 02

Date: 2026-08-08
Branch: `revision/guide-00-100-2026`
Guide: 05 — Bookkeeping and Payroll Specialist

## Gate purpose

Deterministically extract the legacy English DOCX and searchable PDF, preserve both text extractions as audit evidence, and measure whether one artifact can safely be treated as the sole source for the 2026 reconstruction. This is a source-reconciliation control, not factual revalidation, tax or legal advice, publication approval, independent human review, certification, accreditation, or accessibility certification.

## Artifact fingerprints

- DOCX Git blob SHA: `51f522332fc8b91077c6d842c27bee88b6df3e92`
- PDF Git blob SHA: `3a6e258509b7688ceb6dde8322648cbeca82e85d`
- DOCX SHA-256: `959dda5efa6cb362e098bdbebf437427cc670203467902ee282d2420f1d2398d`
- PDF SHA-256: `b4bed1a31f755a450d3ad1f1c5a35806192b90573bde425cd7568d22431f68a5`
- DOCX extracted non-empty blocks: 258
- PDF pages: 10
- DOCX extracted characters: 19,366
- PDF extracted characters: 27,545

## Deterministic comparison

- Normalized character-sequence similarity: **0.7102**
- Normalized unique-token Jaccard similarity: **0.9655**
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

- `project/revision-2026/guide-05/qa/evidence/guide05_legacy_docx_extract.txt`
- `project/revision-2026/guide-05/qa/evidence/guide05_legacy_pdf_extract.txt`

## Controlled decision

**HOLD for substantive reconciliation.** The extracted evidence is deterministic and auditable, but the 2026 English working master must not be frozen from an automated similarity score alone. Review the extracted substantive sections, identify any PDF-only or DOCX-only material, and record the composite-source decision before drafting the revised master.
