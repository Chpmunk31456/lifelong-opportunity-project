#!/usr/bin/env python3
"""Deterministic source-parity gate for Guide 07.

Automated controls only. This does not certify translation quality, accessibility,
legal accuracy, professional translation, or independent human review.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "project/revision-2026/guide-07/source"
QA = ROOT / "project/revision-2026/guide-07/qa/GUIDE_07_TRILINGUAL_PARITY_QA_09.md"

FILES = {
    "English": BASE / "GUIDE_07_ENGLISH_WORKING_MASTER_v2.md",
    "es-419": BASE / "GUIDE_07_SPANISH_LATAM_WORKING_MASTER_v2.md",
    "pt-BR": BASE / "GUIDE_07_PORTUGUESE_BR_WORKING_MASTER_v2.md",
}

CRITICAL_TOKENS = [
    "US$20.59", "US$14.75", "US$30.16", "5%", "2024", "2034", "341,700",
    "US$40,910", "US$19.67", "US$39,098", "US$18.80", "2026",
    "NOC 64409", "C$16.00", "C$22.00", "C$33.14", "84.1%", "2023–2024",
    "US$5,250", "2025", "48", "SENA",
]

ANCHORS = {
    "English": ["privacy", "cybersecurity", "responsible AI", "accessibility", "Colombia", "Canada"],
    "es-419": ["privacidad", "ciberseguridad", "IA responsable", "accesibilidad", "Colombia", "Canadá"],
    "pt-BR": ["privacidade", "cibersegurança", "IA responsável", "acessibilidade", "Colômbia", "Canadá"],
}


def read(path: Path) -> str:
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        raise SystemExit(f"Unexpected UTF-8 BOM: {path}")
    text = raw.decode("utf-8", errors="strict")
    if "\ufffd" in text:
        raise SystemExit(f"Replacement character detected: {path}")
    return text


def urls(text: str) -> set[str]:
    return set(re.findall(r"https?://[^\s)>\]]+", text))


def numbered_sections(text: str) -> list[int]:
    return [int(m.group(1)) for m in re.finditer(r"^##\s+(\d{1,2})\.\s+", text, re.MULTILINE)]


def main() -> int:
    texts = {name: read(path) for name, path in FILES.items()}
    expected_sections = list(range(1, 20))
    results: list[str] = []

    for locale, text in texts.items():
        sections = numbered_sections(text)
        if sections != expected_sections:
            raise SystemExit(f"{locale}: expected sections 1-19, got {sections}")
        results.append(f"- {locale}: numbered sections 1–19 — PASS")

        missing_tokens = [token for token in CRITICAL_TOKENS if token not in text]
        if missing_tokens:
            raise SystemExit(f"{locale}: missing critical tokens: {missing_tokens}")
        results.append(f"- {locale}: critical numeric/date/NOC/SENA tokens — PASS")

        missing_anchors = [a for a in ANCHORS[locale] if a.casefold() not in text.casefold()]
        if missing_anchors:
            raise SystemExit(f"{locale}: missing control anchors: {missing_anchors}")
        results.append(f"- {locale}: regional/privacy/security/AI/accessibility anchors — PASS")

    canonical_urls = urls(texts["English"])
    if not canonical_urls:
        raise SystemExit("English: no controlled URLs found")
    for locale in ("es-419", "pt-BR"):
        candidate = urls(texts[locale])
        if candidate != canonical_urls:
            raise SystemExit(
                f"{locale}: URL set mismatch; missing={sorted(canonical_urls-candidate)}, extra={sorted(candidate-canonical_urls)}"
            )
    results.append(f"- Shared controlled URL set ({len(canonical_urls)} URLs) — PASS")

    # Assurance claims must remain bounded in localized editions.
    assurance_checks = {
        "es-419": ["no certificada profesionalmente", "no se afirma certificación humana independiente"],
        "pt-BR": ["não certificada profissionalmente", "não se afirma certificação humana independente"],
    }
    for locale, phrases in assurance_checks.items():
        missing = [p for p in phrases if p.casefold() not in texts[locale].casefold()]
        if missing:
            raise SystemExit(f"{locale}: missing assurance boundary phrases: {missing}")
    results.append("- Localization assurance boundaries — PASS")

    QA.parent.mkdir(parents=True, exist_ok=True)
    QA.write_text(
        "# Guide 07 — Trilingual source parity QA 09\n\n"
        "**Status:** PASS — automated structural/content-token parity only\n"
        "**Branch:** `revision/guide-00-100-2026`\n"
        "**Guide:** 07 — Customer Service Specialist / Customer Service Representative\n\n"
        "## Automated checks\n\n"
        + "\n".join(results)
        + "\n\n## Assurance boundary\n\n"
        "This automated PASS verifies structural, URL, critical numeric/date, control-anchor, UTF-8, and assurance-boundary parity. "
        "It does not claim independent human review, professional translation certification, accessibility certification, accreditation, legal review, or publication approval.\n",
        encoding="utf-8",
    )
    print("Guide 07 trilingual source parity: PASS")
    print(f"Shared URLs: {len(canonical_urls)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
