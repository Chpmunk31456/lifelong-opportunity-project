#!/usr/bin/env python3
"""Bind Guide 00 publication recovery to the exact blobs in the latest technical QA."""
from __future__ import annotations

import re
import sys
from pathlib import Path

import guide00_publication_recovery as pub

TECH = Path("project/revision-2026/guide-00/qa/GUIDE_00_TRILINGUAL_TECHNICAL_QA_08.md")


def bind() -> None:
    text = TECH.read_text(encoding="utf-8-sig")
    patterns = {
        "en": r"\*\*English:\*\*[^\n]*\n\s+- Git blob: `([0-9a-f]{40})`",
        "es-419": r"\*\*es-419:\*\*[^\n]*\n\s+- Git blob: `([0-9a-f]{40})`",
        "pt-BR": r"\*\*pt-BR:\*\*[^\n]*\n\s+- Git blob: `([0-9a-f]{40})`",
    }
    expected = {}
    for locale, pattern in patterns.items():
        m = re.search(pattern, text)
        if not m:
            raise SystemExit(f"could not parse {locale} blob from latest technical QA")
        expected[locale] = m.group(1)
    if "**Trilingual Technical QA: PASS.**" not in text:
        raise SystemExit("latest technical QA is not PASS")
    pub.EXPECTED_BLOBS = expected
    print(f"Bound publication preflight to technical-QA blobs: {expected}")


def main() -> None:
    if len(sys.argv) != 2 or sys.argv[1] not in {"build", "close-status"}:
        raise SystemExit("usage: guide00_publication_recovery_dynamic.py {build|close-status}")
    bind()
    if sys.argv[1] == "build":
        pub.build()
    else:
        pub.close_status()


if __name__ == "__main__":
    main()
