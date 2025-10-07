# Funções

Funções de Manipulação de Strings

```sql
-- TO_CHAR: Converte números ou datas para uma string formatada
SELECT TO_CHAR(SYSDATE, 'DD/MM/YYYY') AS data_formatada;

-- SUBSTR: Extrai uma substring de uma string
SELECT SUBSTR('CommunityLink', 1, 8) AS resultado;

-- INSTR: Retorna a posição de uma substring em uma string
SELECT INSTR('CommunityLink', 'Link') AS posicao;

-- LENGTH: Retorna o tamanho (número de caracteres) de uma string
SELECT LENGTH('CommunityLink') AS tamanho;

-- REPLACE: Substitui uma substring por outra dentro de uma string
SELECT REPLACE('CommunityLink', 'Link', 'Hub') AS resultado;

-- CONCAT: Concatena (junta) duas strings
SELECT CONCAT('Hello', ' World') AS resultado;

-- UPPER: Converte uma string para letras maiúsculas
SELECT UPPER('sql') AS resultado;

-- LOWER: Converte uma string para letras minúsculas
SELECT LOWER('SQL') AS resultado;

-- LTRIM: Remove espaços ou caracteres do início de uma string
SELECT LTRIM(' Hello') AS resultado;

-- RTRIM: Remove espaços ou caracteres do final de uma string
SELECT RTRIM('Hello ') AS resultado;

-- TRIM: Remove espaços ou caracteres do início e do final de uma string
SELECT TRIM(' Hello ') AS resultado;
```

---

Funções Matemáticas

```sql
-- TO_NUMBER: Converte uma string para um número
SELECT TO_NUMBER('123.45') AS numero;

-- ROUND: Arredonda um número para o número especificado de casas decimais
SELECT ROUND(123.456, 2) AS resultado;

-- TRUNC: Trunca (corta) um número para o número especificado de casas decimais
SELECT TRUNC(123.456, 2) AS resultado;

-- MOD: Retorna o resto de uma divisão
SELECT MOD(10, 3) AS resultado;

-- CEIL: Retorna o menor número inteiro maior ou igual ao número fornecido
SELECT CEIL(12.34) AS resultado;

-- FLOOR: Retorna o maior número inteiro menor ou igual ao número fornecido
SELECT FLOOR(12.34) AS resultado;
```

---

Funções de Data e Hora

```sql
-- TO_DATE: Converte uma string para um formato de data
SELECT TO_DATE('2025-01-01', 'YYYY-MM-DD') AS data;

-- SYSDATE: Retorna a data e a hora atuais
SELECT SYSDATE AS data_atual;

-- CURRENT_DATE: Retorna a data atual no fuso horário do cliente
SELECT CURRENT_DATE AS data_atual;

-- ADD_MONTHS: Adiciona ou subtrai meses a uma data
SELECT ADD_MONTHS(SYSDATE, 2) AS nova_data;

-- MONTHS_BETWEEN: Calcula o número de meses entre duas datas
SELECT MONTHS_BETWEEN(SYSDATE, TO_DATE('2025-01-01', 'YYYY-MM-DD')) AS diferenca;

-- LAST_DAY: Retorna o último dia do mês de uma data específica
SELECT LAST_DAY(SYSDATE) AS ultimo_dia;
```

---

Funções de Manipulação de Nulos

```sql
-- NVL: Substitui valores nulos por um valor padrão
SELECT NVL(NULL, 'Valor padrão') AS resultado;
```

---

Funções de Agregação

```sql
-- SUM: Retorna a soma de um conjunto de valores
SELECT SUM(salario) AS total_salario FROM empregado;

-- AVG: Retorna a média de um conjunto de valores
SELECT AVG(salario) AS media_salario FROM empregado;

-- COUNT: Conta o número de linhas ou valores não nulos
SELECT COUNT(*) AS total_linhas FROM empregado;

-- MIN: Retorna o menor valor de um conjunto de valores
SELECT MIN(salario) AS menor_salario FROM empregado;

-- MAX: Retorna o maior valor de um conjunto de valores
SELECT MAX(salario) AS maior_salario FROM empregado;
```