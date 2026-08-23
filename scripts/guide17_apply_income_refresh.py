from pathlib import Path

MASTER = Path("17-bank-teller-and-member-services-representative/references/english-v2-working-master.md")
RECHECK = Path("17-bank-teller-and-member-services-representative/references/english-v2-private-income-recheck-2026-08-09.md")

OLD = "- **Salary.com:** $37,554/year average, approximately $18/hour; source states **As of August 01, 2026**."
NEW = "- **Salary.com:** $37,557/year average, approximately $18/hour; source states **As of July 01, 2026**."

text = MASTER.read_text(encoding="utf-8")
if "\ufffd" in text:
    raise SystemExit("FAIL: Unicode replacement character present in Guide 17 master")

if OLD in text:
    text = text.replace(OLD, NEW, 1)
elif NEW not in text:
    raise SystemExit("FAIL: expected Salary.com source-state line not found; refusing broad edit")

# These are the currently reproducible private-market source states for this controlled gate.
required = [
    "- **Indeed:** $19.25/hour average base salary; page updated July 20, 2026 and based on approximately 15.2k salaries from job postings over the prior 36 months.",
    "- **ZipRecruiter:** $36,351/year average, approximately $17.48/hour; page state reviewed July 27, 2026, with a reported central range around $32,000-$40,000.",
    NEW,
]
for item in required:
    if item not in text:
        raise SystemExit(f"FAIL: required verified private-income statement missing: {item}")

unverified = [
    "$19.28/hour",
    "15.5k salaries",
    "updated August 2, 2026",
    "page state reviewed August 9, 2026",
    "$37,554/year average",
    "As of August 01, 2026",
]
for item in unverified:
    if item in text:
        raise SystemExit(f"FAIL: superseded/unreproducible private-income value still present: {item}")

MASTER.write_text(text, encoding="utf-8", newline="\n")

RECHECK.write_text(
    "# Guide 17 — private-income correction recheck\n\n"
    "**QA date:** 2026-08-09\n"
    "**Target:** `references/english-v2-working-master.md`\n"
    "**Gate:** affected private-income traceability and source-state recheck\n"
    "**Result:** **PASS**\n\n"
    "## Verified working-master state\n\n"
    "- Indeed remains labeled as a non-government estimate at **$19.25/hour**, based on approximately **15.2k salaries**, with the source page stating **updated July 20, 2026**.\n"
    "- ZipRecruiter remains labeled as a non-government estimate at **$36,351/year** (approximately **$17.48/hour**), with the source page stating **As of Jul 27, 2026** and a displayed central range around **$32,000-$40,000**.\n"
    "- Salary.com is corrected to **$37,557/year** (approximately **$18/hour**), with the retrievable source page stating **As of July 01, 2026** and **Last Updated on July 01, 2026**.\n\n"
    "The three figures remain separated from official BLS wage statistics and are not averaged together or represented as guaranteed pay.\n\n"
    "## Gate result\n\n"
    "The private-income defect that blocked the English pre-freeze gate is corrected. This PASS applies only to the affected private-income source-state and traceability check. English source freeze still requires the remaining controlled pre-freeze checks to be confirmed.\n\n"
    "## Certification boundary\n\n"
    "This is an internal automated QA record. It is not independent human review, professional translation certification, accessibility certification, accreditation, legal review, regulator approval, financial advice, or an income guarantee.\n",
    encoding="utf-8",
    newline="\n",
)

print("Guide 17 private-income refresh: PASS")
