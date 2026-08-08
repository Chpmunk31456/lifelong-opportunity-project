# Repository Security Controls

## Purpose

This document defines Phase 1 security expectations for the Lifelong
Opportunity Guides repository.

The repository contains public educational content in Markdown, DOCX, and PDF
formats. The current working tree also contains untracked local tools that parse
Office Open XML, call a translation service, write translation caches, and
invoke document-conversion software.

These controls supplement:

- [GOVERNANCE.md](./GOVERNANCE.md), which requires factual accuracy,
  documented review, privacy, human localization review, and preserved revision
  history;
- [CONTRIBUTING.md](./CONTRIBUTING.md), which prohibits unauthorized private or
  confidential material and requires human review of machine-assisted
  translations;
- [ACCESSIBILITY.md](./ACCESSIBILITY.md), which defines document and PDF review
  requirements; and
- [project/ANNUAL_REVIEW.md](./project/ANNUAL_REVIEW.md), which defines factual
  review records.

This file documents policy controls only. It does not claim that GitHub branch
protection, private vulnerability reporting, artifact signing, automated
scanning, or other external controls are enabled.

## 1. Document-processing risks

### Risks

DOCX and related formats are ZIP-based containers containing XML, relationships,
embedded objects, links, and potentially active content. PDF and office
conversion software also process complex binary formats.

A crafted document could:

- exploit a parser or conversion-tool vulnerability;
- contain macros, embedded objects, or external relationships;
- consume excessive memory, disk, or CPU;
- cause unexpected network requests;
- overwrite or create unexpected output; or
- compromise a workstation that holds Git or other credentials.

### Required controls

- Treat externally supplied DOCX, DOCM, DOTM, PDF, and archive files as
  untrusted.
- Do not open or render a suspicious document on a workstation that holds
  repository credentials.
- Do not process macro-enabled Office documents as part of the normal guide
  workflow.
- Check contributed documents for macros, embedded files, and external
  relationships before conversion.
- Use maintained document-processing software from a known source.
- Prefer a disposable, restricted processing environment with no repository
  credentials and no unnecessary network access.
- Limit accepted file types, archive size, uncompressed size, entry count,
  processing time, memory, and output location when tooling supports those
  controls.
- Review generated output before it becomes a published artifact.

The current working tree contains a local rendering tool, but it does not
contain evidence of a document-processing sandbox or enforced resource limits.
Those controls remain required work rather than verified controls.

## 2. Translation-service risks

### Risks

Translation tools may send complete guide paragraphs to an external service and
then insert returned text into generated documents. Risks include:

- disclosure through provider, proxy, or URL logs;
- unexpected service behavior or response-format changes;
- incorrect, unsafe, or manipulated translation;
- loss of warnings, qualifications, or technical meaning; and
- cache corruption or substitution.

### Required controls

- Send only material that is already approved for public disclosure.
- Do not send personal information, confidential drafts, credentials, or
  proprietary third-party text.
- Record the source edition, version, target language, and review status.
- Treat machine translation as a draft.
- Require review by a proficient human before labeling a translation reviewed
  or publishing it as complete.
- Verify that safety notices, disclaimers, links, quantities, credential names,
  and jurisdiction-specific qualifications retain their meaning.
- Validate translation responses and cache files before using them to build
  documents.
- Keep translation caches and failure logs out of commits unless a documented
  review determines they are intentional project records.

These requirements reflect the existing translation policy in
[CONTRIBUTING.md](./CONTRIBUTING.md). The repository does not demonstrate an
automated enforcement gate, so the release checklist remains necessary.

## 3. Release integrity controls

### Required controls

- Start changes from the editable source rather than editing a generated PDF.
- Review material factual corrections against authoritative sources.
- Preserve warnings against guarantees and predatory programs.
- Record the guide, language, old and new version, factual-review date, changed
  sources, accessibility status, and translation-review status when applicable.
- Confirm that repository status and catalog records match the files actually
  intended for publication.
- Review the complete change set before release, including generated binaries.
- Keep unrelated changes out of a release.
- Confirm that no unexpected scripts, executables, archives, caches, logs, or
  temporary files are included.
- Update the revision log for material published changes.
- Complete [RELEASE_SECURITY_CHECKLIST.md](./RELEASE_SECURITY_CHECKLIST.md).

The repository does not verify branch protection, required reviews, signed
commits, signed releases, or artifact attestations. Those controls must not be
represented as active unless verified separately.

## 4. Secrets handling

### Prohibited repository content

- passwords, API keys, access tokens, session cookies, or private keys;
- populated environment files or credential exports;
- private medical, financial, legal, employment, or education records;
- confidential drafts not approved for publication; and
- diagnostic logs containing sensitive paths, request data, or credentials.

### Required controls

- Store secrets outside the repository.
- Use environment variables or a provider-supported secret store when a future
  tool genuinely requires authentication.
- Do not print secrets or complete authentication headers to logs.
- Review staged files and generated artifacts before every release.
- If exposure occurs, revoke or rotate the secret before cleaning repository
  content or history.
- Treat history rewriting as a separate, carefully reviewed incident-response
  action; deleting a current file alone does not invalidate an exposed secret.

The working-tree translation tools currently use an unauthenticated endpoint;
this document does not introduce or require a paid service or repository secret.

## 5. Dependency and supply-chain controls

### Risks

Local document generation depends on language runtimes, libraries, command-line
clients, and document/PDF conversion software. Unpinned or substituted tools can
compromise the workstation or generated artifacts.

### Required controls

- Obtain tools and dependencies from known sources.
- Record exact runtime, library, and document-converter versions used for a
  release.
- Verify available vendor signatures or published hashes for downloaded binary
  tools.
- Do not rely on a personal absolute executable path as proof of tool identity.
- Add dependency manifests and lockfiles before treating local scripts as a
  reproducible build system.
- Review dependency changes independently from guide-content changes.
- Remove unused dependencies and keep required processors updated.
- Maintain a source-to-output record or hashes for published generated
  artifacts when practical.
- Do not run dependency installation or document conversion from an untrusted
  pull request with privileged credentials.

No dependency lockfiles, software bill of materials, automated dependency
scanner, or verified binary manifest is currently documented in the repository.
They are future controls, not existing controls.
