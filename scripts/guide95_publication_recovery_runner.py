#!/usr/bin/env python3
"""Guide 95 recovery runner with narrow publication-only compatibility fixes.

The frozen English master correctly uses the adjectival form "48-hour virtual
complementary program", while es-419 and pt-BR use "48 horas". The original
recovery validator accepted only whitespace-separated "48 hours/horas".

The frozen masters also contain reader-verification URLs whose raw display text
can exceed the Word/PDF line width. This runner keeps every hyperlink target
unchanged but uses a temporary Pandoc Lua filter to display long raw URLs as
"Source link" in generated DOCX/PDF editions. Frozen Markdown is never edited.
"""
from __future__ import annotations

import sys
from pathlib import Path

import guide95_publication_recovery as recovery

OLD = r"48\s+(?:hours|horas)"
NEW = r"(?:48(?:\s+|-)hours?|48\s+horas)"

if OLD not in recovery.CONTROLS:
    raise SystemExit("Guide 95 recovery control set changed unexpectedly; refusing to patch")

recovery.CONTROLS = [NEW if pattern == OLD else pattern for pattern in recovery.CONTROLS]

if len(recovery.CONTROLS) != len(set(recovery.CONTROLS)):
    raise SystemExit("Guide 95 recovery controls contain an unexpected duplicate")

FILTER = Path("/tmp/guide95_url_safe.lua")
FILTER_TEXT = r'''local function is_long_url(s)
  return string.match(s, '^https?://') and string.len(s) > 45
end

function Link(el)
  local text = pandoc.utils.stringify(el.content)
  if is_long_url(text) then
    return pandoc.Link({pandoc.Str('Source link')}, el.target, el.title)
  end
  return el
end

function Str(el)
  local text = el.text
  if is_long_url(text) then
    local target = text
    local trailing = ''
    local last = string.sub(target, -1)
    if last == '.' or last == ',' or last == ';' or last == ':' then
      trailing = last
      target = string.sub(target, 1, -2)
    end
    local link = pandoc.Link({pandoc.Str('Source link')}, target)
    if trailing ~= '' then
      return {link, pandoc.Str(trailing)}
    end
    return link
  end
  return el
end
'''

_original_run = recovery.run


def publication_safe_run(cmd: list[str], *, capture: bool = False):
    """Inject a display-only URL filter into Pandoc DOCX generation."""
    patched = list(cmd)
    if patched and patched[0] == "pandoc" and "-t" in patched:
        target_index = patched.index("-t") + 1
        if target_index < len(patched) and patched[target_index] == "docx":
            FILTER.write_text(FILTER_TEXT, encoding="utf-8")
            option = f"--lua-filter={FILTER}"
            if option not in patched:
                insert_at = patched.index("-o") if "-o" in patched else len(patched)
                patched.insert(insert_at, option)
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
