#!/usr/bin/env python3
"""Build and QA the controlled Guide 01 English v1.1 integrated master."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "01-community-health-worker/source/Lifelong_Opportunity_Community_Health_Worker_Guide_English_v1.1_EXTRACTED_BASELINE.md"
MASTER = ROOT / "01-community-health-worker/source/Lifelong_Opportunity_Community_Health_Worker_Guide_English_v1.1_INTEGRATED_MASTER.md"
QA_DIR = ROOT / "project/revision-2026/guide-01"
QA_MD = QA_DIR / "ENGLISH_INTEGRATED_MASTER_QA_01.md"
QA_JSON = QA_DIR / "ENGLISH_INTEGRATED_MASTER_QA_01.json"


def replace_section(text: str, heading: str, next_heading: str, body: str) -> str:
    pattern = rf"(?ms)^# {re.escape(heading)}\n.*?(?=^# {re.escape(next_heading)}\n)"
    replacement = f"# {heading}\n\n{body.strip()}\n\n"
    updated, count = re.subn(pattern, replacement, text)
    if count != 1:
        raise SystemExit(f"Expected one section '{heading}', replaced {count}")
    return updated


def main() -> int:
    text = BASE.read_text(encoding="utf-8-sig")
    text = text.replace("English Edition • Version 1.0 • July 2026", "English Edition • Version 1.1 • August 2026")

    # Remove DOCX-derived page-number table of contents; generated publication files create their own navigation.
    text, toc_count = re.subn(r"(?ms)^# Table of Contents\n.*?(?=^# 1\. How to Use This Guide\n)", "", text)
    if toc_count != 1:
        raise SystemExit(f"Expected one extracted table of contents, removed {toc_count}")

    pay = r"""## United States official statistics

The U.S. Bureau of Labor Statistics (BLS) reported a median wage of **USD 51,030 per year (USD 24.54 per hour)** for community health workers in May 2024. BLS projected **11% employment growth from 2024 through 2034** and approximately **7,800 openings per year** on average. The BLS occupation page was last modified on August 28, 2025.

These are national occupational statistics, not a promise of local pay, hours, benefits, hiring, or job availability. State requirements and employer expectations vary.

## United States current commercial estimates

Commercial platforms provide supplementary market signals, not official statistics:

- Indeed displayed an average base-pay estimate of **USD 24.40 per hour**, with a displayed range of USD 12.72–46.79 per hour, updated July 20, 2026. Indeed stated that the estimate used about 3,500 salaries from job postings over the preceding 36 months.
- Glassdoor displayed an estimated average of approximately **USD 52,306 per year**, with a typical reported range of about USD 43,743–62,860, based on 1,936 submitted salaries as of June 2026.

Platform methodology, title matching, sample mix, geography, and posting quality can materially affect these estimates. Check current local postings and written offers.

## Canada classification and wages

The Government of Canada Job Bank maps “community health worker” to the broader **Social and community service workers, NOC 42201** classification. This Canadian classification is not identical to the U.S. BLS occupation. Job Bank states that entry usually requires a college diploma, an apprenticeship of two or more years, or relevant supervisory experience, but requirements vary by province, territory, employer, and setting.

Job Bank national wage data updated November 19, 2025 reported **CAD 19.00 low, CAD 26.00 median, and CAD 36.06 high per hour**. It also reported that 83.6% of workers in NOC 42201 received at least one non-wage benefit. These figures cover the broader NOC classification.

Glassdoor Canada displayed an estimated average base pay of approximately **CAD 52,000 per year**, with a displayed range of about CAD 47,000–58,000, based on 164 submitted salaries and observed July 19, 2026. This commercial estimate is not directly interchangeable with Job Bank data.

## Local wage and offer research

- Match the exact title, duties, location, schedule, employment status, education, experience, language, travel, and technology requirements.
- Separate base pay from overtime, bonuses, differentials, commissions, stipends, or per-diem rates.
- Value health insurance, retirement, paid leave, tuition support, union benefits, transportation costs, and unpaid time.
- Record the posting and verification dates.
- Never present a broader or higher-level occupation’s wage as guaranteed for this role."""
    text = replace_section(text, "6. Pay, Benefits, and Outlook", "7. Education and Credentials", pay)

    education = r"""## Entry requirements and free-first pathway

In the United States, a high school diploma or equivalent is commonly sufficient for entry, although some employers prefer postsecondary education. Short-term on-the-job training is typical, and some states require certification. Canada and Latin American countries may use different titles, classifications, and training rules.

Begin with the least expensive credible option:

- employer-paid onboarding and supervised training;
- public libraries, adult education, and reputable open courses;
- public community or technical colleges;
- state, provincial, territorial, or local workforce services;
- recognized nonprofit or public-health programmes;
- registered apprenticeship or other paid work-based learning where available; and
- SENA or other authorized public training in Colombia.

Pay only when the programme produces a verified next step, such as employer acceptance, transferable credit, recognized certification eligibility, supervised practice, or documented occupational competence.

## United States funding and training searches

- Search American Job Centers and state or local workforce boards for eligibility-based training support.
- Search Apprenticeship.gov for current registered apprenticeship opportunities; availability varies by place and sponsor.
- Verify Federal Student Aid eligibility only through official aid and institution records.
- Ask health systems, public-health departments, unions, associations, foundations, and community organisations about current scholarships or employer-paid training.

## Canada funding and training searches

- Check provincial and territorial employment and training services.
- Compare public colleges, CEGEPs, recognized work-integrated learning, and apprenticeship routes where applicable.
- Verify student aid through the relevant government portal.
- Ask employers and unions about paid onboarding, tuition support, and sector training funds.

## Colombia pathway

SENA’s Betowa catalogue has displayed **Promotor de salud** training offers, but availability is specific to location and cohort. Search the current catalogue by occupation and region rather than relying on an older listing. SENA reported certifying 21 Auxiliares Promotores de Salud in Antioquia on April 24, 2026 and 81 in Casanare on July 15, 2026. These examples show active public initiatives, not permanent nationwide availability, automatic hiring, professional licensure, or fixed pay.

Also check the Agencia Pública de Empleo SENA, territorial health secretariats, authorized training providers, and Ministry of Education programme status when a formal credential is involved.

## Latin America title and scope warning

Community health worker, promotora or promotor de salud, agente comunitario de salud, auxiliar promotor de salud, patient navigator, and social and community service worker are not automatically equivalent. A role may be salaried, contracted, stipend-supported, or volunteer. Verify the country-specific legal scope, training system, employer requirements, compensation model, and employment status.

## Provider and credential verification

- Verify institutional authorization or accreditation when applicable; short non-degree training does not always require the same form of accreditation.
- Confirm programme recognition, certification or examination eligibility, and employer acceptance.
- Ask whether credits, supervised hours, apprenticeship hours, and credentials transfer.
- Review total cost, completion and placement methodology, refunds, complaints, closure protections, and record access.
- Confirm whether practical placement is guaranteed, competitive, or the learner’s responsibility."""
    text = replace_section(text, "7. Education and Credentials", "8. Employer-Supported Learning", education)

    employer = r"""## Tuition benefits and repayment

Employers may pay tuition directly, reimburse successful completion, cover certification fees, provide scholarships, or offer forgivable loans. Obtain the complete written agreement before enrolling or accepting funds.

Verify coverage limits, eligible programmes, grade or exam requirements, tax treatment, scheduling, the service-commitment start date, the actual required employment period, prorated repayment, local enforceability, and any final-wage deduction authority. The agreement should address layoff, position elimination, closure, restructuring, disability, military activation, retirement, death, and employer-directed transfer. Never assume repayment is automatically waived.

## Internships, apprenticeships, and career ladders

- Distinguish internships, practicums, cooperative education, pre-apprenticeships, registered apprenticeships, job shadowing, and ordinary probationary employment.
- Verify pay, benefits, supervision, work and classroom hours, workers’ compensation, wage progression, portability, and any academic or certification credit.
- Require written learning objectives and qualified supervision.
- Search official apprenticeship and public workforce portals, then verify each opportunity with the named sponsor or employer.
- Treat mentoring, cross-training, rotational assignments, and bridge programmes as valuable only when duties, supervision, outcomes, and worker protections are clear."""
    text = replace_section(text, "8. Employer-Supported Learning", "9. Accessibility and Inclusion", employer)

    # Correct sequence numbering inherited from the source DOCX.
    text = re.sub(r"(?m)^8\.  Weeks 1–2:", "1. Weeks 1–2:", text)
    text = re.sub(r"(?m)^9\.  Weeks 3–4:", "2. Weeks 3–4:", text)
    text = re.sub(r"(?m)^10\. Weeks 5–6:", "3. Weeks 5–6:", text)
    text = re.sub(r"(?m)^11\. Weeks 7–8:", "4. Weeks 7–8:", text)
    text = re.sub(r"(?m)^12\. Weeks 9–10:", "5. Weeks 9–10:", text)
    text = re.sub(r"(?m)^13\. Weeks 11–12:", "6. Weeks 11–12:", text)

    sources = r"""## Official and primary sources

- U.S. Bureau of Labor Statistics, Community Health Workers: https://www.bls.gov/ooh/community-and-social-service/community-health-workers.htm
- Government of Canada Job Bank, facts and figures: https://www.jobbank.gc.ca/marketreport/summary-occupation/296075/ca
- Government of Canada Job Bank, wages: https://www.jobbank.gc.ca/marketreport/wages-occupation/296075/ca
- Apprenticeship.gov: https://www.apprenticeship.gov/
- U.S. Department of Education accreditation information: https://www.ed.gov/accreditation
- Federal Student Aid: https://studentaid.gov/
- SENA Betowa, Promotor de salud: https://betowa.sena.edu.co/oferta/promotor-de-salud?modality=P&offertype=company
- SENA Antioquia certification report, April 24, 2026: https://www.sena.edu.co/es-co/Noticias/Paginas/noticia.aspx?IdNoticia=9298
- SENA Casanare certification report, July 15, 2026: https://www.sena.edu.co/es-co/Noticias/Paginas/noticia.aspx?IdNoticia=9614
- EEOC disability discrimination guidance: https://www.eeoc.gov/disability-discrimination

## Clearly labelled commercial salary comparisons

- Indeed U.S., observed July 20, 2026: https://www.indeed.com/career/community-health-worker/salaries
- Glassdoor U.S., observed June 2026: https://www.glassdoor.com/Salaries/community-health-worker-salary-SRCH_KO0,23.htm
- Glassdoor Canada, observed July 19, 2026: https://www.glassdoor.ca/Salaries/community-health-worker-salary-SRCH_KO0,23.htm

Commercial estimates are supplementary market signals, not official statistics or guaranteed offers.

## Version and maintenance policy

- Version 1.1 is a controlled revision dated August 2026.
- Review wages, outlook, training availability, funding, certification rules, and links at least annually and before high-impact decisions.
- Mark uncertain or jurisdiction-dependent information for verification instead of guessing.
- Report errors, broken links, accessibility barriers, or outdated information through the project correction process.
- Automated QA is not independent human certification, professional translation certification, accreditation review, accessibility certification, legal review, or medical review.

**Governing principle:** When speed and completeness conflict, completeness wins. When confidence and uncertainty conflict, disclose the uncertainty. When an institution’s interest conflicts with the reader’s protection, the reader comes first."""
    pattern = r"(?ms)^# 19\. Sources, Versioning, and Maintenance\n.*\Z"
    text, count = re.subn(pattern, f"# 19. Sources, Versioning, and Maintenance\n\n{sources.strip()}\n", text)
    if count != 1:
        raise SystemExit(f"Expected one sources section, replaced {count}")

    # Normalize whitespace and UTF-8/LF output.
    lines = [line.rstrip(" \t") for line in text.replace("\r\n", "\n").replace("\r", "\n").split("\n")]
    text = "\n".join(lines).strip() + "\n"
    MASTER.write_text(text, encoding="utf-8", newline="\n")

    required = {
        "version_1_1": "English Edition • Version 1.1 • August 2026",
        "bls": "USD 51,030 per year",
        "canada": "NOC 42201",
        "colombia": "SENA’s Betowa catalogue",
        "latin_america": "Latin America title and scope warning",
        "apprenticeship": "Apprenticeship.gov",
        "commercial_label": "Commercial estimates are supplementary market signals",
        "scope_limit": "Automated QA is not independent human certification",
    }
    checks = {key: value in text for key, value in required.items()}
    headings = re.findall(r"(?m)^#{1,6} .+$", text)
    urls = sorted(set(re.findall(r"https?://[^\s)>]+", text)))
    defects = []
    if not all(checks.values()):
        defects.append("one or more required controlled statements are missing")
    if "Version 1.0" in text:
        defects.append("obsolete Version 1.0 metadata remains")
    if re.search(r"(?m)[ \t]+$", text):
        defects.append("trailing whitespace detected")
    if "\ufffd" in text or text.startswith("\ufeff"):
        defects.append("encoding defect detected")
    if len(text.split()) < 3000:
        defects.append("integrated master unexpectedly short")

    report = {
        "guide": "01",
        "edition": "English",
        "version": "1.1",
        "status": "controlled integrated master; automated QA only",
        "source_sha256": hashlib.sha256(BASE.read_bytes()).hexdigest(),
        "master_sha256": hashlib.sha256(MASTER.read_bytes()).hexdigest(),
        "characters": len(text),
        "words": len(text.split()),
        "headings": len(headings),
        "unique_urls": len(urls),
        "required_checks": checks,
        "blocking_defects": defects,
        "independent_human_certification": False,
    }
    QA_DIR.mkdir(parents=True, exist_ok=True)
    QA_JSON.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    qa_lines = [
        "# Guide 01 — English Integrated Master QA",
        "",
        f"- Status: {'PASS' if not defects else 'FAIL'}",
        f"- Master SHA-256: `{report['master_sha256']}`",
        f"- Words: {report['words']}",
        f"- Headings: {report['headings']}",
        f"- Unique URLs: {report['unique_urls']}",
        "- Review scope: deterministic integration, required-content presence, versioning, structure, UTF-8/LF, and whitespace checks.",
        "- Independent human certification, professional translation certification, accreditation review, accessibility certification, legal review, and medical review were not obtained or claimed.",
        "",
        "## Required checks",
        "",
    ]
    qa_lines.extend(f"- {key}: {'pass' if passed else 'fail'}" for key, passed in checks.items())
    qa_lines.extend(["", "## Blocking defects", ""])
    qa_lines.extend(f"- {item}" for item in defects) if defects else qa_lines.append("- None detected.")
    QA_MD.write_text("\n".join(qa_lines) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 1 if defects else 0


if __name__ == "__main__":
    raise SystemExit(main())
