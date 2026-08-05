#!/usr/bin/env python3
"""Reconcile Guide 01 trilingual working-master status blocks.

This script performs exact, fail-closed replacements so repository status text
matches completed Guide 01 controls without prematurely declaring publication
approval.
"""
from pathlib import Path

ROOT = Path("project/revision-2026/guide-01/working-masters")

replacements = {
    ROOT / "GUIDE_01_COMMUNITY_HEALTH_WORKER_ENGLISH_WORKING_MASTER.md": [
        (
            "**Review date:** August 3, 2026  ",
            "**Review date:** August 5, 2026  ",
        ),
        (
            "**Status:** Substantive English working master completed from the controlled official-source baseline. Legacy-file comparison, final link validation, translation, DOCX/PDF generation, and publication QA remain pending.",
            "**Status:** Substantive English working master completed from the controlled official-source baseline. Legacy comparison, trilingual integration, structural-parity review, terminology normalization, market-income reconciliation, and controlled link review are recorded. Final editorial and translation freeze, final live-link validation, DOCX/PDF generation, metadata, checksums, and publication QA remain pending.",
        ),
        (
            "- create aligned neutral Latin American Spanish and Brazilian Portuguese masters;\n- run terminology and structural-parity QA;",
            "- complete final sentence-level review of the aligned neutral Latin American Spanish and Brazilian Portuguese masters;\n- reconcile any intentional localization exceptions and freeze terminology and structural parity;",
        ),
    ],
    ROOT / "GUIDE_01_TRABAJADOR_COMUNITARIO_DE_SALUD_ES419_WORKING_MASTER.md": [
        (
            "**Fecha de revisión:** 4 de agosto de 2026  ",
            "**Fecha de revisión:** 5 de agosto de 2026  ",
        ),
        (
            "**Estado:** Maestro sustantivo en español es-419 completado a partir del maestro controlado en inglés y del registro terminológico trilingüe. Aún están pendientes la comparación con el archivo heredado, la validación final de enlaces, la revisión de paridad, la generación de DOCX/PDF y el control de calidad de publicación.",
            "**Estado:** Maestro sustantivo en español es-419 completado a partir del maestro controlado en inglés y del registro terminológico trilingüe. La integración trilingüe, la revisión de paridad estructural, la normalización terminológica, la conciliación de estimaciones de ingresos y la revisión controlada de enlaces están registradas. Aún están pendientes la congelación editorial y de traducción, la validación final de enlaces en vivo, la generación de DOCX/PDF, los metadatos, las sumas de comprobación y el control de calidad de publicación.",
        ),
    ],
    ROOT / "GUIDE_01_AGENTE_COMUNITARIO_DE_SAUDE_PTBR_WORKING_MASTER.md": [
        (
            "**Data de revisão:** 4 de agosto de 2026  ",
            "**Data de revisão:** 5 de agosto de 2026  ",
        ),
        (
            "**Status:** Mestre substantivo em pt-BR concluído a partir do mestre controlado em inglês e do registro terminológico trilíngue. Ainda estão pendentes a comparação com o arquivo legado, a validação final de links, a revisão de paridade, a geração de DOCX/PDF e o controle de qualidade de publicação.",
            "**Status:** Mestre substantivo em pt-BR concluído a partir do mestre controlado em inglês e do registro terminológico trilíngue. A integração trilíngue, a revisão de paridade estrutural, a normalização terminológica, a reconciliação das estimativas de renda e a revisão controlada de links estão registradas. Ainda estão pendentes o congelamento editorial e da tradução, a validação final de links ativos, a geração de DOCX/PDF, os metadados, as somas de verificação e o controle de qualidade de publicação.",
        ),
    ],
}

for path, pairs in replacements.items():
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        raise SystemExit(f"Unexpected UTF-8 BOM: {path}")
    text = raw.decode("utf-8")
    for old, new in pairs:
        count = text.count(old)
        if count == 0 and text.count(new) == 1:
            continue
        if count != 1:
            raise SystemExit(f"Expected exactly one controlled match in {path}: {old[:80]!r}; found {count}")
        text = text.replace(old, new, 1)
    if "\ufffd" in text:
        raise SystemExit(f"Replacement-character encoding defect: {path}")
    path.write_text(text, encoding="utf-8", newline="\n")
    print(f"Reconciled {path}")
