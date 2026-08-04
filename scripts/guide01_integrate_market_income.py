#!/usr/bin/env python3
"""Integrate verified supplementary U.S. CHW market-income estimates.

Fail-closed: exact anchors and pending-QA statements must each occur once.
The script is idempotent and writes UTF-8/LF only after all three masters pass
preflight checks. It does not claim official status for non-government data.
"""
from pathlib import Path

ROOT = Path("project/revision-2026/guide-01/working-masters")

SPECS = {
    "GUIDE_01_COMMUNITY_HEALTH_WORKER_ENGLISH_WORKING_MASTER.md": {
        "anchor": "Pay varies by state, metropolitan area, employer, schedule, union coverage, duties, language skills, experience, and certification requirements. The median is not an entry wage.\n",
        "paragraph": "\n### United States supplementary market estimates\n\nCurrent non-government estimates provide additional context but are not official statistics and must not replace the BLS figures above. Glassdoor reported an estimated average annual pay of **USD 52,306** for Community Health Workers in the United States, based on **1,936 anonymous salary submissions**, as of June 2026. ZipRecruiter reported an estimated average annual pay of **USD 44,925** as of July 27, 2026, using employer job postings and third-party data.\n\nThese estimates use different methods, samples, and update cycles. Do not average them together, treat them as guaranteed offers, or assume that they apply to a particular state, employer, experience level, or employment arrangement.\n",
        "source_anchor": "- U.S. Bureau of Labor Statistics, Occupational Outlook Handbook, Community Health Workers, modified August 28, 2025: https://www.bls.gov/ooh/community-and-social-service/community-health-workers.htm\n",
        "sources": "- Glassdoor, Community Health Worker salary estimate for the United States, accessed August 2026; estimated average USD 52,306 based on 1,936 anonymous salary submissions: https://www.glassdoor.com/Salaries/community-health-worker-salary-SRCH_KO0,23.htm\n- ZipRecruiter, Community Health Worker salary estimate for the United States, dated July 27, 2026; estimated average USD 44,925 using employer postings and third-party data: https://www.ziprecruiter.com/Salaries/Community-Health-Worker-Salary\n",
        "old": "- add a defensible, clearly labeled current non-government market estimate only if one passes the evidence controls;",
        "new": "- revalidate the supplementary non-government market estimates immediately before publication and retain their methodology limitations;",
        "numbers": ("52,306", "44,925", "1,936"),
    },
    "GUIDE_01_TRABAJADOR_COMUNITARIO_DE_SALUD_ES419_WORKING_MASTER.md": {
        "anchor": "La remuneración varía según el estado, área metropolitana, empleador, horario, cobertura sindical, funciones, idiomas, experiencia y requisitos de certificación. La mediana no es un salario inicial.\n",
        "paragraph": "\n### Estimaciones complementarias del mercado de Estados Unidos\n\nLas estimaciones no gubernamentales actuales aportan contexto adicional, pero no son estadísticas oficiales ni deben reemplazar las cifras de la Oficina de Estadísticas Laborales indicadas anteriormente. Glassdoor informó una remuneración anual promedio estimada de **USD 52.306** para trabajadores comunitarios de salud en Estados Unidos, basada en **1.936 reportes salariales anónimos**, a junio de 2026. ZipRecruiter informó una remuneración anual promedio estimada de **USD 44.925** al 27 de julio de 2026, utilizando anuncios de empleo de empleadores y datos de terceros.\n\nEstas estimaciones usan métodos, muestras y ciclos de actualización distintos. No las promedie entre sí, no las interprete como ofertas garantizadas ni suponga que se aplican a un estado, empleador, nivel de experiencia o modalidad de empleo específicos.\n",
        "source_anchor": "- Oficina de Estadísticas Laborales de Estados Unidos, *Occupational Outlook Handbook*, trabajadores comunitarios de salud, modificado el 28 de agosto de 2025: https://www.bls.gov/ooh/community-and-social-service/community-health-workers.htm\n",
        "sources": "- Glassdoor, estimación salarial para trabajadores comunitarios de salud en Estados Unidos, consultada en agosto de 2026; promedio estimado de USD 52.306 basado en 1.936 reportes salariales anónimos: https://www.glassdoor.com/Salaries/community-health-worker-salary-SRCH_KO0,23.htm\n- ZipRecruiter, estimación salarial para trabajadores comunitarios de salud en Estados Unidos, fechada el 27 de julio de 2026; promedio estimado de USD 44.925 basado en anuncios de empleadores y datos de terceros: https://www.ziprecruiter.com/Salaries/Community-Health-Worker-Salary\n",
        "old": "- añadir una estimación actual del mercado no gubernamental, claramente identificada y defendible, solo si supera los controles de evidencia;",
        "new": "- revalidar las estimaciones complementarias no gubernamentales inmediatamente antes de la publicación y conservar sus limitaciones metodológicas;",
        "numbers": ("52.306", "44.925", "1.936"),
    },
    "GUIDE_01_AGENTE_COMUNITARIO_DE_SAUDE_PTBR_WORKING_MASTER.md": {
        "anchor": "A remuneração varia por estado, região metropolitana, empregador, jornada, cobertura sindical, funções, idiomas, experiência e requisitos de certificação. A mediana não é um salário inicial.\n",
        "paragraph": "\n### Estimativas complementares do mercado dos Estados Unidos\n\nAs estimativas não governamentais atuais oferecem contexto adicional, mas não são estatísticas oficiais e não devem substituir os dados do Bureau of Labor Statistics apresentados acima. A Glassdoor informou remuneração média anual estimada de **USD 52.306** para agentes comunitários de saúde nos Estados Unidos, com base em **1.936 relatos salariais anônimos**, em junho de 2026. A ZipRecruiter informou remuneração média anual estimada de **USD 44.925** em 27 de julho de 2026, utilizando anúncios de vagas de empregadores e dados de terceiros.\n\nEssas estimativas usam métodos, amostras e ciclos de atualização diferentes. Não faça uma média entre elas, não as trate como ofertas garantidas e não presuma que se apliquem a um estado, empregador, nível de experiência ou modalidade de trabalho específicos.\n",
        "source_anchor": "- Bureau of Labor Statistics dos Estados Unidos, *Occupational Outlook Handbook*, Community Health Workers, modificado em 28 de agosto de 2025: https://www.bls.gov/ooh/community-and-social-service/community-health-workers.htm\n",
        "sources": "- Glassdoor, estimativa salarial para agentes comunitários de saúde nos Estados Unidos, consultada em agosto de 2026; média estimada de USD 52.306 baseada em 1.936 relatos salariais anônimos: https://www.glassdoor.com/Salaries/community-health-worker-salary-SRCH_KO0,23.htm\n- ZipRecruiter, estimativa salarial para agentes comunitários de saúde nos Estados Unidos, datada de 27 de julho de 2026; média estimada de USD 44.925 com base em anúncios de empregadores e dados de terceiros: https://www.ziprecruiter.com/Salaries/Community-Health-Worker-Salary\n",
        "old": "- adicionar uma estimativa atual de mercado não governamental, claramente identificada e defensável, somente se ela passar pelos controles de evidência;",
        "new": "- revalidar as estimativas complementares não governamentais imediatamente antes da publicação e manter suas limitações metodológicas;",
        "numbers": ("52.306", "44.925", "1.936"),
    },
}


def main() -> None:
    prepared: dict[Path, str] = {}
    for filename, spec in SPECS.items():
        path = ROOT / filename
        text = path.read_text(encoding="utf-8")
        integrated = (
            all(number in text for number in spec["numbers"])
            and text.count("Glassdoor") >= 2
            and text.count("ZipRecruiter") >= 2
        )
        if not integrated:
            for key in ("anchor", "source_anchor", "old"):
                count = text.count(spec[key])
                if count != 1:
                    raise SystemExit(f"{filename}: expected one {key}; found {count}")
            text = text.replace(spec["anchor"], spec["anchor"] + spec["paragraph"], 1)
            text = text.replace(spec["source_anchor"], spec["source_anchor"] + spec["sources"], 1)
            text = text.replace(spec["old"], spec["new"], 1)
        for number in spec["numbers"]:
            if number not in text:
                raise SystemExit(f"{filename}: missing {number}")
        if text.count("Glassdoor") < 2 or text.count("ZipRecruiter") < 2:
            raise SystemExit(f"{filename}: paragraph/source parity failed")
        if "guarante" not in text.lower() and "garant" not in text.lower():
            raise SystemExit(f"{filename}: non-guarantee language missing")
        prepared[path] = text

    for path, text in prepared.items():
        path.write_text(text, encoding="utf-8", newline="\n")
        print(path)


if __name__ == "__main__":
    main()
