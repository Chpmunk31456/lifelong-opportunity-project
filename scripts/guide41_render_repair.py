from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    ROOT / 'project/revision-2026/guide-41/working-masters/GUIDE_41_CARPENTER_AND_CABINETMAKING_TECHNICIAN_ENGLISH_v2.md',
    ROOT / 'project/revision-2026/guide-41/working-masters/GUIDE_41_CARPENTER_AND_CABINETMAKING_TECHNICIAN_ES419_v2.md',
    ROOT / 'project/revision-2026/guide-41/working-masters/GUIDE_41_CARPENTER_AND_CABINETMAKING_TECHNICIAN_PTBR_v2.md',
]
URL_RE = re.compile(r'https://[^\s)<>`]+')

for path in FILES:
    text = path.read_text(encoding='utf-8')
    heading = '## Current sources' if 'ENGLISH' in path.name else ('## Fuentes actuales' if 'ES419' in path.name else '## Fontes atuais')
    start = text.find(heading)
    if start < 0:
        raise SystemExit(f'{path}: source heading not found')
    end_candidates = [text.find(h, start + len(heading)) for h in ('## Source and review note','## Nota sobre fuentes y revisión','## Nota de fonte e revisão')]
    end_candidates = [x for x in end_candidates if x >= 0]
    if not end_candidates:
        raise SystemExit(f'{path}: source-section end heading not found')
    end = min(end_candidates)
    before, section, after = text[:start], text[start:end], text[end:]
    # Replace only naked URLs in source bullets with markdown links. This keeps the exact URL
    # in the source and parity controls while preventing long URLs from rendering past page margins.
    def repl(m):
        url = m.group(0)
        prefix = section[max(0,m.start()-2):m.start()]
        if prefix.endswith(']('):
            return url
        return f'[source]({url})'
    updated_section = URL_RE.sub(repl, section)
    updated = before + updated_section + after
    path.write_text(updated, encoding='utf-8')

# Fail closed: URL sets must remain identical across all three editions.
sets = [set(URL_RE.findall(p.read_text(encoding='utf-8'))) for p in FILES]
if not (sets[0] == sets[1] == sets[2]):
    raise SystemExit('Guide 41 render repair altered trilingual source URL parity')
if len(sets[0]) != 13:
    raise SystemExit(f'Guide 41 render repair expected 13 frozen source URLs, found {len(sets[0])}')
print('Guide 41 render repair PASS: source URLs preserved, markdown display labels applied, trilingual URL parity intact.')
