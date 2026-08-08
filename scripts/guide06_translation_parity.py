#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "project/revision-2026/guide-06/source"
FILES = {
    "en": BASE / "GUIDE_06_ENGLISH_WORKING_MASTER_v2.md",
    "es": BASE / "GUIDE_06_SPANISH_LATAM_WORKING_MASTER_v2.md",
    "pt": BASE / "GUIDE_06_PORTUGUESE_BR_WORKING_MASTER_v2.md",
}

REQUIRED_SECTIONS = [str(i) for i in range(1, 20)]
REQUIRED_URLS = [
    "https://www.bls.gov/ooh/office-and-administrative-support/secretaries-and-administrative-assistants.htm",
    "https://www.irs.gov/newsroom/irs-updates-frequently-asked-questions-about-section-127-educational-assistance-programs",
    "https://www.apprenticeship.gov/",
    "https://www.careeronestop.org/LocalHelp/AmericanJobCenters/american-job-centers.aspx",
    "https://studentaid.gov/",
    "https://studentaid.gov/understand-aid/types/scholarships",
    "https://www.ziprecruiter.com/Salaries/Administrative-Asst-Salary",
    "https://www.ziprecruiter.com/Salaries/Office-Coordinator-Salary",
    "https://www.jobbank.gc.ca/marketreport/summary-occupation/24789/ca",
    "https://www.jobbank.gc.ca/wagereport/occupation/295982",
    "https://betowa.sena.edu.co/oferta/asistencia-administrativa?programId=179054",
    "https://www.serviciodeempleo.gov.co/",
]
NUMERIC_GROUPS = [
    ["47,460", "47.460"],
    ["33,840", "33.840"],
    ["76,550", "76.550"],
    ["46,290", "46.290"],
    ["43,768", "43.768"],
    ["21.04", "21,04"],
    ["42,872", "42.872"],
    ["20.61", "20,61"],
    ["19.23", "19,23"],
    ["26.44", "26,44"],
    ["36.88", "36,88"],
    ["5,250", "5.250"],
    ["2024 to 2034", "entre 2024 y 2034", "de 2024 a 2034", "2024 a 2034", "2024–2034", "2024-2034"],
    ["2023–2024", "2023-2024", "2023 a 2024"],
]


def fail(msg: str) -> None:
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
    if "\ufffd" in text:
        fail(f"replacement character present in {lang}")
    texts[lang] = text

for lang, text in texts.items():
    headings = re.findall(r"^##\s+(\d+)\.", text, flags=re.M)
    if headings != REQUIRED_SECTIONS:
        fail(f"{lang} expected numbered sections {REQUIRED_SECTIONS}, got {headings}")
    for url in REQUIRED_URLS:
        if url not in text:
            fail(f"{lang} missing required URL: {url}")
    for group in NUMERIC_GROUPS:
        if not any(token in text for token in group):
            fail(f"{lang} missing high-impact numeric/date control: {group}")

for lang, text in texts.items():
    if lang == "en" and "independent human" not in text.casefold():
        fail("English missing independent-human-certification disclaimer")
    if lang == "es" and "certificación humana independiente" not in text.casefold():
        fail("Spanish missing independent-human-certification disclaimer")
    if lang == "pt" and "certificação humana independente" not in text.casefold():
        fail("Portuguese missing independent-human-certification disclaimer")

canonical = set(REQUIRED_URLS)
for lang, text in texts.items():
    found = set(re.findall(r"https?://[^\s)>\]]+", text))
    if found != canonical:
        fail(f"{lang} URL set differs from controlled source ledger: {sorted(found ^ canonical)}")

print("PASS: Guide 06 trilingual source parity controls satisfied")
