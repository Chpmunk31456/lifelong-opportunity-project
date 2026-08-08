# Technical QA Helper

## Mission
Run deterministic checks on the frozen trilingual source set before publication artifact generation.

## Required inputs
- Frozen English, es-419, and pt-BR masters.
- Translation QA records.

## Required checks
- UTF-8 decoding; reject unexpected BOM/replacement-character defects where project policy requires.
- Markdown structure, malformed links, duplicate/missing headings, broken local targets, filenames, and version identifiers.
- External URL inventory and current validation status.
- Heading/list/table/code-block structural parity across languages.
- Numeric, date, percentage, currency, unit, URL, citation/reference, warning, and required-section parity.
- Placeholder/TODO markers and suspicious source-language leakage.
- Deterministic hashes of frozen source inputs when useful for build provenance.

## Required output
Create a technical QA report and machine-readable results where practical. Record command/tool versions or workflow run identifiers sufficient to reproduce the checks.

## PASS conditions
PASS only when no blocking structural, encoding, link, parity, or placeholder defect remains.

## Blocking conditions
- Encoding corruption.
- Broken required internal link or malformed Markdown affecting meaning.
- Material cross-language numeric/date/URL/warning mismatch.
- Publication build would not be reproducible from identified frozen inputs.
