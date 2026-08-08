# Release Security Checklist

Use this checklist before publishing a new guide, translation, regenerated
document, or material revision.

Record review evidence in the appropriate guide QC file, project revision log,
or release notes. Do not mark an item complete unless it was actually checked.

## 1. Change scope

- [ ] The intended guide numbers, languages, formats, and versions are listed.
- [ ] The change set contains no unrelated guide or project changes.
- [ ] The editable source corresponding to each generated PDF is identified.
- [ ] Drafts and reviewed editions are clearly distinguished.
- [ ] Material changes have an appropriate version update.

## 2. Source and factual review

- [ ] Material claims were checked against current authoritative sources.
- [ ] Source access dates and factual-review dates are recorded.
- [ ] Employment, income, admission, funding, licensing, and promotion
      guarantees were not introduced.
- [ ] Legal, medical, financial, tax, immigration, licensing, and
      jurisdiction-specific statements retain appropriate qualifications.
- [ ] The next review date is recorded where required.

## 3. Document safety

- [ ] No unexpected DOCM, DOTM, executable, script, or archive is included.
- [ ] Externally supplied documents were treated as untrusted.
- [ ] Documents were checked for macros, embedded files, and unexpected external
      relationships before processing.
- [ ] Suspicious documents were not opened or rendered on a workstation holding
      repository credentials.
- [ ] Document conversion used a known and maintained tool version.
- [ ] Generated documents open correctly and contain the expected number and
      order of sections/pages.

## 4. Translation review

- [ ] The source edition, source version, target language, and locale are
      recorded.
- [ ] Machine-assisted output is identified as such until human review is
      complete.
- [ ] Human factual and linguistic review status is recorded accurately.
- [ ] Safety warnings, disclaimers, quantities, links, credential names, and
      jurisdictional qualifications were compared with the source.
- [ ] Translation caches or service responses were not accepted as proof of
      correctness.
- [ ] No confidential, private, or personally identifying material was sent to
      a translation service.

## 5. Accessibility and generated output

- [ ] The applicable checks in [ACCESSIBILITY.md](./ACCESSIBILITY.md) were
      completed.
- [ ] Headings, lists, tables, links, images, and reading order were reviewed.
- [ ] PDF text remains searchable and selectable.
- [ ] Relative links and filenames work.
- [ ] The editable source was corrected before regenerating derived formats.

## 6. Secrets and privacy

- [ ] The change set contains no credentials, tokens, private keys, populated
      environment files, or private configuration.
- [ ] Logs, translation caches, temporary files, and local QA renders are not
      included unless intentionally reviewed as project records.
- [ ] Documents were checked for unintended author, organization, comments,
      revision history, hidden text, or other sensitive metadata.
- [ ] Issues, review notes, and QC records contain no private medical or other
      unnecessary personal information.
- [ ] Any suspected exposed credential was revoked or rotated before release.

## 7. Dependencies and build provenance

- [ ] Runtime, library, and document-converter versions used for generation are
      recorded.
- [ ] Downloaded binary tools came from a known source and were verified where
      a signature or checksum was available.
- [ ] Dependency or tooling changes received separate review.
- [ ] Generated files correspond to the reviewed source files.
- [ ] Unexpected differences between prior and regenerated output were
      investigated.

## 8. Repository integrity

- [ ] The complete staged change list was reviewed.
- [ ] No unexpected executable, cache, log, temporary, or generated QA file is
      staged.
- [ ] [PROJECT_STATUS.md](./PROJECT_STATUS.md) and [CATALOG.md](./CATALOG.md)
      match the release contents when availability changed.
- [ ] [project/REVISION_LOG.md](./project/REVISION_LOG.md) was updated for
      material published changes.
- [ ] Required review was obtained under the repository's actual verified
      GitHub settings; no unverified protection was assumed.

## 9. Final approval

- [ ] The reviewer confirms that factual, accessibility, translation, privacy,
      and security statuses are represented accurately.
- [ ] Known unresolved risks or incomplete reviews are clearly disclosed.
- [ ] The final release contains only the files intended for publication.
