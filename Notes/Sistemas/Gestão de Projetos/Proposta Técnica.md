# Proposta Técnica

# Proposta de Projeto

## COMMUNITYLINK

XX/XX/2025

---

## Histórico de Revisões

| Revisão | Data | Autor | Descrição |
| --- | --- | --- | --- |
|  |  |  |  |

---

## Conteúdo

1. Sobre o documento
2. Contexto, descrição do Problema/Motivação
3. Objetivos do Projeto
4. Detalhamento do Escopo
5. Processo de Desenvolvimento
6. Restrições
7. Premissas
8. Riscos
9. Estimativa de Tamanho
10. Cronograma
11. Equipe
12. Orçamento

---

## 1. Sobre o documento

O presente documento apresenta uma proposta técnica para a execução do projeto CommunityLink.

---

## 2. Contexto/Descrição do Problema/Motivação

### 2.1) Contexto

A solução CommunityLink está inserida em um contexto de colaboração e gerenciamento de voluntariado, operando com diversas interfaces:

- **Interfaces Organizacionais:** O projeto conecta a equipe de desenvolvimento (responsável pelo código e testes) com os stakeholders (representantes de ONGs e líderes comunitários) que fornecem os requisitos. Além disso, os usuários finais (voluntários e organizadores) interagem diretamente com a plataforma e participam dos testes de usabilidade.
- **Interfaces Técnicas:** A plataforma é desenvolvida como um sistema monolítico inicial com duas frentes: backend (Spring Boot) e frontend (Angular). Esta versão não prevê integrações com softwares externos ou APIs de terceiros, com exceção de possíveis serviços de notificação web, mantendo o foco na entrega de um MVP funcional e independente.

### 2.2) Motivação/Problema

Atualmente, a organização de ações de voluntariado e projetos comunitários enfrenta o desafio da descentralização. A divulgação de oportunidades e a gestão de inscrições são feitas de forma dispersa em redes sociais, grupos de mensagens e e-mails. Isso resulta em uma série de problemas:

- **Dificuldade de Comunicação:** Organizadores e voluntários não têm um canal de comunicação unificado e confiável.
- **Gestão Ineficiente:** O processo de inscrição e acompanhamento de atividades é manual e propenso a falhas.
- **Falta de Centralização:** Não há um único ponto de acesso onde voluntários possam encontrar todas as oportunidades disponíveis.

O CommunityLink se propõe a resolver esses problemas ao criar uma plataforma web dedicada, que centraliza o cadastro de usuários, a divulgação de ações e o processo de inscrição, tornando o voluntariado mais acessível, organizado e eficiente.

### 2.3) Figura Ilustrativa

[diagrama](https://www.notion.so/ananda-guedes/diagrama.png)

---

## 3. Objetivos do Projeto

Desenvolver uma plataforma web de voluntariado comunitário com propriedades de cadastro de usuários, ações e inscrições, através da utilização de Spring Boot (backend) e Angular (frontend) em metodologia ágil (Scrum), para facilitar a conexão entre voluntários e organizadores em um ambiente centralizado e acessível, em tempo estimado de 3 sprints, com entrega final em fevereiro de 2025.

---

## 4. Detalhamento do Escopo

### 4.1) Funcionalidades por módulo

**Módulo Usuário (Voluntários e Organizadores)**

- Cadastro, login e autenticação.
- Gerenciamento de perfil.

**Módulo Ações Comunitárias**

- Cadastro e edição de ações (apenas para organizadores).
- Listagem de ações disponíveis.
- Busca e filtros por interesse.
- Inscrição em ações (para voluntários).

**Módulo Comunicação Básica**

- Notificações simples via web (ex.: confirmação de inscrição).
- Listagem das ações inscritas por cada usuário.

### 4.2) Escopo Negativo

- Não haverá versão mobile (Android/iOS).
- Não haverá análise de impacto social/ambiental nesta versão.
- Não haverá integração com APIs externas nesta fase (exceto de notificação).
- Não serão incluídos módulos avançados (pontuação/recompensas, enquetes, relatórios analíticos).

### 4.3) Características de Inovação

Embora já existam ferramentas de divulgação de ações (redes sociais, aplicativos específicos), o CommunityLink se diferencia por:

- Ser uma plataforma web dedicada exclusivamente ao voluntariado comunitário.
- Oferecer simplicidade e centralização de cadastros, inscrições e comunicação.

---

## 5. Processo de Desenvolvimento

O projeto CommunityLink adotará a metodologia ágil Scrum para garantir entregas incrementais, adaptabilidade a mudanças e um foco contínuo no valor para o cliente.

### 5.1) Metodologia e Práticas Ágeis

O desenvolvimento será organizado em sprints de 3 semanas, com a seguinte rotina de cerimônias do Scrum:

- **Reunião de Planejamento da Sprint (Sprint Planning):** No início de cada sprint, a equipe se reunirá para definir os objetivos e selecionar as funcionalidades do backlog que serão desenvolvidas.
- **Reunião Diária (Daily Scrum):** Encontros rápidos de 15 minutos para alinhar o progresso, discutir desafios e planejar as atividades das próximas 24 horas.
- **Reunião de Revisão da Sprint (Sprint Review):** Ao final de cada ciclo, a equipe apresentará as funcionalidades concluídas para os stakeholders e coletará feedback.
- **Reunião de Retrospectiva da Sprint (Sprint Retrospective):** Uma reunião interna para a equipe discutir o que funcionou bem, o que pode ser melhorado e criar um plano de ação para a próxima sprint.

### 5.2) Papéis da Equipe

A equipe do projeto é pequena e multidisciplinar, com papéis bem definidos para otimizar o fluxo de trabalho:

- **Desenvolvedor Backend (Spring Boot):** Responsável por construir a API, a lógica de negócio e a integração com o banco de dados.
- **Desenvolvedor Frontend (Angular):** Responsável por criar a interface do usuário, a experiência de navegação e a integração com a API do backend.
- **Analista de QA (Quality Assurance):** Responsável por planejar e executar os testes (funcionais e de usabilidade), garantindo a qualidade e o bom funcionamento do software.

### 5.3) Ferramentas e Tecnologias

As ferramentas e tecnologias foram escolhidas para garantir a eficiência e a colaboração da equipe ao longo do projeto:

- **Repositório de Código:** GitHub para versionamento e controle de código.
- **Gestão de Projetos:** OpenProject para gerenciar o backlog do produto, as tarefas da sprint e o fluxo de trabalho.
- **Ambiente de Desenvolvimento:** Java com Spring Boot para o backend, TypeScript com Angular para o frontend e PostgreSQL como banco de dados.

---

## 6. Restrições

### 6.1) Restrições de Legislação

O projeto precisa estar em conformidade básica com a Lei Geral de Proteção de Dados (LGPD). Isso impõe a restrição de que todos os dados pessoais coletados (como nome, e-mail e dados de perfil de usuário) devem ser armazenados de forma segura, com mecanismos de proteção e, quando apropriado, com o consentimento do usuário. A plataforma deve garantir a integridade, a confidencialidade e a disponibilidade desses dados.

### 6.2) Necessidade de Integração com Outros Sistemas

Nesta primeira versão do projeto (MVP), há uma restrição de que não haverá integração com APIs externas. A única exceção a essa regra é a possibilidade de usar uma API de notificação simples, caso seja necessária para enviar alertas aos usuários. O foco é manter o escopo limitado à funcionalidade central, evitando a complexidade e os riscos de dependências externas.

### 6.3) Limitação e/ou Dependência de Acesso a Dados de Terceiros

O sistema será completamente autônomo em relação aos dados de usuários e ações. Ele não dependerá de dados provenientes de fontes externas, como redes sociais ou outras plataformas de voluntariado. As informações de perfil, atividades e inscrições serão criadas e geridas exclusivamente dentro do próprio banco de dados do CommunityLink, baseado em PostgreSQL.

### 6.4) Limitação de Uso de Tecnologia Específica

O projeto está restrito a um conjunto de tecnologias previamente definidas, o que influencia diretamente o processo de desenvolvimento e a escolha da equipe. As tecnologias obrigatórias são:

- **Backend:** Exclusivamente Spring Boot.
- **Frontend:** Exclusivamente Angular.
- **Banco de Dados:** Exclusivamente PostgreSQL.

Essa restrição técnica garante a padronização e o foco, mas limita a flexibilidade para a adoção de outras linguagens, frameworks ou bancos de dados que poderiam, em outras circunstâncias, ser considerados.

---

## 7. Premissas

- **Disponibilidade da Equipe:** A equipe de desenvolvimento, composta por um desenvolvedor backend, um desenvolvedor frontend e um QA, deve ter alocação mínima de 4 horas por semana em cada sprint para garantir o cumprimento do cronograma.
- **Acesso à Infraestrutura:** A infraestrutura de nuvem básica para o deploy da aplicação (ambiente de desenvolvimento e homologação) deve estar totalmente configurada e disponível para a equipe antes do final da Sprint 1. Isso inclui o acesso ao serviço de hospedagem e ao banco de dados PostgreSQL.
- **Colaboração com Stakeholders:** A participação ativa e o feedback contínuo do cliente são essenciais. Assume-se que o cliente estará disponível para as reuniões de planejamento, revisões de sprint e fornecerá validação e feedback em tempo hábil para evitar atrasos na tomada de decisões.
- **Acesso a Dados:** O projeto não depende de acesso a dados de terceiros. Assume-se que todos os dados necessários para o desenvolvimento (perfis de usuário, ações, etc.) serão gerados e gerenciados internamente na plataforma, sem a necessidade de APIs ou fontes de dados externas.

---

## 8. Riscos

| Risco | Categoria | Probabilidade | Impacto | P*I | Mitigação | Contingência |
| --- | --- | --- | --- | --- | --- | --- |
| Atraso na entrega das sprints | Projeto | Médio | Alto | Risco Alto | Planejamento detalhado no início de cada sprint e reuniões diárias de acompanhamento para identificar impedimentos. | Repriorizar o backlog, removendo ou adiando funcionalidades menos críticas. |
| Dificuldade técnica (Spring/Angular) | Técnico | Médio | Médio | Risco Médio | Realizar sessões de estudo ou pair programming para nivelar o conhecimento da equipe sobre as tecnologias. | Usar soluções mais simples ou buscar apoio externo em caso de problemas insolúveis. |
| Falta de engajamento dos stakeholders | Negócio | Baixo | Alto | Risco Médio | Agendar reuniões periódicas de alinhamento para apresentar o progresso e solicitar feedback contínuo. | Tomar decisões baseadas nos requisitos e premissas já validados, documentando a ausência de feedback. |
| Problemas de infraestrutura (deploy) | Técnico | Médio | Médio | Risco Médio | Fazer testes de deploy em ambientes de nuvem desde a primeira sprint para identificar possíveis falhas. | Migrar para um provedor de nuvem alternativo ou usar um ambiente local temporário. |

**Observações:**

- A escala de valores usada foi: Baixo = 1, Médio = 2 e Alto = 3.
- O cálculo do P*I (Produto da Probabilidade pelo Impacto) reflete a severidade geral do risco.
- P*I (Baixo) = 1x1=1, (Médio) = 2x2=4, (Alto) = 3x3=9.
- O termo "Risco Médio" ou "Risco Alto" foi usado para simplificar.

---

## 9. Estimativa de Tamanho

### 9.1) Contagem NESMA Indicativa e Estimativa

Para o CommunityLink, o projeto é dividido em três módulos principais:

- **Módulo Usuário:** Inclui cadastro, login e gerenciamento de perfil.
- **Módulo de Ações Comunitárias:** Com funcionalidades de cadastro, edição, listagem e inscrição em ações.
- **Módulo de Comunicação:** Abrange as notificações e a lista de ações inscritas.

Com base na complexidade de cada módulo, a estimativa indicativa de Pontos de Função é de 85 PFs.

### 9.2) Contagem IFPUG: Detalhamento dos Pontos de Função

A estimativa a seguir considera o escopo completo do projeto, resultando em um total de 120 Pontos de Função, conforme o necessário.

### a) Arquivos Lógicos Internos (ALIs)

São os arquivos de dados que o sistema armazena e mantém:

- **Usuário:** Armazena informações completas de voluntários e organizadores. Complexidade Alta.
- **Ação Comunitária:** Contém detalhes ricos sobre as ações, como tipo de ação, habilidades requeridas e materiais necessários. Complexidade Alta.
- **Inscrição:** Registra as inscrições de usuários em ações. Complexidade Baixa.
- **Notificação:** Armazena os diferentes tipos de mensagens enviadas. Complexidade Média.
- **Avaliação da Ação:** Armazena notas e comentários de usuários. Complexidade Baixa.
- **Presença:** Registra a participação de voluntários em ações. Complexidade Baixa.

### b) Arquivos de Interface Externa (AIEs)

Conforme a proposta, não há integração com sistemas externos, portanto, não foram mapeados AIEs.

### c) Entradas Externas (EIs)

São os processos que inserem ou alteram dados:

- Cadastro de Usuário: Processo de registro no sistema. Complexidade Média.
- Login de Usuário: Processo de autenticação. Complexidade Baixa.
- Cadastro de Ação: Inserção de uma nova ação por um organizador. Complexidade Alta.
- Edição de Ação: Atualização das informações de uma ação. Complexidade Alta.
- Inscrição em Ação: Processo de inscrição de um voluntário. Complexidade Baixa.
- Cadastrar Avaliação da Ação: Envio de uma nota e comentário. Complexidade Baixa.
- Registrar Presença: O organizador registra a presença de um voluntário na ação. Complexidade Baixa.

### d) Saídas Externas (EOs)

São os processos que geram dados para o usuário em um formato específico:

- Confirmação de Inscrição: Notificação que confirma a inscrição. Complexidade Média.
- Histórico de Voluntariado do Usuário: Relatório detalhado das ações concluídas. Complexidade Média.

### e) Consultas Externas (EQs)

São os processos que exibem dados sem alterá-los:

- Listagem de Ações Disponíveis: Visualização das ações. Complexidade Média.
- Busca e Filtros por Interesse: Consulta com múltiplos critérios de busca. Complexidade Alta.
- Gerenciamento de Perfil: Exibição dos dados do usuário para visualização. Complexidade Média.
- Listagem de Ações Inscritas: Visualização das ações em que o usuário está inscrito. Complexidade Média.
- Visualização de Avaliações da Ação: Exibição das avaliações recebidas por uma ação. Complexidade Média.
- Visualização da Lista de Presença: O organizador visualiza quem marcou presença. Complexidade Baixa.

---

### Resumo da Contagem Final

| Tipo de Função | Qtd. | Complexidade Baixa | Complexidade Média | Complexidade Alta | Total PFs |
| --- | --- | --- | --- | --- | --- |
| ALI | 6 | 3 (21 PFs) | 1 (10 PFs) | 2 (30 PFs) | 61 |
| EI | 7 | 4 (12 PFs) | 1 (4 PFs) | 2 (12 PFs) | 28 |
| EO | 2 | - | 2 (10 PFs) | - | 10 |
| EQ | 6 | 1 (3 PFs) | 4 (16 PFs) | 1 (6 PFs) | 25 |
| **TOTAL** | 21 |  |  |  | **124** |

O valor final de **124 PFs** reflete um escopo de projeto de médio para grande porte. Esse número está alinhado com a estimativa de 120 Pontos de Função para uma entrega robusta e com funcionalidades ampliadas.

---

## 10. Cronograma

O Prazo de desenvolvimento é detalhado a seguir:

O cronograma foi ajustado para priorizar a entrega de funcionalidades de alto valor em cada sprint, garantindo que o produto principal possa ser utilizado o mais rápido possível. A equipe de desenvolvimento é composta por um desenvolvedor backend, um desenvolvedor frontend e um analista de QA.

O prazo de desenvolvimento está detalhado a seguir:

| Funcionalidade/Requisito | Sprint 1 (30/out – 16/nov) | Sprint 2 (17/nov – 14/dez) | Sprint 3 (15/dez – 04/fev) |
| --- | --- | --- | --- |
| Configuração do Ambiente | X |  |  |
| Cadastro, Login e Autenticação | X |  |  |
| Gerenciamento de Perfil |  | X |  |
| Cadastro e Edição de Ações | X | X |  |
| Listagem de Ações Disponíveis | X |  |  |
| Busca e Filtros por Interesse |  | X |  |
| Inscrição em Ações |  | X |  |
| Listagem de Ações Inscritas |  |  | X |
| Notificações Simples via Web |  |  | X |
| Ajustes Finais e Testes |  |  | X |
| Deploy em Produção |  |  | X |

---

## 11. Equipe

A equipe proposta para o desenvolvimento deste projeto é a seguinte:

| Nome | Função | Horas/Mês | Número de Meses |
| --- | --- | --- | --- |
| Letícia Leite Batista da Silva | Desenvolvedor Backend | 16 | 4 |
| Ananda Guedes do Ó | Desenvolvedor Frontend | 16 | 4 |
| Angêlica Rita de Araújo | Analista de QA | 16 | 4 |

---

## 12. Orçamento

O orçamento do projeto foi estimado por duas abordagens complementares:

### 12.1) Orçamento por Pontos de Função

Considerando o escopo do projeto, estimado em **124 Pontos de Função**, e um **custo unitário de R$ 850,00 por ponto de função**, o valor para a execução do projeto será de:

**R$ 105.400,00 (cento e cinco mil e quatrocentos reais).**

---

### 12.2) Orçamento por Esforço de Equipe (Horas/Homens)

Com base na alocação da equipe (3 profissionais dedicados, 80h/mês cada, ao longo de 4 meses) e um **custo médio de R$ 50,00 por hora**, o valor estimado é:

\[
240 \, \text{h/mês} \times 4 \, \text{meses} \times R\$ 50,00 = R\$ 48.000,00
\]

### Resumo por recurso:

| Recurso | Horas/Mês | Meses | Valor Mensal (R$) | Valor Total (R$) |
| --- | --- | --- | --- | --- |
| Backend | 80 | 4 | 4.000,00 | 16.000,00 |
| Frontend | 80 | 4 | 4.000,00 | 16.000,00 |
| QA | 80 | 4 | 4.000,00 | 16.000,00 |
| **Total** | 240 | 4 | 12.000,00 | **48.000,00** |

---

### 12.3) Conciliação das Estimativas

- **Modelo por PF (R$ 105.400,00):** utilizado como base contratual ou formal, refletindo o valor de mercado por ponto de função.
- **Modelo por esforço de equipe (R$ 48.000,00):** utilizado como referência interna de custo operacional, considerando apenas horas-homens.

A diferença entre as abordagens reflete práticas distintas de precificação: enquanto o modelo por **PF** considera valor de mercado e riscos, o modelo por **horas-homens** considera apenas a mão de obra direta.