#!/usr/bin/env python3
"""Fail-closed source-parity checks for Guide 04 controlled masters.

This automated consistency control does not constitute professional translation
certification, independent human review, accreditation, accessibility
certification, legal review, or publication approval.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "project/revision-2026/guide-04/working"
FILES = {
    "English": SOURCE / "GUIDE_04_ENGLISH_WORKING_MASTER_06.md",
    "Spanish": SOURCE / "GUIDE_04_ES_419_WORKING_MASTER_08.md",
    "Portuguese": SOURCE / "GUIDE_04_PT_BR_WORKING_MASTER_10.md",
}


def read(path: Path) -> str:
    data = path.read_bytes()
    if data.startswith(b"\xef\xbb\xbf"):
        raise SystemExit(f"UTF-8 BOM is not permitted: {path}")
    text = data.decode("utf-8", errors="strict")
    if "\ufffd" in text:
        raise SystemExit(f"Unicode replacement character found: {path}")
    if "\r" in text:
        raise SystemExit(f"Non-LF line ending found: {path}")
    return text


def plain(text: str) -> str:
    return re.sub(r"[*_`]+", "", text)


def numbered_headings(text: str) -> list[int]:
    return [int(m.group(1)) for m in re.finditer(r"^#\s+(\d{1,2})\.\s+", text, re.MULTILINE)]


def urls(text: str) -> set[str]:
    return set(re.findall(r"https?://[^\s)>\]]+", text))


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise SystemExit(f"Missing {label}: {needle}")


def main() -> int:
    docs = {name: read(path) for name, path in FILES.items()}
    clean = {name: plain(text) for name, text in docs.items()}
    expected_sections = list(range(1, 23))

    for language, text in docs.items():
        sections = numbered_headings(text)
        if sections != expected_sections:
            raise SystemExit(f"{language} numbered-section sequence mismatch: {sections}")

    controls = [
        ("US$100,750", "US$100.750", "US$100.750", "BLS median annual wage"),
        ("6%", "6 %", "6%", "BLS projected growth"),
        ("78,200", "78.200", "78.200", "BLS annual openings"),
        ("US$59,915", "US$59.915", "US$59.915", "market annual estimate"),
        ("US$28.81", "US$28,81", "US$28,81", "market hourly estimate"),
        ("Jul 20, 2026", "Jul 20, 2026", "Jul 20, 2026", "market-source displayed date"),
        ("August 8, 2026", "8 de agosto de 2026", "8 de agosto de 2026", "market-source check date"),
        ("SOC 13-1082", "SOC 13-1082", "SOC 13-1082", "BLS occupational code"),
        ("4,656 hours", "4.656 horas", "4.656 horas", "SENA technologist duration"),
        ("48 hours", "48 horas", "48 horas", "SENA short-course duration"),
        ("41,000", "41.000", "41.000", "SENA free-place statement"),
        ("2024 to 2034", "2024 a 2034", "2024 a 2034", "BLS projection period"),
    ]
    for en, es, pt, label in controls:
        require(clean["English"], en, f"English {label}")
        require(clean["Spanish"], es, f"Spanish {label}")
        require(clean["Portuguese"], pt, f"Portuguese {label}")

    url_sets = {language: urls(text) for language, text in docs.items()}
    for language in ("Spanish", "Portuguese"):
        if url_sets[language] != url_sets["English"]:
            missing = sorted(url_sets["English"] - url_sets[language])
            extra = sorted(url_sets[language] - url_sets["English"])
            raise SystemExit(f"URL-set mismatch for {language}. Missing={missing}; extra={extra}")

    formal_terms = [
        "BLS", "SOC 13-1082", "WIOA", "FAFSA", "Registered Apprenticeship",
        "NOC", "SENA", "Betowa", "Servicio Público de Empleo", "CAPM", "PMP",
    ]
    for language, text in clean.items():
        for term in formal_terms:
            require(text, term, f"{language} formal-term anchor")

    claims_anchors = {
        "English": [
            "does not promise",
            "non-government market source",
            "Funding is not automatic",
            "no universal Project Coordinator license",
            "no general rule in this guide",
        ],
        "Spanish": [
            "no promete",
            "fuente de mercado no gubernamental",
            "El financiamiento no es automático",
            "No existe una licencia universal",
            "no existe una regla general",
        ],
        "Portuguese": [
            "não promete",
            "fonte de mercado não governamental",
            "O financiamento não é automático",
            "Não existe uma licença universal",
            "não estabelece uma regra geral",
        ],
    }
    for language, phrases in claims_anchors.items():
        for phrase in phrases:
            require(clean[language], phrase, f"{language} claims-control anchor")

    print("Guide 04 English↔es-419↔pt-BR automated parity checks: PASS")
    print("Numbered sections per language: 22")
    print(f"Shared external URLs: {len(url_sets['English'])}")
    print(f"High-impact numeric/date controls per language: {len(controls)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
