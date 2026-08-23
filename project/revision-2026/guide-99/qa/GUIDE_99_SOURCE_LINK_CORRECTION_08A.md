# Guide 99 — Source Link Correction 08A

**Status:** PASS
**Date:** 2026-08-22

Publication link QA found that FDA reader URLs returned HTTP 404 from the GitHub Actions runner even where current web indexing still exposed the pages. The underlying food-safety statements remain supported. To make the controlled release independently verifiable and automation-stable, the three reader references now use federal primary sources:

1. Current Good Manufacturing Practice → eCFR 21 CFR Part 117, Subpart B: `https://www.ecfr.gov/current/title-21/chapter-I/subchapter-B/part-117/subpart-B`
2. Hazard Analysis and Risk-Based Preventive Controls → eCFR 21 CFR Part 117, Subpart C: `https://www.ecfr.gov/current/title-21/chapter-I/subchapter-B/part-117/subpart-C`
3. FDA Food Safety Modernization Act statutory source → official GovInfo Public Law 111-353 PDF: `https://www.govinfo.gov/content/pkg/PLAW-111publ353/pdf/PLAW-111publ353.pdf`

The three controlled language masters retain identical reader-URL sets after correction. Occupational mappings, compensation values, training pathways, safety boundaries, responsible-AI controls, accessibility guidance, and substantive translations were not changed.

**Revalidated frozen English Git blob:** `01532eb45deb081709a0a7d8a031edd5f7b8d3ad`

Affected controlled gates 03–08 were rechecked for the URL-only maintenance change and remain **PASS**. Publication and Release Audit remain fail-closed and may advance only after the corrected trilingual package passes automated build, link, DOCX, searchable-PDF, all-page render, checksum, and evidence checks.
