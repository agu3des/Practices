# Projeto

> https://drive.google.com/drive/folders/1BuLajdgZg24qb08glQ9qH20bEcg8PWrt?usp=sharing
> 

> https://agu3des.github.io/Disaster/
> 

[https://github.com/agu3des/Disaster](https://github.com/agu3des/Disaster)

As primeiras 4 sugestões:

[https://chat.openai.com/share/e5b8f60e-d222-46c0-bdc1-f2965ff2da56](https://chat.openai.com/share/e5b8f60e-d222-46c0-bdc1-f2965ff2da56)

Sugestões de ongs:

[https://chat.openai.com/share/5a75999b-b721-4ec3-a752-206cb40eb6b0](https://chat.openai.com/share/5a75999b-b721-4ec3-a752-206cb40eb6b0)

Desastres naturais:

[https://chat.openai.com/share/329cd9f9-77b8-4ca0-87f5-f8386350a64a](https://chat.openai.com/share/329cd9f9-77b8-4ca0-87f5-f8386350a64a)

**"Sistema de Gerenciamento de Desastres Naturais"**

1. Descrição do negócio e da necessidade

De acordo com a CNN Brasil, “Foram registrados 1.161 eventos de desastres, sendo 716 associados a eventos hidrológicos, como transbordamento de rios, e 445 de origem geológica, como deslizamentos de terra. Na média, foram registrados pelo menos três desastres por dia.“

Diante da ocorrência desses desastres naturais, é crucial ter um sistema informatizado para controlar e gerenciar as vítimas, recursos disponíveis e agências de resgate, além de facilitar a coordenação de voluntários e abrigos associados.

O sistema deve permitir o registro de dados detalhados sobre os desastres naturais, como a quantidade de vítimas afetadas. De cada vítima devem ser armazenadas suas informações, sua relação com o desastre, além de sua necessidade de abrigo ou doações. Das doações devem ser armazenados itens baseados em sua tipagem. Ademais, se faz necessário um registro de voluntários e suas respectivas contribuições. O sistema também deve guardar informações a respeito de abrigos e agências parceiras. Para uma melhor compreensão dos desastres também serão armazenados relatos de testemunhas 

1. Requisitos Funcionais ou funcionalidades previstas para a aplicação
- Registrar desastre natural
- Cadastrar vítimas
- Verificar doações
- Administrar abrigos
- Cadastrar as Agências de Resgate
- Registrar Relatos
- Manutenção de voluntarios

3.Requisitos de Dados

**Desastre Natural** (cod - default, data, tipo, qtdvitimas, duracao, local, intensidade, agencia de resgate)

**Vítimas (**Identificador único, Nome da vítima, Idade, Gênero, Nacionalidade, Contato de emergência, condição médica, abrigo**)**

**Abrigos** (Identificador único, nome, enderenço, disponibilidade)

**Doação** (tipo da doação - alimentação (cod, pereciveis ou n, validade, desc), ajuda financeira (cod, desc ), higiene (cod,desc,validade)-, Quantidade disponível, Localização da distribuição, Data e hora da distribuição) 

**Doador** (nome, cpf, doação)

**Agências de Resgate** (Identificador único, Nome da agência, Tipo de agência (governo, ONG, etc.), Contato de emergência, Localização da base operacional, Recursos disponíveis)

**Relatos** (pessoa, desastre, relato, tipo de testemunha)

**Voluntários** (id, nome, tipo de doação)

## **Roteiro para Projeto de Banco de Dados Relacional (Requisitos)**

**1.**     **Descreva o escopo da aplicação que precise do banco de dados (seu projeto).**

**a.      Descrição geral das regras do negócio e do que se espera da aplicação/banco de dados**

*De acordo com a CNN Brasil, “Foram registrados 1.161 eventos de desastres, sendo 716 associados a eventos hidrológicos, como transbordamento de rios, e 445 de origem geológica, como deslizamentos de terra. Na média, foram registrados pelo menos três desastres por dia.”*

*Diante da ocorrência desses desastres naturais, é crucial ter um sistema informatizado para controlar e gerenciar as vítimas, recursos disponíveis e agências de resgate, além de facilitar a coordenação de voluntários e abrigos associados.*

*O sistema deve permitir o registro de dados detalhados sobre os desastres naturais, como a quantidade de vítimas afetadas. De cada vítima devem ser armazenadas suas informações, sua relação com o desastre, além de sua necessidade de abrigo ou doações. Das doações devem ser armazenados itens baseados em sua tipagem. Ademais, se faz necessário um registro de voluntários e suas respectivas contribuições. O sistema também deve guardar informações a respeito de abrigos e agências parceiras. Para uma melhor compreensão dos desastres também serão armazenados relatos de testemunhas.*

**b.      Requisitos Funcionais da aplicação**

- *Registrar desastre natural*
- *Cadastrar vítimas*
- *Verificar doações*
- *Administrar abrigos*
- *Cadastrar as Agências de Resgate*
- *Registrar Relatos*
- *Manutenção de voluntários*

**c.      Requisitos de Dados**

*Desastre Natural*

*Vítimas*

*Abrigos*

*Doação*

*Doador*

*Agências de Resgate*

*Relatos*

*Voluntários*

**2.** 	**Diagrama Entidade-Relacionamento em nível Conceitual (versão 1)**

Especifique uma versão inicial do seu DER conceitual com as *entidades*, *relacionamentos* e *principais atributos*. As entidades e relacionamentos devem ser especificados conforme requisitos e escopo descritos na seção anterior.

[](https://lh7-us.googleusercontent.com/aeLO2-Sj_rGyhCIi8n8GVxiywreCOLsl-6SuUnJyHbEhm5YWLoM1_LOxx3MBn7vPPeZMJ2jmzmRrW9mWV6Dau36FOeQE3xCJtYm5HJCHCjI5ExNyNfcEejkXmeXrn4kVu53kNqo9IqLq4_rCLZ0KJCg)

Ideias de nomes para o sistema:

1. **GeoGuard**
2. **SafeEarth**
3. **Disaster Watch**
4. **NatureShield**
5. **Crisis Control**
6. **Disaster Response**
7. **StormGuard**

1. **Rapid Response**
2. **Hazard Watch**
3. **QuakeAlert**
4. **EarthSafe**
5. **Disaster Ready**
6. **Emergency Pulse**
7. **Nature Resilience**
8. **Disaster Network**
- **Criação tabelas**
    
    20 tabelas
    
    ```sql
    --entidades:
    
    CREATE TABLE Regiao 
    ( 
     codigoRegiao INT,  
     nomeRegiao varchar(20) NOT NULL,
     CONSTRAINT PK_codigoRegiao_regiao PRIMARY KEY (codigoRegiao)  
    ); 
    
    CREATE TABLE Desastre_Natural 
    ( 
     codDesastre INT,
     dataDeOcorrencia date NOT NULL,  
     duracao INT,  
     intensidade INT,    
     qtdVitimas INT,
     CONSTRAINT PK_codDesastre_desastre PRIMARY KEY (codDesastre)  
    ); 
    
    CREATE TABLE Testemunha 
    ( 
     testemunhaCpf char(11),
     nome varchar(100) NOT NULL,
     genero char(1),   
     dataDeNascimento date,  
     nacionalidade varchar(15),
     contato varchar(12) UNIQUE,
     CONSTRAINT PK_testemunhaCpf_testemunha PRIMARY KEY (testemunhaCpf)    
    ); 
    
    CREATE TABLE Relato 
    ( 
     codigoRelato INT,  
     relato varchar(300) NOT NULL,  
     dataDeEmissao date NOT NULL,  
     codDesastre INT NOT NULL, --adicao de coluna relacionamento com desastre
     testemunha char(11) NOT NULL,
     CONSTRAINT PK_codigoRelato_relato PRIMARY KEY (codigoRelato),
     CONSTRAINT FK_codDesastre_relato FOREIGN KEY (codDesastre) REFERENCES
     Desastre_Natural(codDesastre),
     CONSTRAINT FK_testemunha_relato FOREIGN KEY (testemunha) REFERENCES
     Testemunha(testemunhaCpf)  
    ); 
    
    CREATE TABLE Tipo 
    ( 
     codTipo INT,  
     descricao varchar(20) NOT NULL,
     CONSTRAINT PK_codTipo_tipo PRIMARY KEY (codTipo)  
    ); 
    
    CREATE TABLE Abrigo 
    ( 
     cnpj char(14),  
     nome varchar(100) NOT NULL,  
     cep char(8) NOT NULL,
     numero int,
     rua varchar(20),
     bairro varchar(20),
     cidade varchar(20),
     estado varchar(20), 
     disponibilidade boolean NOT NULL,
     CONSTRAINT PK_cnpj_abrigo PRIMARY KEY (cnpj)  
    ); 
    
    CREATE TABLE Vitima 
    ( 
     vitimaCpf char(11),
     nome varchar(100) NOT NULL,
     dataDeNascimento date,  
     genero char(1),     
     nacionalidade varchar(10),  
     condicaoMedica varchar(30),  
     cnpjAbrigo char(14),
     dataEntrada date,
     dataSaida date,
     contato varchar(12) unique,  
     CONSTRAINT PK_vitimaCpf_vitima PRIMARY KEY (vitimaCpf),
     CONSTRAINT FK_cnpjAbrigo_vitima FOREIGN KEY (cnpjAbrigo) REFERENCES abrigo(cnpj)
    ); 
    
    CREATE TABLE Categoria 
    ( 
     codCateg INT,
     descricao varchar(30) NOT NULL,  
     valor numeric(20,2),  
     perecivel boolean NOT NULL,  
     validade date,  
     CONSTRAINT PK_codCateg_categoria PRIMARY KEY (codCateg)  
    );
    
    CREATE TABLE Doador 
    ( 
     doadorCpf char(11),  
     nome varchar(100) NOT NULL,
     CONSTRAINT PK_doadorCpf_doador PRIMARY KEY (doadorCpf) 
    ); 
    
    CREATE TABLE Doacao 
    ( 
     codDoacao INT,
     qtdEstoque INT NOT NULL,  
     dataDoacao date NOT NULL,  
     localArmazenamento varchar(30),
     codCateg INT NOT NULL,
     doadorCPF char(11) NOT NULL,
     CONSTRAINT PK_codDoacao_doacao PRIMARY KEY (codDoacao),
     CONSTRAINT FK_codCateg_doacao FOREIGN KEY (codCateg) REFERENCES categoria(codCateg),
     CONSTRAINT FK_doadorCPF_doacao FOREIGN KEY (doadorCPF) REFERENCES Doador(doadorCPF)
    ); 
    
    CREATE TABLE AgenciaDeResgate 
    ( 
     cnpj char(14), 
     nomeAgencia varchar(20) NOT NULL, 
     telefone varchar(20),    
     cep char(8) NOT NULL,
     numero INT,
     rua varchar(20),
     bairro varchar(20),
     cidade varchar(20),
     estado char(2),
     CONSTRAINT PK_cnpj_AgenciaDeResgate PRIMARY KEY (cnpj)
    ); 
    
    CREATE TABLE Voluntario (
    	cpfVoluntario char(11),
    	nomeVoluntario varchar(100),
    	CONSTRAINT PK_cpfVoluntario_Voluntario PRIMARY KEY (cpfVoluntario)
    );
    
    --relacionamentos:
    
    CREATE TABLE ocorrencia --ocorre
    ( 
     codigoRegiao INT,  
     codDesastre INT,
     CONSTRAINT PK_codigoRegiao_codDesastre_ocorrencia PRIMARY KEY (codigoRegiao, codDesastre),
     CONSTRAINT FK_codigoRegiao_ocorrencia FOREIGN KEY (codigoRegiao) REFERENCES 
     Regiao(codigoRegiao),
     CONSTRAINT FK_codDesastre_ocorrencia FOREIGN KEY (codDesastre) REFERENCES 
     Desastre_Natural(codDesastre)  
    ); 
    
    CREATE TABLE TipoDesastre --tem
    ( 
     codTipo INT,  
     codDesastre INT,
     CONSTRAINT PK_codTipo_codDesastre_TipoDesastre PRIMARY KEY (codTipo, codDesastre),
     CONSTRAINT FK_codTipo_TipoDesastre FOREIGN KEY (codTipo) REFERENCES Tipo(codTipo),
     CONSTRAINT FK_codDesastre_TipoDesastre FOREIGN KEY (codDesastre) REFERENCES 
     Desastre_Natural(codDesastre)  
    ); 
    
    CREATE TABLE VitimaDesastre --causa
    ( 
     codDesastre INT,  
     vitimaCpf char(11), 
     CONSTRAINT PK_codDesastre_vitimaCpf_VitimaDesastre PRIMARY KEY (codDesastre, vitimaCpf),
     CONSTRAINT FK_codDesastre_VitimaDesastre FOREIGN KEY (codDesastre) REFERENCES 
     Desastre_Natural(codDesastre),
     CONSTRAINT FK_vitimaCpf_VitimaDesastre FOREIGN KEY (vitimaCpf) REFERENCES 
     Vitima(vitimaCpf) 
    ); 
    
    CREATE TABLE DoacaoVitima --vitima recebe
    (
      codDoacao INT,
      vitimaCpf CHAR(11),
      CONSTRAINT PK_codDoacao_vitimaCpf_DoacaoVitima PRIMARY KEY (codDoacao, vitimaCpf),
      CONSTRAINT FK_codDoacao_doacaoVitima FOREIGN KEY (codDoacao) REFERENCES 
      Doacao(codDoacao),
      CONSTRAINT FK_vitimaCpf_doacaoVitima FOREIGN KEY (vitimaCpf) REFERENCES 
      Vitima(vitimaCpf)
    );
    
    /* não tem mais
    relacionamento 1:n, fica adição de coluna na tabela doacao
    CREATE TABLE DoacaoDoador --doador faz doacao
    ( 
     codDoacao INT,  
     doadorCpf char(11),
     CONSTRAINT PK_codDoacao_doadorCpf_DoacaoDoador PRIMARY KEY (codDoacao, doadorCpf),
     CONSTRAINT FK_codDoacao_DoacaoDoador FOREIGN KEY (codDoacao) REFERENCES 
     Doacao(codDoacao),
     CONSTRAINT FK_doadorCpf_DoacaoDoador FOREIGN KEY (doadorCpf) REFERENCES 
     Doador(doadorCpf)  
    ); */
    
    CREATE TABLE atuacao
    (
     cnpjAgencia char(14),  
     codDesastre INT,
     dataDeAtuacao date NOT NULL,
     CONSTRAINT PK_cnpjAgencia_codDesastre_atuacao PRIMARY KEY (cnpjAgencia, codDesastre),
     CONSTRAINT FK_cnpjAgencia_atuacao FOREIGN KEY (cnpjAgencia) REFERENCES 
     AgenciaDeResgate(cnpj),
     CONSTRAINT FK_codDesastre_atuacao FOREIGN KEY (codDesastre) REFERENCES 
     Desastre_Natural(codDesastre)  
    );
    
    CREATE TABLE DoacaoAgencia --agencia recebe
    (
      codDoacao INT,
      cnpjAgencia CHAR(14),
      CONSTRAINT PK_codDoacao_cnpjAgencia_DoacaoAgencia PRIMARY KEY (codDoacao, cnpjAgencia),
      CONSTRAINT FK_codDoacao_doacaoAgencia FOREIGN KEY (codDoacao) REFERENCES 
      Doacao(codDoacao),
      CONSTRAINT FK_cnpjAgencia_doacaoAgencia FOREIGN KEY (cnpjAgencia) REFERENCES 
      AgenciaDeResgate(cnpj)
    ); 
    
    CREATE TABLE voluntarioAgencia (
      cnpjAgencia CHAR(14),
      CPFVoluntario CHAR(11),
      CONSTRAINT PK_cnpjAgencia_cpfVoluntario_voluntarioAgencia PRIMARY KEY 
      (cnpjAgencia, CPFVoluntario),
      CONSTRAINT FK_cnpjAgencia_voluntarioAgencia FOREIGN KEY (cnpjAgencia) REFERENCES 
      AgenciaDeResgate(cnpj),
      CONSTRAINT FK_CPFVoluntario_voluntarioAgencia FOREIGN KEY (CPFVoluntario) REFERENCES 
      Voluntario(CPFVoluntario)
    );
    
    CREATE TABLE voluntarioAbrigo (
      cnpjAbrigo CHAR(14),
      CPFVoluntario CHAR(11),
      CONSTRAINT PK_cnpjAbrigo_cpfVoluntario_voluntarioAbrigo PRIMARY KEY 
      (cnpjAbrigo, CPFVoluntario),
      CONSTRAINT FK_cnpjAbrigo_voluntarioAbrigo FOREIGN KEY (cnpjAbrigo) REFERENCES 
      Abrigo(cnpj),
      CONSTRAINT FK_CPFVoluntario_voluntarioAbrigo FOREIGN KEY (CPFVoluntario) REFERENCES 
      Voluntario(CPFVoluntario)
    );
     
     /*
     não tem mais para cardinalidade: doacao (0,n) tem (1,1) categoria
     CREATE TABLE DoacaoCategoria --possui
    ( 
     codDoacao INT,  
     codCateg INT,
     CONSTRAINT PK_codDoacao_codCateg_DoacaoCategoria PRIMARY KEY (codDoacao, codCateg),
     CONSTRAINT FK_codDoacao_DoacaoCategoria FOREIGN KEY (codDoacao) REFERENCES 
     Doacao(codDoacao),
     CONSTRAINT FK_codCateg_DoacaoCategoria FOREIGN KEY (codCateg) REFERENCES 
     Categoria(codCateg)
    );
    */
    
    /*
    não tem mais
    CREATE TABLE IF NOT EXISTS contatoVitima
    (
    	vitimaCpf varchar(11) NOT NULL,
    	telefone VARCHAR(12) NOT NULL,
    	CONSTRAINT CHK_telefoneVitima CHECK(LENGTH(telefone) >= 12),
    	CONSTRAINT PK_vitimaCpf_telefone_contatoVitima PRIMARY KEY (vitimaCpf, telefone),
    	CONSTRAINT FK_vitimaCpf_contatoVitima FOREIGN KEY (vitimaCpf)
    	REFERENCES vitima(vitimaCpf)
    );
    
    CREATE TABLE IF NOT EXISTS contatoTestemunha
    (
    	testemunhaCpf varchar(11) NOT NULL,
    	telefone VARCHAR(12) NOT NULL,
    	CONSTRAINT CHK_telefoneTestemunha CHECK(LENGTH(telefone) >= 12),
    	CONSTRAINT PK_testemunhaCpf_telefone_contatoTestemunha 	PRIMARY KEY 
    	(testemunhaCpf, telefone),
    	CONSTRAINT FK_testemunhaCpf_contatoTestemunha FOREIGN KEY (testemunhaCpf)
    	REFERENCES testemunha(testemunhaCpf)
    );
    
    CREATE TABLE AtuacaoAbrigo 
    (
        cnpjAbrigo varchar(14),
        codDesastre INT,
        dataDeAtuacao date NOT NULL,
        CONSTRAINT PK_cnpjAbrigo_codDesastre_AtuacaoAbrigo PRIMARY KEY 
        (cnpjAbrigo, codDesastre),
        CONSTRAINT FK_cnpjAbrigo_AtuacaoAbrigo FOREIGN KEY (cnpjAbrigo) REFERENCES 
        Abrigo(cnpj),
        CONSTRAINT FK_codDesastre_AtuacaoAbrigo FOREIGN KEY (codDesastre) REFERENCES 
        DesastreNatural(codDesastre)
    );
    */
    
    /*
    não tem mais
    CREATE TABLE TestemunhaRelato --faz
    (
     codRelato INT, 
     testemunhaCpf varchar(11),
     CONSTRAINT PK_codRelato_testemunhaCpf_TestemunhaRelato PRIMARY KEY 
     (codRelato, testemunhaCpf),
     CONSTRAINT FK_codRelato_TestemunhaRelato FOREIGN KEY (codRelato) REFERENCES 
     Relato(codRelato),
     CONSTRAINT FK_testemunhaCpf_TestemunhaRelato FOREIGN KEY (testemunhaCpf) REFERENCES
     testemunha(testemunhaCpf)    
    ); */
    
    /*
    não tem mais
    CREATE TABLE DoacaoAbrigo --abrigo recebe
    (
      codDoacao INT,
      cnpjAbrigo VARCHAR(14),
      CONSTRAINT PK_codDoacao_cnpjAbrigo_doacaoAbrigo PRIMARY KEY (codDoacao, cnpjAbrigo),
      CONSTRAINT FK_codDoacao_doacaoAbrigo FOREIGN KEY (codDoacao) REFERENCES 
      Doacao(codDoacao),
      CONSTRAINT FK_cnpjAbrigo_doacaoAbrigo FOREIGN KEY (cnpjAbrigo) REFERENCES 
      Abrigo(cnpj)
    );
    */
    ```
    

- Exemplos de inserções
    
    ```sql
    INSERT INTO Regiao (codigoRegiao, nomeRegiao) VALUES
    (1, 'Centro-Oeste'),
    (2, 'Nordeste'),
    (3, 'Norte'),
    (4, 'Sudeste'),
    (5, 'Sul');
    
    INSERT INTO Desastre_Natural (codDesastre, dataDeOcorrencia, duracao, intensidade, qtdVitimas) VALUES
    (1, '2023-01-15', 72, 5, 120),
    (2, '2023-02-10', 48, 7, 80),
    (3, '2023-03-25', 36, 4, 50),
    (4, '2023-04-12', 60, 6, 90),
    (5, '2023-05-05', 24, 8, 150);
    
    INSERT INTO Testemunha (testemunhaCpf, nome, genero, dataDeNascimento, nacionalidade, contato) VALUES
    ('12345678901', 'Maria Silva', 'F', '1985-06-25', 'Brasileira', '11987654321'),
    ('10987654321', 'João Santos', 'M', '1978-11-15', 'Brasileiro', '11876543210'),
    ('23456789012', 'Ana Costa', 'F', '1990-02-20', 'Brasileira', '11765432109'),
    ('34567890123', 'Carlos Almeida', 'M', '1982-07-30', 'Brasileiro', '11654321098'),
    ('45678901234', 'Lucia Pereira', 'F', '1995-09-10', 'Brasileira', '11543210987');
    
    INSERT INTO Relato (codigoRelato, relato, dataDeEmissao, codDesastre, testemunha) VALUES
    (1, 'Muitas casas foram destruídas e pessoas estão desabrigadas.', '2023-01-16', 1, '12345678901'),
    (2, 'Há necessidade urgente de assistência médica.', '2023-02-11', 2, '10987654321'),
    (3, 'Há relatos de danos a infraestruturas importantes.', '2023-03-26', 3, '23456789012'),
    (4, 'O número de vítimas está aumentando.', '2023-04-13', 4, '34567890123'),
    (5, 'A situação é crítica e precisa de ajuda urgente.', '2023-05-06', 5, '45678901234');
    
    INSERT INTO Tipo (codTipo, descricao) VALUES 
    (1, 'Enxurrada'),
    (2, 'Furacão'),
    (3, 'Inundação'),
    (4, 'Deslizamento Terra'),
    (5, 'Incêndio Florestal');
    
    INSERT INTO Abrigo (cnpj, nome, cep, numero, rua, bairro, cidade, estado, disponibilidade) VALUES
    ('12345678000195', 'Abrigo Centro', '01001000', 100, 'Rua A', 'Centro', 'São Paulo', 'SP', TRUE),
    ('23456789000196', 'Abrigo Norte', '02002000', 200, 'Rua B', 'Norte', 'Rio de Janeiro', 'RJ', TRUE),
    ('34567890000197', 'Abrigo Sul', '03003000', 300, 'Rua C', 'Sul', 'Porto Alegre', 'RS', TRUE),
    ('45678901000198', 'Abrigo Leste', '04004000', 400, 'Rua D', 'Leste', 'Fortaleza', 'CE', TRUE),
    ('56789012000199', 'Abrigo Oeste', '05005000', 500, 'Rua E', 'Oeste', 'Brasília', 'DF', TRUE);
    
    INSERT INTO Vitima (vitimaCpf, nome, dataDeNascimento, genero, nacionalidade, condicaoMedica, cnpjAbrigo, dataEntrada, dataSaida, contato) VALUES
    ('67890123456', 'Pedro Oliveira', '1987-05-12', 'M', 'Brasileiro', 'Ferido', '12345678000195', '2023-01-16', NULL, '11912345678'),
    ('78901234567', 'Juliana Lima', '1990-08-23', 'F', 'Brasileira', 'Leve', '23456789000196', '2023-02-11', NULL, '11876543210'),
    ('89012345678', 'Marcelo Santos', '1985-12-30', 'M', 'Brasileiro', 'Grave', '34567890000197', '2023-03-26', NULL, '11765432109'),
    ('90123456789', 'Fernanda Souza', '1992-11-11', 'F', 'Brasileira', 'Leve', '45678901000198', '2023-04-13', NULL, '11654321098'),
    ('01234567890', 'Ricardo Almeida', '1980-07-22', 'M', 'Brasileiro', 'Ferido', '56789012000199', '2023-05-06', NULL, '11543210987');
    
    INSERT INTO Categoria (codCateg, descricao, valor, perecivel, validade) VALUES
    (1, 'Roupas', 200.00, FALSE, NULL),
    (2, 'Alimentos', 150.00, TRUE, '2023-06-01'),
    (3, 'Medicamentos', 300.00, TRUE, '2023-07-01'),
    (4, 'Água', 100.00, FALSE, NULL),
    (5, 'Móveis', 500.00, FALSE, NULL);
    
    INSERT INTO Doador (doadorCpf, nome) VALUES
    ('12345678901', 'Carlos Martins'),
    ('23456789012', 'Patrícia Oliveira'),
    ('34567890123', 'Roberto Silva'),
    ('45678901234', 'Ana Paula Costa'),
    ('56789012345', 'Eduardo Santos');
    
    INSERT INTO Doacao (codDoacao, qtdEstoque, dataDoacao, localArmazenamento, codCateg, doadorCPF) VALUES
    (1, 100, '2023-01-20', 'Depósito A', 1, '12345678901'),
    (2, 50, '2023-02-15', 'Depósito B', 2, '23456789012'),
    (3, 75, '2023-03-10', 'Depósito C', 3, '34567890123'),
    (4, 120, '2023-04-05', 'Depósito D', 4, '45678901234'),
    (5, 80, '2023-05-01', 'Depósito E', 5, '56789012345');
    
    INSERT INTO AgenciaDeResgate (cnpj, nomeAgencia, telefone, cep, numero, rua, bairro, cidade, estado) VALUES
    ('01234567000123', 'Agência Centro', '1122334455', '06060600', 10, 'Rua X', 'Centro', 'São Paulo', 'SP'),
    ('12345678000124', 'Agência Norte', '2233445566', '07070700', 20, 'Rua Y', 'Norte', 'Rio de Janeiro', 'RJ'),
    ('23456789000125', 'Agência Sul', '3344556677', '08080800', 30, 'Rua Z', 'Sul', 'Porto Alegre', 'RS'),
    ('34567890000126', 'Agência Leste', '4455667788', '09090900', 40, 'Rua W', 'Leste', 'Fortaleza', 'CE'),
    ('45678901000127', 'Agência Oeste', '5566778899', '10101010', 50, 'Rua V', 'Oeste', 'Brasília', 'DF');
    
    INSERT INTO Voluntario (cpfVoluntario, nomeVoluntario) VALUES
    ('11122334455', 'Lucas Ferreira'),
    ('22233445566', 'Juliana Rocha'),
    ('33344556677', 'Marcos Lima'),
    ('44455667788', 'Fernanda Castro'),
    ('55566778899', 'Gabriel Pereira');
    
    INSERT INTO voluntarioAbrigo (cnpjAbrigo, CPFVoluntario) VALUES
    ('12345678000195', '11122334455'),
    ('23456789000196', '22233445566'),
    ('34567890000197', '33344556677'),
    ('45678901000198', '44455667788'),
    ('56789012000199', '55566778899');
    
    INSERT INTO voluntarioAgencia (cnpjAgencia, CPFVoluntario) VALUES
    ('01234567000123', '11122334455'),
    ('12345678000124', '22233445566'),
    ('23456789000125', '33344556677'),
    ('34567890000126', '44455667788'),
    ('45678901000127', '55566778899');
    
    INSERT INTO ocorrencia (codigoRegiao, codDesastre) VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5);
    
    INSERT INTO TipoDesastre (codTipo, codDesastre) VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5);
    
    INSERT INTO VitimaDesastre (codDesastre, vitimaCpf) VALUES
    (1, '67890123456'),
    (2, '78901234567'),
    (3, '89012345678'),
    (4, '90123456789'),
    (5, '01234567890');
    
    INSERT INTO DoacaoVitima (codDoacao, vitimaCpf) VALUES
    (1, '67890123456'),
    (2, '78901234567'),
    (3, '89012345678'),
    (4, '90123456789'),
    (5, '01234567890');
    
    INSERT INTO DoacaoAgencia (codDoacao, cnpjAgencia) VALUES
    (1, '01234567000123'),
    (2, '12345678000124'),
    (3, '23456789000125'),
    (4, '34567890000126'),
    (5, '45678901000127');
    
    INSERT INTO atuacao (cnpjAgencia, codDesastre, dataDeAtuacao) VALUES
    ('01234567000123', 1, '2024-08-01'),
    ('12345678000124', 2, '2024-08-05'),
    ('23456789000125', 3, '2024-08-10'),
    ('34567890000126', 4, '2024-08-15'),
    ('45678901000127', 5, '2024-08-20');
    
    /*
    INSERT INTO DoacaoDoador (codDoacao, doadorCpf) VALUES
    (1, '12345678901'),
    (2, '23456789012'),
    (3, '34567890123'),
    (4, '45678901234'),
    (5, '56789012345');
    */
    ```
    

- **1** consulta com uma tabela usando operadores básicos de filtro (e.g., IN,  between, is null, etc).
    
    ```sql
    /*
    Encontrar Desastres com Quantidade de Vítimas maior que 20 e 
    Data de Ocorrência entre janeiro e março de 2023 */ 
    SELECT *
    FROM Desastre_Natural
    WHERE qtdVitimas > 20 
      AND dataDeOcorrencia BETWEEN '2023-01-01' AND '2023-03-31';
    
    ```
    

- **3** consultas com inner JOIN na cláusula FROM (pode ser self join, caso o  domínio indique esse uso).
    
    ```sql
    --Consultar Testemunhas e Seus Relatos Correspondentes
    SELECT t.nome AS nome_testemunha, r.relato, r.dataDeEmissao
    FROM Testemunha t
    INNER JOIN Relato r ON t.testemunhaCpf = r.testemunha;
    
    --Consultar Vítimas e Seus Abrigos Correspondentes
    SELECT v.vitimaCpf, v.nome AS nome_vitima, a.nome AS nome_abrigo, a.cidade
    FROM Vitima v
    INNER JOIN Abrigo a ON v.cnpjAbrigo = a.cnpj;
    
    --Consultar Relatos e Seus Desastres Correspondentes
    SELECT r.codigoRelato, r.relato, r.dataDeEmissao, d.dataDeOcorrencia, d.intensidade, ti.descricao
    FROM Relato r
    INNER JOIN Desastre_Natural d ON r.codDesastre = d.codDesastre
    join tipodesastre td on d.codDesastre = td.codDesastre
    join tipo ti on ti.codtipo = td.codtipo;
    ```
    

- **1** consulta com left/right/full outer join na cláusula FROM
    
    ```sql
    /*Esta consulta usa FULL OUTER JOIN para listar todos os registros de vítimas 
    e abrigos, mostrando todos os registros de ambas as tabelas. Se não houver 
    correspondência, os campos relacionados serão NULL.
    */
    
    SELECT v.vitimaCpf, v.nome AS nome_vitima, v.condicaoMedica, a.cnpj, a.nome AS nome_abrigo, a.cidade
    FROM Vitima v
    FULL OUTER JOIN Abrigo a ON v.cnpjAbrigo = a.cnpj;
    
    ```
    

- **2** consultas usando Group By (e possivelmente o having)
    
    ```sql
    --1. Consulta para Contar o Número de Vítimas por Abrigo
    /*
    Motivo do LEFT JOIN: Aqui, queremos listar todos os abrigos e contar o 
    número de vítimas associadas a cada um. Usar LEFT JOIN assegura que mesmo 
    os abrigos que não têm vítimas associadas (ou seja, vítimas com cnpj não 
    correspondentes aos abrigos) sejam incluídos na contagem. Abrigos sem vítimas 
    serão listados com um total de 0 vítimas.
    */
    SELECT a.nome AS nome_abrigo, COUNT(v.vitimaCpf) AS total_vitimas
    FROM Abrigo a
    LEFT JOIN Vitima v ON a.cnpj = v.cnpjAbrigo
    GROUP BY a.nome;
    
    --2. Consulta para contar o número de desastres por região
    SELECT r.nomeRegiao, COUNT(d.codDesastre) AS total_desastres
    FROM Regiao r
    LEFT JOIN ocorrencia o ON r.codigoRegiao = o.codigoRegiao
    LEFT JOIN Desastre_Natural d ON o.codDesastre = d.codDesastre
    GROUP BY r.nomeRegiao;
    
    /*
    Explicação
    Regiao r: Seleciona a tabela Regiao e a apelida como r.
    LEFT JOIN ocorrencia o ON r.codRegiao = o.codRegiao: Faz um LEFT JOIN entre Regiao 
    e ocorrencia, garantindo que todas as regiões sejam incluídas, mesmo que não haja 
    desastres registrados para algumas delas.
    LEFT JOIN DesastreNatural d ON o.codDesastre = d.codDesastre: Faz um LEFT JOIN entre 
    ocorrencia e DesastreNatural, garantindo que todos os desastres relacionados à 
    ocorrência sejam considerados.
    GROUP BY r.nomeRegiao: Agrupa os resultados pelo nome da região.
    COUNT(d.codDesastre) AS total_desastres: Conta o número de desastres em cada região.
    */
    
    ```
    

- **1** consulta usando alguma operação de conjunto (union, except ou intersect)
    
    ```sql
    /* Consulta para encontrar vítimas que têm registros tanto na tabela Vitima 
    quanto na tabela DoacaoVitima */
    SELECT v.vitimaCpf
    FROM Vitima v
    INTERSECT
    SELECT dv.vitimaCpf
    FROM DoacaoVitima dv;
    ```
    

- **2** consultas que usem subqueries
    
    ```sql
    /* Consulta para encontrar desastres naturais que tiveram a atuação de uma agência 
    específica*/
    SELECT d.codDesastre, d.dataDeOcorrencia, d.duracao, d.intensidade, d.qtdVitimas
    FROM Desastre_Natural d
    WHERE d.codDesastre IN (
        SELECT a.codDesastre
        FROM atuacao a
        WHERE a.cnpjAgencia = '01234567000123'
    );
    
    -- Consulta para encontrar desastre com o maior número de vítimas
    SELECT d.codDesastre, d.dataDeOcorrencia, d.duracao, d.intensidade, d.qtdVitimas
    FROM Desastre_Natural d
    WHERE d.qtdVitimas = (
        SELECT MAX(dn.qtdVitimas)
        FROM Desastre_Natural dn
    );
    
    ```
    

- **1** visão que permita inserção
    
    ```sql
    CREATE VIEW vw_CategoriaResumo AS
    SELECT codCateg AS codCategoria, descricao, perecivel
    FROM Categoria;
    
    select * from vw_CategoriaResumo;
    ```
    

- **2** visões robustas (e.g., com vários *joins*) com justificativa semântica, de acordo com os  requisitos da aplicação.
    
    ```sql
    /*
    Visão 1: Resumo Detalhado de Desastres Naturais
    Objetivo: Fornecer um resumo detalhado de desastres naturais, incluindo informações 
    sobre a região afetada, o tipo de desastre, a quantidade de vítimas e as categorias 
    de doações associadas.
    
    Justificativa Semântica: Essa visão permite um entendimento abrangente dos desastres 
    naturais ocorridos, detalhando suas localizações, tipos, e impactos. Além disso, 
    inclui informações sobre doações relacionadas, auxiliando na análise de resposta a 
    emergências e planejamento futuro.
    */
    
    CREATE VIEW ResumoDesastres AS
    SELECT 
        D.codDesastre,
        D.dataDeOcorrencia,
        D.intensidade,
        D.qtdVitimas,
        R.nomeRegiao,
        T.descricao AS tipoDesastre,
        COALESCE(Ca.descricao, 'Não especificada') AS categoriaDoacao,
        COALESCE(SUM(DOA.qtdEstoque), 0) AS totalDoado
    FROM 
        Desastre_Natural D
    JOIN 
        ocorrencia O ON D.codDesastre = O.codDesastre
    JOIN 
        Regiao R ON O.codigoRegiao = R.codigoRegiao
    JOIN 
        TipoDesastre TD ON D.codDesastre = TD.codDesastre
    JOIN 
        Tipo T ON TD.codTipo = T.codTipo
    JOIN 
    	vitimaDesastre vd on d.coddesastre = vd.coddesastre
    join 
    	doacaovitima dv on vd.vitimacpf = dv.vitimacpf
    join
        Doacao DOA ON DOA.coddoacao = dv.coddoacao
    join
        Categoria Ca ON DOA.codCateg = Ca.codCateg
    GROUP BY 
        D.codDesastre, D.dataDeOcorrencia, D.intensidade, D.qtdVitimas, R.nomeRegiao, T.descricao, Ca.descricao;
    
    select * from ResumoDesastres;
    
    /*
    Visão 2: Resumo de Vítimas e Abrigos
    Objetivo: Fornecer um resumo das vítimas e dos abrigos que as receberam, incluindo 
    a condição médica e as doações recebidas.
    
    Justificativa Semântica: Esta visão oferece um panorama das vítimas acolhidas em 
    abrigos, suas condições médicas e as doações recebidas pelos abrigos. Tal visão é 
    fundamental para verificar o estado atual das vítimas, os recursos disponíveis e 
    planejar melhor a distribuição de assistência.
    */
    CREATE VIEW ResumoVitimasAbrigos AS
    SELECT 
        V.vitimaCpf,
        V.nome AS nomeVitima,
        V.condicaoMedica,
        A.nome AS nomeAbrigo,
        A.cidade,
        A.estado,
        SUM(DOA.qtdEstoque) AS totalDoacoes,
        C.descricao AS categoriaDoacao
    FROM 
        Vitima V
    JOIN 
        Abrigo A ON V.cnpjAbrigo = A.cnpj
    LEFT JOIN 
        DoacaoVitima DV ON V.vitimaCpf = DV.vitimaCpf
    LEFT JOIN 
        Doacao DOA ON DV.codDoacao = DOA.codDoacao
    LEFT JOIN 
        Categoria C ON DOA.codCateg = C.codCateg
    GROUP BY 
        V.vitimaCpf, V.nome, V.condicaoMedica, A.nome, A.cidade, A.estado, C.descricao;
    
    select * from ResumoVitimasAbrigos;
    ```
    

- **3** índices para campos indicados com justificativa dentro do contexto das consultas formuladas
    
    ```sql
    /*
    1.
    Realizar consultas que filtram ou ordenam com base no número de vítimas geram
    informações muito relevantes
    */
    CREATE INDEX idx_desastre_qtdVitimas ON Desastre_Natural(qtdVitimas);
    
    /*
    2.
    Pode ser útil fazer consultas envolvendo a quantidade em estoque das doações
    */
    CREATE INDEX idx_doacao_qtdEstoque ON Doacao(qtdEstoque);
    
    /*
    3.
    Pode ser útil fazer consultas que filtram ou ordenam os desastres naturais pela 
    data de ocorrência, como encontrar desastres ocorridos em um intervalo específico
    */
    CREATE INDEX idx_desastre_dataDeOcorrencia ON Desastre_Natural(dataDeOcorrencia);
    
    ```
    

- Identificar 2 exemplos de consultas dentro do contexto da aplicação (questão 2.a) que  possam e devam ser melhoradas. Reescrevê-las e justificar a reescrita.
    
    ```sql
    /* Reescrita da consulta para encontrar desastres naturais que tiveram a atuação de uma agência 
    específica*/
    SELECT DISTINCT d.codDesastre, d.dataDeOcorrencia, d.duracao, d.intensidade, d.qtdVitimas
    FROM Desastre_Natural d 
    INNER JOIN atuacao a ON d.codDesastre = a.codDesastre
    WHERE a.cnpjAgencia = '01234567000123';
    -- O join é mais otimizado em relação as subconsultas porque permitem que o banco de dados compare diretamente os dados de múltiplas tabelas 
    -- de forma eficiente, utilizando índices e otimizando o plano de execução. Além disso, evitam execuções repetitivas como ocorre em subconsultas. 
    -- Isso reduz o tempo de processamento e o uso de recursos.
    
    /*Reescrita da consulta que usa FULL OUTER JOIN para listar todos os registros de vítimas 
    e abrigos, mostrando todos os registros de ambas as tabelas. Se não houver 
    correspondência, os campos relacionados serão NULL.
    */
    -- Retorna todas as vítimas, mesmo que não tenham abrigo associado
    SELECT v.vitimaCpf, v.nome AS nome_vitima, v.condicaoMedica, a.cnpj, a.nome AS nome_abrigo, a.cidade
    FROM Vitima v
    LEFT JOIN Abrigo a ON v.cnpjAbrigo = a.cnpj
    -- O union faz a junção dos dois resultados garantindo que os valores com null permaneçam e elimina automaticamente duplicatas 
    UNION
    -- Retorna todos os abrigos, mesmo que não tenham vítimas associadas
    SELECT v.vitimaCpf, v.nome AS nome_vitima, v.condicaoMedica, a.cnpj, a.nome AS nome_abrigo, a.cidade
    FROM Vitima v
    RIGHT JOIN Abrigo a ON v.cnpjAbrigo = a.cnpj;
    -- Essa abordagem simula o comportamento do FULL OUTER JOIN de uma forma que pode ser mais eficiente em bancos de dados que não lidam bem com o FULL OUTER JOIN. 
    -- O uso de LEFT JOIN + RIGHT JOIN com UNION garante que se obtenha todas as combinações de registros, assim como o FULL OUTER JOIN, mas com a flexibilidade de otimizar índices e controlar melhor o desempenho.
    ```
    

- **1** função que use SUM, MAX, MIN, AVG ou COUNT
    
    ```sql
    --A função retornará o desastre natural mais recente com base na data de ocorrência.
    CREATE OR REPLACE FUNCTION desastre_mais_recente()
    RETURNS varchar AS $$
    DECLARE
        rec RECORD;
        msg varchar;
    BEGIN
        -- Seleciona o desastre mais recente e armazena o resultado na variável de registro
        SELECT
            dn.codDesastre,
            dn.dataDeOcorrencia,
            dn.qtdVitimas
        INTO rec
        FROM Desastre_Natural dn
        WHERE dn.dataDeOcorrencia = (
            SELECT MAX(dn2.dataDeOcorrencia)
            FROM Desastre_Natural dn2
        );
    
        -- Formata a mensagem usando os dados do desastre mais recente
        msg := format(
            'O desastre mais recente é o de código %s, ocorrido em %s, com %s vítimas',
            rec.codDesastre,
            rec.dataDeOcorrencia::text,
            rec.qtdVitimas
        );
    
        RETURN msg;
    END;
    $$ LANGUAGE plpgsql;
    
    -- Executando a função:
    SELECT desastre_mais_recente();
    
    ```
    

- Outras **2** funções com justificativa semântica, conforme os requisitos da aplicação
    
    ```sql
    --1. Esta função contará a quantidade de relatos associados a um desastre natural
    drop function contar_relatos_por_desastre(codigoDesastre INT);
    CREATE OR REPLACE FUNCTION contar_relatos_por_desastre(codigoDesastre INT)
    RETURNS INT AS $$
    DECLARE
        contador INT := 0;
        c_desastre CURSOR FOR
            SELECT codigoRelato
            FROM Relato r
            WHERE r.codDesastre = codigoDesastre;
    BEGIN
        for cur in c_desastre loop
            contador := contador + 1;
    	end loop;
        RETURN contador;
    END;
    $$ LANGUAGE plpgsql;
    
    select contar_relatos_por_desastre(1);
    
    /*2. função recebe como parametro o codigo do desastre e mostra a quantidade de 
    vitimas no banco de dados*/
    
    drop function contar_vitimas_por_desastre(INT);
    CREATE OR REPLACE FUNCTION contar_vitimas_por_desastre(codigoDesastre INT)
    RETURNS INT AS $$
    DECLARE
        contador INT := 0;
        cur CURSOR FOR
            SELECT vitimaCpf
            FROM VitimaDesastre
            WHERE codDesastre = codigoDesastre;
        vitima RECORD;
    BEGIN
        OPEN cur;
        LOOP
            FETCH cur INTO vitima;
            EXIT WHEN NOT FOUND;
            contador := contador + 1;
        END LOOP;
        CLOSE cur;
        RETURN contador;
    END;
    $$ LANGUAGE plpgsql;
    
    SELECT contar_vitimas_por_desastre(5);
    ```
    

- **1** procedure com justificativa semântica, conforme os requisitos da aplicação
    
    ```sql
    /*Esta procedure atualizará a quantidade de estoque de doações e 
    irá lidar com exceções, como tentar atualizar um estoque que não existe.*/
    CREATE OR REPLACE PROCEDURE atualizar_estoque_doacao(
        p_codDoacao INTEGER,
        p_nova_qtde INTEGER
    )
    LANGUAGE plpgsql
    AS $$
    BEGIN
        -- Atualiza a quantidade de estoque
        UPDATE Doacao
        SET qtdEstoque = p_nova_qtde
        WHERE codDoacao = p_codDoacao;
    
        -- Verifica se a atualização foi bem-sucedida
        IF NOT FOUND THEN
            RAISE EXCEPTION 'Doação com código % não encontrada.', p_codDoacao;
        END IF;
    
        -- Notificação de sucesso
        RAISE NOTICE 'Estoque da doação com código % atualizado para %.', p_codDoacao, p_nova_qtde;
    
    EXCEPTION
        WHEN OTHERS THEN
            RAISE EXCEPTION 'Erro ao atualizar estoque: %', SQLERRM;
    END;
    $$;
    ```
    

- 3 diferentes triggers com justificativa semântica, de acordo com os requisitos da
aplicação
    
    ```sql
    /*
    1.
    Se um abrigo tiver mais de 10 vítimas associadas, a sua disponibilidade é 
    automaticamente ajustada para FALSE, indicando que não há mais vagas disponíveis. 
    Caso contrário, a disponibilidade é definida como TRUE.
    */
    CREATE OR REPLACE FUNCTION atualizar_disponibilidade_abrigo() 
    RETURNS TRIGGER AS $$
    BEGIN
        -- Verifica o número de vítimas associadas ao abrigo
        DECLARE
            numero_vitimas INT;
        BEGIN
            -- Conta o número total de vítimas associadas ao abrigo
            SELECT COUNT(*) INTO numero_vitimas
            FROM Vitima
            WHERE cnpjAbrigo = NEW.cnpjAbrigo;
    
            -- Atualiza a disponibilidade com base no número de vítimas
            IF numero_vitimas > 10 THEN
                UPDATE Abrigo
                SET disponibilidade = FALSE
                WHERE cnpj = NEW.cnpjAbrigo;
            ELSE
                UPDATE Abrigo
                SET disponibilidade = TRUE
                WHERE cnpj = NEW.cnpjAbrigo;
            END IF;
    
            RETURN NEW;
        END;
    END;
    $$ LANGUAGE plpgsql;
    
    -- Trigger para acionar a função após inserção ou exclusão de vítimas
    CREATE TRIGGER trg_atualizar_disponibilidade_abrigo
    AFTER INSERT OR DELETE ON Vitima
    FOR EACH ROW
    EXECUTE FUNCTION atualizar_disponibilidade_abrigo();
    
    /*
    2.
    Objetivo: Impedir que um abrigo receba mais voluntários do que uma capacidade máxima 
    predefinida.
    
    Justificativa Semântica: Esse trigger garante que os abrigos mantenham um limite 
    operacional de voluntários, evitando sobrecarga e garantindo que cada abrigo receba 
    uma quantidade controlada de voluntários. É importante para manter a eficiência 
    do gerenciamento de recursos humanos no abrigo.
    */
    CREATE OR REPLACE FUNCTION verificar_capacidade_voluntarios()
    RETURNS TRIGGER AS $$
    DECLARE
        qtd_atual_voluntarios INT;
        capacidade_maxima INT := 20; -- Definindo capacidade máxima como 20 voluntários
    BEGIN
        -- Contando a quantidade de voluntários associados ao abrigo
        SELECT COUNT(*)
        INTO qtd_atual_voluntarios
        FROM voluntarioAbrigo
        WHERE cnpjAbrigo = NEW.cnpjAbrigo;
    
        -- Verificando se a capacidade máxima foi atingida
        IF qtd_atual_voluntarios >= capacidade_maxima THEN
            RAISE EXCEPTION 'Abrigo com CNPJ % já atingiu a capacidade máxima de voluntários.', NEW.cnpjAbrigo;
        END IF;
    
        RETURN NEW; -- Permite a inserção caso a capacidade não tenha sido atingida
    END;
    $$ LANGUAGE plpgsql;
    
    CREATE TRIGGER trg_verificar_capacidade_voluntarios
    BEFORE INSERT ON voluntarioAbrigo
    FOR EACH ROW
    EXECUTE FUNCTION verificar_capacidade_voluntarios();
    
    /*
    3.
    Objetivo: Impedir que uma doação fique com valor igual a zero no estoque.
    
    Justificativa Semântica: Esse trigger garante que as doações não possuam valor igual a zero. 
    Estabelecendo dessa forma um valor mínimo de 10 itens, que ao ser atingido irá impedir que o usuário remova algum item até aumentar a quantidade existente.
    De modo que as vítimas fiquem sem o acesso a um item de necessidade.
    */
    CREATE OR REPLACE FUNCTION verificar_capacidade_estoque()
    RETURNS TRIGGER AS $$
    DECLARE
        qtd_atual_estoque INT;
        capacidade_minima INT := 10; -- Definindo capacidade mínima como 10 itens da doação
    BEGIN
        -- Contando a quantidade total de itens na doação, excluindo a quantidade do item que está sendo removido
        SELECT qtdEstoque
        INTO qtd_atual_estoque
        FROM doacao
        WHERE codDoacao = OLD.codDoacao;
        
        -- Verificando se a capacidade mínima será atingida após a exclusão
        IF qtd_atual_estoque - OLD.quantidade < capacidade_minima THEN
            RAISE EXCEPTION 'A doação com código % não pode ser removida porque a quantidade ficaria abaixo da capacidade mínima.', OLD.codDoacao;
        END IF;
    
        RETURN OLD; -- Permite a remoção caso a capacidade mínima não tenha sido atingida
    END;
    $$ LANGUAGE plpgsql;
    
    CREATE TRIGGER trg_verificar_capacidade_estoque
    BEFORE DELETE ON doacao
    FOR EACH ROW
    EXECUTE FUNCTION verificar_capacidade_estoque();
    
    ```