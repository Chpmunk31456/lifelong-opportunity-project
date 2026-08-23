# Guia de Oportunidades para Toda a Vida 84 — Analista de Business Intelligence

**Versão:** 2.0 — mestre de trabalho controlado  
**Idioma:** português brasileiro (`pt-BR`)  
**Referência principal dos EUA:** O*NET-SOC 15-2051.01 — Business Intelligence Analysts  
**Comparação com o Canadá:** NOC 21221 — Business systems specialists  
**Comparação com a Colômbia:** CUOC 25110 — Analistas de sistemas  
**Data de revisão:** 2026-08-21

## O que é esta carreira

Um analista de Business Intelligence (BI) transforma perguntas de negócio em métricas, relatórios, dashboards e informações confiáveis para apoiar decisões. O trabalho normalmente exige entender qual decisão o stakeholder precisa tomar, localizar os dados relevantes, validar definições, consultar e transformar informações, criar resultados compreensíveis, reconciliar os resultados com fontes autorizadas e explicar o que os dados mostram — e o que não mostram.

Este guia usa **O*NET-SOC 15-2051.01 — Business Intelligence Analysts** como principal referência dos Estados Unidos. O Canada Job Bank associa o título orientado a TI **Business Intelligence Analyst - Information Technology (IT)** ao **NOC 21221 — Business systems specialists**. Na Colômbia há correspondência direta dentro de **CUOC 25110 — Analistas de sistemas**, cujas denominações oficiais incluem **Analista de inteligencia de negocios**, **Analista de inteligencia de negocio TI**, **Analista de Power BI** e **Analista de analytics**.

BI fica entre negócio, dados, tecnologia e comunicação. Um bom analista não é apenas alguém que monta dashboards. Ele precisa saber de onde veio cada número, quais regras o produziram, se os dados estão completos e atualizados e como uma pessoa razoável poderia interpretar o resultado de forma incorreta.

## Por que pode ser uma boa oportunidade

As organizações coletam cada vez mais dados de finanças, vendas, marketing, operações, cadeia de suprimentos, atendimento, RH, tecnologia e risco. Elas precisam de profissionais capazes de converter esses dados em informação confiável, e não apenas em mais gráficos.

BI pode ser uma rota a partir de:

- operações de negócio;
- apoio financeiro ou contábil;
- reporting;
- entrada de dados ou registros;
- operações de clientes;
- suporte de TI;
- bancos de dados e relatórios;
- qualidade/melhoria de processos;
- análise ou pesquisa.

Uma progressão possível é:

**suporte de reporting/dados → analista BI → analista BI sênior / analytics engineer / desenvolvedor BI → liderança de analytics, data product, engenharia de dados, ciência de dados, sistemas de negócio ou gestão.**

A trajetória depende de profundidade técnica, conhecimento do domínio, educação, expectativas do empregador e capacidade de entregar suporte confiável à decisão.

## Analista BI, analista de dados, desenvolvedor BI, analytics engineer e cientista de dados não são a mesma coisa

### Analista de Business Intelligence

Normalmente enfatiza:

- requisitos de negócio;
- definição de KPI/métricas;
- SQL/consultas;
- relatórios recorrentes;
- dashboards e visualização;
- tendências;
- comunicação com stakeholders;
- validação e reconciliação;
- suporte à decisão.

### Analista de dados

Pode ter grande sobreposição com BI e incluir análise ad hoc, estatística, experimentação, análise operacional ou pesquisa.

### Desenvolvedor BI

Pode aprofundar-se em:

- modelos semânticos;
- arquitetura de relatórios;
- DAX/camadas de cálculo;
- ETL/ELT;
- implantação e desempenho;
- administração da plataforma BI.

### Analytics engineer

Frequentemente transforma dados brutos do warehouse em modelos analíticos documentados, testados e reutilizáveis.

### Cientista de dados

Pode trabalhar com estatística avançada, machine learning, experimentação e modelagem preditiva. O*NET atualmente coleta os dados oficiais de salários e emprego para Business Intelligence Analysts a partir de **Data Scientists**, mas esse crosswalk estatístico não torna as duas funções equivalentes.

## Regra central: comece pela pergunta de negócio

Um dashboard não deve começar com “qual gráfico eu posso criar?”.

Pergunte:

1. Qual decisão precisa ser apoiada?
2. Qual pergunta de negócio precisa ser respondida?
3. Qual métrica ou evidência responderia à pergunta?
4. Qual população, período e granularidade importam?
5. Qual é a fonte autorizada?
6. Quais regras/exclusões se aplicam?
7. Qual atualidade é necessária?
8. Quem pode ver o resultado?
9. Como o número será validado?
10. Quais limitações precisam ser declaradas?

Bom BI reduz ambiguidade antes de criar visualizações.

## Fonte de verdade e linhagem de dados

Toda métrica relevante deve ser rastreável.

Documente:

- sistema de origem;
- tabela/arquivo/API;
- proprietário de negócio;
- timestamp ou frequência de atualização;
- transformações;
- joins e chaves;
- filtros/exclusões;
- regras de cálculo;
- relatório/dashboard de saída;
- versão/histórico de mudanças quando necessário.

Não substitua silenciosamente uma fonte autorizada por uma planilha conveniente só porque o resultado parece melhor.

## Fundamentos de dados relacionais

Um analista BI deve compreender:

- tabelas e linhas;
- colunas/campos;
- chaves primárias;
- chaves estrangeiras;
- relações um-para-um, um-para-muitos e muitos-para-muitos;
- normalização;
- duplicados;
- nulos/faltantes;
- tipos de dados;
- data/hora;
- granularidade.

Erro clássico: unir tabelas em granularidades incompatíveis e multiplicar registros sem perceber.

Antes de um join, confirme o que uma linha representa, se a chave é única, como registros não correspondentes serão tratados e se medidas podem ser duplicadas.

## SQL

SQL aparece em **35%** das vagas dos EUA ligadas ao O*NET 15-2051.01 em 2025, sendo o sinal tecnológico mais forte.

Conceitos úteis:

- `SELECT`;
- filtros;
- ordenação;
- agregação;
- `GROUP BY`;
- joins;
- `CASE`;
- CTE;
- subqueries;
- window functions;
- lógica de datas;
- nulos;
- deduplicação;
- validação da consulta.

A meta não é apenas fazer a consulta rodar, mas retornar a população e a medida corretas.

Valide com contagens, chaves duplicadas, registros conhecidos, totais contra fonte autorizada, datas-limite, nulos, categorias inesperadas e efeito de cada join/filtro.

## Limpeza, transformação e reprodutibilidade

Trabalho comum inclui:

- padronização de categorias;
- tratamento de datas;
- valores ausentes;
- tabelas de mapeamento aprovadas;
- reshape;
- joins de referência;
- campos derivados;
- remoção de duplicados verdadeiros;
- validação de faixas;
- documentação da lógica.

Não remova observações legítimas só porque são inconvenientes para o gráfico.

Resultados críticos devem ser reproduzíveis por meio de SQL salvo, transformações documentadas, scripts versionados quando adequado, fontes nomeadas, timestamps, parâmetros controlados, cálculos reutilizáveis e testes.

## Modelagem dimensional e esquema estrela

Conceitos importantes:

- **fact tables** para eventos mensuráveis;
- **dimension tables** para contexto;
- granularidade;
- chaves substitutas;
- dimensão de data;
- slowly changing dimensions;
- dimensões conformadas;
- medidas aditivas/não aditivas;
- esquema estrela versus desenho operacional normalizado.

## Modelo semântico e governança de métricas

Modelos semânticos podem definir relações, medidas, hierarquias, colunas calculadas, rótulos, segurança, inteligência temporal e lógica de KPI reutilizável.

Para cada KPI importante, documente:

- nome e finalidade;
- fórmula;
- numerador/denominador;
- população e exclusões;
- base temporal;
- fonte;
- frequência de atualização;
- proprietário;
- meta, se houver;
- limitações.

Não altere uma métrica porque o stakeholder não gostou do resultado. Mudanças de definição precisam de aprovação, data de vigência e avaliação do impacto histórico.

## Filtros, datas e qualidade de dados

Filtros podem mudar materialmente a interpretação. Torne explícitos período, calendário/fiscal, fuso horário, status, geografia, produto, registros internos/teste, cancelamentos/devoluções e lógica de snapshot/transação.

Dimensões de qualidade incluem:

- completude;
- exatidão;
- consistência;
- validade;
- tempestividade;
- unicidade;
- integridade;
- rastreabilidade.

Antes de publicar, revise contagens, duplicados, nulos, categorias, totais, limites de datas, amostras e atualização.

## Reconciliação

Dashboards críticos devem ser conciliados com fontes autorizadas, por exemplo:

- receita com finanças;
- pedidos com sistema operacional;
- headcount com RH;
- clientes com customer master;
- inventário com o registro governado.

Diferenças podem ser legítimas; precisam ser explicadas, não ocultadas.

## Estatística e interpretação

Conceitos úteis incluem média, mediana, percentis, taxas, distribuição, variância, desvio padrão, crescimento, média móvel, sazonalidade, coortes e efeito do denominador.

Correlação não prova causalidade. Separe fatos observados de interpretação e recomendação.

## Dashboards e visualização

Boas práticas:

- título e objetivo claros;
- período visível;
- unidades corretas;
- escalas coerentes;
- rótulos legíveis;
- filtros claros;
- definições para métricas ambíguas;
- acesso a detalhe quando apropriado.

Escolha gráficos pelo propósito: barras para categorias, linhas para tendências, scatter para relações numéricas, tabelas para detalhe, KPI cards para uma medida principal, histogramas para distribuição e mapas apenas quando geografia realmente importa.

## Evite visualizações enganosas

Não:

- corte eixos para exagerar diferenças sem aviso;
- use escalas inconsistentes para criar uma impressão desejada;
- compare períodos incompatíveis sem explicar;
- esconda dados ausentes;
- distorça magnitudes com área/volume;
- dependa somente de cor;
- mostre precisão sem suporte;
- confunda valores acumulados e de período.

## Power BI, Tableau e habilidades transferíveis

Sinais atuais incluem **Power BI 20%** e **Tableau 19%**.

Conhecimentos transferíveis:

- conexão a fontes;
- modelagem/relacionamentos;
- medidas/cálculos;
- filtros/contexto;
- drill-down/drill-through;
- row-level security;
- refresh;
- desempenho;
- workspaces/implantação;
- design visual;
- compartilhamento governado.

## Sinais atuais de tecnologias nos EUA

O*NET/Lightcast para 2025:

- SQL **35%**;
- Microsoft Power BI **20%**;
- Python **20%**;
- Tableau **19%**;
- SAP **19%**;
- Microsoft Excel **17%**;
- R **10%**;
- AWS **9%**;
- Microsoft PowerPoint **8%**;
- Microsoft Office **8%**;
- Microsoft Azure **8%**;
- Snowflake **5%**;
- SAS **5%**;
- Salesforce **5%**.

São sinais do mercado, não uma lista obrigatória.

## Excel, Python, R e nuvem

Excel ainda aparece em **17%** das vagas vinculadas. Use tabelas, fórmulas, pivots, validação, Power Query, gráficos e reconciliação de forma controlada.

Python **20%** e R **10%** podem apoiar limpeza, APIs, automação, estatística, validação e visualização. Nem todo cargo exige programação avançada.

AWS **9%**, Azure **8%** e Snowflake **5%** mostram relevância de ambientes modernos. Entenda storage/warehouse, identidade/acesso, refresh, pipelines, custo, governança, logs e secrets sem assumir autoridade de arquiteto.

## Requisitos e comunicação com stakeholders

Clarifique:

- decisão desejada;
- audiência;
- definições;
- frequência;
- latência aceitável;
- granularidade;
- segurança;
- exportação;
- critérios de sucesso;
- teste de aceitação.

Separe no relato:

- fatos observados;
- métricas calculadas;
- premissas;
- interpretação;
- recomendação.

## Privacidade e cibersegurança

BI pode expor dados de clientes, funcionários, finanças, saúde, preços, contratos e identificadores.

Práticas:

- privilégio mínimo;
- fontes aprovadas;
- exports controlados;
- armazenamento e compartilhamento seguros;
- masking/agregação quando necessário;
- retenção/exclusão governada;
- MFA quando exigido;
- proteção de credenciais/tokens;
- contas de serviço com permissões mínimas;
- não contornar row-level security;
- não copiar produção para ferramentas pessoais não gerenciadas;
- relatar exposição inesperada.

NIST Cybersecurity Framework e Privacy Framework oferecem contexto de governança, sem substituir políticas e leis aplicáveis.

## IA e automação responsáveis

IA pode ajudar a:

- redigir SQL;
- explicar consultas;
- sugerir DAX/fórmulas;
- criar testes;
- resumir resultados não sensíveis;
- documentar dashboards;
- gerar exemplos sintéticos.

Controles:

- use apenas sistemas/dados aprovados;
- não envie dados confidenciais, credenciais ou extratos protegidos para IA pública não aprovada;
- valide SQL antes de executar;
- valide fórmulas e cálculos;
- reconcilie com fontes autorizadas;
- diferencie narrativa gerada de evidência observada;
- revise causalidade, erro sistemático e viés;
- não publique automaticamente outputs críticos sem aprovação quando exigida.

O NIST AI Risk Management Framework e o Generative AI Profile são orientações voluntárias e não substituem governança de dados.

## Acessibilidade

Práticas úteis:

- contraste legível;
- texto adequado;
- títulos e rótulos significativos;
- navegação por teclado quando suportada;
- ordem lógica;
- não depender só de cor;
- alternativas em texto/tabela quando prático;
- alt text apropriado em gráficos exportados;
- linguagem concisa e unidades claras.

Ferramentas automáticas não comprovam conformidade legal completa. WCAG 2.2 e Section 508 oferecem contexto quando aplicável.

## Portfólio ético

Use dados públicos, sintéticos ou autorizados.

Ideias:

- dashboard de vendas sintéticas;
- dashboard de tickets fictícios;
- KPI de inventário;
- reconciliação financeira sintética;
- análise SQL com testes;
- star schema;
- dashboard Power BI/Tableau com checklist de acessibilidade;
- caso de join incorreto duplicando receita;
- relatório de qualidade de dados;
- dicionário de métricas e linhagem.

Nunca publique dados confidenciais ou screenshots de empregador/cliente sem autorização.

## Caminho nos Estados Unidos

O*NET classifica 15-2051.01 em **Job Zone Four — Considerable Preparation Needed**.

Respostas atuais de educação para novas contratações:

- **68% bachelor's degree**;
- **23% master's degree**;
- **5% associate degree**.

São padrões de preparação, não exigências legais universais.

O*NET lista **Business Intelligence Engineer** como exemplo aprovado de Registered Apprenticeship. Isso não garante uma vaga local.

CareerOneStop pode ajudar a localizar formação WIOA e outros programas. Elegibilidade e financiamento precisam ser confirmados.

## Salários e perspectiva nos EUA — divulgação obrigatória do crosswalk

O*NET declara explicitamente que os dados de salário e emprego para **Business Intelligence Analysts** são coletados de **Data Scientists**.

As cifras abaixo são portanto referências oficiais BLS/O*NET da série mapeada, **não uma população amostrada exclusivamente de BI Analysts**.

### Série salarial BLS 2025 usada pelo O*NET

| Percentil | Anual | Por hora |
|---|---:|---:|
| 10 | $67,240 | $32.33 |
| 25 | $85,660 | $41.18 |
| Mediana | $120,230 | $57.80 |
| 75 | $158,880 | $76.39 |
| 90 | $199,130 | $95.74 |

### Projeções 2024–2034 usadas pelo O*NET

- emprego 2024: **245,900**;
- emprego projetado 2034: **328,300**;
- crescimento: **34%**, muito mais rápido que a média;
- **23,400 aberturas projetadas por ano**.

Não multiplique aberturas anuais em um total garantido e não presuma que cada vaga tenha o título Business Intelligence Analyst.

### Contexto atual específico do título BI, não governamental

Indeed informou média base de **$94,707/ano** para **Business Intelligence Analyst** nos Estados Unidos, com faixa de **$61,569–$145,682/ano**, baseada em aproximadamente **1.6k salários** de vagas nos **36 meses** anteriores, atualizada em **3 de agosto de 2026**.

É uma estimativa BI-específica não governamental e não deve ser misturada com a série oficial de Data Scientists como se ambas medissem a mesma população.

## Caminho no Canadá

Canada Job Bank associa **Business Intelligence Analyst - Information Technology (IT)** ao **NOC 21221 — Business systems specialists**.

Requisitos atuais típicos:

- bachelor's em computer science, business administration, information systems ou disciplina relacionada **ou** conclusão de college program em computer science geralmente exigido;
- treinamento/certificação de fornecedor pode ser exigido por alguns empregadores;
- segundo Job Bank, a ocupação **não é regulamentada no Canadá**.

Salários nacionais, atualizados em 19 de novembro de 2025:

- baixo: **C$30.67/hora**;
- mediana: **C$45.13/hora**;
- alto: **C$62.50/hora**.

O NOC é mais amplo que BI puro; trate-o como comparação. Perspectivas variam por província/território.

## Caminho na Colômbia

### CUOC 25110 — Analistas de sistemas

OCUPACOL inclui explicitamente:

- Analista de analytics;
- Analista de inteligencia de negocio TI;
- **Analista de inteligencia de negocios**;
- Analista de Power BI;
- Analista de información comercial;
- Analista de procesamiento de información;
- Analista informático para análisis de negocio;
- Especialista en inteligencia comercial.

As funções incluem análise de requisitos/processos, especificações funcionais, testes, integração de dados com visualização/análise, sistematização de dados massivos e gestão de representações de dados.

OCUPACOL mostra faixa histórica/derivada de **COP 800,000–7,113,801**, mas afirma que os dados **não possuem representatividade estatística**. Este guia não usa essa faixa como salário nacional atual representativo de BI.

### SENA — Programación para analítica de datos

- **Técnico**;
- **2,208 horas**;
- formação titulada;
- processamento de dados, metodologia estatística e integração/visualização.

A disponibilidade de turmas varia.

### SENA — Visualización de datos usando Power BI

- complementaria/curso especial;
- **48 horas**;
- turmas 2026 em algumas localidades/modalidades;
- conhecimentos básicos de informática, banco de dados e estatística recomendados.

É treinamento pontual, não qualificação BI completa.

### SENA — Analítica de datos para procesos logísticos

- complementaria virtual;
- **48 horas**;
- armazenamento/tratamento, consulta, homogeneização e apresentação analítica.

É complemento de domínio, não credencial universal.

## América Latina

OIT/Cinterfor pode ajudar a localizar instituições de formação por país. Verifique programa, custo, modalidade, admissão e reconhecimento diretamente.

## Currículo e entrevista

Bullets fortes mostram evidência: reconciliação de métricas, automação validada, definição de KPI, descoberta de join defeituoso, controle de acesso e qualidade de dados. Não invente impacto, certificações ou experiência.

Em entrevistas, esteja pronto para explicar requisitos, validação SQL, joins muitos-a-muitos, fact/dimension, reconciliação, conflito de KPI, seleção de gráficos, privacidade e validação de IA.

## Perguntas ao empregador

Pergunte sobre fontes autorizadas, ferramentas BI, warehouse/lakehouse, governança de métricas, qualidade, implantação, acesso, divisão analista/engenharia, SQL, estatística, política de IA, documentação, formação e acessibilidade.

## Primeiros 30 e 90 dias

Nos primeiros 30 dias: aprenda negócio, fontes, métricas, refresh, acesso, dashboards, processo de publicação e stakeholders. Não altere KPI de produção sem aprovação.

Em 90 dias: busque esclarecer requisitos, escrever/validar SQL, explicar linhagem, manter métricas, reconciliar dashboards, detectar qualidade, comunicar limitações, criar visualizações acessíveis e usar IA sob controle.

## Checklist antes de se candidatar

Confirme domínio de:

- pergunta de negócio/KPI;
- joins e agregação SQL;
- granularidade;
- transformação;
- esquema estrela;
- reconciliação;
- dashboards;
- estatística descritiva;
- visualização não enganosa;
- privacidade/acesso;
- IA responsável;
- portfólio documentado.

## Perguntas antes de comprar treinamento

Verifique SQL prático, modelagem, qualidade/reconciliação, plataformas, capstone/portfólio, instrutores, custo total, financiamento, acessibilidade e reconhecimento pelos empregadores. Não dependa de garantias de emprego ou renda.

## Fontes controladas

1. https://www.onetonline.org/link/details/15-2051.01
2. https://www.onetonline.org/link/summary/15-2051.01
3. https://www.onetonline.org/link/localwages/15-2051.01
4. https://www.onetonline.org/link/localtrends/15-2051.01
5. https://www.onetonline.org/link/hot_tech/15-2051.01
6. https://www.onetonline.org/link/demand/15-2051.01
7. https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx
8. https://www.careeronestop.org/FindTraining/find-training.aspx
9. https://www.indeed.com/career/business-intelligence-analyst/salaries
10. https://www.jobbank.gc.ca/marketreport/summary-occupation/296881/ca
11. https://www.jobbank.gc.ca/marketreport/requirements/296881/ca
12. https://www.jobbank.gc.ca/marketreport/wages-occupation/296881/ca
13. https://www.canada.ca/en/services/jobs/training.html
14. https://ocupacol.mintrabajo.gov.co/Profile/OccupationalProfile/25110
15. https://betowa.sena.edu.co/oferta/programacion-para-analitica-de-datos?location=57054001&modality=P&programId=133094
16. https://betowa.sena.edu.co/oferta/visualizacion-de-datos-usando-power-bi?modality=V&offertype=company&programId=160058
17. https://betowa.sena.edu.co/oferta/analitica-de-datos-para-procesos-logisticos?modality=V&offertype=company
18. https://www.oitcinterfor.org/statsfp/paises
19. https://www.cisa.gov/secure-our-world
20. https://www.nist.gov/cyberframework
21. https://www.nist.gov/privacy-framework
22. https://www.nist.gov/itl/ai-risk-management-framework
23. https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
24. https://www.section508.gov/create/
25. https://www.w3.org/TR/WCAG22/

## Aviso de escopo e ausência de garantia

Este guia oferece informações educacionais e de planejamento de carreira. Não garante emprego, renda, admissão, financiamento, certificação, licença, promoção ou outro resultado. Requisitos, remuneração e oportunidades variam por jurisdição, empregador e tempo.

Não fornece certificação jurídica, contábil, de privacidade, cibersegurança, regulatória ou de acessibilidade. Siga a legislação aplicável, políticas do empregador, governança aprovada de dados/métricas e autoridade atribuída.

Criado e dirigido por **Alberto “Al” Leiva**. O ChatGPT apoiou pesquisa, organização, edição, suporte à tradução e preparação de documentos sob a direção do autor. O autor permanece responsável pelas decisões editoriais e de publicação.

Salvo indicação diferente em algum arquivo, estes materiais estão licenciados sob **CC BY-NC-SA 4.0**.
