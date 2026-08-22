# Guia de Oportunidades para Toda a Vida 87 — Analista e Testador de Qualidade de Software

**Versão:** 2.0 — mestre de trabalho controlado  
**Idioma:** Português do Brasil (`pt-BR`)  
**Referência principal dos EUA:** O*NET-SOC 15-1253.00 — Software Quality Assurance Analysts and Testers  
**Comparações do Canadá:** NOC 21222 — Information systems specialists; NOC 22222 — Information systems testing technicians  
**Comparação da Colômbia:** CUOC 25190 — Desarrolladores y analistas de software y multimedia no clasificados en otras ocupaciones  
**Data de revisão:** 2026-08-22  
**Fonte inglesa congelada:** blob `446a05a75eaed4739a007d9327faba8234210d19`

## O que é esta carreira

Analistas e testadores de garantia da qualidade de software ajudam as equipes a determinar se um sistema se comporta como esperado, atende a requisitos definidos, lida com erros com segurança e pode ser liberado com um nível de risco compreendido. O trabalho pode incluir revisar requisitos, projetar casos de teste, preparar dados, executar verificações manuais ou automatizadas, documentar defeitos, retestar correções, apoiar regressão e avaliar usabilidade e acessibilidade.

QA não é simplesmente “caçar bugs”. É trabalho de evidência. Um bom testador sabe o que está sendo verificado, qual ambiente e build foram usados, quais precondições e dados se aplicam, qual resultado era esperado, o que realmente aconteceu e como outra pessoa pode reproduzir a observação.

Nos Estados Unidos existe correspondência direta em **O*NET-SOC 15-1253.00**. O Canadá separa melhor os escopos: trabalho de QA em nível de analista é comparado com **NOC 21222**, enquanto execução técnica de testes é comparada com **NOC 22222**. Na Colômbia, **CUOC 25190** oferece uma forte correspondência para QA/testes.

## Por que esta carreira continua importante

Software afeta bancos, saúde, governo, transporte, educação, comércio, comunicações, manufatura e serviços digitais. Defeitos podem causar cálculos incorretos, indisponibilidade, transações falhas, perda de dados, exposição de privacidade, fragilidades de segurança, interfaces inacessíveis, retrabalho e perda de confiança.

Automação e IA podem ampliar a capacidade de testes, mas não eliminam a necessidade de pessoas que definam verificações confiáveis, interpretem falhas, identifiquem evidências fracas, investiguem casos extremos e comuniquem risco.

## Títulos de trabalho relacionados

Dependendo da função e senioridade, procure por:

- Software QA Analyst;
- Software Quality Assurance Analyst;
- QA Tester;
- Software Tester;
- Manual Tester;
- QA Engineer;
- Test Engineer;
- Automation Tester;
- Test Automation Engineer;
- Quality Engineer;
- SDET;
- API Tester;
- Accessibility Tester;
- Performance Tester;
- UAT Analyst.

Leia as responsabilidades reais, profundidade de programação, escopo de testes e autoridade de liberação.

## Base de teste e rastreabilidade

Todo teste importante deve partir de uma base definida, por exemplo:

- requisito aprovado;
- critério de aceitação;
- história de usuário;
- contrato de interface ou API;
- projeto ou especificação;
- correção de defeito;
- risco;
- fluxo de usuário documentado;
- requisito regulatório ou de política quando aplicável.

A rastreabilidade pode conectar:

**requisito ou risco → caso de teste → execução → evidência → defeito ou resultado → reteste / decisão de liberação.**

QA não deve inventar silenciosamente requisitos para fazer um teste passar ou falhar.

## Projeto de casos de teste

Um caso de teste defensável pode incluir:

- objetivo;
- requisito ou risco;
- precondições;
- ambiente;
- build/versão;
- dados de teste;
- passos;
- resultado esperado;
- resultado real;
- status aprovado/reprovado/bloqueado;
- evidência;
- limpeza ou reset;
- defeito ou requisito relacionado.

Quando o requisito é ambíguo ou contraditório, a ambiguidade deve ser escalada em vez de escolher o resultado esperado depois de observar o produto.

## Relatórios de defeitos reproduzíveis

Um relatório útil deve permitir que outra pessoa reproduza e investigue o problema. Inclua, quando relevante:

- título conciso;
- ambiente, navegador, dispositivo ou plataforma;
- build/versão;
- precondições;
- passos reproduzíveis;
- resultado esperado;
- resultado real;
- frequência;
- capturas, logs ou vídeo seguros;
- severidade/impacto;
- requisito ou teste relacionado;
- identificador de dados sem expor informação protegida.

Descreva o que foi observado. Não culpe desenvolvedores nem afirme causa raiz não comprovada.

## Severidade versus prioridade

- **Severidade**: impacto do defeito no usuário, sistema, dados, segurança ou negócio.
- **Prioridade**: urgência ou ordem em que a organização decide tratá-lo.

As escalas variam entre equipes. Use as definições e processos de escalonamento do empregador.

## Níveis e tipos de teste

Podem incluir:

- unitário;
- integração;
- sistema;
- end-to-end;
- aceitação;
- funcional;
- regressão;
- negativo/erro;
- valores-limite;
- compatibilidade;
- API;
- validação de dados;
- usabilidade;
- acessibilidade;
- desempenho/carga/estresse;
- recuperação/resiliência;
- segurança somente com autorização explícita.

Uma pessoa não necessariamente executa todos esses tipos. QA também não possui automaticamente a autoridade final de liberação.

## Testes exploratórios e roteirizados

Testes roteirizados ajudam repetibilidade e rastreabilidade. Testes exploratórios usam julgamento para investigar comportamento e combinações inesperadas. Eles se complementam.

Exploração ainda deve respeitar escopo, ambiente, dados, autorização e documentação mínima do que foi feito.

## Dados de teste

Prefira:

- dados sintéticos;
- dados mascarados aprovados;
- contas de teste específicas;
- conjuntos controlados com resultados conhecidos.

Não copie casualmente dados de produção para ambientes de teste. Proteja credenciais, tokens e chaves. Não anexe dados protegidos em tickets sem necessidade e autorização. Higienize logs, capturas e vídeos quando necessário.

## Ambientes e configuração

Registre informações importantes como:

- versão/build;
- sistema operacional;
- navegador/dispositivo;
- versão de API ou serviço;
- feature flags;
- estado do banco de dados;
- função/perfil da conta;
- dependências;
- configuração específica do ambiente.

Não declare uma correção final antes do reteste na versão e ambiente relevantes.

## Regressão

A regressão verifica se uma mudança prejudicou comportamento que funcionava antes. Priorize considerando:

- componentes alterados;
- dependências;
- fluxos críticos;
- histórico de defeitos;
- impacto de negócio;
- privacidade/segurança;
- integrações;
- tempo disponível;
- confiabilidade da automação.

Uma suíte enorme e pouco confiável não é automaticamente melhor que uma suíte menor e baseada em risco.

## Automação de testes

Sinais atuais de vagas O*NET incluem **Python, Selenium, Atlassian JIRA, SQL, Java, Jenkins CI, JavaScript, Postman, AWS, Git, Linux, Microsoft Azure, Apache JMeter, C#, GitHub, C++, Microsoft Playwright, Azure DevOps Services, TestNG, RESTful API, Appium e REST Assured**.

Automação exige:

- código sustentável;
- seletores ou interfaces estáveis;
- asserções significativas;
- controle de versão;
- revisão quando exigida;
- dados controlados;
- diagnóstico de falhas;
- tratamento de testes flaky;
- manutenção quando o produto muda.

Uma suíte automatizada aprovada não prova que o produto esteja livre de defeitos.

## Testes flaky

Um teste flaky produz resultados inconsistentes sem alteração relevante do produto. Causas comuns:

- suposições rígidas de tempo;
- estado compartilhado;
- dados instáveis;
- dependências não confiáveis;
- race conditions;
- seletores frágeis;
- capacidade do ambiente;
- instabilidade de rede.

Não normalize flakiness sem explicação. Registre, investigue e repare, coloque em quarentena ou substitua conforme política.

## Testes de API

Podem verificar:

- códigos de status;
- esquemas;
- campos obrigatórios;
- autorização;
- validação;
- regras de negócio;
- paginação;
- casos-limite;
- tratamento de erros;
- desempenho sob condições aprovadas.

A ferramenta não define por si só qual comportamento é correto.

## Banco de dados e validação de dados

QA pode verificar se:

- transações criam registros esperados;
- alterações afetam linhas corretas;
- tipos e restrições funcionam;
- cálculos reconciliam;
- migrações preservam dados necessários;
- duplicatas são tratadas conforme requisitos;
- registros de auditoria são gerados quando aplicável.

Use acesso de leitura/gravação apenas dentro da autorização.

## CI/CD e liberação

Um gate de qualidade confiável deve deixar claro:

- build testado;
- suítes executadas;
- falhas e testes ignorados;
- confiabilidade dos resultados;
- evidência retida;
- critério de liberação;
- quem pode aprovar exceções.

Passar em testes automatizados é evidência, não autorização automática de liberação.

## Limite de testes de segurança

QA funcional não é automaticamente penetration testing.

Pode-se fazer verificações seguras e autorizadas de papéis, autorização, sessão, validação de entrada, padrões seguros e privacidade. Varredura intrusiva, exploração, ataques a credenciais, payloads destrutivos ou pentest exigem autorização explícita e regras de engajamento.

NIST SSDF e OWASP WSTG são referências úteis, mas não dão permissão para atacar sistemas.

## Acessibilidade

QA pode revisar teclado, foco visível, rótulos, mensagens de erro, cabeçalhos, contraste, zoom/reflow, leitores de tela, legendas e alternativas.

Scanners automáticos detectam apenas parte dos problemas. Passar em uma varredura não estabelece conformidade legal de acessibilidade.

## Desempenho

Testes podem medir tempo de resposta, throughput, concorrência, uso de recursos, estabilidade e recuperação. Carga/estresse pode afetar sistemas; utilize ambientes, limites, dados e horários aprovados.

## Privacidade e segurança da evidência

Tickets, capturas, vídeos, logs e exportações podem conter dados sensíveis. Use privilégio mínimo, repositórios aprovados, MFA, mascaramento, verificação de destinatários e regras de retenção. Não use e-mail ou armazenamento pessoal para artefatos protegidos nem exponha credenciais ou segredos.

## IA responsável em QA

Quando permitido pela política, IA pode ajudar a:

- sugerir ideias de teste;
- redigir casos;
- gerar dados sintéticos;
- explicar stack traces;
- redigir automação;
- sugerir edge cases;
- preparar documentação.

Validação humana continua obrigatória. Não envie código-fonte protegido, credenciais, dados de clientes, logs privados ou informações não publicadas para ferramentas não aprovadas. Não aceite requisitos inventados por IA. Não permita que IA feche defeitos ou aprove releases fora da governança. Não trate uma explicação gerada como causa raiz comprovada.

NIST AI RMF e o perfil de IA generativa são orientações voluntárias de gestão de riscos.

## Limites éticos

Não se deve:

- fabricar resultados;
- marcar PASS sem evidência;
- esconder falhas conhecidas;
- alterar resultado esperado após execução apenas para criar um PASS;
- excluir defeitos sem disposição autorizada;
- usar dados de produção sem autorização;
- explorar sistemas fora de escopo;
- divulgar defeitos ou vulnerabilidades confidenciais;
- afirmar que um produto está “sem bugs” porque uma suíte passou.

## Educação e entrada — Estados Unidos

O*NET classifica a ocupação em **Job Zone Four — Considerable Preparation Needed**. Respostas atuais de educação para novas contratações incluem aproximadamente:

- **50%** bachelor’s degree;
- **26%** associate degree;
- **9%** certificado pós-secundário.

Não são requisitos universais. Empregadores podem aceitar combinações de educação, experiência, portfólio, estágio, apprenticeship, suporte técnico, desenvolvimento e automação.

CareerOneStop/American Job Centers ajudam a investigar treinamento e programas WIOA. Elegibilidade e financiamento não são automáticos.

O*NET lista o título de Registered Apprenticeship **Software Quality Assurance Tester (Nof)**. Verifique vagas reais em Apprenticeship.gov.

## Canadá

### QA em nível de analista — NOC 21222

**Software QA (Quality Assurance) Analyst** é comparado a **NOC 21222**. Salários nacionais atuais:

- **C$28.85/hora** baixo;
- **C$46.15/hora** mediano;
- **C$68.68/hora** alto.

### Software Tester — NOC 22222

**Software Tester** é comparado a **NOC 22222**. Salários nacionais atuais:

- **C$17.50/hora** baixo;
- **C$35.00/hora** mediano;
- **C$51.28/hora** alto.

Regulação não é uniforme. Job Bank atualmente identifica a ocupação de testing technician como regulada em Manitoba pela Certified Technicians and Technologists Association of Manitoba. Verifique a província/território aplicável.

## Colômbia

**CUOC 25190** inclui títulos como Analista de prueba de software, Analista de pruebas - tester, Analista de aseguramiento de la calidad informática, Probador de sistemas, Probador de software, Coordinador de prueba de software e Líder de pruebas testing.

Não se fabrica um salário nacional representativo colombiano porque o perfil oficial atual não fornece evidência estatisticamente representativa adequada para essa afirmação.

### Rotas SENA

**Procesamiento de pruebas de software**  
- Técnico;
- **2.208 horas**;
- formação titulada.

**Manejo de pruebas de software**  
- formação complementar virtual;
- **40 horas**.

**Modelos de calidad de software**  
- formação complementar virtual;
- **40 horas**.

**Procesos para software de calidad**  
- formação complementar virtual;
- **40 horas**.

Os cursos de 40 horas são complementares e não equivalem ao Técnico de 2.208 horas. Verifique disponibilidade, vagas, modalidade e requisitos no Betowa.

## América Latina e Caribe

OIT/Cinterfor pode ajudar a localizar instituições nacionais de formação profissional. Não garante cursos, bolsas, vagas ou financiamento em testes de software.

## Salários e perspectiva — use a população correta

### Estados Unidos

BLS 2025/O*NET para 15-1253.00:

| Percentil | Anual | Por hora |
|---|---:|---:|
| 10 | $61,440 | $29.54 |
| 25 | $80,310 | $38.61 |
| Mediana | $104,300 | $50.14 |
| 75 | $133,180 | $64.03 |
| 90 | $167,010 | $80.29 |

Projeção 2024–2034:

- emprego 2024: **201,700**;
- emprego projetado 2034: **221,900**;
- crescimento: **10%**;
- aberturas anuais projetadas: **14,000**.

### Estimativa não governamental atual

Indeed, revisado em agosto de 2026, informou para **Software Quality Assurance Analyst** aproximadamente:

- média **$87,641/ano**;
- baixa **$56,161/ano**;
- alta **$136,766/ano**;
- **208** observações;
- **36 meses** de postings;
- atualizado em **2 de agosto de 2026**.

É uma estimativa de mercado específica do título, não uma estatística oficial.

## Sequência prática de aprendizagem

1. Fundamentos: requisitos, casos, defeitos, severidade/prioridade, regressão, acessibilidade e privacidade.
2. Fundamentos técnicos: HTML/CSS/JavaScript, SQL, HTTP/API, DevTools, Git, logs e linha de comando.
3. Automação: um framework, seletores estáveis, asserções, dados, setup/teardown, debugging e CI.
4. Especialização: API, mobile, performance, acessibilidade, dados ou QA com segurança autorizada.

## Portfólio seguro

Use software público, licenciado, open source ou próprio e dados sintéticos. Projetos úteis incluem plano de testes, matriz de rastreabilidade, defeitos bem escritos, coleção API, suíte automatizada, revisão de acessibilidade, teste controlado de desempenho e workflow CI.

Não publique código de empregadores, requisitos proprietários, dados reais de clientes, credenciais, logs privados ou vulnerabilidades sem autorização.

## Plano inicial de quatro semanas

### Semana 1
Escreva dez casos de teste para um app demo, defina resultados esperados antes de executar e documente dois defeitos reproduzíveis.

### Semana 2
Pratique HTTP/API e SQL básico com sistemas locais/demo e documente dados e limpeza.

### Semana 3
Automatize um fluxo estável com Playwright, Selenium ou outro framework apropriado; adicione asserções e investigue uma falha intencional.

### Semana 4
Prepare README, evidências, limitações, um fluxo CI simples quando aplicável e bullets de currículo precisos.

## Perguntas antes de aceitar uma vaga

- O papel é principalmente manual, automação, análise QA ou execução técnica?
- Quem define severidade e prioridade?
- Quem tem autoridade final de liberação?
- Quais frameworks são usados?
- Como testes flaky são tratados?
- Como dados de teste são criados e protegidos?
- Que testes de segurança pertencem ao escopo QA?
- Como acessibilidade é verificada?
- Há trabalho fora do horário ou fins de semana em releases?
- O que diferencia júnior de sênior?

## Fontes e links de verificação

### Estados Unidos
- O*NET: https://www.onetonline.org/link/details/15-1253.00
- O*NET resumo: https://www.onetonline.org/link/summary/15-1253.00
- O*NET salários: https://www.onetonline.org/link/localwages/15-1253.00
- O*NET perspectiva: https://www.onetonline.org/link/localtrends/15-1253.00
- CareerOneStop WIOA: https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx
- Apprenticeship.gov: https://www.apprenticeship.gov/
- Indeed: https://www.indeed.com/career/software-quality-assurance-analyst/salaries

### Canadá
- QA Analyst: https://www.jobbank.gc.ca/marketreport/summary-occupation/22511/ca
- QA Analyst requisitos: https://www.jobbank.gc.ca/marketreport/requirements/22511/ca
- QA Analyst salários: https://www.jobbank.gc.ca/marketreport/wages-occupation/22511/ca
- Software Tester: https://www.jobbank.gc.ca/marketreport/summary-occupation/3950/ca
- Software Tester requisitos: https://www.jobbank.gc.ca/marketreport/requirements/3950/ca
- Software Tester salários: https://www.jobbank.gc.ca/wagereport/occupation/3950
- Treinamento Canadá: https://www.canada.ca/en/services/jobs/training.html

### Colômbia
- CUOC 25190: https://ocupacol.mintrabajo.gov.co/Profile/OccupationalProfile/25190
- SENA Procesamiento de pruebas: https://betowa.sena.edu.co/oferta/procesamiento-de-pruebas-de-software?level=2&modality=V&programId=171614
- SENA Manejo de pruebas: https://betowa.sena.edu.co/oferta/manejo-de-pruebas-de-software?programId=103412
- SENA Modelos de calidad: https://betowa.sena.edu.co/oferta/modelos-de-calidad-de-software?modality=V&offertype=open&programId=73282&technology=1
- SENA Procesos para software de calidad: https://betowa.sena.edu.co/oferta/procesos-para-software-de-calidad?programId=68240

### Desenvolvimento seguro, IA e acessibilidade
- NIST SSDF: https://csrc.nist.gov/pubs/sp/800/218/final
- OWASP WSTG: https://owasp.org/www-project-web-security-testing-guide/
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- Section 508: https://www.section508.gov/create/
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- OIT/Cinterfor: https://www.oitcinterfor.org/statsfp/paises

## Aviso importante

Este guia fornece informação geral de educação e planejamento de carreira. Não garante emprego, renda, admissão, financiamento, apprenticeship, certificação, promoção ou qualquer outro resultado. Mapeamentos ocupacionais podem não ser equivalências exatas entre jurisdições.

Não se declara certificação humana independente, acreditação profissional, revisão jurídica, avaliação de segurança, certificação de acessibilidade, certificação de liberação de software ou certificação de tradução, salvo documentação separada.

## Autor e assistência de IA

Criado e dirigido por **Alberto “Al” Leiva**. O ChatGPT apoiou pesquisa, organização, edição, suporte à tradução e preparação de documentos sob a direção do autor. O autor permanece responsável pelas decisões editoriais e de publicação.

## Licença

Salvo indicação contrária, este material é licenciado sob **CC BY-NC-SA 4.0**.
