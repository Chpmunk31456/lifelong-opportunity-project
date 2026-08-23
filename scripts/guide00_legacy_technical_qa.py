#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path('.')
GUIDE = Path('project/revision-2026/guide-00')
QA = GUIDE / 'qa/GUIDE_00_TRILINGUAL_TECHNICAL_QA_08.md'
HELPER = GUIDE / 'GUIDE_00_HELPER_STATUS.json'
SOURCES = {
    'English': Path('00-foundation-guide/source/Lifelong_Opportunity_Foundation_Guide_English_v1.1_INTEGRATED_MASTER.md'),
    'es-419': Path('00-foundation-guide/source/Lifelong_Opportunity_Foundation_Guide_es-419_v1.1_INTEGRATED_MASTER.md'),
    'pt-BR': Path('00-foundation-guide/source/Lifelong_Opportunity_Foundation_Guide_pt-BR_v1.1_INTEGRATED_MASTER.md'),
}
OBSOLETE_RED_SEAL = 'https://www.red-seal.ca/eng/contact/c.4nt.1ct.shtml'


def blob(path: Path) -> str:
    return subprocess.check_output(['git', 'hash-object', str(path)], text=True).strip()


def urls(text: str) -> list[str]:
    vals = re.findall(r'https?://[^\s)<>\]]+', text)
    return sorted({u.rstrip('.,;:') for u in vals})


def section_numbers(text: str) -> list[int]:
    nums = []
    for line in text.splitlines():
        m = re.match(r'^#\s+(\d+)\.', line.strip())
        if m:
            nums.append(int(m.group(1)))
    return nums


def validate() -> None:
    failures: list[str] = []
    records: dict[str, dict] = {}

    for locale, path in SOURCES.items():
        if not path.is_file():
            failures.append(f'{locale}: missing source {path}')
            continue
        text = path.read_text(encoding='utf-8-sig')
        u = urls(text)
        secs = section_numbers(text)
        if '\ufffd' in text:
            failures.append(f'{locale}: Unicode replacement character present')
        if secs != list(range(1, 18)):
            failures.append(f'{locale}: expected numbered sections 1..17 exactly once, got {secs}')
        if OBSOLETE_RED_SEAL in text:
            failures.append(f'{locale}: obsolete Red Seal URL remains')
        if '1.1' not in text:
            failures.append(f'{locale}: version 1.1 marker not found')
        records[locale] = {
            'path': path.as_posix(),
            'blob': blob(path),
            'urls': u,
            'url_count': len(u),
            'sections': secs,
        }

    if len(records) == 3:
        en = set(records['English']['urls'])
        for locale in ('es-419', 'pt-BR'):
            other = set(records[locale]['urls'])
            if other != en:
                failures.append(
                    f'{locale}: URL set differs from English; missing={sorted(en-other)}, extra={sorted(other-en)}'
                )

        red_seal = sorted(u for u in en if 'red-seal.ca/' in u)
        if not red_seal:
            failures.append('English: no Red Seal URL found after correction')
        elif any('/contact/c.4nt.1ct.shtml' in u for u in red_seal):
            failures.append(f'English: obsolete Red Seal URL remains in set {red_seal}')

    if failures:
        print('Guide 00 technical QA FAIL:')
        for item in failures:
            print(f'- {item}')
        raise SystemExit(1)

    common_urls = records['English']['urls']
    red_seal = [u for u in common_urls if 'red-seal.ca/' in u]
    lines = [
        '# Guide 00 — Trilingual Technical QA 08',
        '',
        '**Guide:** 00 — Lifelong Opportunity Foundation Guide',
        '**Branch:** `revision/guide-00-100-2026`',
        '**QA date:** 2026-08-22',
        '**Status:** PASS',
        '',
        '## Sources validated',
        '',
    ]
    for locale in ('English', 'es-419', 'pt-BR'):
        r = records[locale]
        lines += [
            f"- **{locale}:** `{r['path']}`",
            f"  - Git blob: `{r['blob']}`",
            f"  - Numbered sections: **17 / 17**",
            f"  - Unique HTTP/HTTPS links: **{r['url_count']}**",
        ]

    lines += [
        '',
        '## Technical controls',
        '',
        '- Numbered sections 1 through 17 present exactly once and in order in all three masters: **PASS**',
        '- English / `es-419` / `pt-BR` URL sets are identical: **PASS**',
        '- Obsolete Red Seal contact URL occurrences: **0**',
        f"- Controlled Red Seal URL(s) present after correction: **{', '.join(red_seal)}**",
        '- Unicode replacement-character scan: **PASS — none found**',
        '- Version 1.1 marker present in all three sources: **PASS**',
        '- Existing structural/terminology parity record retained: `project/revision-2026/guide-00/TRILINGUAL_PARITY_QA_01.md`',
        '- Existing correction control retained: `project/revision-2026/guide-00/TRILINGUAL_RED_SEAL_URL_CORRECTION_01.md`',
        '',
        '## Link inventory result',
        '',
        f'- Shared trilingual URL set: **{len(common_urls)} unique links**',
        '- The final source-parity scan proves that translated masters did not alter or omit source URLs relative to the frozen English master.',
        '- This gate validates source parity and the controlled Red Seal correction. It does not substitute for final DOCX/PDF hyperlink, render, metadata, checksum, or all-page visual review.',
        '',
        '## Gate decision',
        '',
        '**Trilingual Technical QA: PASS.**',
        '',
        'Guide 00 may proceed to Publication requalification. Publication and Release Audit remain PENDING until the final document package is independently rechecked against the frozen sources and rendered pages.',
    ]
    QA.parent.mkdir(parents=True, exist_ok=True)
    QA.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'PASS: Guide 00 technical QA; {len(common_urls)} shared URLs; report={QA}')


def close_status() -> None:
    if not QA.is_file():
        raise SystemExit('Technical QA report missing; refusing status closure')
    text = QA.read_text(encoding='utf-8')
    if '**Trilingual Technical QA: PASS.**' not in text:
        raise SystemExit('Technical QA report does not contain PASS decision')
    data = json.loads(HELPER.read_text(encoding='utf-8-sig'))
    stage = data['stages']['technical_qa']
    stage['status'] = 'PASS'
    ev = stage.setdefault('evidence', [])
    report = QA.as_posix()
    if report not in ev:
        ev.append(report)
    data['updated'] = '2026-08-22'
    data['notes'] = (
        'Legacy closure reconciliation. Trilingual Technical QA PASS. '
        'First active gate: Publication. Historical publication manifest remains automated-QA-only until requalified.'
    )
    HELPER.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print('PASS: Guide 00 helper advanced to Publication as first pending gate')


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'validate'
    if mode == 'validate':
        validate()
    elif mode == 'close-status':
        close_status()
    else:
        raise SystemExit(f'Unknown mode: {mode}')
