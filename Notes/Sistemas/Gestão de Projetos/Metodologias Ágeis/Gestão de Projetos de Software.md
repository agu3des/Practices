# Gestão de Projetos de Software

- **1. Plano de Gerenciamento de Integração e Stakeholders**
    
    ## Plano de Gerenciamento de Integração e Stakeholders
    
    ### Integração no Projeto (PMBOK + Scrum)
    
    A integração será feita por meio da atuação ativa da **Coordenadora de Projeto**, que atuará como *Product Owner*, sendo responsável por consolidar as entregas das equipes e garantir a coerência do produto com os objetivos estratégicos. Ela será o elo entre o time ágil e os stakeholders, promovendo uma visão unificada do progresso.
    
    O gerenciamento da integração será contínuo, com:
    
    - **Revisões de Sprint** ao final de cada iteração, funcionando como checkpoints de integração entre o que foi desenvolvido e o planejamento do projeto.
    - **Daily Scrum** como ferramenta para antecipar problemas e alinhar rapidamente ações que impactam mais de uma frente de trabalho.
    - **Backlog Refinement** como momento de integrar novas demandas, sugestões ou mudanças de escopo com impacto mínimo.
    
    Ferramentas como Asana serão utilizadas para integrar atividades de backend, frontend e prototipação de forma sincronizada.
    
    ---
    
    ### Engajamento dos Stakeholders
    
    O engajamento será guiado por práticas do PMBOK aplicadas de forma leve e iterativa:
    
    1. **Identificação e Classificação**:
        - Stakeholders mapeados: Defesa Civil, ONGs, doadores, comunidades afetadas, governo local, pesquisadores.
        - Classificados com base em **poder** e **influência** (matriz poder-interesse).
        
        [https://www.figma.com/board/2JUjIOj4CbBqID1PbHav5N/Impact-vs.-Effort-%7C-Action-Prioritization-Matrix-Template--Community-?node-id=0-1&t=dRww3gs5ebh5knBX-1](https://www.figma.com/board/2JUjIOj4CbBqID1PbHav5N/Impact-vs.-Effort-%7C-Action-Prioritization-Matrix-Template--Community-?node-id=0-1&t=dRww3gs5ebh5knBX-1)
        
        Obs: Influência = capacidade de impactar decisões do projeto ; Interesse = nível de envolvimento, preocupação ou afetação com o projeto.
        
        | **Stakeholder** | **Poder** | **Interesse** | **Classificação na Matriz** | **Ação Recomendada** |
        | --- | --- | --- | --- | --- |
        | Defesa Civil e Corpo de Bombeiros | Alto | Alto | Gerenciar de perto | Reuniões frequentes, atualizações diretas |
        | ONGs e instituições filantrópicas | Alto | Alto | Gerenciar de perto | Parcerias formais, comunicação ativa |
        | Governo municipal/estadual | Alto | Médio | Manter satisfeito | Relatórios estratégicos, envolvimento político/institucional |
        | Doadores e voluntários | Médio | Alto | Manter informado | Notificações, relatórios transparentes, UX clara |
        | Comunidades afetadas | Baixo | Alto | Manter informado | Interface acessível, comunicação direta |
        | Universidades e pesquisadores | Baixo | Médio | Monitorar com esforço mínimo | Publicação de dados, abertura da base de dados |
        | Equipe de desenvolvimento (interna) | Médio | Alto | Gerenciar de perto | Reuniões ágeis, definição de tarefas e entregas |
        | Coordenadora de Projeto | Alto | Alto | Gerenciar de perto | Responsável pela integração entre todos os stakeholders |
    2. **Planejamento de Engajamento**:
        - Canais de comunicação definidos: reuniões semanais com parceiros-chave, e-mail e atualizações em plataforma colaborativa (como Asana ou GitHub).
        - Atualizações visuais serão compartilhadas com stakeholders estratégicos.
    3. **Gerenciamento e Monitoramento Contínuo**:
        - Feedbacks coletados ao fim de cada sprint.
        - Adequações de escopo e backlog baseadas em sugestões dos stakeholders.
        - Testes de usabilidade com comunidades e voluntários para validação das funcionalidades.
    
    ---
    
    ### Justificativa da Abordagem Integrada
    
    A união do **PMBOK** (foco em controle e planejamento) com o **Scrum** (foco em agilidade e entrega iterativa) assegura a qualidade do produto final e o alinhamento com as reais necessidades das comunidades afetadas. Essa abordagem híbrida promove flexibilidade para inovação e robustez para lidar com a complexidade e urgência dos desastres naturais.
    
    ---
    
- **2. Product Backlog (Escopo)**
    
    **Produto Backlog**
    
    →R01. Banco de Dados Relacional Estruturado
    
    1. O sistema deve utilizar um banco de dados relacional com estrutura robusta.
    2. As tabelas devem ser inter-relacionadas para representar entidades como: Desastre Natural, ONGs, Voluntários.
    
    →R02. Interface Web Responsiva e Intuitiva
    
    1. O sistema deve possuir uma interface web acessível por dispositivos móveis e desktops.
    2. A usabilidade deve ser pensada para operadores em campo, cidadãos e gestores, mesmo em situações de instabilidade de conexão.
    
    →R03. Sistema de Cadastro e Consulta de Desastres e Voluntários
    
    1. O sistema deve permitir o cadastro e a consulta de desastres e voluntários.
    2. Deve haver formulários simples e diretos para envio de relatos por cidadãos.
    3. Deve ser possível anexar mídias (fotos).
    
    →R04. Informações sobre o Portal
    
    1. O sistema deve ter uma página explicando as principais funcionalidades da plataforma
    2. O sistema deve ter uma página exibindo as ONGs/Abrigos verificados e seus contatos
    3. O sistema deve ter uma página de contato para quem quiser fazer doações ou anúncios na plataforma
    
    →R05. Disponibilidade e Escalabilidade
    
    1. A infraestrutura deve ser capaz de lidar com picos de acesso.
    2. O sistema deve contar com backups e replicação de dados.
    3. A arquitetura deve estar preparada para escalabilidade horizontal
    
    →RNF01. Plano de Gerenciamento de Integração e Stakeholders
    
    →RNF02. Plano de Gerenciamento de Tempo
    
    →RNF03. Plano de Gerenciamento de Recursos
    
    →RNF04. Plano de Gerenciamento de Qualidade
    
    →RNF05. Plano de Gerenciamento de Comunicação
    
    →RNF06. Plano de Gerenciamento de Aquisição
    
    →RNF07. Plano de Gerenciamento de Custos
    
    →RNF08. Plano de Gerenciamento de Riscos
    
    - Feito [Última atualização 13/08/2025]:
    
    R01: Database de desastres naturais (Sprint 2), Database de voluntários (Sprint 3), Database de ONGs (Sprint 4)
    
    R02: Interface Web (Sprint 2)
    
    R03: CRUD de desastres naturais (Sprint 2), CRUD de voluntários (Sprint 3)
    
    R04: a fazer na Sprint 5
    
    R05: -
    
    RNF01: ok
    
    RNF02: ok
    
    RNF03: ok
    
    RNF04: ok
    
    RNF05: ok (Sprint 4)
    
    RNF06: ok (Sprint 4)
    
    RNF07: a fazer na Sprint 5
    
    RNF08: a fazer na Sprint 5
    
- **3. Sprint 2 backlog**
    1. Criação do protótipo no figma
    2. Criação do banco de dados com a entidade desastres naturais
    3. Criação do CRUD de desastres no front
    4. Criação do CRUD de desastres no back
    5. Integração do back com o front
    6. Elaboração do Plano de Gerenciamento de Integração e Stakeholders (base PMBOK + Scrum)
    7. Elaboração do Plano de Gerenciamento de Tempo
- **4. Plano de Gerenciamento de Tempo**
    
    Apesar de o Scrum ser flexível, ele pode se beneficiar dos fundamentos do PMBOK para dar **mais estrutura ao gerenciamento de prazos**. Veja como integrar:
    
    ### **Integrações possíveis:**
    
    | **Prática do PMBOK** | **Adaptação no Scrum** |
    | --- | --- |
    | Planejar o cronograma | Planejamento do **Product Backlog** e do **Sprint Planning** |
    | Definir/Sequenciar atividades | Itens do backlog priorizados e organizados para cada sprint |
    | Estimar duração e recursos | Estimativas com **Planning Poker** ou story points por sprint |
    | Desenvolver cronograma | **Gráfico de Gantt, Burndown charts** ou **Release Plans** para visualização do progresso |
    | Controlar o cronograma | **Daily Scrum** para ajustes diários e **Sprint Review/Retrospective** para melhoria contínua |
    
    ### **Aplicação no Projeto de GPS (Gestão de Projetos de Software):**
    
    - **Definir**:
        - Criar um **Backlog do Produto** com todas as funcionalidades.
        - Realizar **planejamento das sprints** com estimativas de esforço (story points ou planning poker).
        - Utilizar ferramentas como Asana para organizar e visualizar prazos.
    - **Controlar**:
        - Realizar **Daily Scrum** para acompanhar o andamento.
        - Usar **gráficos** para monitorar o ritmo de entrega e ajustar o planejamento.
    - **Validar**:
        - Executar **reviews ao final de cada sprint** com os stakeholders.
        - Avaliar se os itens entregues estão dentro do prazo e conforme os critérios de aceitação.
    
    Essa integração garante que o cronograma seja **flexível**, porém **controlado**, e que o projeto se mantenha dentro dos **limites de tempo definidos**.
    
- **5. Plano de Gerenciamento de Recursos**
    
    No contexto da aplicação Disaster, todos os eventos scrum estão sendo considerados e aplicados a este orçamento. 
    
    OBS: Os valores seriam conversados e acordados em contrato com as partes interessadas, tanto a equipe quanto com os stakeholders. A reserva técnica estaria disponível ao começo de cada sprint (proporcional a sprint), caso fosse necessário usá-la. Caso não seja, o valor permaneceria em caixa.
    
    - Duração de 1 ano.
    - Equipe composta por 3 desenvolvedores back-end (em que um indivíduo também atua como Scrum Master) e 2 desenvolvedores front-end (em que um indivíduo também atua como Product Owner), todos contratados como Pessoa Jurídica (PJ) em formato remoto.
    - Custo de um designer UX/UI e testes de usabilidade.
    - Recursos técnicos, incluindo registro de domínio internacional e hospedagem da plataforma.
    - Reserva técnica de 30% para possíveis extensões de período de trabalho.
    
    ## **Recursos Humanos**
    
    ### Desenvolvedores Back-End
    
    - Quantidade: 3 profissionais
    - Salário médio mensal por profissional: R$ 7.100
    - Total anual para 3 profissionais: R$ 255.600
    
    *Fonte: Glassdoor ([https://www.glassdoor.com.br/Sal%C3%A1rios/brasil-desenvolvedor-back-end-pleno-sal%C3%A1rio-SRCH_IL.0%2C6_IN36_KO7%2C35.htm](https://www.glassdoor.com.br/Sal%C3%A1rios/brasil-desenvolvedor-back-end-pleno-sal%C3%A1rio-SRCH_IL.0%2C6_IN36_KO7%2C35.htm))*
    
    ### Desenvolvedores Front-End
    
    - Quantidade: 2 profissionais
    - Salário médio mensal por profissional: R$ 5.000
    - Total anual para 2 profissionais: R$ 120.000
    
    *Fonte: Glassdoor ([https://www.glassdoor.com.br/Sal%C3%A1rios/desenvolvedor-front-end-pleno-sal%C3%A1rio-SRCH_KO0%2C29.htm](https://www.glassdoor.com.br/Sal%C3%A1rios/desenvolvedor-front-end-pleno-sal%C3%A1rio-SRCH_KO0%2C29.htm))*
    
    ### Adicional para Scrum Master
    
    - Profissional: 1 dos desenvolvedores back-end
    - Adicional mensal estimado: R$ 1.800
    - Total anual: R$ 21.600
    
    ### Adicional para Product Owner
    
    - Profissional: 1 dos desenvolvedores front-end
    - Adicional mensal estimado: R$ 1.500
    - Total anual: R$ 18.000
    
    ### Designer UX/UI e Testes de Usabilidade
    
    - Custo total estimado: R$ 8.000
    
    *Estimativa baseada em valores de mercado para serviços de design freelance no Brasil.*
    
    ## **Recursos Técnicos**
    
    ### Registro de Domínio Internacional (.com)
    
    - Custo anual: R$ 50
    
    *Fonte: Registro.br ([https://registro.br/](https://registro.br/))*
    
    ### Hospedagem da Plataforma
    
    - Serviço de hospedagem em nuvem (AWS, Azure, Google Cloud):
        - Custo mensal estimado: R$ 500
        - Custo anual estimado: R$ 6.000
    
    *Fonte: Estimativas baseadas em calculadoras de preços das respectivas plataformas.*
    
    ## **Custo por Sprint**
    
    Considerando que:
    
    - As sprints têm duração de 3 semanas.
    - O projeto terá 17 sprints ao longo de 1 ano (51 semanas).
    
    ### **Custo por Sprint**
    
    - **Custo total anual (sem reserva)**: R$ 429.250
    - **Custo por sprint**: R$ 429.250 / 17 ≈ R$ 25.250
    
    ## **Observações**
    
    - **Reserva Técnica**: Inclui uma margem de 30% sobre o subtotal para cobrir possíveis extensões de prazo, ajustes de escopo e contingências, conforme recomendado pelas práticas do PMBOK.
    - **Modelo de Contratação PJ**: Embora profissionais PJ não estejam sujeitos aos encargos trabalhistas tradicionais, é prudente considerar possíveis custos adicionais, como benefícios ou bonificações, que podem ser negociados individualmente.
    - **Gerenciamento Ágil**: A alocação e o acompanhamento dos recursos humanos serão realizados por meio de cerimônias do Scrum (Sprint Planning, Daily Scrum, Sprint Review e Retrospective), garantindo alinhamento contínuo com os objetivos do projeto.
    
    ![image.png](Gest%C3%A3o%20de%20Projetos%20de%20Software%202802e5a697c380ae9547c5e874604b0a/image.png)
    
- **6. Plano de Gerenciamento de Qualidade**
    
    A **qualidade pode ser estruturada** da seguinte forma:
    
    | **Etapa** | **Como aplicar no Scrum para o projeto** |
    | --- | --- |
    | **Planejar Qualidade** | • Definir métricas e Critérios de aceite: dados corretos, interface funcional em dispositivos móveis e desktop.                                     |
    | **Garantir Qualidade** | • Revisões semanais do backlog com Product Owner e especialistas para validar conteúdo e dados; • Pair review de código; • Auditoria de segurança em integrações de pagamentos (e.g., Pix, PayPal). |
    | **Controlar Qualidade** | • Testes de performance simulando alta demanda ; • Verificação contínua de SEO, acessibilidade e responsividade mobile; • Aplicar reteste em bugs, pequenas mudanças já dentro da Sprint. |
    
    ### **Como isso contribui para o Plano de Gerenciamento de Qualidade:**
    
    - **Clareza dos padrões**: métricas definidas (planejamento).
    - **Processos ativos**: revisão de trabalho e auditoria (garantia).
    - **Feedback e ajuste contínuo**: testes e correções constantes (controle).
- **7. Sprint 3 backlog**
    
    Sprint Backlog:
    
    1. Criação de banco de dados no Firebase para a entidade Voluntários
    2. Criação do CRUD de voluntários no front
    3. Integração do Firebase com o front
    4. Pesquisa sobre o Plano de Gerenciamento de Recursos
    5. Elaboração do Plano de Gerenciamento de Recursos
    6. Pesquisa sobre o Plano de Gerenciamento de Qualidade
    7. Elaboração do Plano de Gerenciamento de Qualidade
    
    DOD da Sprint: Quando a aplicação estiver fazendo o CRUD da entidade Voluntários
    
- **8. Sprint 4 backlog**
    
    Sprint Backlog:
    
    1. Criação de banco de dados no Firebase para a entidade ONGs
    2. Criação do CRUD de ONGs no front
    3. Criação do CRUD de ONGs no back
    4. Elaborar Plano de gerenciamento de comunicação
    5. Elaborar Plano de gerenciamento de aquisição
    
    DOD da Sprint: Quando a aplicação estiver fazendo o CRUD da entidade ONGs
    
- **9. Plano de Gerenciamento de Comunicação**
    
    O objetivo deste Plano de Gerenciamento de Comunicação é estabelecer um fluxo de informações claro, conciso e eficaz para o projeto da plataforma Disaster, garantindo o alinhamento de todos os stakeholders, conforme a abordagem híbrida PMBOK e Scrum.
    
    ### Canais e Ferramentas Padrão
    
    - **Reuniões:** Daily Scrum, Sprint Planning/Review/Retrospective, Reuniões com Parceiros-Chave.
    - **Plataformas Colaborativas:** Asana (gestão de tarefas), GitHub (código).
    - **E-mail:** Para comunicações formais e suporte.
    - **Interface da Plataforma Web:** Notificações, painéis, páginas informativas.
    - **Documentação:** Notion para armazenamento de informações técnicas e guias.
    
    ### Responsabilidades
    
    - **Coordenadora de Projeto (Product Owner):** Ponto focal para stakeholders externos, consolida relatórios, traduz feedback, lidera cerimônias Scrum (planejamento, revisão).
    - **Scrum Master:** Facilita cerimônias Scrum, remove impedimentos, garante a comunicação interna da equipe.
    - **Equipe de Desenvolvimento:** Comunica status e impedimentos diariamente, participa de todas as cerimônias Scrum.
    - **Designer UX/UI:** Comunica progresso de protótipos e resultados de testes de usabilidade.
    
    ### Processo de Escalada
    
    Problemas de comunicação ou conflitos serão escalados sequencialmente:
    
    1. **Internos (equipe):** Daily Scrum / Retrospective. Se persistir, Scrum Master.
    2. **Com Stakeholders:** Coordenadora de Projeto.
    3. **Maiores/Altos Riscos:** Liderança superior ou reunião formal com stakeholders envolvidos.
    
    ### Monitoramento e Controle
    
    A eficácia da comunicação será continuamente avaliada através de:
    
    - **Feedback:** Coletado em Sprint Reviews e Retrospectives.
    - **Métricas de Engajamento:** Participação em reuniões, uso de plataformas.
    - **Avaliação de Satisfação dos Stakeholders:** Implementação de pesquisas periódicas focadas nos stakeholders-chave para coletar dados qualitativos sobre a satisfação com a comunicação e a percepção do projeto.
    
    ### Requisitos e Conteúdo da Comunicação por Stakeholder
    
    | **Stakeholder** | **O que comunicar (foco)** | **Frequência (padrão)** | **Responsável Principal** | **Canais Principais** |
    | --- | --- | --- | --- | --- |
    | Defesa Civil e Corpo de Bombeiros | Progresso, funcionalidades operacionais, dados e impactos. | Semanal/Conforme Necessidade | Coordenadora de Projeto | Reuniões, E-mail, Painel na Plataforma |
    | ONGs e instituições filantrópicas | Funcionalidades de apoio, métricas de engajamento, oportunidades. | Semanal/Conforme Necessidade | Coordenadora de Projeto | Reuniões, E-mail, Notificações na Plataforma |
    | Governo municipal/estadual | Progresso estratégico, alinhamento com políticas, escalabilidade. | Mensal/Trimestral	 | Coordenadora de Projeto | Relatórios, Apresentações |
    | Doadores e voluntários | Impacto do uso da plataforma, progresso transparente, novas funcionalidades | Quinzenal/Mensal	 | Coordenadora de Projeto | E-mail  |
    | Comunidades afetadas | Guias de uso, notícias de resposta, recursos disponíveis. | Conforme Necessidade | Coordenadora de Projeto | Interface da Plataforma, E-mail (suporte) |
    | Universidades e pesquisadores | Dados Consolidados e protegidos, impacto social do projeto. | Conforme Necessidade	 | Coordenadora de Projeto | Publicação de Dados, E-mail |
    | Equipe de desenvolvimento (interna) | Status de tarefas, impedimentos, definições técnicas, feedback do PO. | Diário (Daily Scrum), Sprint | Scrum Master / Equipe | Asana, GitHub, Reuniões Scrum |
    | Coordenadora de Projeto | Visibilidade total do projeto, riscos, feedback, alinhamento estratégico. | Diário/Semanal	 | Coordenadora de Projeto | Asana, Reuniões Scrum, Relatórios Internos |
- **10. Plano de Gerenciamento de Aquisição**
    
    O objetivo deste plano de Gerenciamento de Aquisição é estabelecer diretrizes, critérios e estratégias para aquisição de recursos e serviços necessários à execução do projeto **Disaster**, garantindo qualidade, cumprimento de prazos, otimização de custos e alinhamento com os valores do projeto e com os princípios do Scrum e do PMBOK.
    
    ## **1. Planejar o Gerenciamento das Aquisições**
    
    | **Item/Serviço** | **Descrição** |
    | --- | --- |
    | Serviços de profissionais PJ | Desenvolvedores back-end, front-end, Scrum Master e Product Owner (equipe PJ remota). |
    | Serviços de Designer UX/UI | Design de interfaces e condução de testes de usabilidade. |
    | Registro de Domínio Internacional | Registro do domínio “.com” para a plataforma. |
    | Hospedagem em Nuvem | AWS, Azure ou Google Cloud, conforme análise técnica. |
    | Reserva Técnica | 30% de margem para contingências. |
    
    ### **1.1 O que será adquirido**
    
    ### **1.2 Quantidade e duração**
    
    - **Profissionais PJ**: Contratação de 5 desenvolvedores (3 back-end e 2 front-end) pelo período de 12 meses.
    - **Designer UX/UI**: Contratação pontual (curto prazo), com valor fixo estimado.
    - **Serviços Técnicos**: Registro e hospedagem para o período de 1 ano, com possibilidade de renovação.
    
    ### **1.3 Estratégia de aquisição**
    
    - Modelo **Pessoa Jurídica (PJ)** para contratação de profissionais, com valores definidos em contrato.
    - Seleção de designer e serviços técnicos via **RFP (Request for Proposal)** e análise de portfólio e custo-benefício.
    - Critérios para escolha de hospedagem: custo, escalabilidade, segurança e suporte.
    - Reserva técnica alocada no início de cada sprint (proporcional), permanecendo em caixa se não utilizada.
    
    ### **1.4 Critérios de Seleção de Fornecedores**
    
    - Experiência comprovada no tipo de serviço;
    - Portfólio e cases relacionados;
    - Custo compatível com o orçamento estimado;
    - Disponibilidade no modelo remoto;
    - Conformidade com as necessidades do projeto e aderência às cerimônias ágeis;
    - Reputação e referências (para serviços de terceiros como hospedagem e domínio).
    
    ### **1.5 Documentos de apoio**
    
    - Termo de Abertura do Projeto (TAP);
    - Plano de Gerenciamento de Recursos;
    - Plano de Qualidade;
    - Plano de Comunicação;
    - Cronograma de Sprints (17 sprints em 12 meses).
    
    ## **2. Conduzir as Aquisições**
    
    ### **2.1 Processo**
    
    - Divulgação de demanda via plataformas profissionais (LinkedIn, Workana, etc.) e por RFP para serviços pontuais (designer, hospedagem).
    - Recebimento e avaliação de propostas por equipe multidisciplinar (Product Owner, Scrum Master, membros técnicos).
    - Negociação de prazos, custos, entregas e adicionais contratuais.
    - Formalização contratual com cláusulas sobre escopo, prazo, entregas, responsabilidades, sigilo e pagamento.
    
    ### **2.2 Integração com outras áreas**
    
    - **Escopo e requisitos**: Os contratos serão baseados nas histórias de usuário e funcionalidades priorizadas no backlog.
    - **Riscos**: Cláusulas contratuais incluirão penalidades e condições para ajustes em caso de risco.
    - **Custos**: Alinhamento com o orçamento de R$ 429.250, mais reserva técnica.
    - **Comunicação**: Canais definidos (e-mail, reuniões, plataformas) serão usados também com fornecedores.
    
    ## **3. Controlar as Aquisições**
    
    ### **3.1 Monitoramento**
    
    - Acompanhamento semanal da performance dos contratados por meio das cerimônias do Scrum (Daily, Review, Retrospective).
    - Registro de entregas e pagamentos no Notion (documentação) e Asana (controle de tarefas).
    - Verificação técnica dos entregáveis (código, design, desempenho da hospedagem).
    - Aplicação de testes, validações e pair reviews com base no plano de qualidade.
    
    ### **3.2 Indicadores e ações**
    
    | **Indicador** | **Método de Avaliação** |
    | --- | --- |
    | Entregas no prazo | Comparação backlog planejado vs. entregue por sprint |
    | Qualidade técnica | Testes, código limpo, ausência de retrabalho |
    | Disponibilidade dos serviços | Uptime da hospedagem, tempo de resposta do suporte |
    | Satisfação do cliente interno | Feedback em reuniões e retrospectives |
    
    ### **3.3 Ações corretivas**
    
    - Reuniões extraordinárias com contratados em caso de desvios.
    - Ativação de cláusulas de ajuste contratual.
    - Redistribuição de backlog ou acionamento da reserva técnica para compensar falhas.
    
    ## **4. Encerrar as Aquisições**
    
    ### **4.1 Atividades de encerramento**
    
    - Verificação e aceitação formal de todas as entregas.
    - Revisão de contratos, conferência de pagamentos e arquivamento dos documentos.
    - Avaliação de desempenho dos contratados (técnica e comportamental).
    - Liberação de pagamentos finais e encerramento administrativo.
    - Atualização do repositório de lições aprendidas no Notion.
    
    ### **4.2 Responsáveis**
    
    - **Product Owner**: Validação e aceite de entregas, contato com stakeholders externos.
    - **Scrum Master**: Verificação de cumprimento dos processos internos, reporte de desempenho.
    - **Equipe de Aquisições/Financeira (se houver)**: Fechamento legal e contábil dos contratos.
    
- **11. Sprint 5 backlog**
    
    Sprint Backlog:
    
    1. Criação da página de contato para quem quiser fazer doações ou anúncios na plataforma
    2. Criação da página explicando as principais funcionalidades da plataforma
    3. Elaborar Plano de gerenciamento de riscos
    4. Elaborar Plano de gerenciamento de custos
    
    DOD da Sprint: Quando a aplicação contiver todas as informações sobre o Disaster
    
- **12. Plano de Gerenciamento de Custos**
    
    O presente plano tem como objetivo definir os processos, ferramentas e critérios utilizados para estimar, orçar e controlar os custos do projeto **Disaster**, garantindo que seja concluído dentro do orçamento aprovado, alinhado às práticas do **PMBOK** e integrado à abordagem ágil **Scrum** utilizada pela equipe.
    
    ## **1. Objetivos**
    
    - Estabelecer a metodologia de estimativa de custos.
    - Determinar a composição do orçamento total do projeto.
    - Definir procedimentos de controle e monitoramento de custos por sprint.
    - Fornecer subsídios para tomada de decisão em relação ao uso da **reserva técnica (30%)**.
    
    ## **2. Estrutura dos Custos do Projeto**
    
    ### **2.1 Recursos Humanos**
    
    - Desenvolvedores Back-End (3): R$ 255.600/ano
    - Desenvolvedores Front-End (2): R$ 120.000/ano
    - Scrum Master (adicional): R$ 21.600/ano
    - Product Owner (adicional): R$ 18.000/ano
    - Designer UX/UI e testes: R$ 8.000
    
    **Subtotal Recursos Humanos:** **R$ 423.200**
    
    ### **2.2 Recursos Técnicos**
    
    - Registro de domínio internacional: R$ 50/ano
    - Hospedagem em nuvem: R$ 6.000/ano
    
    **Subtotal Recursos Técnicos:** **R$ 6.050**
    
    ### **2.3 Custo Total do Projeto (sem reserva)**
    
    **R$ 429.250**
    
    ### **2.4 Reserva Técnica (30%)**
    
    **R$ 128.775**
    
    ### **2.5 Orçamento Total do Projeto**
    
    **R$ 558.025**
    
    ## **3. Processo de Estimativa de Custos**
    
    As estimativas de custos foram realizadas com base em:
    
    - **Dados históricos de mercado** (Glassdoor, Registro.br, AWS/Azure).
    - **Analogias** com projetos semelhantes em desenvolvimento web.
    - **Estimativas paramétricas**, considerando salários médios e custos técnicos fixos.
    - **Opinião especializada** da equipe e stakeholders.
    
    ## **4. Orçamento**
    
    - O orçamento será distribuído ao longo das **17 sprints** (3 semanas cada).
    - O custo médio por sprint será de aproximadamente **R$ 25.250** (sem reserva).
    - A reserva técnica de 30% será **alocada proporcionalmente por sprint**, disponível em caixa no início de cada ciclo.
    
    ## **5. Controle de Custos**
    
    O controle será realizado de forma contínua e integrado às cerimônias do **Scrum**.
    
    ### **5.1 Indicadores**
    
    - **Planned Value (PV):** custo planejado para cada sprint.
    - **Earned Value (EV):** valor agregado conforme entregas concluídas no backlog.
    - **Actual Cost (AC):** custo real incorrido por sprint.
    - **CPI (Cost Performance Index):** EV/AC, indicador de eficiência de custos.
    - **SPI (Schedule Performance Index):** EV/PV, indicador de eficiência de prazos.
    
    ### **5.2 Procedimentos**
    
    - Revisão de custos ao final de cada sprint (Sprint Review).
    - Ajuste de previsão para sprints futuras em caso de variação significativa.
    - Utilização da reserva técnica apenas com aprovação do **Product Owner** e ciência do **Scrum Master**.
    - Registro dos custos e status financeiro no **Notion/Asana** junto ao backlog.
    
    ## **6. Relatórios**
    
    - **Relatório de Custos por Sprint:** comparando planejado x real.
    - **Relatório Mensal de Custos:** consolidando o desempenho financeiro.
    - **Relatório Final:** comparativo entre orçamento planejado, executado e utilização da reserva.
    
    ## **7. Premissas**
    
    - Profissionais contratados como **PJ remoto** por 12 meses.
    - Custos de infraestrutura permanecem estáveis ao longo do período.
    - Não foram incluídos encargos trabalhistas devido ao modelo PJ.
    - Reserva técnica cobre possíveis **mudanças de escopo, extensão de prazo ou riscos**.
    
    ## **9. Restrições**
    
    - O orçamento máximo aprovado é de **R$ 558.025**.
    - O uso da reserva técnica exige justificativa formal e aprovação do Product Owner.
    - Custos não previstos fora da reserva não serão cobertos pelo projeto.
    
    ## **10. Responsabilidades**
    
    - **Product Owner:** aprovar uso da reserva, validar relatórios financeiros.
    - **Scrum Master:** monitorar custos junto ao progresso das sprints.
    - **Equipe:** registrar horas e entregas que impactam nos custos.
    - **Stakeholders:** acompanhar relatórios financeiros mensais.
- **13. Plano de Gerenciamento de Riscos**
    
    O objetivo deste plano é identificar, analisar, planejar respostas e monitorar os riscos que podem impactar negativamente o projeto, garantindo que a equipe esteja preparada para lidar com imprevistos de forma proativa.
    
    ### **1. Identificação e Análise de Riscos**
    
    Os riscos foram mapeados e classificados de acordo com sua **probabilidade** (a chance de ocorrer) e **impacto** (o efeito caso ocorra), utilizando uma escala de Baixo, Médio e Alto.
    
    | **Risco** | **Probabilidade** | **Impacto** | **Classificação** |
    | --- | --- | --- | --- |
    | Atraso na entrega de funcionalidades | Médio | Alto | Alto |
    | Dificuldade na comunicação com a equipe remota | Médio | Médio | Médio |
    | Instabilidade da conexão em áreas de desastre | Alto | Alto | Alto |
    | Mudanças de escopo tardias (após a sprint) | Médio | Alto | Alto |
    | Aumento inesperado de custos (infraestrutura, salários) | Baixo | Alto | Médio |
    | Falta de engajamento de stakeholders-chave | Médio | Médio | Médio |
    | Vazamento de dados sensíveis | Baixo | Alto | Médio |
    | Recursos técnicos (servidor/domínio) não atendem à demanda | Baixo | Alto | Médio |
    | Problemas de integração entre back-end e front-end | Alto | Médio | Alto |
    
    ### **2. Planejamento das Respostas aos Riscos**
    
    Para cada risco de alta ou média classificação, uma resposta específica foi definida.
    
    - **Risco: Atraso na entrega de funcionalidades.**
        - **Resposta:** Monitoramento diário do progresso no Daily Scrum. Se um item atrasar, o Scrum Master deve atuar para remover impedimentos. O Product Owner pode renegociar o escopo da sprint ou mover o item para uma sprint futura.
    - **Risco: Dificuldade na comunicação com a equipe remota.**
        - **Resposta:** Utilizar ferramentas colaborativas como o Asana e o Slack/Teams para comunicação em tempo real. Realizar videochamadas regulares e reforçar a importância do Daily Scrum para alinhamento.
    - **Risco: Instabilidade da conexão em áreas de desastre.**
        - **Resposta:** Desenvolver a interface web para ser leve e responsiva, com recursos de modo offline. O design deve priorizar a usabilidade mesmo com baixa largura de banda.
    - **Risco: Mudanças de escopo tardias.**
        - **Resposta:** As mudanças serão coletadas e priorizadas na revisão de backlog (Backlog Refinement), no início de cada sprint, com a participação dos stakeholders. O Product Owner é responsável por comunicar o impacto e garantir que as mudanças estejam alinhadas com os objetivos do projeto.
    - **Risco: Aumento inesperado de custos.**
        - **Resposta:** Utilizar a reserva técnica de 30% do orçamento. Qualquer uso da reserva deve ser aprovado pelo Product Owner, com a devida justificativa, e o impacto nos custos futuros será monitorado no Plano de Gerenciamento de Custos.
    - **Risco: Falta de engajamento de stakeholders-chave.**
        - **Resposta:** A Coordenadora de Projeto (Product Owner) deve agendar reuniões de alinhamento com os stakeholders de "alto poder/interesse" e enviar relatórios visuais de progresso, conforme definido no Plano de Gerenciamento de Comunicação.
    - **Risco: Problemas de integração entre back-end e front-end.**
        - **Resposta:** Realizar integração e testes contínuos ao longo da sprint. A comunicação entre as equipes de desenvolvimento será reforçada no Daily Scrum, para que os problemas sejam identificados e resolvidos rapidamente.
    - **Risco: Recursos técnicos não atendem à demanda.**
        - **Resposta:** A arquitetura da plataforma será pensada para ser escalável. A equipe de desenvolvimento fará testes de performance antes do lançamento oficial, garantindo que o servidor suporte picos de acesso.
    
    ### **3. Monitoramento e Controle de Riscos**
    
    O gerenciamento de riscos é um processo contínuo no projeto.
    
    - **Daily Scrum:** A equipe deve discutir rapidamente os impedimentos e riscos que surgem diariamente, garantindo uma resposta rápida.
    - **Sprint Review e Retrospective:** Avaliação dos riscos que se materializaram ou que foram evitados. Lições aprendidas serão registradas para aprimorar a gestão de riscos nas próximas sprints.
    - **Product Owner:** Responsável por revisar os riscos de maior impacto com os stakeholders e garantir que o planejamento de respostas esteja em andamento.