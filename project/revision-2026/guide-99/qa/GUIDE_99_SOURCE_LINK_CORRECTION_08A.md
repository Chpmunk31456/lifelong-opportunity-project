# Guide 99 — Source Link Correction 08A

**Status:** PASS
**Date:** 2026-08-22

Publication link QA identified three FDA reader URLs returning HTTP 404 from the GitHub Actions runner. The underlying food-safety statements remain supported; this maintenance correction replaces only those reader links with current official sources:

1. FDA CGMP reader link → `https://www.fda.gov/food/guidance-regulation-food-and-dietary-supplements`
2. FDA Preventive Controls reader link → current eCFR 21 CFR Part 117: `https://www.ecfr.gov/current/title-21/chapter-I/subchapter-B/part-117`
3. FDA FSMA rules/guidance reader link → current FDA FSMA hub: `https://www.fda.gov/food/guidance-regulation-food-and-dietary-supplements/food-safety-modernization-act-fsma`

The three controlled language masters retain identical reader-URL sets after correction. Occupational mappings, compensation values, training pathways, safety boundaries, responsible-AI controls, accessibility guidance, and substantive translations were not changed.

**Revalidated frozen English Git blob:** `c16332f361206af0b137d6ff8eda9300a445c9b0`

Affected controlled gates 03–08 were rechecked for the URL-only maintenance change and remain **PASS**. Publication and Release Audit remain fail-closed and may advance only after the corrected trilingual package passes automated build, link, DOCX, searchable-PDF, all-page render, checksum, and evidence checks.
