# Guide 03 — Legacy English Extraction and Reconciliation 02

Date: 2026-08-07
Branch: `revision/guide-00-100-2026`
Guide: 03 — Medical Billing and Coding Specialist

## Gate purpose

Deterministically extract the legacy English DOCX and searchable PDF, preserve both text extractions as audit evidence, and measure whether one artifact can safely be treated as the sole source for the 2026 reconstruction. This is a source-reconciliation control, not factual revalidation, publication approval, independent human review, certification, accreditation, or accessibility certification.

## Artifact fingerprints

- DOCX SHA-256: `13406ad51499557806d97dc6271249b24138c6488ef9a628ebceb0afe97f6939`
- PDF SHA-256: `c2aab91b4511a5c3a18828f3ac0b4ebb9d2d1fa1aad73cf7f7f2c8aae3779556`
- DOCX extracted non-empty blocks: 258
- PDF pages: 10
- DOCX extracted characters: 19,396
- PDF extracted characters: 27,602

## Deterministic comparison

- Normalized character-sequence similarity: **0.7265**
- Normalized unique-token Jaccard similarity: **0.9711**
- Material token/fact set only in DOCX: `none detected`
- Material token/fact set only in PDF: `0, 4.0`
- Automated classification: **RECONCILE**

The character score is deliberately sensitive to pagination, line wrapping and repeated PDF headers. The token score is more tolerant of layout noise. Neither score by itself proves substantive equivalence.

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

- `project/revision-2026/guide-03/qa/evidence/guide03_legacy_docx_extract.txt`
- `project/revision-2026/guide-03/qa/evidence/guide03_legacy_pdf_extract.txt`

## Controlled decision

**HOLD for substantive reconciliation.** The extracted evidence is deterministic and auditable, but the 2026 English working master must not be frozen from an automated similarity score alone. Review the extracted substantive sections, identify any PDF-only or DOCX-only material, and record the composite-source decision before drafting the revised master.
