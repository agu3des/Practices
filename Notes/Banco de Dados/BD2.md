# BD2

[Projeto ](BD2%20c9497986ed1649d5b3669def31ffa7fb/Projeto%20b3f7322f619e4f01a8ab31065e5438d7.md)

IS_TEMPLATE: This parameter is used when you want to clone the database. If the value of the parameter is set to TRUE, then any user can clone the database. **If the value of the parameter is set to FALSE, then only the database owner or superuser can clone it**.

**INSERT**

INSERT INTO produto VALUES (1, ‘Queijo', 9.99);
INSERT INTO produto (num, nome, preço)
VALUES (1, ‘Queijo', 9.99);

INSERT INTO produto (num, nome, preço)
VALUES (1, ‘Queijo', DEFAULT);

INSERT INTO produto (num, nome, preço) VALUES (1, ‘Queijo', 9.99), (2, ‘Pão', 1.99), (3, ‘Leite', 2.99);

**UPDATE**

UPDATE produto
SET preço = 10
WHERE preço = 5;

UPDATE produto
SET preço = preço * 1.10;

UPDATE teste
SET a = 5, b = 3, c = 1
WHERE a > 0;

**DELETE**

DELETE FROM produto
WHERE preço = 10;

DELETE FROM
produto;

**SELECT**

```sql
Select [distinct] {*,colunas [alias],
      expressões, funções}
From {tabelas [alias]}
[Where condições]
[Group by colunas]
[Having condição]
[Order by colunas [ASC|DESC]];
```

![Untitled](BD2%20c9497986ed1649d5b3669def31ffa7fb/Untitled.png)

![Untitled](BD2%20c9497986ed1649d5b3669def31ffa7fb/Untitled%201.png)

### Join:

As funções são muito intuitivas, ex: monthname = nome do mês 

Consultas combinadas

Unir tudo

Permite que sejam combinados dados de tabelas (2 ou +)

```sql
 select f.ident, f.nome, d.numero, d.nome
 --essa letra é o alias
 from funcionario f cross join/join departamento d
									--pega tudo 
										inner join/join
 on f.dnumero = d.numero --faz um filtro e sai somente onde essa igualdade é estabelecida
									  left join --pega tudo que está na tabela da esquerda/exemplo valores nulos
									  right join
									  union/full outer join --junta o left e o right join
									  --usar a mesma tabela com alias diferentes auto-relacionamento
```

### Subquery:

Subconsulta é uma consulta aninhada

Depende do valor de uma consulta externa

Podem ser substituídas por join

Uma subconsulta correlacionada pode referenciar a qualquer nível na consulta principal, desde que seja mais alto que seu próprio nível 

- Escalares: recuperam um único valor, aparecem como parte de uma expressão em uma lista de itens select, where ou having

```sql
selct job, 
	(select avg(salary) 
		from employee)
	as 'Avg Sal'
from employee
```

- Tabela: recuperam mais de um valor ou linha de valores

- Aninhadas: Recuperam mais de uma coluna ou linha, aparecem em cláusulas de from de instruções de select

```sql
selct avg(edlevel) , avg(salary) 
from (select edlevel, salary
		from employee) as 'emprand'
group by edlevel
```

Uma subconsulta não pode ter order by

Não pode estar confinada em uma função agregada

Subconsultas podem estar relacionadas com outras instruções, insert, update e delete

```sql
--Tabela ainhada generalizada
SELECT column1, column2,...(scalar subquery)--scalar subconsulta na lista de intens select ou where ou having de uma subconsulta
FROM table1,...(nested table subquery) --nested subconsulta aninhada no from com as
AS subquery_table_name]
WHERE foo = (scalar subquery)
OR foo in (table subquery)--subquery no where quando se tem: in, any, some, exists, all

--exemplo:
SELECT column1
FROM table1 AS t1
WHERE foo IN --cláusula in apenas para exemplo
	(SELECT value1
	FROM table2 AS t2
	WHERE t2.pk_identifier = t1.fk_identifier)
```

### Visão (view):

você tem acesso a uma parte dos dados

```sql
CREATE [ OR REPLACE ] [ TEMP ] VIEW
name [ ( column_name [, ...] ) ]
AS query
[ WITH CHECK OPTION ]

--Temp: a view não deve ser armazenada
--Replace: recria a view, caso já exista
--With Check Option:
--Esta opção está associada às visões atualizáveis. Novos dados
--devem satisfazer às condições que definem a visão. Se as
--condições não forem satisfeitas, a atualização será rejeitada.
```

Os dados da view não é guardado

a view é um resumo de uma tabela ou um conjunto de tabelas

Dá a impressão de uma tabela física, mas ela não é

Os dados dela não são armazenados, mas ela é

o comando temp ao lado da view vai dizer que a visão (o comando) não deve ser armazenado nos esquemas

Tem 2 tipos: 

1. **simples** (quero uma parte do bd, posso dar insert e update, alterando o do bd real, tem que ter consistência - se algo é null na tabela de origem na view tem que ter)

![Untitled](BD2%20c9497986ed1649d5b3669def31ffa7fb/Untitled%202.png)

1. **complexa** (view resultante do cruzamento de várias tabela, não posso dar nem insert nem update)

![Untitled](BD2%20c9497986ed1649d5b3669def31ffa7fb/Untitled%203.png)

Ver o comando da view:

![Untitled](BD2%20c9497986ed1649d5b3669def31ffa7fb/Untitled%204.png)

```sql
[ WITH [recursive] <common_table_expression>
[ ,...n ] ]
<common_table_expression>::= expression_name
[ ( column_name [ ,...n ] ) ] AS (
CTE_query_definition )

--CTE_query_definition
--Especifica uma instrução SELECT cujo conjunto de
--resultados popula a expressão de tabela comum

with nomeEng as (select nome
				from engenheiro 
				where codeng not in 
				 (select codeng from atuacao))
select * from nomeEng;

with EngenheirosComAtuacao as (
    select codeng
    from atuacao
),
EngenheirosSemAtuacao as (
    select nome
    from engenheiro
    where codeng not in (select codeng from EngenheirosComAtuacao)
)
select nome from EngenheirosSemAtuacao;
```

### Funções Extras

```sql
--funcoes extras -> numeros
select abs(-15)"Valor Absoluto";
select ceil(15.7);
select floor(15.7);
select mod(10,4);
select power(3,2);
select round(15.193,1) "Round";
select round(42.4382,2);
select trunc(42.8);
select trunc(42.4382,2);

--funcoes extras -> caracteres
Select CONCAT(CONCAT(primeironome,' é'),cargo)
From empregado
Where matricula = 12;
Select primeironome || ' é '||cargo
From empregado
Where matricula = 12;

Select INITCAP('si');
Select LOWER('SI') "Minúsculas";
Select REPLACE('Juliana','Juli','Mari');
Select SUBSTR('Juliana',1,4);
Select UPPER('Informática');
Select LENGTH('Informatica');
Select LPAD('1234',10,'0'); --esse numero com 10 caraacteres, ele completa com zeros
Select RPAD('1234',10,'0');

--funcoes datas
Select TO_CHAR(Current_date,'MM-DD-YYYY') "Hoje";
Select age(timestamp '2024-03-18', timestamp'2004-06-05');
Select age(timestamp '1999-06-13');
Select current_time;
Select now();
select primeironome,
extract(year from dataadmissao) Ano from empregado;

--funcoes de conversao
Select to_char(current_date,'MONTH,DD,YYYY,HH24:MI:SS'); --data - varchar especificado
Select to_char(current_timestamp,'HH12:MI:SS');
Select to_char(10000,'L99G999D99') "Valor";--integer - varchar especificado
Select To_date('01052016','DD/MM/YY'); --char/varchar - date
SELECT to_number('1210.73', '9999.99');--char/varchar - numeric
Select to_timestamp('05 Dec 2017','DD Mon YYYY'); --string - timestamp

--funcoes genericas
Select coalesce(null,'Nao preenchido','Nada');--verifica todos os campos , se for nulo ele pula, se n achar ele manda a mensagem, 1° que nao e nulo

Select primeironome, salario, --coluna de acordo com condicoes
	case when salario < 1000 then 'Baixa'
		when salario > 1000 and salario < 2000
			then 'Média'
		when salario > 2000 then 'Boa'
	end faixa
From empregado;

Select descricao as "Descrição", valor as "Valor atual",
	case
		when valor < 10 then valor * 0.3
	when valor >=10 and valor < 13 then valor * .2
	else valor * .1
	end as "Percentual"
	from produto;
	
Select greatest(2,4,3,6) "Greatest"; --maior de uma lista
Select least(2,4,3,6) "Least"; --menor de uma lista
```

**Acid**

Atomicidade: ou tudo vai ou não vai nada

Consistencia: a execução deve estar consistente

Isolamento: as transações não podem ter conhecimento do outro de modo a não ocorrer leitura de dados errados

Durabilidade: as mudanças devem ser persistentes

Os estágios intermediários não podem estar acessíveis para outras transações, se dois ou mis usuários estiverem alterando eles só poderão visualizar as alterações a partir do momento que um deles dê commit

![Untitled](BD2%20c9497986ed1649d5b3669def31ffa7fb/Untitled%205.png)

```sql
--postgrees
insert into vendedor values(26, 'Vinícius Júnior', '17/04/2003', 2800, 'B');
commit;--ao commitar vai liberar para o outro usuário
--ago
insert into vendedor values(26, 'augustinho Carrara', '11/05/1973', 2800, 'C');--fica waiting
--quando o outro usuário der commit ele vai dar erro dizendo que a chave não pode ser acessada/ se o outro der rollback, dá certo
```

### Index

```sql
--postgrees
create index idx_nome on disciplina(nome)
```

Tornar mais rápida a procura, para databases maiores funciona melhor

Utiliza árvore binária

Por que não se aplica a todas as colunas

"pg_catalog” = índice criado automaticamente

![Untitled](BD2%20c9497986ed1649d5b3669def31ffa7fb/Untitled%206.png)

![Untitled](BD2%20c9497986ed1649d5b3669def31ffa7fb/Untitled%207.png)

width = largura em bytes do registro

cost = tempo em milisegudos estimado

rows = linhas

hash e hash join é mais rápido com tabelas maiores do que os outros

![Untitled](BD2%20c9497986ed1649d5b3669def31ffa7fb/Untitled%208.png)

## Código

### Plpgsql

bloco anonimo nõ está associado anenhum função/procidery, ele não salva, executa e pronto

▪ Procedimento: bloco nomeado, guardado no BD, pode ser
chamado por qualquer outro procedimento/função; pode receber
argumentos na chamada. Não retorna valor.

e.g., processarProdução(mês);

▪ Função: bloco nomeado, guardado no BD, podendo ser
chamado por qualquer outro procedimento/função; pode receber
argumentos na chamada. Retorna um valor e pode ser
atribuído a uma variável.

e.g., Var_mensal:= calcularMensalidade(matriculaAluno);
▪ Trigger: Rotina disparada automaticamente normalmente
antes ou depois de um evento como comandos UPDATE,
INSERT ou DELETE.

```sql
DO $$DECLARE i int:= 0;
BEGIN
	WHILE I <= 1000000 LOOP
		INSERT INTO testaEMP select
from empregado;
		I := I + 1;
	END LOOP;
END$$;
```

### Variáveis

▪ Modularidade: códigos devem residir em blocos pequenos
▪ Processamento: decisão, repetição, sequência
▪ Variáveis: tipos primitivos (char, integer) e compostos
(registros, vetores)

name [ CONSTANT ] type [
NOT NULL ] [ { DEFAULT |
:= | = } expression ];
° qualquer datatype válido para
SQL
° DEFAULT especifica o valor
inicial atribuído à variável
• Se não for fornecida, a variável
será inicializada com valor
nulo

° CONSTANT impede que a
variável seja atribuída após a
inicialização

```sql
BEGIN
tax = subtotal * 0.06;
my_record.user_id := 20;
valor := (horas_trabalhadas * salario_hora) + bonus;
país = 'France';
país := UPPER('Canada');
valid_id := TRUE;
empRec.firstName = 'Antonio';
empRec.lastName := 'Ortiz';
END;
```

%type: sempre terá o mesmo tipo de uma coluna da
tabela

```sql
idcli cliente.codcli%type;
```

Nome_variável tabela%ROWTYPE;
Variável com exatamente a mesma estrutura/tipo de
uma tabela = REGISTRO

Declare

```sql
V_vendedor_rec vendedor%ROWTYPE;
```

strict: forçar ser algo, tem que ser isso se não quebra

SELECT expressions INTO [STRICT] target FROM ...;
Onde target pode ser uma variável de registro, uma variável
de linha ou uma lista de variáveis (separadas por vírgula)

Select x into strict y from tabela where id = 1;

```sql
DECLARE
bonus numeric(8,2);
emp_id integer := 100;
BEGIN
SELECT salary * 0.10 INTO bonus
FROM employees
WHERE employee_id = emp_id;
END;
```

raise notice 'Mensagem a ser mostrada’;

Ou

```sql
RAISE NOTICE ''O valor da variável é %'',
variavel;
```

* No exemplo, o símbolo % será substituído pelo valor
presente em variavel.

E.g., raise notice 'Nome = %', nomeVar;

### Condições

```sql
IF boolean-expression THEN statements END IF;
IF v_user_id <> 0 THEN
UPDATE users SET email = v_email
WHERE user_id = v_user_id;
END IF;

IF boolean-expression THEN statements
ELSE statements

END IF;
IF v_count > 0 THEN
INSERT INTO users_count (count) VALUES (v_count);
RETURN 't';
ELSE RETURN 'f';
END IF;

IF boolean-expression THEN statements [ ELSIF boolean-
expression THEN statements [ ELSIF boolean-
expression THEN statements ...]] [ ELSE statements ]

END IF;
IF number = 0
THEN result := 'zero';
ELSIF number > 0
THEN result := 'positive';
ELSIF number < 0
THEN result := 'negative';
ELSE
-- hmm, that number is null
result := 'NULL';

END IF;
```

```sql
CASE search-expression
WHEN expression [, expression [ ... ]] THEN statements
[ WHEN expression [, expression [ ... ]] THEN statements
... ]
[ ELSE statements ]
END CASE;

CASE
WHEN x BETWEEN 0 AND 10
THEN msg := 'value is between zero and ten';
WHEN x BETWEEN 11 AND 20
THEN msg := 'value is between eleven and twenty';

END CASE;
```

### Repetições

```sql
[<<label>> ]
LOOP
statements
EXIT [ label ] [ WHEN boolean-expression ];
END LOOP [ label ];
<<ablock>>
LOOP
-- some computations
IF stocks > 100000
THEN EXIT ablock;
-- computations here will be skipped when stocks > 100000
END Loop;
```

```sql
[ <<label>> ]
WHILE boolean-expression LOOP
statements
END LOOP [ label ];

WHILE amount_owed > 0 AND gift_certificate_balance > 0
LOOP
-- some computations here
END LOOP;
```

```sql
[ <<label>> ]
FOR name IN [ REVERSE ] expression .. expression [ BY
expression ] LOOP
statements
END LOOP [ label ];
FOR i IN 1..10 LOOP
<comandos>
END LOOP;
FOR i IN REVERSE 10..1 LOOP
<comandos>
END LOOP;
FOR i IN REVERSE 10..1 BY 2 LOOP
<comandos>
END LOOP;
```

### Cursor

```sql
DO $$
	Declare
		vdesc categoria.desccateg%type;
		vcursor_categ CURSOR for
			Select desccateg from categoria;
Begin
	For vcat IN vcursor_categ LOOP
		vdesc := vcat.desccateg;
		raise notice 'Nome Categoria = %', vdesc;
	END LOOP;
End$$;
```

Percorre tipo um for each, para cada um jogue isso

```sql
DO $$
Declare
	localpais artista.pais%TYPE;
	c_artista Cursor (v_pais artista.pais%TYPE) for
		Select * From artista where pais = v_pais;
Begin
	localpais := 'Brasil';
	raise notice 'País = %', localpais;
	For vart IN c_artista(localpais) LOOP
		raise notice 'Nome do Artista = %', vart.nomeart;
End Loop;
End$$;
```

Pode ser implícito

```sql
For varregistro IN (Select ...From ...Where...) LOOP
<comandos;>
End loop;
```

### Functions/Procedures

Function

```sql
CREATE [ OR REPLACE ] FUNCTION name ( [ [ argmode ] [
argname ] argtype [ { DEFAULT | = } default_expr ] [, ...] ] ) [
RETURNS rettype | RETURNS TABLE ( column_name column_type
[, ...] ) ] { LANGUAGE lang_name } | AS 'definition'

--Remover a function:
drop function insereCategoria(integer,varchar);

--Recompilar:
alter function insereCategoria;
```

```sql
Create or replace function soma(integer, integer)
returns integer as '
Select $1+$2;
' language SQL;

select soma(1,1);
```

```sql
CREATE OR REPLACE FUNCTION InsereCategoria
(codigo INTEGER, nome VARCHAR(25))
RETURNS void
AS $$
BEGIN
INSERT INTO categoria VALUES (codigo, nome);
END;
$$ LANGUAGE 'plpgsql';

Select * from Categoria;
Select InsereCategoria (7, 'Sci-Fi');
```

```sql
CREATE OR REPLACE function mostra_filmes (v_categoria IN
categoria.desccateg%type)
returns void
as $$
declare
vfilme cursor (v_categoria categoria.desccateg%type) for
select titulo, ano
from filme f join categoria c on f.codcateg = c.codcateg
where desccateg = v_categoria;

BEGIN
FOR v_f IN vfilme(v_categoria) LOOP
raise notice 'Título = %',v_f.titulo;
raise notice 'Ano = %',v_f.ano;
END LOOP;
END;
$$ LANGUAGE 'plpgsql';

Select mostra_filmes(‘Ação’);
```

```sql
Create or replace function contafilme (
cat IN categoria.desccateg%type)
RETURNS integer as $$
declare totalfilme integer;
Begin
Select count(*) into totalfilme
from filme f join categoria c on f.codcateg = c.codcateg
Where desccateg = cat;
Return totalfilme;
End;
$$ LANGUAGE 'plpgsql';

Select contafilme(‘Ação’);
```

Procedure

```sql
CREATE OR REPLACE PROCEDURE
mostraNumFilmes(nome varchar(25))
LANGUAGE plpgsql
AS $$
DECLARE
contador integer := 0;
BEGIN
Select count(*) INTO contador
From artista a join personagem p on a.codart = p.codart
Where a.nomeart = nome;
RAISE NOTICE '% Fez % filmes', nome, contador;
END $$;

Call mostraNumFilmes('Joaquin Phoenix');
Call mostraNumFilmes('Cameron Diaz');
```

### Trigger

```sql
create or replace function atualizaC()
returns trigger as $$ 
begin
	raise notice 'Troca realizada: Descrição de cargo mudou %', old.cargo || new.cargo;
	return new;
end;
$$ language 'plpgsql';

create trigger atualizaCargo
after update on empregado 
for each row Execute procedure atualizarCargo();

update empregado
set cargo = 'professor'
where cargo = 'Analista de sistemas Junior';
```

Como se fossem instanciadas várias variáveis com diferentes nomes e eu quero acessa-las

```sql
Select * from departamento;
CREATE OR REPLACE FUNCTION verificaop_Depto() RETURNS
TRIGGER AS $$
BEGIN
--Utiliza a variável TG_OP para descobrir a operação sendo realizada.
IF (TG_OP = 'DELETE') THEN
raise notice 'Operação Delete sobre %', TG_TABLE_NAME;
RETURN old;
ELSIF (TG_OP = 'UPDATE') THEN
raise notice 'Operação Update sobre %', TG_TABLE_NAME;
RETURN new;
ELSIF (TG_OP = 'INSERT') THEN
raise notice 'Operação Insert sobre %', TG_TABLE_NAME;
RETURN new;
END IF;
END;
$$ language plpgsql;

CREATE TRIGGER
TestaDepto_audit
AFTER INSERT OR UPDATE OR
DELETE ON departamento
FOR EACH ROW EXECUTE
PROCEDURE verificaop_Depto();
```

O trigger fica separado pois a função pode ser reutilizada para diferentes tabelas

**Statement:** ação única, ele só faz em uma e para, se forem 4 ele para na primeira

**Row:** ação contínua (como se percorresse a tabela), se você tem 4 linhas ele percorre as 4

```sql
select * from departamento;
Insert into departamento values (8,'Compras','Sede');
update departamento set local = 'Patos' where coddepto = 8;
delete from departamento where coddepto = 8;
```

```sql
drop trigger TestaDepto_audit on departamento;

-- Retire o “for each row”
CREATE TRIGGER TestaDepto_audit2 AFTER INSERT OR
UPDATE OR DELETE ON Departamento
EXECUTE PROCEDURE verificaop_Depto(); --só apaga de depatamento
```

O valor de retorno é ignorado para gatihos after de nível de linha

Before se o retorno for null a ação é abortada, logo para insert (new), update (new ou old), delete (old)

```sql
CREATE OR REPLACE FUNCTION impedeAlteração() RETURNS
TRIGGER AS $$
Declare
v_hoje integer;
v_agora integer;
Begin
v_hoje = to_number(to_char(current_timestamp,'d'),'99'); --converto o dia em formato de dois digitos e coloco para char e dps para numero
v_agora = to_number(to_char(current_timestamp,'hh24mi'),'9999');
If v_agora > 1330 then --mais tarde que 13h30min
RAISE EXCEPTION '%', 'Hora proibida para atualizações' USING
ERRCODE = 45000; --codigo de erro 
End if;
If v_hoje = 1 then --se a data for no dia primeiro
RAISE EXCEPTION '%', 'Dia proibido para atualizações' USING
ERRCODE = 45001;
End if; --caso não tenha esses erros ele vai pro new e faz a ação
return new;
End;
$$ language plpgsql;

CREATE TRIGGER empnotifTrig
BEFORE INSERT OR UPDATE ON empregado --quero bloquear insert e update
FOR EACH ROW EXECUTE PROCEDURE --para cada linha execute a função
impedeAlteração();

INSERT INTO empregado VALUES (18,'TESTE','Morais','12-03-2020','Gerente',10000,1,1);

select * from empregado;
select current_timestamp;

select * from empregado order by primeironome;
```

Eu consigo associar um trigger a uma view e ele consegue fazer a alteração nas duas tabelas

```sql
Create or replace view vPessoas as
select nome as nome, 'c' as tipo
from cliente
Union
Select nome, 'v' from vendedor;

Select * from vPessoas;

CREATE or replace FUNCTION insere_view_vPessoas()
RETURNS trigger AS $$
Declare v_cod_vend integer;
v_cod_cli integer;
Begin
Select max(codvend)+1 into v_cod_vend from vendedor;
Select max(codcli)+1 into v_cod_cli from cliente;
If new.tipo = 'c' then --é um cliente?
Insert into cliente(codcli, nome) values (v_cod_cli, new.nome);
Else --senão
Insert into vendedor (codvend,nome) values
(v_cod_vend,new.nome);
End if;
Return null; --não me interessa se é new ou old, pq é instedof
END;
$$ language plpgsql;

Create trigger insViewVPessoas
Instead of insert on vPessoas -- lugar do before e after
for each row
execute procedure insere_view_vPessoas();

select * from vendedor;
select * from cliente;
select * from vPessoas order by tipo;
insert into vPessoas values('Mercia','v');
insert into vPessoas values('Catarina','c');
```

```sql
create table tabClienteaudit(atualizacao integer, ultimadata date, quem
varchar);
select * from tabClienteaudit;

CREATE OR REPLACE FUNCTION registra_upd_cliente() RETURNS
TRIGGER AS $$
declare qtd_linhas integer;
Begin
select count(*) into qtd_linhas from tabClienteaudit;
if qtd_linhas = 0 then insert into tabclienteAudit values(1,current_date,
current_user);
else Update tabClienteAudit
Set atualizacao = atualizacao + 1, ultimadata = current_date, quem =

current_user;
end if;
return null;
End;
$$ language plpgsql;

CREATE TRIGGER cliente_audit AFTER UPDATE ON
cliente FOR EACH ROW
EXECUTE PROCEDURE registra_upd_cliente();

select * from cliente;
update cliente set cidade = 'João Pessoa' Where codcli = 1;
Select * from tabclienteAudit;
```

## Revisão prova 2

```sql
--Introdução:
create or replace function nome_funcao(parametro int)
	returns int as $$
	declare --declara as variáveis
		user_id integer;
		minhalinha nometabela%rowtype; --uma tupla que recebe os campos vazios de outra tabela já pronta
		meucampo nometabela.nomecoluna%type; --meu canto tem um tipo de um campo específico da tabela
		k integer := 10;
	begin --inicio da implementação
		return (algo);
	end;
$$language plpgsql

select nome_funcao(parametro);

--versao 1
create or replace function olaMundo() returns varchar as $$
begin 
	return 'Olá mundo!';
end;
$$ language plpgsql
--versao 2
create or replace function olaMundo() returns varchar as $$
declare msg varchar := 'Olá mundo!';
begin 
	return msg;
end;
$$ language plpgsql
--versao 3
create or replace function olaMundo(msg varchar) returns varchar as $$
begin 
	return msg;
end;
$$ language plpgsql

select olaMundo('Olá mundo!');

--criar um funcao que crie um objeto professor
create table professor (
	id integer primary key,
	nome varchar(100),
	dt_nasc date,
	salario numeric
);

create or replace function adiciona_professor(id integer, nome varchar, dt_nasc date, salario numeric)
returns void as $$
begin
insert into professor values(id, nome, dat_nasc, salario);
end;
$$ language plpgsql;

select adiciona_professor(1, 'Fulano', '10/08/2007', 1500)

--parametros
--in (entrada, opcional)
--out (saida) saida da função 
--inout (entrada e saida)
--não colocou nada por default é in

create or replace function hi_lo (a numeri, b numeric, c numeric, out hi numeric, out lo numeric) 
returns record as $$ 
--...
select hi_lo(10,20,30); --10,30
select * from hi_lo (310,20,30) --separa em colunas

--crie uma funcao min, avg, max para salário dos proessores
create or replace function min_avg_max_salario (out menor numeric, out media numeric, out maior numeric) 
as $$
begin
	select min(salario) from professor into menor;
	select round(avg(salario),2) from professor into media;
	select max(salario) from professor into maior;
end;
$$ language plpgsql;

select * from min_avg_max_salario();

--procedimento é uma funcao que nao retorna dados, ou seja, semelhante a uma funcao void

create or replace procedure insere_produto(desc_prod varchar, qtd int) as $$
declare
max int 
begin
select max(cod_prod) from produto into max;
insert into produto values (max+1, desc_prod, qtd);
end;
$$language plpgsql;
call insere_produto('leite',12);
--sobrecarga função para fazer a mesma coisa de uma procedure, com o mesmo nome, mas os parametros e seus tipos diferentes

-- if then else
if v_count > 0 then
	insert into users_count(count)
		values (v_count);
	return 't';
else return 'f';
end if;

-- if-then-elsif-else
if number = 0 then result := 'zero';
elsif number > 0 then resut := 'positive';
elsif number < 0 then result := 'negative';
else result := 'null';
end if;

-- uma funcao que dado o id de um prof retorna verdadeiro se ele ganhar mais que a média salarial
create or replace function maior_media(id_prof numeric) returns boolean
as $$
declare
media real;
salario_prof real;
begin 
select avg(salario) from professor into media;
select salario from professor where cod_prof = matricula into salario_prof;

if (salario > media) then return true;
else return false;
end if;
end;
$$ language plpgsql;

select * from maior_media(9);

--laço de repeticao while
while condicao loop ... end loop;

--uam funcao que dado um numero inteiro resulte no seu fatorial
create or replace function fatorial(n integer) returns integer as $$
declare 
fat integer := 1;
i integer := 2;
begin 
while (i <= n) loop
	fat := fat*i;
	i := i+1;
	end loop;
	return fat;
end;
$$ language plpgsql;
select fatorial(5);

for variavel in i..j loop comando end loop; (j-i+1)
for variavel in i..j by k loop comando end loop; (i=i+k) incrementos de k unidades
for variavel in reverse i..j loop comando end loop; 
for variavel in reverse i..j by k loop comando end loop; 

do $$
begin 
for counter in 1..5 loop 
	raise notice 'Counter: %', counter;
end loop;
end; $$ language plpgsql;

do $$
begin 
for counter in 1..5 by 2 loop 
	raise notice 'Counter: %', counter;
end loop;
end; $$ language plpgsql;

create or replace function fatorial(n integer) returns integer as $$
declare 
i integer;
fat integer := 1;
begin
if n < 2 then retun fat;
end if;
for i in 2..n loop
	fat := fat*i;
end loop;
end;
$$ language plpgsql;

--1. Triggers
--Questão: Crie um trigger que dispare uma ação toda vez que o salário de um empregado for atualizado. 
--O trigger deve armazenar a alteração em uma tabela de log chamada salario_log.

create table salario_log (
	id serial primary key,
	empregado_id int,
	old_salario numeric,
	new_salario numeric,
	modificado_em timestamp default current_timestamp
)

create or replace function log_salario_update()
returns trigger as $$

begin
	if old.salario <> new.salario then
		insert into salario_log(emprego_id, old_salario_new_salario)
		values (old.matricula, old.salario, new.salario);
	end if;
	return new;
end;
$$ language plpgsql;

create trigger trg_salario_update
after update of slario on empregado
for each row
execute function log_salario_update();

--2. Functions
--Questão: Crie uma função que calcule o tempo de serviço de um empregado em anos, com base na sua data de admissão.
create or replace function tempo_servico(id_empregado int)
returns int as $$

declare 
	tempo int;
begin
	select abs(extract(year from age(current_date,data_admissao))) into tempo from empregado
	where mtricula = emp_id; --tem que comparar é pra isso que se pega o id
	return tempo;
end;
$$ language plpgsql;

Aqui estão algumas questões relacionadas a banco de dados envolvendo triggers, functions, procedures, laços for, if, else, cursores, e manuseio de exceções com raise notice e raise exception. Abaixo, forneço exemplos práticos para cada conceito.

1. Triggers
Questão: Crie um trigger que dispare uma ação toda vez que o salário de um empregado for atualizado. O trigger deve armazenar a alteração em uma tabela de log chamada salario_log.
sql
Copiar código
CREATE TABLE salario_log (
    id SERIAL PRIMARY KEY,
    empregado_id INT,
    old_salario NUMERIC,
    new_salario NUMERIC,
    modificado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE OR REPLACE FUNCTION log_salario_update() RETURNS TRIGGER AS $$
BEGIN
    IF OLD.salario <> NEW.salario THEN
        INSERT INTO salario_log(empregado_id, old_salario, new_salario)
        VALUES (OLD.matricula, OLD.salario, NEW.salario);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_salario_update
AFTER UPDATE OF salario ON empregado
FOR EACH ROW
EXECUTE FUNCTION log_salario_update();
2. Functions
Questão: Crie uma função que calcule o tempo de serviço de um empregado em anos, com base na sua data de admissão.
sql
Copiar código
CREATE OR REPLACE FUNCTION calcular_tempo_servico(emp_id INT) RETURNS INT AS $$
DECLARE
    tempo_servico INT;
BEGIN
    SELECT EXTRACT(YEAR FROM AGE(CURRENT_DATE, dataadmissao))
    INTO tempo_servico
    FROM empregado
    WHERE matricula = emp_id;

    RETURN tempo_servico;
END;
$$ LANGUAGE plpgsql;

--3. Procedures
--Questão: Crie uma procedure que aumente o salário de todos os empregados em um determinado departamento por uma porcentagem fornecida.
create or replace procedure atualiza_cargo_emp(cod_depto integer)
```