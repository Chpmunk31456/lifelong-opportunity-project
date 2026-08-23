# Guide 33 Baseline Inventory 01

**Guide:** 33 — Machinist and CNC Machine Operator  
**Branch:** `revision/guide-00-100-2026`  
**Stage:** Baseline Inventory / Legacy-Source Reconciliation  
**Status:** PASS  
**Inventory date:** August 11, 2026

## Authoritative live-state check

Guide 32 was closed with Release Auditor PASS before this inventory began. PR #17 remains open and Draft on `revision/guide-00-100-2026`. No existing `project/revision-2026/guide-33` controlled-work directory was present when this stage started, so this is the first controlled Guide 33 evidence set rather than a duplicate or stale handoff.

## Legacy guide inventory

Repository directory: `33-machinist-and-cnc-machine-operator/`.

The root legacy guide contains:

- `README.md` describing Guide 33 and linking English, Latin American Spanish, and Brazilian Portuguese DOCX/PDF editions;
- `english/`, `spanish/`, and `portuguese/` edition trees;
- the English tree includes an edition README, DOCX, searchable PDF, and a `source/` directory;
- English DOCX: `english/docx/machinist-and-cnc-machine-operator.docx` (legacy blob `00fd66cd21e40fae10129f0b9360d114bf71b954`);
- English PDF: `english/pdf/machinist-and-cnc-machine-operator.pdf` (legacy blob `ab36984af46572425d8dfb7030a667dc7ef2ef05`);
- English source notes: `english/source/sources.md` and `english/source/qc.md`.

The English edition README identifies the legacy edition as Version 1.0, published July 2026, and explicitly warns that exact source equivalence and human linguistic review should not be assumed unless separately documented.

## Legacy evidence condition

The existing `english/source/sources.md` records a July 2026 review using the U.S. Bureau of Labor Statistics occupation family “Machinists and Tool and Die Makers,” including May 2024 pay figures and 2024–2034 outlook data. It also states that apprenticeship, education, tax, accessibility, labor, and safety claims require current official and jurisdiction-specific verification.

These legacy source notes are useful provenance but are **not** sufficient for the expanded 2026 controlled standard. The controlled revision must independently refresh and trace the occupation scope, pay/outlook, training and apprenticeship, safety, credential boundaries, funding, Canada, Latin America, Colombia, responsible-AI/privacy/cybersecurity, accessibility, and current non-government compensation research before English Editorial can pass.

## Controlled revision requirements

Guide 33 will therefore proceed fail-closed through:

1. current-source research with official U.S., Canadian, Latin American/Colombian sources where applicable and a clearly labeled current non-government compensation estimate;
2. English Version 2.0 reconstruction and editorial QA;
3. evidence/traceability QA and English source freeze;
4. neutral Latin American Spanish (`es-419`) localization and QA;
5. Brazilian Portuguese (`pt-BR`) localization and QA;
6. technical QA covering structure, terminology, links, encoding, numeric parity, DOCX/PDF integrity, searchable text, rendering, metadata, and checksums;
7. Publication Helper and Release Auditor gates.

No legacy “reviewed” label will be treated as independent human certification, professional translation certification, accreditation, legal review, safety/code approval, licensing approval, or accessibility certification.

## Baseline conclusion

**Baseline Inventory: PASS.** The legacy Guide 33 package, its available provenance, and the gaps against the controlled revision standard are identified. The first incomplete successor gate is **Research Helper / current-source evidence intake**.
