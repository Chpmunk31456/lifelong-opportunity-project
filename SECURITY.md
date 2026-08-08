# Security Policy

## Project scope

The Lifelong Opportunity Guides repository contains public educational
materials, editable Microsoft Word documents, PDFs, and quality records. The
current working tree also contains local document-generation and translation
tools.

Security concerns may involve:

- malicious or unexpectedly active content in contributed documents;
- unsafe document parsing or conversion;
- unauthorized changes to published guides;
- exposed credentials, tokens, private drafts, or personal information;
- compromised dependencies or document-processing tools;
- manipulated translation data or generated artifacts; and
- links or attachments intended to compromise maintainers or readers.

Factual corrections, accessibility barriers, broken links, and ordinary
translation concerns are not security vulnerabilities by themselves. Report
those through the normal contribution process described in
[CONTRIBUTING.md](./CONTRIBUTING.md).

## Reporting a security concern

First check whether the repository's GitHub Security page offers private
vulnerability reporting. This repository does not document whether that GitHub
feature is enabled.

If private reporting is available, use it and include:

- the affected file, document, script, or process;
- the conditions required to reproduce the issue;
- the potential effect on maintainers, contributors, or readers;
- safe reproduction steps; and
- any suggested mitigation.

If private reporting is not available, do not place secrets, exploit code,
malicious documents, private information, or sensitive reproduction details in
a public issue. A minimal public issue may ask the maintainer to establish a
private reporting channel without disclosing the vulnerability.

No private email address or other private reporting endpoint is published in
this repository, so this policy does not invent one.

## Handling potentially malicious files

Do not attach a suspected malicious DOCX, DOCM, DOTM, PDF, archive, executable,
or script to a public issue or pull request.

Provide hashes, filenames, observed behavior, and non-sensitive diagnostic
details first. A maintainer should not open or render a suspect document on a
workstation that holds repository credentials or other sensitive data.

## Sensitive information

Never include any of the following in an issue, pull request, document, log, or
translation cache:

- passwords, API keys, access tokens, cookies, or private keys;
- private medical, financial, legal, employment, or education information;
- confidential drafts or proprietary source material; or
- personal information that is not already intentionally public.

If a secret is exposed, revoke or rotate it through the relevant provider.
Removing it from the latest Git revision is not sufficient because earlier
history may still contain it.

## Security response

The project is volunteer-led. No response or remediation deadline is promised.
Reports should be evaluated according to potential harm, exploitability, and
the integrity of published materials.

Confirmed incidents should be documented without publishing active secrets,
dangerous payloads, or unnecessary personal information.

## Related policies

- [Governance](./GOVERNANCE.md)
- [Contribution guidelines](./CONTRIBUTING.md)
- [Security controls](./SECURITY_CONTROLS.md)
- [Release security checklist](./RELEASE_SECURITY_CHECKLIST.md)
