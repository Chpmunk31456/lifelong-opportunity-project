#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "project/revision-2026/guide-05/source"
FILES = {
    "en": BASE / "GUIDE_05_ENGLISH_WORKING_MASTER_v2.md",
    "es": BASE / "GUIDE_05_SPANISH_LATAM_WORKING_MASTER_v2.md",
    "pt": BASE / "GUIDE_05_PORTUGUESE_BR_WORKING_MASTER_v2.md",
}

REQUIRED_SECTIONS = [str(i) for i in range(1, 20)]
REQUIRED_URLS = [
    "https://www.bls.gov/ooh/office-and-administrative-support/bookkeeping-accounting-and-auditing-clerks.htm",
    "https://www.bls.gov/ooh/office-and-administrative-support/financial-clerks.htm",
    "https://www.irs.gov/newsroom/irs-updates-frequently-asked-questions-about-section-127-educational-assistance-programs",
    "https://www.apprenticeship.gov/",
    "https://www.careeronestop.org/LocalHelp/AmericanJobCenters/american-job-centers.aspx",
    "https://studentaid.gov/",
    "https://www.ziprecruiter.com/Salaries/Bookkeeper-Salary",
    "https://www.ziprecruiter.com/Salaries/Payroll-Specialist-Salary",
    "https://payroll.org/education-certification/education/learning-paths/fpc-certification",
    "https://payroll.org/education-certification/education/learning-paths/cpp-certification",
    "https://payroll.org/certification/certification/overview",
    "https://www.serviciodeempleo.gov.co/",
]
NUMERIC_GROUPS = [
    ["49,210", "49.210"],
    ["55,290", "55.290"],
    ["170,000", "170.000"],
    ["50,573", "50.573"],
    ["24.31", "24,31"],
    ["56,982", "56.982"],
    ["27.40", "27,40"],
    ["19.55", "19,55"],
    ["28.02", "28,02"],
    ["45.07", "45,07"],
    ["20.00", "20,00"],
    ["30.00", "30,00"],
    ["43.27", "43,27"],
    ["5,250", "5.250"],
    ["2024–2034", "2024-2034", "2024 e 2034"],
    ["2023–2024", "2023-2024", "2023 e 2024"],
]


def fail(msg):
    print(f"FAIL: {msg}")
    sys.exit(1)

texts = {}
for lang, path in FILES.items():
    if not path.exists():
        fail(f"missing {lang} master: {path}")
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        fail(f"UTF-8 BOM present in {lang}")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        fail(f"invalid UTF-8 in {lang}: {exc}")
    texts[lang] = text

for lang, text in texts.items():
    headings = re.findall(r"^##\s+(\d+)\.", text, flags=re.M)
    missing = [s for s in REQUIRED_SECTIONS if s not in headings]
    if missing:
        fail(f"{lang} missing numbered sections: {missing}")
    for url in REQUIRED_URLS:
        if url not in text:
            fail(f"{lang} missing required URL: {url}")
    for group in NUMERIC_GROUPS:
        if not any(token in text for token in group):
            fail(f"{lang} missing high-impact numeric/date control: {group}")

safety_markers = {
    "en": ["not government licenses", "not guarantees", "Do not invent a national"],
    "es": ["no son licencias gubernamentales", "no son garantías", "No invente un salario nacional"],
    "pt": ["não são licenças governamentais", "não são garantias", "Não invente um salário nacional"],
}
for lang, markers in safety_markers.items():
    for marker in markers:
        if marker not in texts[lang]:
            fail(f"{lang} missing safety/assurance marker: {marker}")

print("PASS: Guide 05 trilingual source parity controls satisfied")
