# BD1

**INTRODUÇÃO:**

→ Dados: manter informação, associação

→ Hoje é visto como questão monetária, a partir do conhecimento e manipulação desses.

→ SQL = principal linguagem utilizada, simples, não é de programação é uma linguagem de quarta geração (você diz o que quer e ela faz)

→ Persistência de dados,

→ Base de dados amarradas ao programa

→ Utilizando o projeto de Ape:

1º Quais dados  precisam ser armazenados? matriz, pontuação → Modelagem Conceitual: BrModelo

[](https://lh7-us.googleusercontent.com/icuCTYTX8vHPqbPWKJwXuTGRJKuX_YAOUeuV1Umkj3j-pwN7xomuR7hDpb74k_EDsECbPf5XcSfdb5yO6iXzIQ-vji6q2SiWiwGoEqIUMxuIIz4svA5nTKv58BCbcg7r9aGiFtwdTjvQ58pfIOG8r7Y)

2º Como armazená-los? Binário, txt → Modelagem Lógica relacional (tabelas relacionadas): MySQL Workbench

3º Implementação? Python → SGBD (gerencia vários bancos de dados): MySQL

→ Abstração: qual informação eu vou precisar, o que interessa para o conceito que estou aplicando, ex. comida preferida -x-> suap

**CONCEITOS BÁSICOS:**

→Dado: fato bruto / valor armazenado no computador

José dos Anzóis |  Computec  |  32222222  |   P2345

→Informação: o significado que o dado possui

José dos Anzóis é cliente da empresa Computec.

José dos Anzóis tem o telefone 32222222.

José dos Anzóis fez o pedido de código P2345.

→ Dados podem estar relacionados e formarem uma informação

→ Informações não conflitantes: um mesmo dado pode fornecer informações diferentes e estas não chocam-se entre si.

José dos Anzóis é o cliente que mais compra na empresa Computec.

José dos Anzóis é o cliente que mais deve na empresa Computec.

→ Informações conflitantes: as informações se chocam

José dos Anzóis reside na Rua Verde, no 234.

José dos Anzóis reside na Rua Azul, no 456.

→Conhecimento: conjunto de informações, nas quais se pode ter uma análise acerca destas. Um novo conhecimento pode ser formado a partir desses conhecimentos prévios

Modelagem: é um processo de abstração → captura a realidade e pega apenas o que é relevante para o contexto → depende mais do observador do que a realidade observada → selecionar os dados relevantes para um banco de dados e suas propriedades

→Dados  isolados: problemas de redundância e inconsistência

- Em alguns casos a redundância é necessária, ex. o cadastro dos usuários da google em uma só base e se cair um avião?

[](https://lh7-us.googleusercontent.com/fH_4CVoguPe3mShDRfwl9viL5Cpxq2GdpE0yoTu32ti9Q8Sl3Hw4Ol4WeX9p-kTtAJPyAhOibDkIdOg4fXofA_xIXsOtWpSkQ_5BOYu_AMPZWmf7IV871YuBDGOJO9z80qmFio5Vb1f_mvtG9lN1bW8)

→Dados compartilhados: cada dado é armazenado uma vez, compartilhado entre vários usuários, não há redundância

[](https://lh7-us.googleusercontent.com/M1_o8dkUFYnQmZ6Fuzn6BTNBnTniTaOX3L1dXUWFLs0obGXBJXKGu0Eq6j8k5SVtWAoIgDGRn22DLyQLLumoQZDfnOJb9ZEKacPtbZ-i4_HsCB9vpIm0EGRSt_JbyMAsfx4Ipvrc-VaLuysKF_-U6jw)

→Controlada: um software gerencia a repetição de forma automática e mantém sincronismo entre as modificações desses dados.

→Não Controlada: o gerenciamento da repetição é feito de forma manual por um usuário e não por um software, possibilitando uma grande possibilidade de redundância.

BANCO DE DADOS

→conjunto de dados relacionados e compartilhados que atende a um ou vários usuários.

→dados armazenados de forma lógica (tabela, dicionário, tags) e estruturada (informação de cada campo)

→Regra de negócio: os dados devem refleti-la, de algum ambiente de modo que representem seu estado real

→Dinâmica: consistência, integridade e seguranças nativas

→SGBD: é o software que vai permitir inserir os dados, gerenciando os bancos de dados

- Descrever e definir os dados, construir o banco de dados, armazenar, consultar e compartilhar dados, dar segurança e integridade aos dados.

→ Sistema de banco de dados: Envolve o banco de dados, o hardware, as aplicações, os seus usuários e o SGBD

- O usuário de um banco de dados/de um software pode ser outro software, usuário mesmo (direto com o próprio SGBD)
- Criação e manutenção das aplicações é facilitada
- Permite visões: você vê algo filtrado
- Natureza autodescritiva: dicionário, metadados (dados sobre dados)
- Isolamento entre programas e dados: abstração de

[](https://lh7-us.googleusercontent.com/XzOQGDUJAXhI7Kwr-8skUAfVx9kv-LPODzbZdvw9bNx6Yxo4PkDV-__TS71Scsq3fEwO3da-bjCkvkWuJHDsOMgqQakjon4fZQiUdelydzdQzHWJcSsIOUGDkbPMG-ohEzQ_8QAtMTkTOSc341Mrauk)

Usuários:

- Projetistas de banco de dados (projeto/engenharia reversa)
- Administradores de banco de dados
- Analista de sistemas
- Programadores de aplicação
- Gestores e diretores (análise de dados BI)
- Usuários Finais

Vantagens do BD

- Padronização de acesso;
- Eliminação/controle da redundância;
- Compartilhamento de dados;;
- Segurança de acesso e auditoria;
- Backup e recuperação dos dados;
- Múltiplas interfaces para o usuário;
- Restrições de integridade;
- Crescimento sustentável;
- Isolamento entre dados e aplicações;
- Rapidez no acesso.

**Modelo de Dados:**

- É uma abstração da realidade de representar a estrutura do banco de dados a partir de regras definidas.
- Permite descrever = dados (disciplina, aluno, professor), relacionamentos (professor ensina a disciplina para o aluno), semântica (o que significa) e as regras de consistência entre os dados (se só se pede 3 números, devem ser apenas esses três).

Modelo Entidade-Relacionamento: abstrair infos;

Modelo Relacional: como os dados serão armazenados, em qual formato será armazenado;

Modelo Orientado a Objetos: diagramas que orientam classes formadas de objetos

Modelo Objeto-Relacional: híbrido, tanto com tabelas ou objetos ou ambos juntos.

**Esquema do Banco de Dados:**

- A representação abstrata e simplificada de uma realidade, que descreve um banco de dados segundo um modelo de dados. São dados sobre dados, ou seja, metadados.

[](https://lh7-us.googleusercontent.com/xomImKJCwqTXKABd9GaQ4L2-MJ8zO7L3j14cV3u68wgUfsU2W2gJXwy4Vo6khrSvQ93x2QHLeoNyHQtD5jDACYAWe5Pj6SG6pTjGQ9ly-9xtDq6dLjSW5CYshP17zj8uqNDYUDx5iWtIKiUIl7G8sfo)

[](https://lh7-us.googleusercontent.com/810a-A6ZPRPv-Bl6ihV8L0q8b9MH1xM73hOzHpW2eQcwRQSzyYBBbg33Q47a3GyOOeGLS_24iWUoAv25A_nhtF_3wFfPW2VqQbcdYHQ1xf8UdMuTz9y8XbxlV95Xx10J1ZOQAlSRnUv2_dbpZzAPiaI)

1º esquema externo: determinar quais dados são mais importantes para aplicação e como se relacionam / abstrai / descreve a visão que cada usuário terá do banco de dados

2º esquema conceitual: qual a solução eu vou dar para a resolução esse problema / modela / descreve os dados e as associações entre eles

3º esquema interno:  implementa / Descreve como os dados estão realmente armazenados.

**Independência de Dados:**

- Modificar um nível de abstração sem afetar a

definição do nível mais alto.

- Independência física de dados: modificar o esquema físico sem a necessidade de reescrever os programas aplicativos. Ocasionadas por necessidade de melhoria no desempenho.
- Independência lógica de dados: modificar o esquema conceitual sem a necessidade de reescrever os programas aplicativos. Ocorrem quando a estrutura do banco de dados é alterada, como por exemplo, para a inclusão de novos tipos de dados. É mais difícil de ser alcançada.

[](https://lh7-us.googleusercontent.com/YcoNLtBnQkq1u9NEfvUiys55E6xsJdBz-hWooTbzwyBfgVhlj3FMr3fm899GE3lewsLl7YwD0Gj02JKRxmEAEQSq_SPVoBSIsb_2e6tDTFSrPbLj3xJc0DszVxhgnVv6na-qQqInXPiA2kqJwyApfbs)

utilizar brmodelo, tabelas(relacional) e sgbd

- - ifpb (realidade)

0 - biblioteca (as infos coletadas)  |  1 - abstração (quais os dados)

2 -  solução (representar, tabelas)  |  3 - codificar (relacional)

**MODELO CONCEITUAL:**

- O modelo conceitual é construído a partir do minimundo, não podem estar separados. Se tem no modelo tem que ter no minimundo, ou seja, acrescentar.
- Modelo Entidade-Relacionamento

Relacionamento → Entidade → Atributos

Ex:

[](https://lh7-us.googleusercontent.com/BEQYUXT40onUVqiFzt0t67wuPAr9_6iZz01ZNSJXFXb3UxfVGVv4In4geNSffI2T3Y3QlRpBBfmWKgEj2HduDdf0JTmuGiMhIZN7_7_JVLy9PeQMXI9trTTW2eZtM9ksiBb71Jj7fh_DhcqREFFqZXI)

Um cliente não faz ou faz ‘n’ pedidos / um pedido é feito por um cliente

- Modelo semântico representado por uma linguagem gráfica para construir modelos conceituais de bancos de dados.
- Conjunto de três elementos: entidade (conceito de classe), atributo e relacionamento.

Entidade:

- Existem no mundo real e necessitam ser representados, podem ser concretos ou abstratos e representam dados genéricos do sistema.
- Elemento → de uma entidade → formado → conjunto de valores → ocorrência ou instância
- Ocorrências devem ser identificadas de forma única através dos valores armazenados nos seus atributos

[](https://lh7-us.googleusercontent.com/UHgJFNFDTYQqtNQByvnUtzcjDpEgZhS3X7W6a8r4b9s7qGMwWr9oxYL1c47rJNzUD48-1rBEpeG_g7eaGBwd3RO3s2dwJSs8IBuEpTlh6gb33dc9x9FHs6YsTIEejKH88Vkjlq2jfY9JaEYBcdjkoOg)

- Podem representar:
- Objetos concretos (uma pessoa, um produto).
- Objetos abstratos (um setor, um curso).
- Papéis desempenhados (um médico, um cliente)
- Eventos que acontecem (um pedido, uma locação).
- Entidade Fraca: estão sempre relacionadas (identificador) com outra entidade (entidade identificadora)

só consigo identificar uma entidade se houver outra que a identifique, existindo assim uma relação de dependência

[](https://lh7-us.googleusercontent.com/xNLRj2l0-H7VEznIPk8uABuW76E46dWBBPa6CXC6qWzr11yYy1ggIN4qoac9cZeikT3KK-PIP-73dKB1YN8Ltq5DicVPe3QGhwBFK0umKxXF_mv1mtegKPySXRlpmFdf5Typ9ell6sDBPjgR0qFdM3g)

empregado - entidade identificadora

possui - relacionamento identificador (pois apenas a partir desse relacionamento a entidade ocorre)

dependente - entidade fraca

[](https://lh7-us.googleusercontent.com/I5v9WkxbOGxVNlLi81pFpqPz7sRWU8utpziq2MB716qU_0RW0yFL5DYda0Al8Efypd2MF0pphJKZgDX_vEG9FzCL73WPlAI30HXpuVFcudrir8o15l742fOztGTi3KEAwUxmHpvtcR5R_i7lH_IVe5U)

[](https://lh7-us.googleusercontent.com/3diAhk33A7y1PdCUrt0Uv_hNyB0G4DG9dx6VKdcRe3XxOXdYzvLhv7Jpp9PSCyx9mFoIJBmWQjuZ9xZ4htMYbAN8204dmR7qxQBMaRZAOgen6y2aD3lo0S-e2MRwXxwrLlcjmLtm6lJso2MYmqYiwaE)

trio identificador

[](https://lh7-us.googleusercontent.com/I0qRc_eC60zwQo5gTrvHwKw38JpkEO2ImlB83YKCwJZmDQOxl5dsgcM67Pm-m0j0tcsmq5bJh8rDAlfrZKTavMqP4PGX_z3Lj8y8gLkPIOpXyp17ZYvDNLGW660E4PfcEfajnho85VXdm7C8mbobrGE)

[](https://lh7-us.googleusercontent.com/FtjBLuneEHUWoTDfhNZ1dDI_z8Go5rTDUhg_K3XHuV8PumN7mvMPiNXuZSvlEgqwRUajbtPNxPT4owbGt1Qh2zph1yUP0XQ3gCJ_kyJjBYpm5CBo1FTOcfTn08oonf0xH-ku8mfLoTzKGwlts80sr34)

[](https://lh7-us.googleusercontent.com/dbPp3TwOSV20Il_JFcKKQ-R0DmRJO3tg5ESbxcq6v_CdNjJh-U_bE6HhyciQfUmcXryJpvgVVPf0GuF4-XS_tJm4IHGTgqjeRLA_U1O0xM3qtlIe-esehH6eFrkGdVRy0qFMlrkMW9133lk39PG0nq0)

relacionamento ternário - participação de todas é obrigatória / todos funcionam em torno de um relacionamento

- Entidade Associativa; quando um relação é de n para n

[](https://lh7-us.googleusercontent.com/lgQG1YupAID_bbiVAIwkXwyTxxI8CM_B5MH9ILcxOG3sGScX5OBtlR3mv0hOY7bO5QufDLxiROxZp93HXbSWEoPXXt1pn9fj04B-pl0LnDDJReVV93Crsmb5F6zSkZs3J_C-KYxAk8vS79FJ1tKHq7c)

[](https://lh7-us.googleusercontent.com/1ynmeUaBAHaGzkfUiG5-qvVQIu9FPlsF6s4PC2-LQX5-8FHhpDS8HX93LgNh8MiNA0dOeD0Nxm_pYTM711wCWm9dIWl1OBSP4lCn2_9bxcQBlOz8Z2cz3qUjf-qAB9QEgrndOtJRSbOosLBAmVkj448)

não existe relacionamento entre relacionamentos

[](https://lh7-us.googleusercontent.com/Z4ow9owKlA7i7cim8Q6m8laF6NWUyMEk2EsbQISmF8349l0lmVJhGNsvkMMyK6-KRHE99VJzXw-8BAMWe2h4uTYv7LXym896NELF0kCGHEZIoOH6uGLv6j1FeMsmIhuYs8QHtibmDGRTKIlIyCauPYg)

nesse caso, consulta é uma entidade associativa

Atributo:

- Características
- Simples: não pode ser dividido / atômico

Ex¹:  entidade: cliente — atributo: bairro, sexo

- Composto: pode ser quebrado em vários outros campos

Ex²: entidade: cliente — atributo: endereço (rua, número, complemento, bairro, cidade, estado, cep)

- Identificador: não admite repetição de valores nem

pode ser deixado em branco.

Ex³: entidade: cliente — atributo: codcliente

- Descritivo: representa uma característica de uma entidade ou de um relacionamento, podendo armazenar valores repetidos.

Ex: entidade: cliente — atributo: fone, endereço, telefone

- Derivado: cujo valor pode ser obtido a partir

do valor de outro atributo.

Ex: entidade: cliente — atributo: idade (derivado a partir da data)

- Monovalorado: só um

Ex: apenas um telefone

- Multivalorado: mais de um

Ex: mais de um telefone

- Cardinalidade: quantidade mínima (=0 → opcional; =1 → obrigatório) e máxima de valores que podem ser definidos para um atributo. Mínima: valor mínimo; Máximo: valor máximo

Se tiver 1 é mono, se n multi

Ex: (0,1) no mínimo nenhuma e no máximo 1

Vai estar no sentido oposto ao que leio

[](https://lh7-us.googleusercontent.com/gVaI8vV4HPsYeZ-2YN8x_bidmhpig3-qYxQwq7aOF486xG28GzJCfN3uWoq5sXC1mOZ82s9G7g--U3LpHkNJQhClanAYkQbAYJXZ0otOqo2cpoNI3tlrSjCgth1lRdmi8lHuoEqXLZQL7qq37ZUgaPA)

Relacionamento:

- Pode possuir atributos

[](https://lh7-us.googleusercontent.com/B9l70IsJlMKEBL4Tv3I2kyv6BkkMTvhWA0mMtjUVTRfgmRC6SJ0PwW452R1cu6bkKHyJd_3CMmSbzjSRk4XOcucQJkPtwteckdj_bjzS4V98V6yRtx5REiASpYWbHg912b05KtTgA6dQHbz5sWV_QOk)

bolinha preta - identificador

- São os dados associados às ocorrências de uma entidade ou um relacionamento

[](https://lh7-us.googleusercontent.com/SX8h_j2tqihuTTpMUraS5rHzfrLyhuq0tFgAyU0v1dodQYySvkRD8JviDV5DTX4fllUVtv49HkzmB78j04fcW9T8SGok0S2uDzQIfZIbRBPfghcw9uODgyBu5FUXsEl9wjFrWtKkkYTltEuoq2CDiqc)

- As entidades se relacionam
- Cada instância de um relacionamento é uma associação de instâncias de entidades

Ex¹:

professor → ensina → + de uma turma

turma → só um professor

aluno → matriculado → + de uma turma

disciplina → + de uma turma

nota → atributo de relacionamento

Cardinalidade:

- Número de instâncias de uma entidade que podem estar associadas a uma instância de outra entidade

[](https://lh7-us.googleusercontent.com/hfPIoLETmMEq-V9kECBBvIUg4hMyWmTEjsxwDzvk6AXIw1HbgvoERB8TUgeqc1fEzT5eGDC3yu63GQibaoZPIpoypPXuvRpvsn8iHgYidQ4CdHCwT8Iym_s-n92dpv_m0Zup2BZuIe2kdv8xupz31vw)

0:N -

1:1 - um-para-um

[](https://lh7-us.googleusercontent.com/vRxg8bbwYMKyRqX4EVV2torZ8CpfmRX4hAqVMgsMT987eFAHvSturF3wtQtMohjSvcdwDBTqlQ5_J8hmaUxFdyIRV_vwE8GlPkndQyMi-9dCmt5U6_ODF8SYNEbT1K0Zi8NEipIuMzszIASjfF0-xa4)

relacionamento estável

1:N - um-para-muitos

[](https://lh7-us.googleusercontent.com/oJT7KOE78h8TG5do3pD97cFKispJKUNfegWlwrZgjUi0Y1aq0hPwtYnV06yfaKb7iPkUtERfCx1JoN5Y7tVq1piqvdwX_AioTwb7C-T69pUNIydi9pssV56kzm3jzOdfUKaqs_Z6qQd9ws-pRGeCtiQ)

um professor leciona para n turmas

um é corno

N:1 - muitos-para-um

n turmas são lecionadas por um professor

N:N - muitos-para-muitos

[](https://lh7-us.googleusercontent.com/xSlBh9Z8EdoGvOfVySSowC1zUaX1ezx2HJ2EXJMPkqzoGUo573726m5wLyxsRw54fqKzQCVzyNTBF6Zyc-xtuBNtnMxu1rr8QtsgaQ2Of-NGl7lxu2AU3dtRUQmYQV3nrtiSNdvvwyALOPkNg2gFUsY)

relacionamento aberto

- Auto-Relacionamento: onde os participantes de um relacionamento são da mesma entidade

[](https://lh7-us.googleusercontent.com/x5kMpv_GzL2ULAkmTaiU1JdoyLI1-bXDiQIqbK5JXCtm-p1XDAnkZyC66-bmzcgzfaAeQ2XKvwzMA-fYPbJ6UdbVQ8gSpAXVlZiZDAn0EHHHVlOeKW3U6G87uN3U51FPnPeyVLXMh6zK5MVXtp8mu58)

→ Generalização/Especialização:

- Uma entidade possui diversos subgrupos que precisam ser representados no BD
- Associar atributos específicos para cada entidade especializada
- Estabelecer relacionamentos específicos entre as entidades especializadas e outras entidades

[](https://lh7-us.googleusercontent.com/0UFSPumjQrrtkbRHeq_OBCQVuZqh_VSRIclKXFi_AtxYh7a4KTxe5MQMYfPT17oq7lyB5xD9OhsfTMWU4p1hd2dS0cWJo_JjDIyNNpyy0niPBvb93x5FXlPHJPHiSOqZSCqRLt6wv5ph7z3Lp2_C1F4)

cliente: possui nome e código, tanto pessoa física como jurídica possuem, o atributo identificador está aqui

pessoa física / pessoa jurídica: é uma subtipagem, além do que eu já tenho, eu adiciono mais atributos, recebem herança de características de ciente

o triângulo significa generalização / de baixo para cima

[](https://lh7-us.googleusercontent.com/t6RyCcbzZdv6qd_dYoj2Lds1LiHS5w2ILhkqcTpeIm3ApiXmqEdpRMFOCjd8lGnXEkFOKGxQxUWMunz54yxUIs06p2F5SLnaW_nzBrDbDOBNws2T8dR9EZKfn1EYDPbbOZPz8_H-IosfRCtRlS4ZuN4)

o triângulo significa especialização / de cima para baixo

pode herdar os relacionamentos

[](https://lh7-us.googleusercontent.com/0dob336s1arXeS3ZLP5yVWqS9K3tXbc4x1aKkHpuTkoS66uGlbSkHoJBiEA21HWFHV-p0EO3oXMR1Ri8KWVa2AUZYP3boILz-46v4GrUvBlbRHd5eksHYN53gsmnedIdzSRmEopI_TWYP8gX_NZlYqA)

Total: ou é isso ou é aquilo

Parcial: pode ser isso, aquilo ou o geral

[](https://lh7-us.googleusercontent.com/SlE9zi1J6lXY2lk36TMqEbXjiHX_e4fq9MjlbmU3pHD-w_8zc0SQ6sXebAMTT0PUCWitHuwGf7w6WcMkTPRAsEYWQuz5d0LuYIp7vIf2pYGp1NXvw_VKbRejjfO9nsul5gkVk4sbmMvyed5lrU1peWk)

Identificador:

- Tem que ser mínimo (se retirar ele deixa de existir)
- Tem que haver unicidade (só tem aquele)

**MODELO LÓGICO:**

→ Bancos de dados relacional = composto de tabelas ou relações

TABELA:

→ Conjunto não ordenado de linhas (tuplas)

→ Armazena dados sobre entidades / relacionamentos

→ Cada linha é composta por uma série de campos (atributos)

→ Esses campos possuem informações referentes a e/r

→  Cada campo tem um nome, esse que é representado no topo (cabeçalho) da tabela

→ Campos homônimos de todas as linhas de uma tabela formam uma coluna

→ Os valores de campo de uma tabela são atômicos e monovalorados

→ As linguagens de consulta permitem acesso por quaisquer critérios

E4 e J4 estão errados

- A obtenção se dá a partir da aplicação de regras de derivação sobre um modelo conceitual de dados já construído / descreve: tipo, tamanho (char e varchar), formato, domínio (só tem aquela quantidade x de coisas), chaves dos dados
- Tipagem estática no sgbd

[](https://lh7-us.googleusercontent.com/143LvAay_k1ABXrjO5x_0o6638nCp7sYCRNi_PUqgr0HbKD3VfJECgAZ7hUW28I-rovuStA4OOeT6JEG4cf6kEb_DYocd0QZGZ7CLegZIMIvfTUGGjZ03HQk4xr5M1Rf4R8aF1zGpxgoYiW1hwfM_fY)

- Quando se relaciona as tabelas diminui a redundância, pois acopla as informações, só é possível no mapa.
- Dados armazenados em tabelas
- A tabela é um conjunto de ocorrências, ex: cada linha corresponde a um curso (código, professores, alunos)
- Cada linha é uma tupla
- Cada coluna → atributos, ex: nome, número, horário
- Operações sobre dados são feitas por uma linguagem não procedural
- Tabelas: conjuntos de tuplas/ocorrências, não posso ter o mesmo nome dentro de um BD
- Precisa definir que tipo de dado ela irá receber e é estático para cada coluna / varia de sgbd / natureza / tamanho
- Tamanho:
- char(11/aceita apenas os 11/-flexível/vai alocando) e varchar(11/aceita 2/flexível/+leve, pois se não usar ele aproveita)
- Os dois para cadeias de caracter
- Domínio de uma coluna:
- Valores possíveis que ela pode assumir
- É estático
- Pode-se criar restrições
- Uma coluna pode ter mais de um modelo para ela
- Conjunto de valores distintos que podem ser definidos a um atributo. Pode ser:
- Domínio Discreto: conjunto de valores distintos, definidos previamente. Ex: dias da semana
- Domínio Contínuo: conjunto de valores permitidos dentro de um intervalo. Ex: salário de 100 - 2000
- Domínio Aberto: conjunto de valores permitidos, sem restrições.
- Domínio Nulo (inaplicável ou desconhecido): é um valor nulo, diferente de zero ou espaço em branco. Ex: null - sem valor, entra nos opcionais
- Chave Primária:
- Corresponde ao identificador
- Não pode ser nula e nem admite valores repetidos
- Nem sempre uma chave primária é apenas uma coluna, pode ser mais de um atributo
- Trabalha com minimamente
- Chave Estrangeira:
- Tem que garantir que a chave estrangeira é primária em algum lugar / tem que ter o mesmo domínio
- Auto-relacionamento com chave estrangeira

[](https://lh7-us.googleusercontent.com/oCM2m7EUpmxPyzroDi_zprrKtOVAKp2pacwiLDlt_3IiM_dYLC07LvxXJ5UpXzz_2FBbqEv_UDL7Gc9oRlhj9MkMiAr9WBroJZ3kXlq0ekmanlrjnnLU7rLM_OnfzeyJoC7W1e1Txy0eYDg8Im2HkfA)

**INTEGRIDADE**

→  Integridade de domínio:

- Especifica que um valor associado a um atributo deve pertencer ao domínio do atributo.

→  Integridade de unicidade:

- Especifica que o valor do campo é único, naquela coluna (não pode haver repetição nas outras linhas do mesmo campo).

→  Integridade de vazio:

- Especifica quais os atributos que podem ser nulos.

→  Integridade Referencial:

- Especifica que os valores de uma chave estrangeira devem estar presentes na chave primária da tabela referenciada.
- Especifica que os relacionamentos devem manter integridade entre as tabelas relacionadas.
- É implementada pela definição das ações:

▪ Inclusão de dados;

▪ Exclusão de dados e:

▪ Alteração de dados.

**MUDANÇA DE DADOS**

→ Inclusão de dados – restrita:

- Impede que seja inserido na chave estrangeira da tabela filho, um valor que não exista previamente na coluna referenciada da tabela pai.

[](https://lh7-us.googleusercontent.com/jXrm0JSWiSbzml-7OzMaF65wNF5aZPX9upB6c6DyYqUPFa_P51sSOqbDUhS_etNVaCXiT-4oM8xDQZYs1Nu3Pr1CS95oREysciGadlG8wwRDuZet8Q2ydGsadryF4sio98zPkGDaslCPj0OpbuiSU9s)

→ Exclusão Restrita:

- Não posso apagar se ele é referencial - exclusão default

[](https://lh7-us.googleusercontent.com/peSAeArlBp4th4e8xdOlXXXsnQcjnDZo6gQSjuPHjHHAISCMoF6kFpTg5weAzcCOCymxGqF4k2XF9Ad4bdb1Ayoydk8GXGRsNc0QIZaL_5z-litI6y5naBg4gOnKN_GBUj6nUqA5VW8KTooIy3cz0_M)

→ Exclusão em Cascata:

- Apago o pai e por conseguinte seus filhos - na hora que for criar as tabelas define se permite a exclusão em cascata

[](https://lh7-us.googleusercontent.com/5ucXLBpn4FgE7hDJuDWSPexwBwgHjTbUkbSo4J_zGaFci5e-Sc5hkjVJjFNevVLJXufA6wevqG48AGVhNd0eCZYPMIFWjpgp7Ta2Vnqa2pP1JgMioCbUpnH6ITzDKM8h6Xw6KwEJclmpDyDXdpeUY3I)

→ Alteração de dados – restrita:

- Tabela pai: Impede que um valor de chave primária seja alterado na tabela pai, se existir algum registro relacionado na tabela filho.,

[](https://lh7-us.googleusercontent.com/GJtY2V0O4sQDYxfilPE0od6Vbq5BIGsf2Paz70MH6zpeERTL7r64ZSjCjKtJDjDgsPDZiOP9EpuMSykf32DQSjl2WFKM49lA9EdSF2oYDROjdJjn7KHTmiNsASsd4hgjkHl0NsIT-aycmn8k90ieMkA)

- Tabela filho: Impede que um valor de chave estrangeira seja alterado na tabela filho, se não existir algum registro com o novo valor na coluna relacionada da tabela pai.

[](https://lh7-us.googleusercontent.com/hEaCrSuySBUqv6wBMDEhBE7fOEdGhq8QUZAEL-S_YPGUyD17MnsJZ7_uTrPM7xK2LKznKxgmusJvDLhR_e8WPv6sW_m6eEsS3pGX4zRnKipqiIbjf0j7nFTs7xUCtGZfaUTJfxVLAQLRzYjki2AhvpE)

→ Alteração de dados – cascata:

- Quando um registro da tabela pai é alterado, todos os registros relacionados a ele, existentes na tabela filho, também são alterados.

[](https://lh7-us.googleusercontent.com/eCc-uk5YDinP7NV3cPWlk2fR8aCxQ0rGRJL17HYPBQQOH21tf7y-li9O580a6c1s69noDKZK37axORdrTUQkFPTAzdRrypmhtFicsZX_9wE7c1v6VPR9VJoH2NPklEKBZ_u7KIcLeyWpMKOtpkHSXiE)

→ Integridade semântica:

- É como um filtro
- Garante que o estado dos dados está sempre de acordo com as regras do negócio.
- É implementada pelas restrições de checagem de dados, pela obrigatoriedade e unicidade do dado e pelos triggers.
- Exemplos de restrições semânticas:

* um funcionário não pode ter o salário superior ao salário do seu chefe imediato.

* a quantidade de um produto em um pedido não pode ser superior à quantidade em estoque desse produto.

* um funcionário do setor de vendas não pode ter a função de engenheiro.

- Exemplos de falta de integridade semântica:

* violação de domínio:  funcionário com 200 anos de idade.

* atributos significativos sem valor: nome do funcionário nulo.

*  relacionamentos incorretos ou inexistentes: um pedido para vários clientes.

**MAPEAMENTO**

**Entidades e Atributos**

[](https://lh7-us.googleusercontent.com/0fPR2Sj-fOMLh9GGJgPiLskFJ-aFEkKwOEZD5CjpmMuynpE4blfEt8O_-a6XDkrGYKor2ipVdtOerCOpXRz4fvac8K49Wlg-L3xPbeVwMFdTAYxVz_lfiKMKW06snNIC1P16nyeoI-8i5NKQ_uiZhww)

[](https://lh7-us.googleusercontent.com/oiiDDSGYkco4nQffQtt79SXa3Ua8kMyEOe5r-BbdHdOmnYaNCUIZ7747bwHZR8pegM6H2knN4bLLuZdC7qwPlc7z8Dv8Q8KXJRVcO1abmSXURDwPLlZpsgBnkpeP5vj21eO-xDJs4C9PIrGvibxH0sY)

- Vermelho é chave estrangeira
- O que tá pra dentro é mínima
- Bolinha aberta é 0, 1 é 1 traço, n são 3 traços

[](https://lh7-us.googleusercontent.com/rTgqTgW01k8XwhSyMq6xTW--3S35TdtBeyYECJ9zfh9TsAecpgCRfBHKwxCAOOgdrexoE2HzfjoJZBzX-bWeKlLxFoXyDfvQHjOb-DiiS4Gy1ZsNJSKO49mH24bvlv36TkyoxYN0mOjlQEtp6MU0QR0)

[](https://lh7-us.googleusercontent.com/5U_9ikBOtJ7H6I7kt8faqG57BGdBpNYX7GLxfmEyVY2hHnsFbp86dzN_uI44sO6_qmCiM0Vap6AnKI7oWuyZafG9ULwZrdl_AaHosGu08JaDVbS5CjTOfTVngFA_xlgQxlKegA9DIfAp37xsMlD-w4A)

- Cada entidade torna-se uma tabela.

*Pode ocorrer, em alguns casos, de algumas entidades se unirem para dar origem a uma única tabela (fusão de tabelas).

- Cada atributo da entidade torna-se uma coluna da tabela criada, com um domínio definido.

*O atributo identificador da entidade torna-se a chave primária da tabela.

*Os atributos compostos e multivalorados deverão ser implementados.

*Os atributos derivados deverão ser excluídos.

*Os atributos referenciais deverão ser exibidos.

- Não ‘se tem’ atributo composto, ele é excluído e seus atributos viram linhas

[](https://lh7-us.googleusercontent.com/0SgFXgl6pUcaTx4iDGn6GmI_nfPG_5zGUNrLyoaOIAlnv9qf_nrkh9XWzwTAMkoUMSIyK-_TCy99K-nqRmwmfBLyiQRTd-npj2wPfbuRRWD-59jUrGHqDYBlgXHo93IWjbfQepf46OqH4GrOU92-VD0)

- Atributo multivalorado vira tabela
- Criada artificialmente, obrigatoriamente toda tabela tem sua chave primária, nesse caso é uma chave primária composta

[](https://lh7-us.googleusercontent.com/8G14hqYmBuH3jqlPlSKh9c4r-hP9_2sh6HpSUjl5dIo2AkD-5zcdrmAt0__Luo-by9ztAX-2txmtquLfIuJ18R2_4NHi-6ALc_Ska9KusuXjjWCLOqbR2WS-7UwH9zkUZcUx7RKZ_houSKbAgb019d4)

**ps: codcliente é para estar vermelho**

***MYSQL***

pk = valores únicos

nn = not null - não nulo

uq = unicidade

b = binário

un = inteiros não sinalizados - só positivos

zf = default assume zero

ai = auto incremento - só funciona para inteiro, e ele gerencia o valor da chave primária

g = genéricas

default/expression = padrão - se não for passado nada, você tem algo para ela assumir?

[](https://lh7-us.googleusercontent.com/pWY9GXe9TqLqchuK_KX45CVlMDYoJnibvp8fkeccP6gmAqbV2ofeiEw8_43TGDeMqHzoggg-44XjU7NZSYl6xmZkIxzZBg1XekVhZRJgWETo8kpl_Yf46PmvLYexT4psJww8BpjJrr5bWe3euKyPPsk)

**Relacionamentos**

[](https://lh7-us.googleusercontent.com/AFoOfuZIAL5qGudWTWNJnOGvGpcB28kfEzJdQvOf3Vj5h0Cy2RULI2iDQEm9rCEZHrG_G119M8PbwjxDg5scU-LzkXdSVOl03P-u8Dz5YODoNyNwSZbb1Cg9ys9cPfRYaI4uNKgqkz9YmrlBs7DfhC8)

[](https://lh7-us.googleusercontent.com/zlorfgciGZTdbjQjSB4NLdAc6ETXbzInr_qXm3eyv1jdXr59oU6M9XFqLAgFog2Ipdf2LCWkmW3JLEuUcFZzx50xgKmbVxbfTg_gdj-m5Mqx6HTQ_GLb9Kg3TpSJ0vQmP4VF25Eii6KJIo9BMQT6KgI)

A transformação dos relacionamentos podem ser feitas de 3 formas:

1. Adição de colunas em uma das tabelas que participam do relacionamento. 1:1 ou 1:N

1.1 Colunas correspondentes ao identificador da entidade relacionada (chave estrangeira)

1.2 Colunas correspondentes aos atributos próprios do relacionamento (se existirem)

[](https://lh7-us.googleusercontent.com/Jz7owPxHtdctqkcxQecQo8KNqicU5RNRgiI91LyOoz1oRPulVvaW9gvsOCmOhKDLpjCYXjnDFxpOmiNxIMQvT7CiLIYSdGnPP-iXoU_AAh6ggreu9CQA_28X8Y4orEhYbFmOu7fWWCITgp5ys75xV4U)

Sempre que a entidade que cede a chave estrangeira estiver do lado do relacionamento que tem cardinalidade mínima igual a 0, a chave estrangeira poderá possuir valores nulos em algumas ocorrências.

[](https://lh7-us.googleusercontent.com/QQFjZMomgQVyqiZPupU5c1mMIWLiEQLzaVIs2bmHsCUUG7juOhTIAlvlbrSeKAStRANNRxbJlZ_xtf5oWBb_niYxcT733oaRg5tUg-5n6E1Y8kpubyrbODg72lf5WnVutWTeP87PoVeTyfzuffHSUVE)

1. Criar um tabela própria para o relacionamento, N:N ou 1:N (especial, quando se tem muitos atributos e opcional do lado 1)

2.1 Colunas correspondentes às chaves estrangeiras, oriundas das tabelas relacionadas

2.2 Colunas correspondentes aos atributos do relacionamento (se existirem)

2.3 A chave primária:

- Por duas chaves estrangeiras concatenadas;
- Também pode ser concatenada com colunas do relacionamento (se existirem)
- Se a cardinalidade for de 1:N, a chave primária da tabela própria poderá ser formada apenas por 1 das chaves estrangeiras
- Considerando apenas as ocorrências que estão se relacionando efetivamente, não há chaves estrangeiras nulas

[](https://lh7-us.googleusercontent.com/BCXGzHMgCZEAHjudcE_E3XSt5PeOrWyLMMt5bE1RMsobZkXcB6eSE_38OV-hv2tsxjUQXYcOml7ZAvOCUgDiFLGP9G7o_b4OcmVgWpxU9b14SfRU3gxQBEo1RWJ4VpkFSuAftDMBMQg4oOyYiNBGv3E)

1. Fusão das tabelas que participam do relacionamento, 1:1 (obrigatório em pelo menos um dos lados)

3.1 O relacionamento é representado por uma única tabela, resultante da fusão

3.2 Todas as colunas de uma tabela são movidas para a outra, a chave primária da tabela final permanece inalterada

3.4 A chave primária da tabela que cedeu as colunas pode deixar de existir

3.5 Todas as colunas correspondentes aos atributos do relacionamento (se existirem) também são movidas para a tabela resultante

[](https://lh7-us.googleusercontent.com/vbU3G99rhuJzrpk-pa_H0xXMw8etM2Ft4otJjzGCk_hF7pmyJUBygNNPsOfccDR0lrcplmSVOB6KKHQffkHaEqSsg98uX1U7UU7dz10Olo2np4gqQ7QzMXw9R7MSyzhppqL7ZJfW57ObZyG7ypwSJYQ)

Essa escolha depende das cardinalidades máxima e mínima do relacionamento

1. Relacionamentos especiais:

4.1 Especialização:

3 possibilidades de tabelas = 1 para cada especializada ou 1 para cada entidade ou 1 geral

[](https://lh7-us.googleusercontent.com/IvfQBW_07eWFDjPd6g2CWG3tX757YjzmmR9-yRNyLUudCS1ulLcTcV1GR0Di96W1VFIl8BZv7Ba6l-_RpuCI4Q8qyTcK9A3gX0l4rn66IPajM91LPSYQSk9wo0lrqhy5Kms_oVMxTIs4OXnjt9GZawg)

[](https://lh7-us.googleusercontent.com/cdeUe2ovx0BanZ82KFhuJRVBa-ec6i0rli3Lhmd7lVBfaA4i4A723VE9ejlTEPMGFywh9T5tJWbz4GH_YWsS5OwnOmCJL2ndlYVW_XpslX9E5cPR1vOpFVTL29X46-n4allwBkCRi0AEbJvbjsNpE0Q)

**Lado que cede:**

Se a cardinalidade mínima for 0, a FK e os atributos  podem ser nulos em algumas ocorrências

Se a cardinalidade mínima for 1, a FK e os atributos não podem ser nulos

Se a cardinalidade máxima for 1, a FK não se repete

Se a cardinalidade máxima for n, a FK se repete

**Tabela própria:** não existe FKs nulas, pode receber 2 FKs da mesma tabela

**Relacionamento identificador:**

FK para o lado n

PK do lado n será a FK + a sua PK anterior

**Atributo Multivalorado:**

Retira os atributos

Nova tabela e estabelece um relacionamento identificador com a de origem

**Relacionamento Ternário:**

Criada uma tabela para o relacionamento

3 FKs das tabelas relacionadas, nenhuma nula

PK é formada pela concatenação das FKs de cada lado n

Nunca existirão FKs nulas

**Agregação:**

Uma tabela para a entidade associativa

2 FKs das tabelas relacionadas formando a sua PK

Nunca irão existir FKs nulas

Relacionamento entre a nova tabela e a 3° entidade

**Especialização/Generalização:**

Tabela para cada entidade: 1:1 entre a genérica e as especializadas, obrigatório do lado da genérica e opcional do lado das especializadas, a PK da genérica será FK e PK das especializadas

Tabela apenas para a genérica: todos os atributos das especializadas vão como opcionais, criado um atributo para diferenciar cada linha resultante

Tabelas para as especializadas: todos os atributos da genérica vão para as especializadas não podendo ser nulos

**ENGENHARIA REVERSA**

- Abstração que parte de um modelo de implementação e resulta em um conceitual
- Não é totalmente precisa
- Transforma modelos ricos em mais abstratos
- Pode ser:
1. Modelos relacionais:

[](https://lh7-us.googleusercontent.com/tXX8uLCooVibCY14TF4htAMRQrgPi1Y4c3ZI14yxeFXF2reoFCN0sxor9tQSBvTxddP8MPM3Bv-mvYIsrZ6RiPs4wG4aX4BsU4R4ud583bAGxVsZL378JmmHew5NmgkQB0V9nGeKV-hW2rZISMu-Imc)

1. Arquivos e documento Convencionais:

Permite obter um modelo lógico relacional a partir de um conjunto de dados não relacional

Pode ser usado qualquer conjunto de dados que tenha alguma descrição

As descrições de conjuntos de tabelas são representadas como tabelas não normalizadas

**NORMALIZAÇÃO**

- Consiste na aplicação de um conjunto de regras a todas as tabelas, com o objetivo de garantir a ausência de redundâncias e inconsistências. Além de garantir que as dependências entre os dados fazem sentido.

[](https://lh7-us.googleusercontent.com/NuM-cfgfHMaFwcqm-QNyFWDoa9diGQdKMz6nxbmrfcMDlfuIxJnD5xoCzsfVHx70pF1P_6gyaCgR2Fym79BJfVL_mJZa7w5HpiIlxW7k7j3qfe7owwzBWkynMug-ydJBMX_2dBfAN67XTmG_9mStyLM)

[](https://lh7-us.googleusercontent.com/auikQKqmxBVklW_m6EHahgSkkIKHvoDpM7vNgCG4DbtiYBmOQRgKwPYRVkjJeBuPLS6TOObrWC4ls2nQ7n3OmEQGu9W2a01pmgYue2EJgW_wh3gtlGZ-pUk00-1S8ec2rgj8UGwUoqTsYpDNTV4XAFo)

[](https://lh7-us.googleusercontent.com/jEsIwPui9I18oQ1milTvj6tzpgerq3pZKVskTbjxUbZOjI8hqG2JGy51qwQ2JXVxGzRxoqMh7-t-ehgadpe-QRlXab87V12IXsM4xg38zyJsDuy2yCwfvCMi0ec06ejIfm60Pobmrzm0aYgZHW37cfY)

1. passo: representação de dados na forma de tabela não normalizada

[](https://lh7-us.googleusercontent.com/spYUgeejLTxAvQHURB7uyibR3iOVsyzuA4P_zX1DVOv70YVJPnss8VyfyQFUmkcY05mg_SsVgT6IB6rRF2WgT9SuGlM22B_pSUOm6owxg3K78R1X-FS9oG3qADDtpocet6NKdg6H8O79UKfv9euCQlQ)

1. Percepção de aninhamento(grupo de repetição ou coluna não atômica ou coluna multi-valorada)

A normalização é baseada em um conjunto de regras denominadas formas normais - é uma regra obedecida por uma tabela para que seja considerada bem projetada

**EXEMPLO:**

[](https://lh7-us.googleusercontent.com/6vo40M1nBSvxOuoNDNbnBtKl3Aa7Aln9CeJiURGedU7Nh0WR0sAhAwXWVMARhr-n5ymHt1qwEsRDKBhSfKVqntBFOtO-DiUqfaooDO0yV1Y3nN-hROVSedIzYxMdsOZQmYfnWa7zXdYO9CKWT_3BoPg)

**1FN** - Não possui tabelas aninhadas - para cada tabela aninhada crie uma tabela 1FN, vai ter as suas colunas próprias e a chave da outra tabela a que estava atrelada

[](https://lh7-us.googleusercontent.com/yMxa45QK0AuHQVsWuzPM2mt7du7r83RrnqtaNyExkubOCEMSrmJL4gTEjh6UIVB8VLP-X8RQV3EvT3J_qH1OyjED9YqaRgpUShaoCOEHbGA13fRe0-MEePEpiknyqI0T3lqNGxB4rc-sXN297YRnpJ8)

**Dependência Funcional:** o valor de uma coluna determina o da outra, pode ser com colunas simples ou compostas (dois valores de colunas juntas determinam o valor da terceira)

- Parcial: uma coluna depende apenas de parte de uma chave primária composta

OBS: na segunda forma normal isso não pode acontecer - só pode estar nessa tabelas quando depende da chave composta

[](https://lh7-us.googleusercontent.com/GBZq3vVrTrnORJQpwYgXdBfDwbvqakAutmY85GmHYRwIqhQpbozbUFGoDwOwW-MXOsiO6IZR1darH7BQkweVRX8wRgSU_pBRqRuvdmqTu4rNoJiruKWok6SRWea71sm8VwnLHZEauUcs-XAXe_QNri0)

- 2 colunas de chaves e o resto sem
- Se eu posso identificar o nome do empregado apenas pelo codEmp é uma dependência parcial
- Uma tabela que está 1FN e que possui apenas uma coluna como chave primária, já está na 2FN
- Uma tabela que contenha apenas colunas chave primária já está em 2FN

→ **Passagem da 1FN para a 2FN:**

1 PK: já está em 2FN

2 PKs ou mais: analise se todas as colunas dependem da chave composta ou de apenas parte dela

Vai manter a tabela e vai remover dela todas as colunas que têm dependência parcial, você cria uma nova tabela (empregado) e traz essas colunas dependentes funcionalmente que você retirou (nome, cat, salário), o que identificava elas vira a chave primária (codEmp). Essa tabela é apenas uma coluna simples então já está na 2FN

[](https://lh7-us.googleusercontent.com/AS2GCAeAJ3tdHKTr3e96OVrhHM8Ze-1T8aExy1X0g9BoJa4ytF6BFNGebLgZcaRUBRcivA4RMbxmc4EhHa9WE0obnXS5FgKlLbeGScB_5onrPbZTWxxxVj4pxhIuWn-TlqibhQ9OCTos9xQ15z2DBrc)

uma coluna é dependente de outra coluna que não é chave

Dependência transitiva: quando uma coluna além de depender da chave primária depende de outra coluna da tabela → uma coluna que não é chave determinando outra não que também não é chave,

[](https://lh7-us.googleusercontent.com/5lFbX_J2wLkQVJXEYF_yp-i9jTZ95p81wgEzrcMp0VOq0pV-9DuSUv65J3Ou4B_eXH8XOv8Qf-GxskyuuRPxhN1fZm3zOrzZTXgoW2hVPj6jD53IUq_0jYj4chJf5oDmIR6ceviAZ6meYRpEoNmm1z0)

- **Passagem da 2FN para a 3FN:**

Retira transitividade

Transitividade ocorre quando uma coluna além de depender da chave primária da tabela depende de outra coluna ou um conjunto de colunas

[](https://lh7-us.googleusercontent.com/ML5spf8nJXDKMGQDiiPs6NUBnZQfrm4w3EBff56vcQolZ1aQbUKSVJFBnlxX48yqdbIBwoO4yWdif1MHD6s4tHmgD92q42fXRJ2JUhRf2vyymIRIwm0rer9eILyR4o2_q5nRIm5mP91xXvkgyDGMT6Q)

Para cada coluna não chave verificar: ela depende de outra coluna não chave?

Caso aja:

1. Crie uma tabela que tenha a chave primária a coluna da qual há dependência indireta
2. Copie a coluna dependente
3. A coluna determinante fica na original

A que determina fica, e as que dependem dela saem (empregado - cod, nome, cat e cat referência a uma tabela chamada categoria)

chave candidata não entra como transitiva

[](https://lh7-us.googleusercontent.com/fPf-LeVEI10h2KWG1ZONU0mMul5k3sgARvTuIeb5uUWDFQI1AvFFU4lNy238NEXcgvttQl2POLg2t16-6ImrS3k7l-ASEVkrXiE7ojLkz-JlmETiW7E-ywPVsGHn0C0fHLFXUuGX8uVT2UDCQryGenA)

Anomalias resolvidas

**→ Limitações da normalização:**

- Não conduz a um modelo ER perfeito
- Elimina redundância

[](https://lh7-us.googleusercontent.com/WNd6ZvFg_wuCoCVhsc_Cgfxb3Onv9tyWf6DUyBlI1FDwOZuwplnZIoUA3SvAlagOJlT3dFlD_SIzRtWSV8AnD0g187Zg9-lXjmiy9xVj0z0vpH7AOJ56ycrshgu7QYGuS1WKy9Q9v4evDYQL1jF1-ts)

**Prática:**

[](https://lh7-us.googleusercontent.com/ZqlOvu92fkWCBsOOaq0dMOwml9T22oqRbYiHRC8XVyDeTgiIoOIsTIv7VaEtGqdjZN8cIMKtLBD_bTmb7zDb-j4m9J6ox5qz6qd7aDkqexipUYTxjmLfJMSv8i_utwCVm1EKEcwPvAIzc3Q8EAZbvtk)

- opcional

**MODELO FÍSICO:**

- Detalhes do armazenamento interno de dados, descrevendo estruturas físicas.
- Os detalhes influenciam no desempenho do banco, mas não na funcionalidade.
- Dependente do SGBD utilizado.
- Processo contínuo
- SQL para definir scripts de criação, alteração e melhoria de desempenho do bd.
- Etapa final.

[](https://lh7-us.googleusercontent.com/1gisVgkRz52-zUdeTDuYTBNA0kzc6msbdyEQEyOYsDzg8rsz1Oc4JietVRFG6dCBQAXHXSLqUeMUs-4y7oURi6IVN5J-LKIFfM8R8zFxFwfWDFxKiQD_dsOUziwM9ec7oad3UFkNECniCDu_s4dS8Kk)

→ PROJETO DO BANCO DE DADOS:

[](https://lh7-us.googleusercontent.com/0oB87-jmVCjHV9uH-mvs85lwQKEd0ZJGNdVn1pgcz3sgvwtQo2Qs7u4e3Xhz_QDjkOGyI_v42WtxPpPUG9eYjTu8jSoollT8OP3HIcX_5OZcvLxxlkSg3zpFqWierwZGdAhWglvoUXpX7VVAo7lvA54)

[](https://lh7-us.googleusercontent.com/LEBjeQIvR_L9f6CFZnLoUjyWzJ35NVaxwWUGmqtsBSQfp2vpyDxBR15Ie_efRqkXWx_mMYUtI1z3uVPXUt2WnXowYMg0K6hDrweLgScsDFbCG-PgCWTonCL8G0cPlu5KAkj1XTf2wvSxZzrIb-mnkDE)

**DQL** - linguagem de consulta (trazer dados, select)

→ É a parte mais utilizada, apesar de só ter um comando

**SELECT** - consultar dados

**DML** - manipulação (insert, update, delete)

**INSERT** - inserir

**UPDATE** - alterar

**DELETE** - excluir

OBS: uma ou várias colunas (tuplas)

**DDL** - definição (script)

→ Tem a ver com estruturas

**CREATE** - <nome do objeto> criar objetos

**ALTER** - <nome do objeto> alterar objetos

**DROP** - <nome do objeto> excluir objetos

mudar a estrutura de uma coluna: esquema da coluna é alterado

mudar dados tipo nome: manipulação de dados

**DCL** - controle (acesso de usuário, permissões)

**GRANT** - adiciona permissão

**REVOKE** - remove permissão concedida ou negada anteriormente

**DTL** - transação (bd2)

**BEGIN** - marca o começo de uma transação

**COMMIT** - finaliza a transação

**ROLLBACK** - faz com que as mudanças nos dados existentes desde o último commit ou rollback sejam descartadas

MySql Workbench: interface para tratar o sgbd

Tanto o modelo relacional como tratar com o sgbd

**EXEMPLO**

[](https://lh7-us.googleusercontent.com/h8Iz9Nk0aQXSFQVRLv2MoD4jgxSQKnMcHJdLiS5N-RHP2fb8jJXcMDuhJTGVA5Rs4qOPt0O7dZhVi5D5OcXpnfpx0cg-ALd39POPgtwYTI7B81PsnaKRP1W8wce5r19C2K7nmhj-4c8uu4IfbptuD-o)

—Alterar tabelas

alter table nome_da_tabela

adicionar coluna:

alter table nome_tabela

add coluna tipo;

não pode adicionar coluna dizendo que é not null

sem que ela esteja toda preenchida

alterar tipo:

alter table nome_tabela

modify coluna tipo;

adicionar constraint:

alter table nome_tabela add constraint nome_constraint check(condição);

adicionar coluna com constraint:

alter table nome_tabela

add coluna tipo constraint nome_constraint check(condição);

CHAR_LENGTH: função que verifica a quantidade de caracteres numa coluna

constraints ficam salvas nos indexes

[](https://lh7-us.googleusercontent.com/tWtrgNWpLHECC9CjnAp6JQyajGPmmNqAg4HSGHq4VL0NCi-0Kzpv8oSHRxjFXB60IHE01Qg7BGlNybmp6j-6gX9d5na5gicEj_vOTx5j8j4-OSnwtFfMwXm5VOWnMLbmLNb0JVKi2LBvDS2OiGCg8Kg)

A tabela só é apagada se não houver chave estrangeira nela

a exclusão restrita é default

between - de tanto a tanto, intervalo fechado

not between - antes disso e depois disso, intervalo aberto

is null - onde está nulo

is not null - onde tem coisa

comparar string:

like - igual, ex: nome LIKE `M%`

obs: a porcentagem indica que pode vir qualquer coisa depois

not like - ex: nome LIKE `A_D%`

% - substitui um conjunto de caracteres

_ - substitui um único caractere

**CONSULTA SIMPLES:**

[](https://lh7-us.googleusercontent.com/W78KheUXijYUyQjm0zd-1GCq7f83s2BpHz2gckOp5GPB-YQ3YllLL47uPZK7sLbSwnqOMmGfinY6ztOuY_vNrU53E2LlR9Q46uRz02P0W98BABiRpq4gN0KQFdnlZh_SKquAuMcDdlzjSesUB2roQbk)

Select é sempre temporário

**LIMIT**

**SELECT <lista de colunas>**

**FROM <tabela>**

**LIMIT [<linha_inicial>,]<quantidade_de_linhas>**

1º Se colocar só 1 número, significa que é para pegar até aquele

[](https://lh7-us.googleusercontent.com/rvNdsBeGmiLFmLzCm5d9VUbv_NzwaCe3hFia3_hgnsWRacm02c7gDe5y5OCOdyuf3ixtmlIwV-HbNGPwOULdtVVQ9UqoM57b3-rWAt5Iw8Ad5d-E1UlC0Dd2GK0PyYY-jfcv_sehGBrqZsdtfva0FZE)

2º Se colocar dois números, significa o de início e quantos após ele

[](https://lh7-us.googleusercontent.com/5GZ_FLsAKenkVdyNTh2w9Y2K2auUFMr5lQN1POnl1gBi3WsEPERgQ7QJqzGBOncaXtEIroUlAEzlpDiwed22aqpBqaQorPwLMfgId_T_vu1jhg9s2KKQmbHOlMetnb5xfOxGQYVGF8twupSdcBJDGbQ)

**AGREGAÇÃO:**

Eu aplico e ela me retorna um valor

COUNT: contador

Sintaxe:

SELECT COUNT(*)

FROM <tabela>

Exemplo 1: Obter a quantidade de clientes cadastrados.

SELECT COUNT(*) AS 'Quantidade'

FROM Cliente;

Exemplo 2: Obter a quantidade de pedidos atendidos p/ via aérea.

SELECT COUNT(*) AS 'Quantidade'

FROM Pedido

WHERE via = 'A';

Tem duplicata, então tem que ter cuidado, utilizando o distinct (na hora de contar faça distinção do vendedor, ou seja, não pegue repetido)

[](https://lh7-us.googleusercontent.com/BBXQ3qykE3EDzvQvqnpngUYJVLK-v_ellWkLjLvNSOqBRJDIM5lDI-x5WVxKrLZX1WL_0J8B9wR6GHFpS9oYp0am-xP7CV6dHXt1BDSES1Frxft2wn4iysmb8GZdKA4RcvkB0c2v0_U1sANFLdcvzek)

SUM: somar

Sintaxe:

SELECT SUM(<coluna>)

FROM <tabela>

Exemplo 5: Obter a soma de todos os salários da empresa.

SELECT SUM(salario) AS 'Total'

FROM Funcionário;

Exemplo 6: Obter o valor total em estoque de todos os produtos (preço de

venda x quantidade em estoque).

SELECT SUM(venda*quantest) AS 'Total'

FROM Produto;

AVG: média

Sintaxe:

SELECT AVG(<coluna>)

FROM <tabela>

Exemplo 7: Obter o valor médio de todos os salários da empresa.

SELECT AVG(salario) AS 'Valor médio'

FROM Funcionario;

Exemplo 8: Obter o preço médio de venda dos produtos que não sejam

dos tipos 1, 3 e 4.

SELECT AVG(venda) AS 'Preço médio'

FROM Produto

WHERE idtipo NOT IN (1,3,4);

MAX: o máximo/maior

Sintaxe:

SELECT MAX(<coluna>)

FROM <tabela>

Exemplo 9: Obter o preço do produto mais caro da empresa.

SELECT MAX(venda) AS 'Mais caro'

FROM Produto;

Exemplo 10: Obter o maior salário pago a uma funcionária.

SELECT MAX(salario) AS 'Maior salário'

FROM Funcionario

WHERE sexo = 'F';

podia ser um limit descendente limitando para 1

MIN: o mínimo/menor

Sintaxe:

SELECT MIN(<coluna>)

FROM <tabela>

Exemplo 11: Obter a data da fatura do primeiro pedido da empresa.

SELECT MIN(datafatura) AS 'Data'

FROM Pedido;

Exemplo 12: Obter a data de nascimento do funcionário do sexo masculino

mais velho da empresa

SELECT MIN(datanasc) AS 'Data'

FROM Funcionario

WHERE sexo = 'M';

**AGRUPAMENTO:**

Group by, eu vou agrupar as coisas

Sintaxe:

SELECT <lista de colunas>

FROM <tabela>

GROUP BY <coluna>

[HAVING] <condição>

Exemplo 13: Obter a quantidade de funcionários de cada sexo existente na empresa.

SELECT sexo, COUNT(*) AS 'Quantidade'

FROM Funcionario

GROUP BY sexo;

- Ele faz o grupo e depois conta

Exemplo 14: Obter a quantidade de funcionários e o valor total de salários

de cada setor da empresa.

SELECT idsetor,

COUNT(*) AS 'Quantidade',

SUM(salario) AS 'Total'

FROM Funcionario

GROUP BY idsetor;

[](https://lh7-us.googleusercontent.com/vKDTmNZnk8S8HziiiXWuUZMHUazN0UKNd68JAghYgc_RnD2SLNKO9oGze9ZFJ90nQH89cSdsiHR1kJ4L8nlpAiLPHS_GykOTi_A-vQJJvpuSo8ZWxVfcYr2fj4kD8zuBOODC3eFneySQOhNcUS0nwLA)

HAVING:  Filtrar os grupos

Exemplo 16: Obter o código do pedido e a quantidade de produtos dos

pedidos que tem mais do que três produtos.

SELECT idpedido, COUNT(idproduto) AS 'Quantidade'

FROM Itens

GROUP BY idpedido

HAVING COUNT(idproduto) > 3;

**JUNÇÃO DE TABELAS**

A conexão é sempre duas tabelas por vez, ou seja, feita em pares

A condição é no ***ON***

SELECT <lista de colunas>

FROM <tabela1> [alias1]

[INNER] JOIN <tabela2> [alias2]

ON <condição de relacionamento>

Nenhum select faz alteração de tabela

**Inner Join:** interseção, apenas os registros em que exista ligação entre as duas tabelas, Fica uma tabelona temporária. Não tem relação com ninguém cai fora

[](https://lh7-us.googleusercontent.com/_xO8Z3-JDZ3-L5DH9hogrxpE_7FKh9fgxhxCeFTJlzbZq8AG0l48ZjJjEfBmvstMRLdAtT6nAPPfJeVVZPIewbxOnurzO5Rd7MxRCDooNJgmYt8Qba0tFfqCidnzGQg32gz6jmD4DuSVux_BOVD7dUk)

[](https://lh7-us.googleusercontent.com/Dm8rgPHSHJhGhMqCIprSwWFp3GbUCSWDOdswrChA0u9-tflXXPOi3c0cxmqNKohAulysB6Dh5eDTJUTMekxopCAmUEtBGJ1_gL0BsuDbx3pVDEmQUPC8u_Gnc1GdhFAqY2A5YFadxV7SHYg_-5O10qM)

**Left Outer Join:** eu quero os que estão associados e os que não estão, na minha tabela a esquerda

**Right Outer Join:** exibe todas as linhas da direita e apenas os correspondentes da esquerda, os que não tiverem correspondência ficam null

**Full outer Join:** todos fora