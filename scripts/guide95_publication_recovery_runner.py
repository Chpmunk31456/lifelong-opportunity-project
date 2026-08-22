#!/usr/bin/env python3
"""Guide 95 recovery runner with narrow publication-only compatibility fixes.

The frozen English master correctly uses the adjectival form "48-hour virtual
complementary program", while es-419 and pt-BR use "48 horas". The original
recovery validator accepted only whitespace-separated "48 hours/horas".

Pandoc's default GFM reader also enables dollar-sign TeX math. In salary prose
such as "$63,976/year ... $45,358", that can incorrectly convert ordinary
currency text into one unbreakable math span. This runner disables only the
`tex_math_dollars` GFM extension during DOCX generation. Frozen Markdown,
currency values, hyperlinks, research, and localization content are unchanged.
"""
from __future__ import annotations

import sys

import guide95_publication_recovery as recovery

OLD = r"48\s+(?:hours|horas)"
NEW = r"(?:48(?:\s+|-)hours?|48\s+horas)"

if OLD not in recovery.CONTROLS:
    raise SystemExit("Guide 95 recovery control set changed unexpectedly; refusing to patch")

recovery.CONTROLS = [NEW if pattern == OLD else pattern for pattern in recovery.CONTROLS]

if len(recovery.CONTROLS) != len(set(recovery.CONTROLS)):
    raise SystemExit("Guide 95 recovery controls contain an unexpected duplicate")

_original_run = recovery.run


def publication_safe_run(cmd: list[str], *, capture: bool = False):
    """Disable GFM dollar-sign math only for Pandoc DOCX generation."""
    patched = list(cmd)
    if patched and patched[0] == "pandoc" and "-t" in patched:
        target_index = patched.index("-t") + 1
        if target_index < len(patched) and patched[target_index] == "docx":
            if "-f" not in patched:
                raise SystemExit("Guide 95 Pandoc invocation is missing its input-format flag")
            format_index = patched.index("-f") + 1
            if format_index >= len(patched) or patched[format_index] != "gfm":
                raise SystemExit(
                    f"Guide 95 Pandoc input format changed unexpectedly: {patched[format_index] if format_index < len(patched) else '<missing>'}"
                )
            patched[format_index] = "gfm-tex_math_dollars"
    return _original_run(patched, capture=capture)


recovery.run = publication_safe_run


def main() -> None:
    if len(sys.argv) != 2 or sys.argv[1] not in {"build", "close-status"}:
        raise SystemExit("Usage: guide95_publication_recovery_runner.py {build|close-status}")
    if sys.argv[1] == "build":
        recovery.build()
    else:
        recovery.close_status()


if __name__ == "__main__":
    main()
