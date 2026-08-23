#!/usr/bin/env python3
"""Apply verified Guide 07 English source freshness corrections.

Fails closed if the expected stale text is not present exactly once.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "project/revision-2026/guide-07/source/GUIDE_07_ENGLISH_WORKING_MASTER_v2.md"

REPLACEMENTS = {
    "- ZipRecruiter reported an average U.S. estimate for **Customer Service Specialist** of **US$40,910 per year (US$19.67/hour)** as of **July 16, 2026**.":
    "- ZipRecruiter reported an average U.S. estimate for **Customer Service Specialist** of **US$40,910 per year (US$19.67/hour)** as of **August 8, 2026**.",
    "- ZipRecruiter reported an average U.S. estimate for **Customer Service Representative** of **US$39,098 per year (US$18.80/hour)** as of **July 17, 2026**.":
    "- ZipRecruiter reported an average U.S. estimate for **Customer Service Representative** of **US$39,098 per year (US$18.80/hour)** as of **August 8, 2026**.",
    "SENA's Betowa catalogue currently lists **Servicio al cliente** as a **48-hour complementary program**, with both in-person and virtual offerings appearing in the current catalogue depending on cohort and filter. Availability and enrollment can change, so verify the live offering before planning around it.":
    "SENA's Betowa catalogue currently lists **Servicio al cliente** as a **48-hour complementary, in-person special course** on the cited page. Availability, cohort, location, modality, and enrollment can change, so verify the live offering before planning around it."
}


def main() -> int:
    raw = SOURCE.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        raise SystemExit("Unexpected UTF-8 BOM in Guide 07 English master")
    text = raw.decode("utf-8", errors="strict")
    if "\ufffd" in text:
        raise SystemExit("Replacement character found in Guide 07 English master")

    for old, new in REPLACEMENTS.items():
        count = text.count(old)
        if count != 1:
            raise SystemExit(f"Expected exactly one stale source string, found {count}: {old[:90]!r}")
        text = text.replace(old, new)

    SOURCE.write_text(text, encoding="utf-8", newline="\n")
    print("Guide 07 verified freshness corrections applied: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
