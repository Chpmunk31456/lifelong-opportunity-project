# Guia de Oportunidades para Toda a Vida 86 — Administrador de Banco de Dados

**Versão:** 2.0 — mestre de trabalho controlado  
**Idioma:** Português do Brasil (`pt-BR`)  
**Referência principal dos EUA:** O*NET-SOC 15-1242.00 — Database Administrators  
**Comparação do Canadá:** NOC 21223 — Database analysts and data administrators  
**Comparação da Colômbia:** CUOC 25210 — Diseñadores y administradores de bases de datos  
**Data de revisão:** 2026-08-22  
**Fonte inglesa congelada:** blob `ce3f8215c91230c15e1efdd702e6f73571c7ae18`

## O que é esta carreira

Um Administrador de Banco de Dados (DBA) ajuda a manter os bancos de dados de uma organização disponíveis, corretos, seguros, recuperáveis e sustentáveis. O trabalho pode incluir instalar ou configurar sistemas gerenciadores de bancos de dados, criar e manter bases, controlar acessos, testar mudanças, monitorar desempenho e capacidade, aplicar atualizações aprovadas, apoiar backups e recuperação, solucionar incidentes, documentar configurações e ajudar equipes a usar sistemas de dados com segurança.

Este guia usa **O*NET-SOC 15-1242.00 — Database Administrators** como principal referência dos Estados Unidos. O Canadá é comparado a **NOC 21223 — Database analysts and data administrators**. A Colômbia tem correspondência direta em **CUOC 25210 — Diseñadores y administradores de bases de datos**, que inclui expressamente *Administrador de base de datos*.

Um DBA pode ter acesso técnico muito poderoso. Isso **não** significa autorização irrestrita para ler, copiar, alterar, exportar ou excluir qualquer dado. Mudanças em produção, acesso privilegiado, backups, controles de segurança e ações de recuperação devem permanecer dentro da autorização do empregador, da gestão de mudanças e das obrigações aplicáveis de privacidade e segurança.

## Por que esta carreira continua importante

Organizações dependem de bancos de dados para transações, clientes, finanças, operações, logística, saúde, serviços governamentais, analytics, identidade, aplicações e sistemas internos. Plataformas de nuvem e serviços gerenciados automatizam algumas tarefas de infraestrutura, mas não eliminam a necessidade de pessoas capazes de:

- compreender estruturas e dependências de dados;
- controlar acesso;
- detectar problemas de desempenho ou capacidade;
- proteger integridade e disponibilidade;
- verificar backups e recuperabilidade real;
- planejar e validar mudanças;
- investigar incidentes;
- documentar sistemas;
- coordenar com equipes de aplicações, nuvem, segurança e negócio.

A ocupação está evoluindo, não simplesmente desaparecendo. As projeções atuais dos EUA mostram pequena redução no emprego total de DBAs, enquanto reposição e rotatividade ainda geram milhares de aberturas por ano. Por isso, é importante desenvolver habilidades transferíveis entre bancos tradicionais, serviços gerenciados em nuvem, automação, plataformas de dados e operações com foco em segurança.

## O que Administradores de Banco de Dados realmente fazem

As tarefas atuais do O*NET incluem:

- modificar bancos de dados e plataformas DBMS existentes ou dirigir mudanças aprovadas;
- planejar e implementar medidas de segurança;
- instalar atualizações aprovadas de DBMS;
- especificar usuários e níveis de acesso;
- testar mudanças de bancos de dados e aplicações;
- corrigir erros e fazer modificações necessárias;
- treinar usuários e apoiar pessoal técnico júnior ou clientes;
- planejar e supervisionar instalação e testes de novos sistemas quando atribuído;
- avaliar desempenho;
- desenvolver parâmetros, especificações e modelos de dados.

Uma vaga pode enfatizar apenas parte dessas atividades. Alguns DBAs se concentram em Oracle ou SQL Server; outros trabalham com PostgreSQL, MySQL, bancos gerenciados em nuvem, data warehouses, NoSQL, alta disponibilidade, automação ou suporte de aplicações.

## DBA não é o mesmo que todos os papéis de dados próximos

### Administrador de Banco de Dados

Geralmente enfatiza:

- bancos operacionais;
- segurança e acesso;
- backup e recuperação;
- patches e upgrades;
- desempenho;
- capacidade;
- disponibilidade;
- incidentes;
- mudanças controladas.

### Desenvolvedor de banco de dados

Pode se concentrar mais em:

- objetos de schema;
- stored procedures;
- funções;
- desenvolvimento de consultas;
- lógica de banco de dados para aplicações.

### Arquiteto de banco de dados

Costuma atuar em desenho mais amplo:

- seleção de plataformas;
- arquitetura de dados;
- padrões de integração;
- resiliência;
- padrões técnicos;
- desenho de longo prazo.

### Engenheiro de dados

Muitas vezes trabalha mais com:

- pipelines;
- movimentação e transformação;
- warehouses/lakes;
- orquestração;
- plataformas analíticas.

### Analista de Dados / Analista de BI

Normalmente se concentra mais em consultas, análises, métricas, visualização e interpretação de negócio do que em administração operacional de bancos.

Empregadores podem combinar responsabilidades. Leia a descrição real da vaga, não apenas o título.

## Primeira regra operacional: conheça sua autoridade antes de agir

Antes de uma mudança em produção, confirme:

1. Qual sistema e ambiente estão no escopo?
2. A ação está autorizada?
3. É necessário ticket, aprovação ou janela de manutenção?
4. Qual é o impacto de negócio se falhar?
5. É necessário backup, snapshot, ponto de restauração ou caminho de rollback?
6. O script ou mudança foi testado em ambiente não produtivo apropriado?
7. Quem precisa ser notificado?
8. Que validação comprova sucesso?
9. Que condição exige parar e escalar?
10. Que evidência deve ser mantida para auditoria ou revisão de incidente?

Capacidade técnica não equivale a autoridade organizacional.

## Fundamentos de bancos de dados

Um DBA sólido deve compreender:

- bancos relacionais;
- tabelas, linhas e colunas;
- chaves primárias e estrangeiras;
- constraints;
- índices;
- views;
- schemas;
- transações;
- isolamento e concorrência;
- normalização e desnormalização;
- tipos de dados;
- stored procedures/funções quando usadas;
- arquivos e estruturas de armazenamento;
- logs/journals;
- replicação;
- tipos de backup;
- recuperação;
- padrões de alta disponibilidade.

A implementação varia por plataforma, mas os princípios são transferíveis.

## SQL

SQL é a principal sinalização tecnológica nas ofertas atuais ligadas à ocupação.

Um DBA normalmente precisa compreender:

- `SELECT` e filtros;
- joins;
- agregação;
- linguagem de definição de dados (DDL);
- linguagem de manipulação de dados (DML);
- transações;
- permissões;
- índices;
- planos de execução;
- locks, blocking e concorrência;
- stored procedures/funções quando relevantes;
- views de catálogo/sistema;
- scripting seguro e validação de mudanças.

Uma consulta ou script não é seguro apenas porque executa sem erro.

Antes de uma ação SQL relevante, verifique:

- ambiente-alvo;
- nomes dos objetos;
- escopo de linhas;
- comportamento transacional;
- permissões;
- contagens esperadas;
- preparação de backup/rollback;
- impacto de desempenho;
- validação posterior.

## Sinais tecnológicos atuais

Os dados de ofertas de emprego do O*NET para 2025 mostram sinais de demanda como:

- SQL — **62%**;
- Python — **42%**;
- AWS — **29%**;
- Microsoft Azure — **25%**;
- Snowflake — **16%**;
- Apache Spark — **13%**;
- Microsoft Power BI — **12%**;
- Java — **12%**;
- PostgreSQL — **11%**;
- Apache Kafka — **10%**;
- Apache Airflow — **9%**;
- Microsoft SQL Server — **9%**;
- Tableau — **9%**;
- NoSQL — **9%**;
- Amazon Redshift — **9%**;
- Git — **8%**;
- Linux — **8%**;
- MySQL — **8%**;
- Oracle PL/SQL — **7%**;
- Oracle Database — **7%**;
- UNIX — **6%**;
- Terraform — **5%**;
- PowerShell — **5%**;
- MongoDB — **5%**.

São sinais de vagas, não uma lista obrigatória para todo DBA. Aprofunde conforme a plataforma e o empregador-alvo.

## Identidade, acesso e administração privilegiada

O acesso deve seguir controles aprovados pela organização.

Boas práticas incluem:

- menor privilégio;
- acesso baseado em função quando suportado;
- contas normais e privilegiadas separadas quando exigido;
- MFA para acesso administrativo compatível;
- armazenamento aprovado de credenciais e segredos;
- não colocar senhas ou connection strings em chats, tickets, repositórios públicos ou notas pessoais;
- evitar contas administrativas compartilhadas, salvo processo legado/emergencial expressamente aprovado;
- revisão periódica de acessos;
- remoção rápida de privilégios desnecessários;
- logging/auditoria de ações privilegiadas quando suportado;
- segregação de funções para operações sensíveis quando necessária.

Nunca use acesso de banco de dados para curiosidade ou consulta sem finalidade autorizada.

## Segurança e integridade de banco de dados

O*NET inclui segurança de bancos de dados como responsabilidade central.

Um DBA pode participar de:

- controle de acesso;
- hardening de configuração;
- configuração de criptografia quando atribuída;
- patches/upgrades;
- remediação de vulnerabilidades;
- logging/auditoria;
- exposição segura de rede;
- proteção de backups;
- gestão de segredos;
- monitoramento de acesso suspeito ou falho;
- preservação de evidência em incidentes;
- recuperação após incidentes de integridade ou disponibilidade.

Arquitetura de segurança e interpretação jurídica podem pertencer a outras equipes. Saiba quando escalar.

## Backup não é o mesmo que recuperabilidade

Um log dizendo “backup completed” é útil, mas não comprova sozinho que a organização conseguirá recuperar o que precisa.

Um processo maduro pode incluir:

- cronogramas aprovados de backup;
- regras de retenção;
- criptografia/proteção de mídia ou repositório;
- cópias em outro domínio de falha quando exigido;
- testes de restauração;
- point-in-time recovery quando suportado;
- runbooks documentados;
- monitoramento de backups falhos ou atrasados;
- verificação do escopo;
- exercícios de disaster recovery;
- testes das dependências aplicação/banco.

Organizações podem definir **RPO** (Recovery Point Objective) e **RTO** (Recovery Time Objective). O DBA deve entender os objetivos definidos pela organização, e não inventá-los independentemente.

## Testes de restauração

Um teste de restauração deve responder, por exemplo:

- O backup é realmente legível?
- Contém o banco e a versão esperados?
- Pode ser restaurado no ambiente necessário?
- Chaves e segredos necessários estão disponíveis por processo aprovado?
- O banco restaurado passa verificações de integridade?
- As aplicações reconectam corretamente?
- Os passos de recuperação estão documentados e atualizados?
- O teste atendeu aos objetivos de recuperação?

Nunca faça restauração destrutiva sobre produção sem autorização explícita e plano controlado.

## Alta disponibilidade, replicação e failover

Conforme a plataforma, um DBA pode apoiar:

- réplicas;
- clusters;
- availability groups;
- bancos standby;
- réplicas gerenciadas em nuvem;
- configurações multi-zone ou multi-region;
- procedimentos de failover;
- monitoramento de replication lag.

Alta disponibilidade não substitui backup. Replicação pode copiar corrupção, exclusões ou mudanças maliciosas.

Failover deve ser testado por procedimentos aprovados, não presumido funcional apenas porque os componentes parecem saudáveis.

## Desempenho e capacidade

Um DBA pode investigar:

- consultas lentas;
- planos de execução ineficientes;
- índices ausentes ou excessivos;
- locks, blocking e deadlocks;
- pressão de CPU/memória;
- pressão de armazenamento;
- latência de I/O;
- esgotamento de conexões;
- crescimento de transaction log;
- replication lag;
- crescimento de tabelas/índices;
- custo de manutenção;
- mudanças de workload.

Ajuste com evidência. Uma alteração que melhora uma consulta pode piorar outra carga.

Documente:

- baseline;
- métrica observada;
- hipótese;
- mudança;
- validação;
- plano de rollback;
- resultado.

## Gestão de mudanças

Mudanças em produção podem afetar muitas aplicações e usuários. Um processo disciplinado pode exigir:

- objetivo documentado;
- solicitação/ticket aprovado;
- revisão de dependências;
- script ou pacote testado;
- peer review;
- backup ou ponto de restauração;
- janela de manutenção;
- plano de comunicação;
- passos de execução;
- validações;
- rollback;
- monitoramento após mudança;
- evidência de conclusão.

Não “corrija” produção silenciosamente fora dos controles aprovados apenas porque a alteração parece pequena.

## Mudanças de schema e migrações

Antes de uma migração de schema ou dados, considere:

- tamanho da tabela;
- duração de locks;
- impacto no transaction log;
- compatibilidade de aplicações;
- impacto em índices;
- impacto em replicação;
- viabilidade de rollback;
- conversões de tipo;
- comportamento de nulos/defaults;
- timezone/encoding;
- downtime necessário;
- contagens/checksums de validação;
- impacto de privacidade/segurança.

Para mudanças grandes ou de alto risco, use o padrão testado da organização e não improvise em produção.

## Patches e upgrades

Plataformas exigem manutenção de segurança e ciclo de vida.

Um plano controlado pode incluir:

- revisão do ciclo de suporte do fornecedor;
- avaliação de compatibilidade;
- compatibilidade de drivers/clientes;
- prontidão de backup/recuperação;
- testes não produtivos;
- sequência de HA/failover;
- aprovação da janela de manutenção;
- plano de rollback/fallback;
- validação posterior de integridade/desempenho;
- documentação de versão/configuração.

Não prometa “zero downtime” quando a arquitetura e os testes não o sustentarem.

## Monitoramento e alertas

Domínios úteis incluem:

- disponibilidade;
- conexões falhas;
- falhas de autenticação;
- erros do banco;
- CPU/memória/armazenamento;
- latência de I/O;
- duração de consultas;
- blocking/deadlocks;
- sucesso/falha de backups;
- estado de replicação;
- crescimento do transaction log;
- limiares de capacidade;
- expiração de certificados/credenciais quando aplicável;
- saúde/custos anômalos de serviços cloud.

Alertas devem ter proprietário, severidade e resposta esperada. Alertas demais e de baixa qualidade criam ruído e podem esconder incidentes reais.

## Resposta a incidentes e escalonamento

Um DBA pode participar diante de:

- indisponibilidade;
- corrupção;
- suspeita de acesso não autorizado;
- comprometimento de credenciais;
- ransomware ou atividade destrutiva;
- exclusão acidental;
- falha de replicação;
- recuperação falha;
- degradação severa de desempenho;
- preocupação de integridade;
- exposição inesperada de dados.

Siga o processo de incidentes da organização. Preserve evidência e horários. Não destrua logs nem “limpe” antes de segurança/incidentes determinar o que precisa ser retido.

## Privacidade, retenção e governança de dados

DBAs podem visualizar dados altamente sensíveis. Esse acesso é responsabilidade, não benefício do cargo.

Siga regras aprovadas para:

- finalidade autorizada;
- mínimo acesso necessário;
- classificação de dados;
- retenção e exclusão;
- legal holds quando aplicáveis;
- masking/tokenização quando exigidos;
- extrações seguras;
- dados de teste;
- verificação de destinatários;
- exportação;
- auditoria;
- reporte de incidentes.

Não copie bases de produção para ambientes pessoais ou não controlados.

## Separação de desenvolvimento, teste e produção

Quando a organização permitir:

- desenvolva e teste mudanças fora de produção;
- use dados sintéticos, mascarados ou aprovados;
- restrinja credenciais de produção;
- separe aprovação e desenvolvimento quando exigido;
- controle connection strings e segredos por ambiente;
- valide o alvo antes de executar scripts.

Um erro de alto impacto comum é executar o script certo no ambiente errado.

## Nuvem e bancos gerenciados

Serviços gerenciados podem automatizar hardware, opções de patching, snapshots ou replicação. Eles não removem responsabilidades do cliente.

Um DBA ou operador de plataforma ainda pode gerenciar:

- identidade e acesso;
- exposição de rede;
- security groups/firewalls;
- usuários e roles;
- criptografia/chaves quando configuráveis;
- retenção de backup;
- logging/auditoria;
- manutenção;
- sizing;
- desempenho de consultas;
- arquitetura de resiliência;
- credenciais de aplicações;
- custos/capacidade;
- governança de mudanças.

Entenda o modelo de responsabilidade compartilhada do provedor. “Está na nuvem” não significa que o provedor gerencia toda a segurança.

## Automação, scripting e infraestrutura como código

Automação reduz trabalho repetitivo, mas pode multiplicar erros.

Ferramentas comuns podem incluir:

- Python;
- PowerShell;
- shell scripts;
- SQL scripts;
- Terraform;
- ferramentas de configuration management;
- CI/CD;
- automação cloud.

Controles úteis:

- controle de versão;
- peer review;
- validação de parâmetros;
- proteções por ambiente;
- gestão de segredos;
- dry-run/teste quando disponível;
- logging;
- rollback;
- permissões limitadas para identidades de automação.

## IA responsável no trabalho DBA

A IA pode apoiar tarefas de baixo risco quando a política permitir, como:

- rascunhar SQL ou scripts administrativos;
- explicar um plano de execução;
- rascunhar runbooks;
- propor casos de teste;
- gerar dados sintéticos;
- resumir documentação pública;
- sugerir consultas de monitoramento;
- explicar mensagens de erro.

Validação humana continua obrigatória.

Não:

- envie dados de produção, credenciais, schemas privados, connection strings ou logs protegidos para IA não aprovada;
- execute SQL gerado por IA em produção sem revisão, teste e autorização;
- aceite nomes de objetos, sintaxe, métricas ou comportamento de fornecedor inventados;
- permita mudanças autônomas de produção fora da governança aprovada;
- trate saída de IA como evidência de incidente ou documentação do fornecedor;
- elimine rollback porque uma recomendação pareça plausível.

Para mudanças relevantes, verifique documentação autoritativa e controles organizacionais.

NIST AI RMF e o perfil de IA generativa são orientação voluntária de risco, não substitutos de governança de banco de dados e segurança.

## Acessibilidade e documentação utilizável

Documentação de banco de dados deve ser utilizável pelas pessoas que precisam dela, inclusive durante incidentes.

Práticas úteis:

- títulos e headings claros;
- passos em ordem lógica;
- texto e contraste legíveis;
- tabelas com cabeçalhos adequados;
- descrições textuais de diagramas;
- não depender apenas de cor;
- documentação/ferramentas acessíveis por teclado quando suportado;
- ramos claros de erro/decisão;
- linguagem simples para passos de alto impacto;
- comandos/scripts visualmente distintos das explicações.

Uma verificação automática não comprova conformidade legal de acessibilidade.

## Educação e caminhos de entrada — Estados Unidos

O*NET coloca Database Administrators em **Job Zone Four — Considerable Preparation Needed**.

As respostas atuais de educação indicam:

- **89%** bachelor's degree;
- **4%** certificado post-baccalaureate;
- **3%** associate degree.

São respostas ocupacionais e não uma regra absoluta para toda vaga.

É possível avançar para DBA a partir de:

- suporte de TI;
- suporte de aplicações;
- administração de sistemas;
- desenvolvimento de banco de dados;
- operações de dados;
- desenvolvimento de software;
- suporte cloud;
- reporting/BI;
- programas formais de computação/sistemas;
- treinamento do empregador;
- aprendizagem ou rotas técnicas.

### Localizadores de treinamento e financiamento dos EUA

CareerOneStop e American Job Centers ajudam a investigar treinamento local, provedores WIOA e apoios. Elegibilidade e financiamento variam e não são garantidos.

O*NET lista títulos aprovados de aprendizagem:

- **Database Administrator (Nof)**;
- **Database Technician**.

Use Apprenticeship.gov para verificar oportunidades ativas na sua região.

## Canadá

Canada Job Bank mapeia Database Administrator (DBA) para **NOC 21223 — Database analysts and data administrators**.

Requisitos típicos atuais incluem:

- bachelor's degree ou programa de college, normalmente em ciência da computação, engenharia da computação ou matemática;
- programação e experiência relacionada.

Job Bank afirma atualmente que a ocupação **não é regulamentada no Canadá**. Mesmo assim, exigências de empregadores podem ser substanciais.

### Salários do Canadá

Os salários nacionais atuais são:

- **C$25.00/hora — baixo**;
- **C$40.87/hora — mediana**;
- **C$61.03/hora — alto**.

Aplicam-se ao NOC 21223 e não representam remuneração garantida em toda vaga DBA.

Canada.ca fornece links nacionais de auxílio estudantil, treinamento, serviços de emprego e programas provinciais/territoriais. Elegibilidade e disponibilidade variam.

## Colômbia

A correspondência direta é **CUOC 25210 — Diseñadores y administradores de bases de datos**, nível de competência 4.

Denominações oficiais incluem:

- Administrador de base de datos;
- Administrador de datos;
- Analista de base de datos;
- Arquitecto de bases de datos;
- Data manager;
- Desarrollador de base de datos;
- Diseñador de bases de datos;
- Gerente de base de datos;
- Programador de base de datos.

As funções oficiais cobrem arquitetura, implementação/teste de DBMS, políticas de acesso/uso, backup/recuperação, segurança/integridade, gestão de risco e coordenação técnica.

OCUPACOL atualmente não exibe contagem disponível de ocupados para o perfil. Este guia não fabrica salário nacional representativo para DBA na Colômbia.

### SENA — caminho de longa duração

**Implementación y gestión de bases de datos**

- Tecnólogo;
- **3,984 horas**;
- formación titulada;
- oferta atual no Betowa;
- aplicam-se seleção e requisito de exame de Estado;
- verifique local, modalidade, turma, vagas e datas.

### SENA — caminhos complementares

**Bases de datos: generalidades y sistemas de gestión**

- formação complementar virtual;
- **40 horas**;
- bancos relacionais, normalização, entidade-relacionamento e fundamentos de projeto.

**Construcción de bases de datos con MySQL**

- formação complementar;
- **48 horas**;
- construção focada em MySQL.

Cursos curtos complementam e não substituem o Tecnólogo de longa duração nem experiência exigida pelo empregador.

## América Latina e Caribe

OIT/Cinterfor ajuda a localizar instituições e sistemas de formação profissional na região. É um localizador, não garantia de curso DBA atual, bolsa, admissão ou financiamento.

## Salários oficiais dos Estados Unidos

Dados BLS 2025 apresentados pelo O*NET mostram:

| Percentil | Anual | Por hora |
|---|---:|---:|
| 10 | $60,230 | $28.96 |
| 25 | $79,610 | $38.28 |
| Mediana | $104,620 | $50.30 |
| 75 | $135,460 | $65.13 |
| 90 | $163,320 | $78.52 |

Os valores correspondem a O*NET-SOC 15-1242.00 Database Administrators.

## Perspectiva de emprego nos Estados Unidos

O*NET/BLS mostra:

- emprego 2024: **78,000**;
- emprego projetado 2034: **77,500**;
- crescimento projetado: **-1%**;
- aberturas anuais projetadas: **3,800**.

É pequena queda no emprego total, não crescimento. As aberturas incluem reposição/rotatividade.

## Estimativa atual não governamental dos EUA

A página atual do Indeed para Database Administrator, revisada em agosto de 2026, informa aproximadamente:

- salário-base médio: **$110,414/ano**;
- baixo: **$73,876/ano**;
- alto: **$165,024/ano**;
- **2.1k** salários provenientes de ofertas nos **36 meses** anteriores;
- atualização em **10 de agosto de 2026**.

É uma estimativa de mercado específica do título e não governamental, não uma série oficial nem remuneração garantida.

## Sequência prática de aprendizagem

### Etapa 1 — fundamentos

Aprenda:

- modelos relacionais;
- chaves/constraints;
- normalização;
- SQL;
- transações;
- segurança básica;
- conceitos de backup.

### Etapa 2 — uma plataforma em profundidade

Escolha, por exemplo:

- PostgreSQL;
- Microsoft SQL Server;
- MySQL;
- Oracle Database.

Pratique instalação/configuração, usuários/roles, backup/restauração, monitoramento e mudanças seguras.

### Etapa 3 — operações

Adicione:

- análise de desempenho;
- índices;
- monitoramento;
- manutenção;
- patches;
- testes de recuperação;
- troubleshooting de incidentes;
- automação.

### Etapa 4 — nuvem e resiliência

Aprenda:

- uma plataforma cloud;
- bancos gerenciados;
- controles de identidade/rede;
- replicação/alta disponibilidade;
- retenção de backups;
- automação de infraestrutura;
- responsabilidade compartilhada.

### Etapa 5 — especialização

Possíveis caminhos:

- cloud DBA/data platform engineer;
- database reliability;
- segurança de bancos de dados;
- performance engineering;
- data engineering;
- arquitetura;
- automação de plataforma.

## Projetos de portfólio seguros

Use dados sintéticos, públicos ou licenciados.

Projetos possíveis:

1. criar schema relacional com constraints;
2. documentar modelo entidade-relacionamento;
3. criar roles de menor privilégio;
4. fazer backup e restaurar banco de prática;
5. demonstrar point-in-time recovery em laboratório quando suportado;
6. criar baseline e exercício de tuning de índice;
7. simular replicação/failover em laboratório;
8. escrever migração com validação e rollback;
9. criar dashboard de monitoramento com workload sintético;
10. escrever e testar runbook de recuperação.

Nunca publique:

- dados de empregador ou cliente;
- credenciais ou connection strings;
- schemas/capturas de produção;
- IPs/hostnames privados;
- configurações proprietárias;
- backups reais;
- tokens ou chaves;
- detalhes de vulnerabilidade de sistemas sem autorização.

## Plano inicial de quatro semanas

### Semana 1 — SQL e schema

- instale banco local de prática;
- crie tabelas, chaves e constraints;
- pratique SQL com segurança;
- documente o schema;
- crie usuários não privilegiados.

### Semana 2 — backup e recuperação

- crie backup de laboratório;
- restaure em instância separada;
- registre tempo e passos;
- verifique objetos/contagens;
- documente falhas e correções.

### Semana 3 — monitoramento e desempenho

- crie carga sintética;
- capture baseline;
- identifique consulta lenta;
- revise plano de execução;
- teste melhoria;
- compare evidência antes/depois.

### Semana 4 — mudança e portfólio

- crie pequena migração de schema;
- escreva prechecks, execução, validação e rollback;
- remova segredos/dados privados;
- escreva README;
- pesquise vagas atuais DBA/Database Technician/Cloud Database;
- compare requisitos com o próximo objetivo de aprendizagem.

## Títulos de vaga para pesquisar

- Database Administrator;
- DBA;
- Junior Database Administrator;
- Database Technician;
- SQL Server DBA;
- Oracle DBA;
- PostgreSQL DBA;
- MySQL DBA;
- Cloud Database Administrator;
- Database Support Engineer;
- Database Operations Engineer;
- Database Reliability Engineer;
- Data Platform Administrator;
- Database Analyst.

## Perguntas para um empregador

Considere perguntar:

- Quais plataformas e versões estão no escopo?
- Qual porcentagem é on-premises versus cloud gerenciado?
- Quais são as expectativas de on-call?
- Como contas privilegiadas são administradas?
- MFA é exigido para administração?
- Com que frequência restaurações são testadas?
- RPO/RTO estão documentados?
- Quem é responsável pela configuração de segurança do banco?
- Como patches e mudanças de schema são aprovados?
- Existe janela de manutenção definida?
- Qual plataforma de monitoramento/alerta é usada?
- Como segredos são armazenados?
- Automação está versionada e revisada?
- O que diferencia responsabilidade júnior e sênior?
- Que apoio de treinamento/certificação existe?

## Links de verificação

Verifique valores e disponibilidade de programas antes de decisões importantes.

### Estados Unidos

- O*NET Database Administrators: https://www.onetonline.org/link/details/15-1242.00
- O*NET salários nacionais: https://www.onetonline.org/link/localwages/15-1242.00
- O*NET tendências nacionais: https://www.onetonline.org/link/localtrends/15-1242.00
- O*NET tecnologias atuais: https://www.onetonline.org/link/hot_tech/15-1242.00
- CareerOneStop WIOA: https://www.careeronestop.org/LocalHelp/EmploymentAndTraining/find-WIOA-training-programs.aspx
- Apprenticeship.gov: https://www.apprenticeship.gov/
- Indeed contexto salarial DBA: https://www.indeed.com/career/database-administrator/salaries

### Canadá

- Job Bank resumo DBA: https://www.jobbank.gc.ca/marketreport/summary-occupation/17875/ca
- Job Bank requisitos DBA: https://www.jobbank.gc.ca/marketreport/requirements/17875/ca
- Job Bank salários DBA: https://www.jobbank.gc.ca/marketreport/wages-occupation/17875/ca
- Canada training gateway: https://www.canada.ca/en/services/jobs/training.html

### Colômbia

- OCUPACOL CUOC 25210: https://ocupacol.mintrabajo.gov.co/Profile/OccupationalProfile/25210
- SENA Implementación y gestión de bases de datos: https://betowa.sena.edu.co/oferta/implementacion-y-gestion-de-bases-de-datos?modality=P&offertype=open&programId=178214
- SENA Bases de datos generalidades: https://betowa.sena.edu.co/oferta/bases-de-datos-generalidades-y-sistemas-de-gestion?modality=V&offertype=open&programId=73885

### Regional, segurança, IA e acessibilidade

- OIT/Cinterfor: https://www.oitcinterfor.org/statsfp/paises
- CISA Secure Our World: https://www.cisa.gov/secure-our-world
- NIST Cybersecurity Framework: https://www.nist.gov/cyberframework
- NIST Privacy Framework: https://www.nist.gov/privacy-framework
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- Section 508: https://www.section508.gov/create/
- WCAG 2.2: https://www.w3.org/TR/WCAG22/

## Aviso importante

Este guia oferece informações gerais para educação e planejamento de carreira. Não garante emprego, renda, admissão, financiamento, colocação em aprendizagem, certificação, promoção ou qualquer outro resultado. Mapeamentos ocupacionais são comparações e requisitos variam por empregador e jurisdição. Salários, tecnologias, programas e condições mudam ao longo do tempo.

Este guia não fornece aconselhamento jurídico, de privacidade, cibersegurança, contabilidade ou aconselhamento profissional específico de fornecedor e não certifica independentemente que qualquer sistema seja seguro, recuperável, conforme ou acessível.

## Autor e assistência de IA

Criado e dirigido por **Alberto “Al” Leiva**. O ChatGPT apoiou pesquisa, organização, edição, suporte à tradução e preparação documental sob direção do autor. O autor permanece responsável pelas decisões editoriais e de publicação.

## Licença

Salvo indicação em contrário, este material é licenciado sob **CC BY-NC-SA 4.0**.
