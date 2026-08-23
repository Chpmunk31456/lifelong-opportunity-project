# Guide 17 publication build request

Requested: 2026-08-09
Retry: 3 — rebase-safe publication push

The frozen English source and both controlled localization masters have passed the Guide 17 trilingual localization/parity gate. Structural, locale-aware numeric, DOCX/PDF, searchable-text, raster-rendering, and checksum controls already passed in retry 2; that run failed only because the revision branch advanced before the generated-artifact push. This marker triggers the hardened workflow that rebases the generated publication commit before pushing.
