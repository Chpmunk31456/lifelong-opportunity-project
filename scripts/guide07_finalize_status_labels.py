#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "project/revision-2026/guide-07/source"

REPLACEMENTS = {
    BASE / "GUIDE_07_ENGLISH_WORKING_MASTER_v2.md": [
        (
            "**Controlled 2026 English working master**  \nVersion 2.0, working master • August 2026",
            "**Controlled 2026 English publication candidate**\nVersion 2.0 • August 2026",
        ),
        (
            "> **Controlled status:** This is the revised English working master for the 2026 review. It is not yet a publication candidate. It must pass editorial, claim-traceability, link, accessibility, encoding, translation, DOCX, PDF, metadata, and publication QA before release.",
            "> **Controlled status:** This is the revised English source for the 2026 controlled publication candidate. It has passed the project’s editorial, claim-traceability, link, encoding, localization, DOCX, PDF, metadata, rendering, and publication QA gates documented in the repository. This does not constitute independent human certification, professional translation certification, accessibility certification, accreditation, legal review, or a guarantee of outcomes.",
        ),
        (
            "- English source status: working master, not yet frozen\n- Publication status: not yet a publication candidate",
            "- English source status: frozen for the controlled 2026 publication candidate\n- Publication status: controlled publication candidate; release remains governed by repository QA records",
        ),
    ],
    BASE / "GUIDE_07_SPANISH_LATAM_WORKING_MASTER_v2.md": [
        (
            "**Maestro de trabajo controlado 2026 en español latinoamericano (es-419)**  \nVersión 2.0, maestro de trabajo • agosto de 2026",
            "**Candidata de publicación controlada 2026 en español latinoamericano (es-419)**\nVersión 2.0 • agosto de 2026",
        ),
        (
            "> **Estado controlado:** Esta es la versión revisada en español latinoamericano del maestro de trabajo en inglés de 2026. Todavía no es una candidata de publicación. Debe aprobar controles de paridad de traducción, terminología, enlaces, accesibilidad, codificación, DOCX, PDF, metadatos y publicación antes de su lanzamiento.",
            "> **Estado controlado:** Esta es la versión revisada en español latinoamericano de la fuente inglesa congelada para la candidata de publicación controlada de 2026. Ha aprobado los controles del proyecto de paridad, terminología, enlaces, codificación, DOCX, PDF, metadatos, renderizado y publicación documentados en el repositorio. Esto no constituye certificación humana independiente, certificación profesional de traducción, certificación de accesibilidad, acreditación, revisión legal ni garantía de resultados.",
        ),
        (
            "- Estado de esta traducción: maestro de trabajo es-419, traducción asistida por máquina y revisada editorialmente; no certificada profesionalmente\n- Estado de publicación: todavía no es candidata de publicación",
            "- Estado de esta traducción: fuente es-419 controlada, traducción asistida por IA y revisada editorialmente dentro del proceso del proyecto; no certificada profesionalmente\n- Estado de publicación: candidata de publicación controlada; el lanzamiento sigue sujeto a los registros de QA del repositorio",
        ),
    ],
    BASE / "GUIDE_07_PORTUGUESE_BR_WORKING_MASTER_v2.md": [
        (
            "**Mestre de trabalho controlado 2026 em português do Brasil (pt-BR)**  \nVersão 2.0, mestre de trabalho • agosto de 2026",
            "**Candidata de publicação controlada 2026 em português do Brasil (pt-BR)**\nVersão 2.0 • agosto de 2026",
        ),
        (
            "> **Status controlado:** Esta é a versão revisada em português do Brasil do mestre de trabalho em inglês de 2026. Ainda não é candidata à publicação. Deve passar por controles de paridade de tradução, terminologia, links, acessibilidade, codificação, DOCX, PDF, metadados e publicação antes do lançamento.",
            "> **Status controlado:** Esta é a versão revisada em português do Brasil da fonte inglesa congelada para a candidata de publicação controlada de 2026. Ela passou pelos controles do projeto de paridade, terminologia, links, codificação, DOCX, PDF, metadados, renderização e publicação documentados no repositório. Isso não constitui certificação humana independente, certificação profissional de tradução, certificação de acessibilidade, acreditação, revisão jurídica nem garantia de resultados.",
        ),
        (
            "- Status desta tradução: mestre de trabalho pt-BR, tradução assistida por máquina e revisada editorialmente; não certificada profissionalmente\n- Status de publicação: ainda não é candidata à publicação",
            "- Status desta tradução: fonte pt-BR controlada, tradução assistida por IA e revisada editorialmente no processo do projeto; não certificada profissionalmente\n- Status de publicação: candidata de publicação controlada; o lançamento continua sujeito aos registros de QA do repositório",
        ),
    ],
}

for path, replacements in REPLACEMENTS.items():
    text = path.read_text(encoding="utf-8")
    for old, new in replacements:
        if old not in text:
            raise SystemExit(f"Expected status text not found in {path}: {old[:80]!r}")
        text = text.replace(old, new, 1)
    path.write_text(text, encoding="utf-8")
    print(f"updated {path.relative_to(ROOT)}")
