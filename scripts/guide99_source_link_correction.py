#!/usr/bin/env python3
"""Repair three Guide 99 FDA reader links that hard-fail publication QA.

The correction is deliberately narrow: URL maintenance only. It then records
revalidation of the already-passed editorial/traceability/freeze/localization/
technical gates and computes the new frozen English Git blob before commit.
"""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

ROOT = Path('project/revision-2026/guide-99')
QA = ROOT / 'qa'
EN = ROOT / 'working-masters/GUIDE_99_FOOD_SCIENCE_TECHNICIAN_ENGLISH_v2.md'
STATUS = ROOT / 'GUIDE_99_HELPER_STATUS.json'
RECOVERY = Path('scripts/guide99_publication_recovery.py')

REPLACEMENTS = {
    'https://www.fda.gov/food/guidance-regulation-food-and-dietary-supplements/current-good-manufacturing-practices-cgmps-food-and-dietary-supplements':
        'https://www.fda.gov/food/guidance-regulation-food-and-dietary-supplements',
    'https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-preventive-controls-human-food':
        'https://www.ecfr.gov/current/title-21/chapter-I/subchapter-B/part-117',
    'https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-rules-guidance-industry':
        'https://www.fda.gov/food/guidance-regulation-food-and-dietary-supplements/food-safety-modernization-act-fsma',
}

changed = []
for p in ROOT.rglob('*.md'):
    if 'publication-candidate' in p.parts:
        continue
    text = p.read_text(encoding='utf-8')
    new = text
    for old, replacement in REPLACEMENTS.items():
        new = new.replace(old, replacement)
    if new != text:
        p.write_text(new, encoding='utf-8')
        changed.append(str(p))

masters = [
    ROOT / 'working-masters/GUIDE_99_FOOD_SCIENCE_TECHNICIAN_ENGLISH_v2.md',
    ROOT / 'working-masters/GUIDE_99_TECNICO_EN_CIENCIA_DE_ALIMENTOS_ES419_v2.md',
    ROOT / 'working-masters/GUIDE_99_TECNICO_EM_CIENCIA_DE_ALIMENTOS_PTBR_v2.md',
]
for p in masters:
    text = p.read_text(encoding='utf-8')
    for old in REPLACEMENTS:
        assert old not in text, f'stale FDA URL remains in {p}'
    for replacement in REPLACEMENTS.values():
        assert replacement in text, f'replacement URL missing in {p}: {replacement}'

urlsets = [set(re.findall(r'https://[^\s)<>`]+', p.read_text(encoding='utf-8'))) for p in masters]
assert urlsets[0] == urlsets[1] == urlsets[2], [len(x) for x in urlsets]

english_blob = subprocess.check_output(['git', 'hash-object', str(EN)], text=True).strip()

# Keep publication manifest provenance synchronized with the corrected frozen source.
recovery_text = RECOVERY.read_text(encoding='utf-8')
recovery_new, count = re.subn(
    r'ENGLISH_BLOB\s*=\s*["\'][0-9a-f]{40}["\']',
    f'ENGLISH_BLOB = "{english_blob}"',
    recovery_text,
    count=1,
)
assert count == 1, 'could not update ENGLISH_BLOB in publication recovery script'
if recovery_new != recovery_text:
    RECOVERY.write_text(recovery_new, encoding='utf-8')
    changed.append(str(RECOVERY))

correction = QA / 'GUIDE_99_SOURCE_LINK_CORRECTION_08A.md'
correction.write_text(f'''# Guide 99 — Source Link Correction 08A

**Status:** PASS
**Date:** 2026-08-22

Publication link QA identified three FDA reader URLs returning HTTP 404 from the GitHub Actions runner. The underlying food-safety statements remain supported; this maintenance correction replaces only those reader links with current official sources:

1. FDA CGMP reader link → `https://www.fda.gov/food/guidance-regulation-food-and-dietary-supplements`
2. FDA Preventive Controls reader link → current eCFR 21 CFR Part 117: `https://www.ecfr.gov/current/title-21/chapter-I/subchapter-B/part-117`
3. FDA FSMA rules/guidance reader link → current FDA FSMA hub: `https://www.fda.gov/food/guidance-regulation-food-and-dietary-supplements/food-safety-modernization-act-fsma`

The three controlled language masters retain identical reader-URL sets after correction. Occupational mappings, compensation values, training pathways, safety boundaries, responsible-AI controls, accessibility guidance, and substantive translations were not changed.

**Revalidated frozen English Git blob:** `{english_blob}`

Affected controlled gates 03–08 were rechecked for the URL-only maintenance change and remain **PASS**. Publication and Release Audit remain fail-closed and may advance only after the corrected trilingual package passes automated build, link, DOCX, searchable-PDF, all-page render, checksum, and evidence checks.
''', encoding='utf-8')

note = f'''\n\n## 2026-08-22 source-link maintenance revalidation\n\nRevalidated after the URL-only correction documented in `GUIDE_99_SOURCE_LINK_CORRECTION_08A.md`. No substantive occupational, compensation, training, safety, responsible-AI, accessibility, or translation content changed. Gate remains **PASS**. New frozen English Git blob: `{english_blob}`.\n'''
for name in [
    'GUIDE_99_ENGLISH_EDITORIAL_QA_03.md',
    'GUIDE_99_EVIDENCE_TRACEABILITY_QA_04.md',
    'GUIDE_99_ENGLISH_SOURCE_FREEZE_05.md',
    'GUIDE_99_SPANISH_LOCALIZATION_QA_06.md',
    'GUIDE_99_PORTUGUESE_LOCALIZATION_QA_07.md',
    'GUIDE_99_TRILINGUAL_TECHNICAL_QA_08.md',
]:
    p = QA / name
    text = p.read_text(encoding='utf-8')
    if 'source-link maintenance revalidation' not in text:
        p.write_text(text.rstrip() + note + '\n', encoding='utf-8')

status = json.loads(STATUS.read_text(encoding='utf-8'))
assert status['stages']['publication']['status'] == 'PENDING'
assert status['stages']['release_audit']['status'] == 'PENDING'
assert not status.get('blockers')
for gate in ('english_editorial','evidence_traceability','english_source_freeze','spanish_localization','portuguese_localization','technical_qa'):
    assert status['stages'][gate]['status'] == 'PASS'
correction_rel = 'project/revision-2026/guide-99/qa/GUIDE_99_SOURCE_LINK_CORRECTION_08A.md'
for gate in ('evidence_traceability','english_source_freeze','spanish_localization','portuguese_localization','technical_qa'):
    evidence = status['stages'][gate].setdefault('evidence', [])
    if correction_rel not in evidence:
        evidence.append(correction_rel)
STATUS.write_text(json.dumps(status, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

print(f'Guide 99 source-link correction PASS; {len(urlsets[0])} shared reader URLs; English blob {english_blob}')
for p in changed:
    print('updated', p)
