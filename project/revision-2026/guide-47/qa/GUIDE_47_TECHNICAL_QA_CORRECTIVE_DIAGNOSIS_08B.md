# Guide 47 — Technical QA corrective diagnosis 08B

**Guide:** 47 — Pharmacy Technician  
**Branch:** `revision/guide-00-100-2026`  
**Controlled publication run:** `32207052254`  
**Gate status after diagnosis:** **PENDING — replacement full publication run required**

## Exact failed controls

The controlled publication run reached the trilingual structural/source/numeric/terminology step and stopped before link, DOCX, PDF, rendering, metadata, checksum, or publication commit stages.

The run reported:

- English missing marker `responsible use of ai`;
- English missing controlled value `6%`;
- Spanish (`es-419`) missing controlled value `6%`; and
- Brazilian Portuguese (`pt-BR`) missing controlled value `6%`.

## Diagnosis

These were representation mismatches, not unsupported factual claims. The English master used the semantically equivalent heading `Using AI responsibly in pharmacy work`. The official O*NET/BLS outlook value was already consistently represented as six percent in all three editions, but written as `6 percent`, `6 por ciento`, and `6 por cento` rather than the validator's required percent-symbol representation.

The bounded repair changes only the English AI heading wording and the typography of the already-supported six-percent outlook value. It does not change the occupation, wage figures, outlook magnitude, legal/supervision boundaries, sources, URLs, or assurance language.

## Decision

**Corrective diagnosis: PASS. Technical QA remains PENDING.**

A complete replacement controlled publication run must pass structural/source/numeric/terminology, live-link, DOCX, searchable-PDF, all-page rendering, metadata, and checksum controls before Technical QA may advance.
