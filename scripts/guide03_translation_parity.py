#!/usr/bin/env python3
"""Fail-closed parity checks for Guide 03 translated working masters.

This automated consistency control does not constitute professional translation
certification, independent human review, accreditation, accessibility
certification, legal review, coding certification, or publication approval.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "project/revision-2026/guide-03/source"
FILES = {
    "English": SOURCE / "GUIDE_03_ENGLISH_WORKING_MASTER_v2.md",
    "Spanish": SOURCE / "GUIDE_03_SPANISH_LATAM_WORKING_MASTER_v2.md",
    "Portuguese": SOURCE / "GUIDE_03_PORTUGUESE_BR_WORKING_MASTER_v2.md",
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
    expected_sections = list(range(1, 20))

    for language, text in docs.items():
        sections = numbered_headings(text)
        if sections != expected_sections:
            raise SystemExit(f"{language} numbered-section sequence mismatch: {sections}")

    controls = [
        ("US$50,250", "US$50,250", "US$50.250", "BLS annual wage"),
        ("194,800", "194,800", "194.800", "BLS 2024 employment"),
        ("7%", "7%", "7%", "BLS projected growth"),
        ("14,200", "14,200", "14.200", "BLS annual openings"),
        ("US$45,672", "US$45,672", "US$45.672", "market annual estimate"),
        ("US$21.96", "US$21.96", "US$21,96", "market hourly estimate"),
        ("July 20, 2026", "20 de julio de 2026", "20 de julho de 2026", "market source date"),
        ("October 1, 2026", "1 de octubre de 2026", "1º de outubro de 2026", "ICD effective date"),
        ("May 1, 2026", "1 de mayo de 2026", "1º de maio de 2026", "AHIMA codebook date"),
        ("NOC 12111", "NOC 12111", "NOC 12111", "Canada occupational group"),
        ("C$22.00", "C$22.00", "C$22,00", "Canada NOC low wage"),
        ("C$30.51", "C$30.51", "C$30,51", "Canada NOC median wage"),
        ("C$46.19", "C$46.19", "C$46,19", "Canada NOC high wage"),
        ("C$18.46", "C$18.46", "C$18,46", "Canada billing low wage"),
        ("C$25.00", "C$25.00", "C$25,00", "Canada billing median wage"),
        ("C$35.71", "C$35.71", "C$35,71", "Canada billing high wage"),
        ("November 19, 2025", "19 de noviembre de 2025", "19 de novembro de 2025", "Job Bank update date"),
        ("2023–2024", "2023–2024", "2023–2024", "Job Bank reference period"),
        ("40 hours", "40 horas", "40 horas", "SENA virtual duration"),
        ("48 hours", "48 horas", "48 horas", "SENA in-person duration"),
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
        "BLS", "CMS", "HIPAA", "ICD-10-CM", "ICD-10-PCS", "CPT", "HCPCS",
        "AHIMA", "AAPC", "WIOA", "NOC 12111", "SENA", "Registered Apprenticeship",
    ]
    for language, text in clean.items():
        for term in formal_terms:
            require(text, term, f"{language} formal-term anchor")

    anchors = {
        "Spanish": [
            "no promete",
            "estimación de mercado no gubernamental",
            "no licencias gubernamentales",
            "mínimo necesario",
            "no rigen automáticamente",
            "No invente una",
        ],
        "Portuguese": [
            "não promete",
            "estimativa de mercado não governamental",
            "não licenças governamentais",
            "mínimo necessário",
            "não regem automaticamente",
            "Não invente uma",
        ],
    }
    for language, phrases in anchors.items():
        for phrase in phrases:
            require(clean[language], phrase, f"{language} claims-control anchor")

    print("Guide 03 English↔es-419↔pt-BR automated parity checks: PASS")
    print("Numbered sections per language: 19")
    print(f"Shared external URLs: {len(url_sets['English'])}")
    print(f"High-impact numeric/date controls per language: {len(controls)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
