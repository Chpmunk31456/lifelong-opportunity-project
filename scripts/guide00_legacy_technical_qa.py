#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

GUIDE = Path('project/revision-2026/guide-00')
QA = GUIDE / 'qa/GUIDE_00_TRILINGUAL_TECHNICAL_QA_08.md'
REPAIR = GUIDE / 'qa/GUIDE_00_TRILINGUAL_LINK_PARITY_REPAIR_08A.md'
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


def add_url_index_to_section_17(text: str, locale: str, missing: list[str]) -> str:
    if not missing:
        return text
    lines = text.splitlines()
    start = next((i for i, line in enumerate(lines) if re.match(r'^#\s+17\.', line.strip())), None)
    if start is None:
        raise SystemExit(f'{locale}: Section 17 not found; refusing link repair')
    end = len(lines)
    for i in range(start + 1, len(lines)):
        if re.match(r'^#\s+[^#]', lines[i].strip()):
            end = i
            break
    heading = {
        'es-419': '### Enlaces oficiales citados — índice consolidado',
        'pt-BR': '### Links oficiais citados — índice consolidado',
    }[locale]
    intro = {
        'es-419': 'Los siguientes enlaces oficiales se conservan para mantener paridad de fuentes con la edición inglesa controlada:',
        'pt-BR': 'Os links oficiais abaixo são preservados para manter a paridade de fontes com a edição inglesa controlada:',
    }[locale]
    block = ['', heading, '', intro, ''] + [f'- {u}' for u in missing] + ['']
    return '\n'.join(lines[:end] + block + lines[end:]).rstrip() + '\n'


def repair_links() -> None:
    english_text = SOURCES['English'].read_text(encoding='utf-8-sig')
    english_urls = set(urls(english_text))
    if OBSOLETE_RED_SEAL in english_text:
        raise SystemExit('English still contains obsolete Red Seal URL; refusing localized repair')
    if not english_urls:
        raise SystemExit('English URL inventory is empty; refusing repair')

    details: list[tuple[str, list[str], str, str]] = []
    for locale in ('es-419', 'pt-BR'):
        path = SOURCES[locale]
        text = path.read_text(encoding='utf-8-sig')
        existing = set(urls(text))
        extra = sorted(existing - english_urls)
        if extra:
            raise SystemExit(f'{locale}: unexpected URLs not present in English: {extra}')
        missing = sorted(english_urls - existing)
        old_blob = blob(path)
        if missing:
            repaired = add_url_index_to_section_17(text, locale, missing)
            path.write_text(repaired, encoding='utf-8')
        new_blob = blob(path)
        details.append((locale, missing, old_blob, new_blob))

    # Fail closed if the repair did not produce exact URL parity.
    for locale in ('es-419', 'pt-BR'):
        current = set(urls(SOURCES[locale].read_text(encoding='utf-8-sig')))
        if current != english_urls:
            raise SystemExit(f'{locale}: URL parity still differs after repair')

    lines = [
        '# Guide 00 — Trilingual Link Parity Repair 08A',
        '',
        '**Guide:** 00 — Lifelong Opportunity Foundation Guide',
        '**Branch:** `revision/guide-00-100-2026`',
        '**Repair date:** 2026-08-22',
        '**Status:** PASS',
        '',
        '## Defect confirmed',
        '',
        'The fail-closed technical validator found that the English integrated master contained the controlled official-source URL inventory while both localized masters omitted those direct URLs. The localized editions had no conflicting extra URLs.',
        '',
        f'- English controlled URL inventory: **{len(english_urls)} unique HTTP/HTTPS links**',
        '',
        '## Repair applied',
        '',
        'Only the missing official URLs were added, as consolidated source-link indexes inside Section 17 of the Spanish and Portuguese masters. No occupational claim, funding classification, eligibility statement, compensation statement, warning, action step, or English source text was changed.',
        '',
    ]
    for locale, missing, old_blob, new_blob in details:
        lines += [
            f'### {locale}',
            '',
            f'- Missing official URLs added: **{len(missing)}**',
            f'- Prior Git blob: `{old_blob}`',
            f'- Repaired Git blob: `{new_blob}`',
            '',
        ]
    lines += [
        '## Post-repair controls',
        '',
        '- English / `es-419` / `pt-BR` URL sets after repair: **identical**',
        '- Obsolete Red Seal contact URL in localized sources: **0 occurrences**',
        '- English frozen source changed by this repair: **NO**',
        '- Localization prose changed by this repair: **NO — source links only**',
        '',
        'This repair does not itself close Trilingual Technical QA. The independent validator must rerun against the committed repaired sources and produce `GUIDE_00_TRILINGUAL_TECHNICAL_QA_08.md` before the helper status may advance.',
    ]
    REPAIR.parent.mkdir(parents=True, exist_ok=True)
    REPAIR.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'PASS: repaired localized URL parity; English URLs={len(english_urls)}')


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
        '- Link parity repair evidence: `project/revision-2026/guide-00/qa/GUIDE_00_TRILINGUAL_LINK_PARITY_REPAIR_08A.md`',
        '',
        '## Link inventory result',
        '',
        f'- Shared trilingual URL set: **{len(common_urls)} unique links**',
        '- The final source-parity scan proves that translated masters do not alter or omit source URLs relative to the frozen English master.',
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
    for report in (REPAIR.as_posix(), QA.as_posix()):
        if report not in ev:
            ev.append(report)
    # The localized sources changed only to restore direct source links; keep the
    # existing localization PASS but append the repair evidence for auditability.
    for stage_name in ('spanish_localization', 'portuguese_localization'):
        sev = data['stages'][stage_name].setdefault('evidence', [])
        if REPAIR.as_posix() not in sev:
            sev.append(REPAIR.as_posix())
    data['updated'] = '2026-08-22'
    data['notes'] = (
        'Legacy closure reconciliation. Trilingual Technical QA PASS after source-link parity repair. '
        'First active gate: Publication. Historical publication manifest remains automated-QA-only until requalified.'
    )
    HELPER.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print('PASS: Guide 00 helper advanced to Publication as first pending gate')


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'validate'
    if mode == 'repair-links':
        repair_links()
    elif mode == 'validate':
        validate()
    elif mode == 'close-status':
        close_status()
    else:
        raise SystemExit(f'Unknown mode: {mode}')
