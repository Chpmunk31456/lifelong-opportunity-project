# Guide 02 English semantic-equivalence result 08

- **Purpose:** distinguish real content divergence from predictable DOCX/PDF extraction noise.
- **Controls applied:** removal of extraction-only DOCX heading; removal of repeated PDF page headers/footers; PDF line-break de-hyphenation; punctuation normalization; token, five-token n-gram, and numbered-heading coverage.
- **Not a certification:** automated evidence only; no claim of independent human review, accessibility certification, accreditation, legal review, or factual validation.

## Metrics

| Metric | Result |
|---|---:|
| DOCX cleaned tokens | 2559 |
| PDF cleaned tokens | 2626 |
| Token sequence similarity | 0.967406 |
| DOCX token coverage by PDF | 0.980461 |
| PDF token coverage by DOCX | 0.955446 |
| DOCX 5-gram coverage by PDF | 0.898694 |
| PDF 5-gram coverage by DOCX | 0.884002 |
| DOCX heading coverage by PDF | 0.581395 |
| PDF heading coverage by DOCX | 0.446429 |

## Gate interpretation

**SUBSTANTIVE DIVERGENCE HOLD:** normalized semantic coverage remains below the controlled thresholds; reconstruct the English baseline only after identifying which unmatched content is substantive.

This result does not by itself designate an authoritative source. A baseline-selection record must also consider editability, document provenance, version metadata, substantive unmatched passages, and the requirement to preserve the most complete verified content.
