# Guide 00 — Live Link Validation Batch 03

**Branch:** `revision/guide-00-100-2026`  
**Guide:** 00 — Lifelong Opportunity Foundation Guide  
**Validation date:** 2026-08-03  
**Status:** Completed audit record; source correction still required in the three integrated masters

## Scope

This batch rechecked the two links previously recorded as inconclusive and reviewed their current official status.

## Results

### Canada — Red Seal apprenticeship and certification authorities

**Current canonical official page:**

- https://red-seal.ca/eng/contact/contact.shtml

**Result:** PASS

The page resolves and lists provincial and territorial apprenticeship and certification authorities. It confirms that the Red Seal Program is administered through those authorities.

**Defect identified in the integrated masters:**

- Existing path: `https://www.red-seal.ca/eng/contact/c.4nt.1ct.shtml`
- Required replacement: `https://red-seal.ca/eng/contact/contact.shtml`

The existing path is obsolete/encoded and must be replaced consistently in the English, neutral Latin American Spanish, and Brazilian Portuguese masters before final document generation.

### Chile — Programa Becas Fondo Cesantía Solidario

**Current official page:**

- https://www.chileatiende.gob.cl/fichas/20814-programa-becas-fondo-cesantia-solidario

**Result:** PASS WITH STATUS CONTROL

The official ChileAtiende page was updated on May 28, 2026. It describes fully funded online training for eligible active beneficiaries of the Fondo de Cesantía Solidario and explicitly states that applications are closed.

The integrated masters already state that the reviewed call closed on May 28, 2026 and must not be presented as open unless ChileAtiende or SENCE announces a new active period. No content correction is required for that status statement.

### Chile — Fondo de Cesantía Solidario

**Current official page:**

- https://www.chileatiende.gob.cl/fichas/ver/36646

**Result:** PASS

The page confirms that access depends on unemployment status, insufficient individual-account funds, qualifying termination causes, contribution requirements, and activation in the Bolsa Nacional de Empleo. It also confirms that beneficiaries must accept qualifying employment and training opportunities unless a justified exception applies.

## QA conclusions

- The Red Seal source is valid, but the integrated-master URL is defective and requires a trilingual replacement.
- The Chile scholarship/training call is correctly labeled closed.
- No link in this batch may be described as an open scholarship or guaranteed benefit.
- No independent certification, accreditation, legal review, accessibility certification, or professional translation claim is made.

## Remaining Guide 00 link gate

1. Replace the obsolete Red Seal URL in all three integrated masters.
2. Recheck the replacement in generated DOCX and PDF files.
3. Validate all embedded hyperlinks after document generation.
4. Preserve dated status labels for calls that are closed or periodically reopened.
