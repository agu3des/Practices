# plsql

Procedure language extension to sql with design features of programming language

![image.png](plsql%201b22e5a697c38027919cef680ef6c52f/image.png)

Criar funções e procedimentos, adicionar estruturas de controle a linguagem sql e realizar operações computacionais complexas

Cada sentença sql deve ser executada de modo individual pelo servidor, logo não é possível, por exemplo, utilizar a resposta de um select para outro 

Funções:

```sql
-- Funções
create function somefunc(integer, text) returns integer
as 'function body text'

-- o bloco é escrito da seguinte maneira:
declare
-- declara as variáveis
-- posso utilizar as variáveis declaradas aqui ou os parâmetros
user_id integer;
preco numeric;
url varchar;
minha_linha nometabela%rowtype; -- pega o tipo da linha dessa tabela, em formato de tupla separada pelo tipo dos campos
meu_campo nometabela.nomecoluna%type; -- vai ter o tipo de dado de uma das colunas da minhatabela
quantidade integer default 32; -- por padrão vai valer 32 mas pode ser alterada
uri varchar := 'http://mysite.com'; -- já começa com esse valor
k constant integer := 10; -- uma constante que não pode ser alterada
begin
-- início da implementação
end;

														-- nome + tipo || posso colocar só o tipo e chamá-los por $1 e $2
create function f_aplica_taxa(valor1 real, valor2 real) 
															-- se não coloca nada são parâmetros de entrada
returns real
as 
--declare
--valor1 alias for $1
begin 
return (valor1 + valor2) * 0.06;
end;

select f_aplica_taxa(10,30.50);
```

```sql
-- Primeiro exemplo pratico
															-- (msg2 varchar)
create or replace function f_ola_mundo() returns varchar as 
declare
msg varchar; 
begin 
return msg := 'Olá mundo!';
end;

select f_ola_mundo()

-- Segundo exemplo pratico

create table professor (
id integer,
nome varchar2(150),
dt_nasc date,
salario numeric
);

create or replace function f_adicionar_professor(id integer, nome  varchar2, dt_nasc date,
salario numeric)
returns void as
begin 
insert into professor values(id, nome, dt_nasc, salario);
end;

select f_adicionar_professor(1, 'Professor Obibario', '10/09/1990', 3000);

-- Terceiro exemplo pratico
create or replace function f_hi_lo (a numeric, b numeric, c numeric, out hi numeric, out lo numeric) 
returns record as
begin
hi := greatest(a,b,c);
lo := least(a,b,c);
end;

-- Quarto exemplo pratico
create or replace function f_min_avg_max(out menor numeric, out media numeric, out maior numeric) as
begin 
select min(salario) from professor into menor;
select round(avg(salario),2) from professor into media;
select max(salario) from professor into maior;
end;
```