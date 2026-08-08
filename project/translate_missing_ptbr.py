"""Create the six missing Brazilian Portuguese guide editions.

The script preserves the source DOCX package and formatting, translates visible
paragraph text through Google Translate's public web endpoint, and writes
edition-level README/QC records. It is intentionally limited to the six audited
missing guides.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import tempfile
import time
import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree

from document_safety import parse_xml_part, resolve_repository_path, validate_docx


ROOT = Path(__file__).resolve().parents[1]
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
TEXT_PARTS = re.compile(
    r"^word/(document|header\d+|footer\d+|footnotes|endnotes|comments)\.xml$"
)
NOTICE = (
    "Tradução assistida por máquina. Antes de tomar decisões importantes com "
    "base neste guia, solicite a revisão de uma pessoa fluente em português do "
    "Brasil e com conhecimento técnico relevante."
)

GUIDES = {
    "07-customer-service-specialist": (
        "english/docx/Lifelong_Opportunity_Customer_Service_Specialist_Guide_English_v1.0.docx",
        "Guia_07_Especialista_em_Atendimento_ao_Cliente_PTBR",
        "Especialista em Atendimento ao Cliente",
    ),
    "08-human-resources-assistant": (
        "english/docx/Lifelong_Opportunity_Human_Resources_Assistant_Guide_English_v1.0.docx",
        "Guia_08_Assistente_de_Recursos_Humanos_PTBR",
        "Assistente de Recursos Humanos",
    ),
    "09-logistics-and-supply-chain-coordinator": (
        "english/docx/Lifelong_Opportunity_Logistics_and_Supply_Chain_Coordinator_Guide_English_v1.0.docx",
        "Guia_09_Coordenador_de_Logistica_e_Cadeia_de_Suprimentos_PTBR",
        "Coordenador de Logística e Cadeia de Suprimentos",
    ),
    "19-paralegal-and-legal-assistant": (
        "english/docx/Lifelong_Opportunity_Paralegal_and_Legal_Assistant_Guide_English_v1.0.docx",
        "Guia_19_Paralegal_e_Assistente_Juridico_PTBR",
        "Paralegal e Assistente Jurídico",
    ),
    "34-quality-control-inspector-and-manufacturing-technician": (
        "english/docx/Lifelong_Opportunity_Quality_Control_Inspector_and_Manufacturing_Technician_Guide_English_v1.0.docx",
        "Guia_34_Inspetor_de_Controle_de_Qualidade_e_Tecnico_de_Manufatura_PTBR",
        "Inspetor de Controle de Qualidade e Técnico de Manufatura",
    ),
    "56-nursing-assistant-and-patient-care-technician": (
        "english/docx/Nursing Assistant and Patient Care Technician.docx",
        "Guia_56_Auxiliar_de_Enfermagem_e_Tecnico_de_Atendimento_ao_Paciente_PTBR",
        "Auxiliar de Enfermagem e Técnico de Atendimento ao Paciente",
    ),
}


def should_translate(text: str) -> bool:
    text = text.strip()
    if not text or not re.search(r"[A-Za-z]", text):
        return False
    if re.fullmatch(r"https?://\S+|[\w.+-]+@[\w.-]+\.\w+", text):
        return False
    return True


def collect_paragraphs(docx: Path):
    docx = resolve_repository_path(docx, ROOT, allowed_extensions={".docx"})
    validate_docx(docx)
    parts: dict[str, bytes] = {}
    records: list[tuple[str, int, str]] = []
    with ZipFile(docx) as archive:
        for name in archive.namelist():
            if not TEXT_PARTS.match(name):
                continue
            data = archive.read(name)
            parts[name] = data
            root = parse_xml_part(data, name)
            for index, paragraph in enumerate(root.xpath(".//w:p", namespaces=NS)):
                nodes = paragraph.xpath(".//w:t", namespaces=NS)
                text = "".join(node.text or "" for node in nodes).strip()
                if nodes and should_translate(text):
                    records.append((name, index, text))
    return parts, records


def write_translated_docx(source: Path, destination: Path, translations: dict[str, str]):
    source = resolve_repository_path(source, ROOT, allowed_extensions={".docx"})
    destination = resolve_repository_path(
        destination, ROOT, allowed_extensions={".docx"}, must_exist=False
    )
    part_bytes, records = collect_paragraphs(source)
    grouped: dict[str, dict[int, str]] = {}
    for part, index, text in records:
        grouped.setdefault(part, {})[index] = translations[text]

    updated: dict[str, bytes] = {}
    for part, data in part_bytes.items():
        root = parse_xml_part(data, part)
        for index, paragraph in enumerate(root.xpath(".//w:p", namespaces=NS)):
            replacement = grouped.get(part, {}).get(index)
            if replacement is None:
                continue
            nodes = paragraph.xpath(".//w:t", namespaces=NS)
            nodes[0].text = replacement
            nodes[0].set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
            for node in nodes[1:]:
                node.text = ""
        updated[part] = etree.tostring(
            root, xml_declaration=True, encoding="UTF-8", standalone=True
        )

    destination.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{destination.stem}-", suffix=".tmp.docx", dir=destination.parent
    )
    os.close(descriptor)
    temporary = Path(temporary_name)
    try:
        with ZipFile(source) as original, ZipFile(
            temporary, "w", ZIP_DEFLATED
        ) as output:
            for item in original.infolist():
                output.writestr(item, updated.get(item.filename, original.read(item.filename)))
        validate_docx(temporary)
        os.replace(temporary, destination)
    finally:
        temporary.unlink(missing_ok=True)


def write_support_files(folder: Path, stem: str, title: str):
    pt = folder / "portuguese"
    readme = (
        f"# Guia {folder.name[:2]} — {title}\n\n"
        f"- [Documento editável do Microsoft Word](./docx/{stem}.docx)\n"
        f"- [PDF pesquisável](./pdf/{stem}.pdf)\n\n"
        f"> **Aviso de tradução:** {NOTICE}\n\n"
        "Consulte o README principal do guia para informações sobre escopo, "
        "fontes, acessibilidade e limitações.\n"
    )
    qc = (
        f"# Registro de controle de qualidade — Guia {folder.name[:2]}\n\n"
        "- Idioma: português do Brasil\n"
        "- Origem: edição inglesa presente no mesmo diretório do guia\n"
        "- Método: tradução assistida por máquina com preservação da estrutura DOCX\n"
        "- Formatos: DOCX editável e PDF pesquisável\n"
        "- Estado: revisão linguística e técnica humana recomendada\n"
        "- Verificações exigidas: abertura do DOCX, renderização integral, "
        "pesquisa de texto no PDF e conferência dos links relativos\n\n"
        f"**Aviso:** {NOTICE}\n"
    )
    (pt / "README.md").write_text(readme, encoding="utf-8")
    (pt / "QC.md").write_text(qc, encoding="utf-8")


def collect_source_texts():
    collected: dict[str, str] = {}
    guide_records = []
    for folder_name, (source_rel, stem, title) in GUIDES.items():
        source = ROOT / folder_name / source_rel
        _, records = collect_paragraphs(source)
        guide_records.append((folder_name, source, stem, title, records))
        for _, _, text in records:
            collected.setdefault(text, "")
    return collected, guide_records


def extract():
    collected, _ = collect_source_texts()
    source_json = ROOT / "project" / "ptbr-source-paragraphs.json"
    source_json.write_text(
        json.dumps(list(collected), ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Extracted {len(collected)} unique paragraphs.")


def build():
    _, guide_records = collect_source_texts()
    cache = ROOT / "project" / "ptbr-translation-cache.json"
    collected = json.loads(cache.read_text(encoding="utf-8"))

    for folder_name, source, stem, title, _ in guide_records:
        folder = ROOT / folder_name
        destination = folder / "portuguese" / "docx" / f"{stem}.docx"
        print(f"Writing {destination.relative_to(ROOT)}")
        write_translated_docx(source, destination, collected)
        write_support_files(folder, stem, title)

    print("Document build complete.")


def memory_audit():
    rows = []
    for folder in sorted(ROOT.iterdir()):
        if not folder.is_dir() or not re.match(r"^\d{2,3}-", folder.name):
            continue
        english = list(folder.glob("english/docx/*.docx"))
        portuguese = list(folder.glob("portuguese/[dD][oO][cC][xX]/*.docx"))
        if not english or not portuguese:
            continue
        _, en_records = collect_paragraphs(english[0])
        _, pt_records = collect_paragraphs(portuguese[0])
        rows.append(
            {
                "guide": folder.name,
                "english": len(en_records),
                "portuguese": len(pt_records),
                "difference": len(pt_records) - len(en_records),
            }
        )
    output = ROOT / "project" / "ptbr-memory-audit.json"
    output.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    exact = sum(row["difference"] == 0 for row in rows)
    print(f"Audited {len(rows)} aligned guide pairs; {exact} have equal paragraph counts.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("extract", "build", "memory-audit"))
    args = parser.parse_args()
    if args.mode == "extract":
        extract()
    elif args.mode == "build":
        build()
    else:
        memory_audit()
