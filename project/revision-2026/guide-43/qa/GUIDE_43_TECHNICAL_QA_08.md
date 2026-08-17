# Guide 43 — Trilingual Technical QA Gate 08

**Guide:** 43 — Solar Photovoltaic Installer
**Branch:** `revision/guide-00-100-2026`
**Workflow:** `Guide 43 controlled publication build v2`
**Successful run:** `31996172780`
**Workflow-source commit:** `54a416416f60646e080ab9bf510862b22ca80100`
**Publication-candidate commit:** `574e6e91bb2b2aaacf869cd3da6af8553c60fa35`
**Gate result:** **PASS**

## Preconditions

Baseline Inventory, Current-source Research, English Editorial, Evidence/Traceability, English Source Freeze, Spanish Localization (`es-419`), and Portuguese Localization (`pt-BR`) were PASS before this gate.

## Corrective QA history

Historical runs `31967575374` and `31979822843` failed closed before artifact generation. Run `31979822843` correctly exposed that the original validator did not recognize the controlled pt-BR expression `6 pés (1.8 m)`.

Commit `54a416416f60646e080ab9bf510862b22ca80100` added the corrected v2 workflow. Its expression `6\s+(?:feet|pies|p[eé]s)\s*\(1[\.,]8\s*m\)` continues to require the six-foot / 1.8-m equivalence while accepting the legitimate accented Portuguese word `pés`. The Portuguese master already contained the controlled value; no safety content, numeric requirement, or source was removed or weakened.

## Successful workflow evidence

Run `31996172780` completed every substantive step successfully:

- controlled revision-branch checkout;
- trilingual candidate freeze;
- structural, source, numeric, terminology, UTF-8, and placeholder controls;
- live source-link behavior validation;
- three DOCX and three PDF generations;
- DOCX archive and searchable-PDF validation;
- all-page PDF rendering and automated blank/clipping/malformed-render checks;
- publication metadata and SHA-256 generation;
- rendered-page artifact upload; and
- controlled publication-candidate commit and push.

The trilingual control log records `21` level-two sections and `18` identical source URLs in each language. Fifteen source requests returned HTTP success. BLS, DOL, and Indeed returned HTTP 403 and were retained as access-controlled authoritative/supplemental sources rather than silently deleted.

## Safety, scope, and assurance controls

The controlled editions preserve:

- training does not grant electrician or legal authorization;
- no unsupervised energized electrical work instruction;
- qualified/licensed/registered-person and authority boundaries for grid connection, service equipment, conductor/protection sizing, grounding/bonding, inspection, commissioning, energization, and utility interconnection;
- energized-PV, electrical shock, arc-flash, and thermal-burn warnings;
- roof, fall, access, weather, and structural-suitability controls, including the applicable `6 feet (1.8 m)` / localized equivalence;
- stop-work/escalation conditions for damaged components, exposed conductors, unknown isolation/lockout state, unsafe access or weather, structural uncertainty, permit/design deviations, water intrusion, arcing signs, unexpected voltage, or missing authorization;
- Colombia RETIE qualification and jurisdiction language without asserting a disputed Resolution 40284 year;
- responsible-AI limits and cybersecurity/privacy boundaries; and
- non-guarantee language for employment, wages, funding, admission, certification, licensing, inspection approval, interconnection, and earnings.

## Artifact and visual QA

The manifest records overall PASS:

- English: DOCX `23,394` bytes; PDF `158,017` bytes; `11` PDF pages / `11` rendered pages.
- Spanish (`es-419`): DOCX `24,525` bytes; PDF `162,110` bytes; `12` PDF pages / `12` rendered pages.
- Portuguese (`pt-BR`): DOCX `24,460` bytes; PDF `163,679` bytes; `12` PDF pages / `12` rendered pages.

Workflow artifact `guide43-rendered-pages-v2` has artifact ID `9276905643`, size `8,213,993` bytes, digest `sha256:6e8a3b3da1937bdfcdcb32086033876b72312171447188bdb4d0ce7707d4fbd0`, and expiration August 31, 2026.

Codex inspected all `35` workflow-rendered page images and found no blank page, clipping, overlap, broken layout, or missing glyph. This is an internal execution-partner visual QA review, not independent human review. A separate local structural audit confirmed all six committed file hashes, DOCX ZIP integrity, searchable PDF text, absence of Unicode replacement characters, and page-count/render-count agreement.

## Decision

**Trilingual Technical QA: PASS.** Guide 43 may proceed to Publication. This is internal project QA and does not claim professional translation certification, accessibility certification, legal review, electrical/engineering approval, licensing determination, accreditation, or guaranteed employment or earnings.
