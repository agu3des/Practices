n = int(input('Digite um número inteiro: '))
if n % 2 == 0:
    result = 'Par'
else:
     result = 'Ímpar'   
print(f'O número {n} é {result}')

n = int(input("Digite um número inteiro: "))
if n % 2 == 0:
  print('par')
else:
  print('ímpar')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n2 > n1:
  print(f'{n1}, {n2}')
else:
  print(f'{n2}, {n1}')

n1 = int(input("Digite o 1° número: "))
n2 = int(input("Digite o 2° número: "))
if n1 > n2:
  print(n2,n1)
else:
  print(n1,n2)

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 >= n2 and n3:
 result = n1
if n2 >= n1 and n3:
  result = n2
if n3 >= n1 and n3:
  result = n3 
print(f'O maior é {result}')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 > n2 and n3:
 result = n1
elif n2 > n3:
  result = n2
else: 
  result = n3 
print(f'O maior é {result}')

nome = input('Nome: ')
sexo = input('Sexo(M/F):').upper()
if sexo == 'M':
  trat = 'Sr.'
else:
  trat = 'Sra.'
print(f'Olá, {trat} {nome}!')

sex1 = 'F'
sex2 = 'M'
nome = input('Digite o nome: ')
sexo = input('Digite o sexo: ')
if sexo == sex1:
 print(f'Olá, Sra.{nome}')
else:
  print(f'Olá, Sr.{nome}')

nome = input('Digite aqui o nome do vendedor: ')
totalven = float(input('Digite aqui o total de vendas do vendedor: '))
salariomin = float(input('Digite o valor do salário mínimo atual: '))
salariofim = totalven * 0.05
if salariofim > salariomin:
 print(f'O salário do funcionário {nome}, é: {salariofim}')
else:
   print(f'O salário do funcionário {nome}, é {salariomin}')

conceito_a = 'fortemente recomendado/a'
conceito_b_c = 'recomendado/a'
conceito_d = 'não recomendado/a'
nome = input('Digite o nome do estudante: ')
conceito = input('Digite o conceito do estudante: ')
if conceito == 'A' or conceito == 'a':
 result = conceito_a
elif conceito == 'B' or 'b' or 'C' or 'c':
  result = conceito_b_c
else:
  result = conceito_d
print(f'A recomendação do estudante {nome} é {result}.')