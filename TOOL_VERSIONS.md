# Tool and Dependency Versions

## Purpose

This file distinguishes repository requirements from versions observed in
different environments.

It is intended to become a reproducibility record for guide generation and
document QA. Listing a tool or version here does not prove that the tool is
trusted, that its source has been verified, or that it was used to produce a
particular published artifact.

Python package dependencies are declared separately in
[requirements.txt](./requirements.txt). Machine-level tools such as Python,
Node.js, LibreOffice, Poppler, and curl do not belong in Python dependency
files.

## A. Repository-required tools

| Component | Purpose | Repository evidence | Requirement |
|---|---|---|---|
| Python | Runs repository-local translation and document-rendering scripts | Python files under `project/` | Conditional: required when running those scripts |
| lxml | Parses and rewrites OOXML content | `project/translate_missing_ptbr.py`; `project/translate_missing_spanish.py` | Direct Python dependency for translation generation |
| pdf2image | Reads PDF information and rasterizes PDF pages | `project/qa-ptbr/render_docx.py` | Direct Python dependency for document QA |
| LibreOffice | Converts DOCX or ODT files to PDF | `project/qa-ptbr/render_docx.py`; `project/qa-ptbr/bin/soffice.cmd` | Conditional: document rendering and QA |
| Poppler | Supplies `pdfinfo` and PDF-to-image conversion used by pdf2image | Calls through `pdf2image` in `project/qa-ptbr/render_docx.py` | Conditional: document rendering and QA |
| curl | Sends translation requests from Python | `project/translate_missing_spanish.py`; `project/translate_ptbr_via_curl.py` | Conditional: curl-based translation |
| Node.js | Runs the alternative Portuguese translation script | `project/translate_ptbr.mjs` | Optional translation implementation |
| Google Translate endpoint | Produces machine-assisted translation drafts | Python and Node translation scripts | Conditional external service |

Pillow is not directly imported by repository code. It may be installed as a
dependency of pdf2image, but it is not declared as a direct repository
dependency.

npm is not required by current repository scripts. The Node script imports only
the built-in `node:fs/promises` module and uses built-in Node APIs, including
`fetch`, `URLSearchParams`, and JSON handling. The repository therefore does not
currently require `package.json` or `package-lock.json`.

## B. Verified maintainer-workstation versions

The following versions were reported from the repository owner's actual Windows
PowerShell environment:

| Component | Verified version | Status |
|---|---:|---|
| Node.js | 24.18.0 | Verified on maintainer workstation |
| npm | 12.0.2 | Verified on maintainer workstation; not required by current repository scripts |

A reported version identifies the installed software. It does not by itself
establish source integrity, compatibility with every script, or use in a
particular published release.

## C. Codex and audit-runtime observations

The following versions were observed during a security audit. They are not the
maintainer-workstation release baseline and must not be used as release versions
without separate verification.

| Component | Audit observation | Environment |
|---|---:|---|
| Python | 3.12.13 | Bundled Codex runtime |
| lxml | 6.0.2 | Bundled Codex Python environment |
| pdf2image | 1.17.0 | Bundled Codex Python environment |
| Pillow | 12.2.0 | Bundled Codex Python environment; transitive, not directly imported |
| Node.js | 24.14.0 | Bundled Codex runtime |
| npm | 11.16.0 | Audit shell resolution; not the maintainer-reported version |
| Poppler | 26.05.0 | Bundled Codex runtime |
| LibreOffice | 26.2.5.2 | File metadata inspected during the audit from a workspace-local executable |
| curl | 8.21.0 | Windows system executable resolved during the audit |

These observations may help reproduce the audit itself. They do not establish
which versions generated published repository artifacts.

## D. Versions not yet verified on the maintainer workstation

The following release-toolchain information remains unresolved:

| Component | Maintainer-workstation status | Verification needed |
|---|---|---|
| Python | Not yet verified on maintainer workstation | Run `python --version` and record the executable path |
| lxml | Not yet verified on maintainer workstation | Query installed package metadata in the Python environment used for releases |
| pdf2image | Not yet verified on maintainer workstation | Query installed package metadata in the Python environment used for releases |
| LibreOffice | Not yet verified as the publication-toolchain version | Record the executable used for release generation and obtain its version |
| Poppler | Not yet verified on maintainer workstation | Record `pdfinfo` and `pdftoppm` versions and executable paths |
| curl | Not yet verified as the translation-toolchain version | Run `curl.exe --version` in the environment used by the translation scripts |
| Google Translate endpoint | Unversioned external service | Document the endpoint and date used for each translation run |

Exact Python package pins should be added to `requirements.txt` only after the
maintainer-workstation environment used for generation has been verified.

## Release-toolchain integrity record

For each release that regenerates DOCX, PDF, translation, or QA artifacts:

1. Record the release date and affected guides.
2. Record the exact executable path and reported version for Python, LibreOffice,
   Poppler, curl, and Node.js when applicable.
3. Record installed Python package versions from the environment that actually
   ran the scripts.
4. Identify the source from which each downloaded installer, archive, or binary
   was obtained.
5. Verify any available vendor signature.
6. Compare downloaded files with vendor-published checksums when available.
7. Calculate a local SHA-256 hash of the exact installer or executable used.
8. Label each hash as either:
   - vendor-published checksum; or
   - locally calculated identity hash.
9. Never describe a locally calculated hash as proof of vendor authenticity.
10. Associate the toolchain record with the generated artifacts and their
    review record.

On Windows, a local SHA-256 identity hash can be calculated with:

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath "<exact-file-path>"
```

A vendor signature or published checksum must be verified independently. A
locally calculated hash only detects later changes relative to the recorded
file.

## Dependency update policy

- Update a dependency only through an intentional, separately reviewable
  change.
- Verify versions in the maintainer environment used to generate release
  artifacts.
- Do not adopt a Codex or audit-runtime version merely because it is installed
  or available.
- Verify available vendor signatures and vendor-published checksums for
  downloaded executables.
- Keep machine-level tool versions outside Python dependency files.
- Update this file and `requirements.txt` together when a verified direct Python
  dependency changes.
- Regenerate a representative document after a toolchain change.
- Repeat applicable visual, textual, accessibility, and translation checks.
- Investigate unexpected output differences before accepting regenerated
  artifacts.
- Review relevant security advisories before continuing to use an affected
  version.
- Do not treat installation success, a version string, or a local hash as proof
  that a dependency is trustworthy.
