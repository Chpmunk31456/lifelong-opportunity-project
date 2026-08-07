#!/usr/bin/env python3
"""Fail-closed parity checks for Guide 02 translated working masters.

This automated consistency control does not constitute professional translation
certification, independent human review, accreditation, accessibility
certification, legal review, medical review, or publication approval.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "project/revision-2026/guide-02/source"
FILES = {
    "English": SOURCE / "GUIDE_02_ENGLISH_WORKING_MASTER_v2.md",
    "Spanish": SOURCE / "GUIDE_02_SPANISH_LATAM_WORKING_MASTER_v2.md",
    "Portuguese": SOURCE / "GUIDE_02_PORTUGUESE_BR_WORKING_MASTER_v2.md",
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
    """Remove lightweight Markdown emphasis so QA tests meaning, not styling."""
    return re.sub(r"[*_`]+", "", text)


def numbered_headings(text: str) -> list[int]:
    return [int(m.group(1)) for m in re.finditer(r"^##\s+(\d{1,2})\.\s+", text, re.MULTILINE)]


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
        ("$51,030", "US$51,030", "US$ 51.030", "BLS annual proxy"),
        ("$24.54", "US$24.54", "US$ 24,54", "BLS hourly proxy"),
        ("11%", "11%", "11%", "BLS projected growth"),
        ("2024 to 2034", "2024 y 2034", "2024 e 2034", "BLS outlook period"),
        ("$41,023", "US$41,023", "US$ 41.023", "market annual estimate"),
        ("$19.72", "US$19.72", "US$ 19,72", "market hourly estimate"),
        ("July 16, 2026", "16 de julio de 2026", "16 de julho de 2026", "market as-of date"),
        ("NOC 42201", "NOC 42201", "NOC 42201", "Canada occupational group"),
        ("C$19.00", "C$19.00", "C$ 19,00", "Canada low wage"),
        ("C$26.00", "C$26.00", "C$ 26,00", "Canada median wage"),
        ("C$36.06", "C$36.06", "C$ 36,06", "Canada high wage"),
        ("June 2, 2026", "2 de junio de 2026", "2 de junho de 2026", "Job Bank summary date"),
        ("November 19, 2025", "19 de noviembre de 2025", "19 de novembro de 2025", "Job Bank wage date"),
        ("2023–2024", "2023–2024", "2023–2024", "Job Bank reference period"),
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

    anchors = {
        "Spanish": [
            "no promete",
            "proxy ocupacional oficial",
            "estimación no gubernamental",
            "no constituyen una licencia nacional universal",
            "no establecen una credencial nacional",
            "las credenciales no se transfieren automáticamente entre países",
            "no afirma certificación profesional de traducción",
        ],
        "Portuguese": [
            "não promete",
            "proxy ocupacional oficial",
            "estimativa não governamental",
            "não constituem uma licença nacional universal",
            "não estabelecem uma credencial nacional",
            "credenciais não são automaticamente transferíveis entre países",
            "certificação profissional de tradução",
            "não constitui certificação humana independente",
        ],
    }
    for language, phrases in anchors.items():
        for phrase in phrases:
            require(clean[language], phrase, f"{language} claims-control anchor")

    print("Guide 02 English↔es-419↔pt-BR automated parity checks: PASS")
    print("Numbered sections per language: 19")
    print(f"Shared external URLs: {len(url_sets['English'])}")
    print(f"High-impact numeric/date controls per language: {len(controls)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
