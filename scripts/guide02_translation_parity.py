#!/usr/bin/env python3
"""Fail-closed parity checks for Guide 02 translated working masters.

This is an automated consistency control, not professional translation
certification, independent human review, accreditation, accessibility
certification, legal review, or publication approval.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN = ROOT / "project/revision-2026/guide-02/source/GUIDE_02_ENGLISH_WORKING_MASTER_v2.md"
ES = ROOT / "project/revision-2026/guide-02/source/GUIDE_02_SPANISH_LATAM_WORKING_MASTER_v2.md"


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


def numbered_headings(text: str) -> list[int]:
    return [int(m.group(1)) for m in re.finditer(r"^##\s+(\d{1,2})\.\s+", text, re.MULTILINE)]


def urls(text: str) -> set[str]:
    return set(re.findall(r"https?://[^\s)>\]]+", text))


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise SystemExit(f"Missing {label}: {needle}")


def main() -> int:
    en = read(EN)
    es = read(ES)

    expected_sections = list(range(1, 20))
    en_sections = numbered_headings(en)
    es_sections = numbered_headings(es)
    if en_sections != expected_sections:
        raise SystemExit(f"English numbered-section sequence mismatch: {en_sections}")
    if es_sections != expected_sections:
        raise SystemExit(f"Spanish numbered-section sequence mismatch: {es_sections}")

    # High-impact numerical/date facts must remain equivalent across languages.
    pairs = [
        ("$51,030", "US$51,030", "BLS median annual proxy"),
        ("$24.54", "US$24.54", "BLS hourly proxy"),
        ("11%", "11%", "BLS projected growth"),
        ("2024 to 2034", "2024 y 2034", "BLS outlook period"),
        ("$41,023", "US$41,023", "ZipRecruiter annual estimate"),
        ("$19.72", "US$19.72", "ZipRecruiter hourly estimate"),
        ("July 16, 2026", "16 de julio de 2026", "ZipRecruiter as-of date"),
        ("NOC 42201", "NOC 42201", "Canada occupational grouping"),
        ("C$19.00", "C$19.00", "Canada low wage"),
        ("C$26.00", "C$26.00", "Canada median wage"),
        ("C$36.06", "C$36.06", "Canada high wage"),
        ("June 2, 2026", "2 de junio de 2026", "Job Bank summary date"),
        ("November 19, 2025", "19 de noviembre de 2025", "Job Bank wage-table date"),
        ("2023–2024", "2023–2024", "Job Bank reference period"),
    ]
    for en_token, es_token, label in pairs:
        require(en, en_token, f"English {label}")
        require(es, es_token, f"Spanish {label}")

    # Preserve the same controlled source destinations; translated prose must not
    # silently alter official URLs.
    en_urls = urls(en)
    es_urls = urls(es)
    if en_urls != es_urls:
        missing = sorted(en_urls - es_urls)
        extra = sorted(es_urls - en_urls)
        raise SystemExit(f"URL-set mismatch. Missing in Spanish={missing}; extra in Spanish={extra}")

    # Claims-control anchors.
    require(es, "proxy ocupacional oficial", "official-proxy label")
    require(es, "estimación no gubernamental", "non-government market label")
    require(es, "no constituyen una licencia nacional universal", "SAMHSA credential limitation")
    require(es, "no establecen una credencial nacional", "Colombia credential limitation")
    require(es, "las credenciales no se transfieren automáticamente entre países", "Latin America portability limitation")
    require(es, "no afirma certificación profesional de traducción", "translation-certification limitation")

    # Obvious unsafe overclaims must remain absent.
    forbidden = [
        "traducción certificada",
        "certificación humana independiente obtenida",
        "empleo garantizado",
        "salario garantizado",
    ]
    for phrase in forbidden:
        if phrase.casefold() in es.casefold():
            raise SystemExit(f"Forbidden unsupported claim found in Spanish: {phrase}")

    print("Guide 02 English↔es-419 automated parity checks: PASS")
    print(f"Numbered sections: {len(es_sections)}")
    print(f"Shared external URLs: {len(es_urls)}")
    print(f"High-impact numeric/date controls checked: {len(pairs)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
