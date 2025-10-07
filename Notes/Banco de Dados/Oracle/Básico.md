# Básico

Comandos de Manipulação de Banco de Dados

```sql
-- Criar um banco de dados (feito pelo DBA)
CREATE DATABASE nome_banco;

-- Selecionar um banco de dados (Oracle não usa diretamente, pois cada usuário já está vinculado a um schema)
ALTER SESSION SET CURRENT_SCHEMA = nome_schema;

-- Exibir todos os bancos de dados disponíveis (necessita privilégios)
SELECT * FROM v$database;

-- Exibir todos os schemas disponíveis
SELECT username FROM all_users;
```

---

Comandos de Manipulação de Tabelas

```sql
-- Criar uma tabela
CREATE TABLE empregado (
    id NUMBER PRIMARY KEY,
    nome VARCHAR2(100),
    cargo VARCHAR2(50),
    salario NUMBER(10,2),
    data_admissao DATE
);

-- Listar todas as tabelas do usuário atual
SELECT table_name FROM user_tables;

-- Exibir estrutura de uma tabela (DESCRIBE)
DESC empregado;

-- Alterar uma tabela (Adicionar coluna)
ALTER TABLE empregado ADD departamento VARCHAR2(50);

-- Alterar uma tabela (Modificar tipo de dado)
ALTER TABLE empregado MODIFY salario NUMBER(12,2);

-- Alterar uma tabela (Remover coluna)
ALTER TABLE empregado DROP COLUMN departamento;

-- Excluir uma tabela
DROP TABLE empregado;
```

---

Comandos de Manipulação de Dados (DML)

```sql
-- Inserir dados em uma tabela
INSERT INTO empregado (id, nome, cargo, salario, data_admissao) 
VALUES (1, 'Carlos Silva', 'Analista', 5000.00, TO_DATE('2024-01-10', 'YYYY-MM-DD'));

-- Inserir múltiplas linhas
INSERT ALL 
    INTO empregado (id, nome, cargo, salario, data_admissao) VALUES (2, 'Ana Souza', 'Gerente', 8000.00, SYSDATE)
    INTO empregado (id, nome, cargo, salario, data_admissao) VALUES (3, 'João Pedro', 'Desenvolvedor', 4500.00, SYSDATE)
SELECT * FROM dual;

-- Atualizar dados de uma tabela
UPDATE empregado 
SET salario = 5500 
WHERE id = 1;

-- Deletar todos os registros
DELETE FROM empregado;

-- Deletar um registro
DELETE FROM empregado WHERE id = 1;

-- Deletar todos os registros de uma tabela (sem remover a estrutura)
TRUNCATE TABLE empregado;
```

---

Consultas com SELECT

```sql
-- Selecionar todos os registros de uma tabela
SELECT * FROM empregado;

-- Selecionar colunas específicas
SELECT nome, cargo, salario FROM empregado;

-- Filtrar resultados com WHERE
SELECT * FROM empregado WHERE salario > 5000;

-- Ordenação de resultados (ASC = crescente, DESC = decrescente)
SELECT * FROM empregado ORDER BY salario DESC;

-- Contar registros
SELECT COUNT(*) FROM empregado;

-- Retornar valores distintos (sem duplicatas)
SELECT DISTINCT cargo FROM empregado;

-- Filtrar com operadores lógicos
SELECT * FROM empregado WHERE cargo = 'Desenvolvedor' AND salario > 4000;

-- Filtrar com LIKE (busca parcial)
SELECT * FROM empregado WHERE nome LIKE 'A%';  -- Começa com "A"
SELECT * FROM empregado WHERE nome LIKE '%o';  -- Termina com "o"
SELECT * FROM empregado WHERE nome LIKE '%Silva%';  -- Contém "Silva"

-- Limitar número de resultados (TOP não é suportado no Oracle, usa-se ROWNUM ou FETCH FIRST)
SELECT * FROM empregado WHERE ROWNUM <= 5;
SELECT * FROM empregado FETCH FIRST 5 ROWS ONLY;

-- Filtrar valores dentro de um intervalo (BETWEEN)
SELECT * FROM empregado WHERE salario BETWEEN 4000 AND 6000;

-- Filtrar valores dentro de um conjunto (IN)
SELECT * FROM empregado WHERE cargo IN ('Desenvolvedor', 'Gerente');

-- Função de agregação (SUM, AVG, MIN, MAX)
SELECT AVG(salario) AS media_salarial FROM empregado;
```

---

Junções (JOINs)

```sql
-- Criar tabelas relacionadas
CREATE TABLE departamento (
    id NUMBER PRIMARY KEY,
    nome VARCHAR2(100)
);

ALTER TABLE empregado ADD id_departamento NUMBER;
ALTER TABLE empregado ADD CONSTRAINT fk_emp_dep FOREIGN KEY (id_departamento) REFERENCES departamento(id);

-- INNER JOIN: Retorna registros que possuem correspondência nas duas tabelas
SELECT e.nome, e.cargo, d.nome AS departamento
FROM empregado e
INNER JOIN departamento d ON e.id_departamento = d.id;

-- LEFT JOIN: Retorna todos os registros da tabela à esquerda, mesmo sem correspondência
SELECT e.nome, e.cargo, d.nome AS departamento
FROM empregado e
LEFT JOIN departamento d ON e.id_departamento = d.id;

-- RIGHT JOIN: Retorna todos os registros da tabela à direita, mesmo sem correspondência
SELECT e.nome, e.cargo, d.nome AS departamento
FROM empregado e
RIGHT JOIN departamento d ON e.id_departamento = d.id;

-- FULL OUTER JOIN: Retorna todos os registros de ambas as tabelas
SELECT e.nome, e.cargo, d.nome AS departamento
FROM empregado e
FULL OUTER JOIN departamento d ON e.id_departamento = d.id;
```

---

Índices, Views e Stored Procedures

```sql
-- Criar um índice para melhorar a performance de consultas
CREATE INDEX idx_nome ON empregado(nome);

-- Criar uma View (tabela virtual baseada em uma consulta)
CREATE VIEW vw_empregados AS
SELECT nome, cargo, salario FROM empregado WHERE salario > 5000;

-- Usar a View
SELECT * FROM vw_empregados;

-- Criar uma Procedure armazenada
CREATE OR REPLACE PROCEDURE aumentar_salario(p_id NUMBER, p_percentual NUMBER) AS 
BEGIN
    UPDATE empregado
    SET salario = salario * (1 + p_percentual / 100)
    WHERE id = p_id;
    COMMIT;
END;
/

-- Executar a Procedure
BEGIN
    aumentar_salario(1, 10);
END;
/
```

---

Transações (Controle de Dados - TCL)

```sql
-- Iniciar uma transação
BEGIN;

-- Fazer alterações nos dados
UPDATE empregado SET salario = salario * 1.1 WHERE cargo = 'Desenvolvedor';

-- Confirmar as alterações (salvar no banco)
COMMIT;

-- Reverter as alterações (desfazer mudanças antes do commit)
ROLLBACK;
```