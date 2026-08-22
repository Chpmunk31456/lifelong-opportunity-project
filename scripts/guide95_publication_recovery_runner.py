#!/usr/bin/env python3
"""Guide 95 recovery runner with corrected cross-language 48-hour control.

The frozen English master correctly uses the adjectival form "48-hour virtual
complementary program", while es-419 and pt-BR use "48 horas". The original
recovery validator accepted only whitespace-separated "48 hours/horas".
This wrapper preserves every other validator and release mechanic unchanged.
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


def main() -> None:
    if len(sys.argv) != 2 or sys.argv[1] not in {"build", "close-status"}:
        raise SystemExit("Usage: guide95_publication_recovery_runner.py {build|close-status}")
    if sys.argv[1] == "build":
        recovery.build()
    else:
        recovery.close_status()


if __name__ == "__main__":
    main()
