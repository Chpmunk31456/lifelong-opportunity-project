# Repository Status

This page records what is actually present in the repository. It should be updated whenever guides or language editions are added or release validation materially changes.

## Snapshot — August 2026

- Intended sequence: Guides 00–100
- Guide folders present: 101
- English editions with both DOCX and PDF: 101
- Spanish editions with both DOCX and PDF: 101
- Brazilian Portuguese editions with both DOCX and PDF: 101
- Total publication-format pairs represented: 303 DOCX + 303 PDF
- Known DOCX/PDF availability gaps: None

The presence of a language directory or publication file does not by itself establish exact translation equivalence, independent human linguistic review, professional certification, accreditation, legal review, or accessibility certification. Review claims must remain limited to evidence actually recorded in the repository.

## Complete-collection release baseline — August 2026

The repository now contains the complete 101-guide collection in English, Latin American Spanish, and Brazilian Portuguese, with both DOCX and PDF publication formats for every guide/language combination.

Release-hardening work completed on `main` includes:

- completion of the remaining Spanish publication editions;
- correction of structurally incomplete Brazilian Portuguese publication editions;
- correction and validation of Guide 63 across all three languages;
- repository-level document-safety controls and release-validation tooling;
- repository-wide DOCX security validation reporting 303 discovered, 303 passed, 0 failed;
- repository completeness validation reporting 101 numbered guides (00–100), 101 Spanish folders, and no unexpected DOCX/PDF pairing defects; and
- a Windows PowerShell 5.1 validator fix verified on a Windows GitHub Actions runner so the release validator reaches the final completeness stage reliably.

See [COMPLETE_COLLECTION_RELEASE.md](./COMPLETE_COLLECTION_RELEASE.md) for the release baseline, evidence summary, limitations, and follow-on review status.

## Controlled 2026 content revision

A separate controlled revision program is continuing in draft PR #17 to revalidate and expand individual guides under the 2026 opportunity standard. That program is a content-refresh track and is not the basis for the present file-availability release baseline. Until each revised guide passes its own controlled gates, the existing published edition remains the repository edition of record.

## Status Labels

- **DOCX + PDF:** Both formats are present in the language folder.
- **PDF only:** The PDF is present but the editable DOCX is absent.
- **Not present:** No DOCX or PDF was found for that language.

## Next Review

Review all guides by July 2027 or sooner after material changes to wages, outlook, licensing, accreditation, apprenticeships, education benefits, worker protections, technology, accessibility, or official links.

## README normalization — July 2026

- Main README updated to reflect complete six-file availability for all 101 guides
- 101 guide-level READMEs normalized
- 303 language-level READMEs normalized
- All generated local download links validated
- Audit records stored under `project/`
- Exact source equivalence and human linguistic review remain separate quality questions
