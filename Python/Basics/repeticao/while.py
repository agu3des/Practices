quant = 30
cont = 1
soma = 0
while cont <= quant:
  n = int(input())
  soma = soma + n
  cont = cont + 1
print('Soma =', soma)

soma = 0
cont = 0
n = int(input('Digite um número inteiro: '))
while n != 999:
 cont = cont + 1
 soma = soma + n
 n = int(input('Digite um número interiro: '))
media = soma/cont
print(f'A média entre os números é {media:.1f}')

flag = 0
print('Digite vários números.')
n = int(input('Digite um número inteiro: '))
maior = n
menor = n
while n != flag:
 if n > maior:
    maior = n
 if n < menor:
   menor = n
 n = int(input('Digite um número inteiro: '))  
print(f'{maior}, {menor}')

flag = 0
print(f'Informe os dados dos alunos. Para encerrar, digite a matrícula {flag}.')
mat = int(input('\nMatrícula: '))
while mat != flag:
    nome = input('Nome: ')
    nota1 = float(input('1ª Nota: '))
    nota2 = float(input('2ª Nota: '))
    media = (nota1 + nota2) / 2
    if media >= 7.0:
        sit = 'Aprovado'
    else:
        sit = 'Reprovado'
    print(f'\nMatrícula: {mat}')
    print(f'Nome: {nome}')
    print(f'Média: {media:.1f}')
    print(f'Situação: {sit}')
    mat = int(input('\nMatrícula: '))
print('Fim do programa.')

pergunt = 'sim'
while pergunt == 'sim':
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
       print('par')
    else: 
       print('ímpar')
    pergunt = input('Você desje continuar (sim/não)? ').lower()
    print()
print('Fim do programa.')

flag = 0
print(f'Informe as idades, para encerrar digite: {flag}')
idade = int(input('Digite a idade do visitante: '))
cont = 0
soma = 0
menor = idade
total

while idade != flag:
 if idade < menor:
  menor = idade
 if idade <= 21 and idade >= 18:
 media = soma/cont+1
 
 idade = int(input('Digite a idade do visitante: '))
 print()
print('Fim do programa.')

flag = 'x'
cod = 0
soma = 0
qtd = 0
valor = 0

cod = input('Digite o código correspondente: ')
qtd = int(input('Digite a quantidade desejada: '))

while cod != flag:
  if cod == 'H':
   valor = qtd * 5 
  elif cod =='C':
   valor = qtd * 6 
  elif cod == 'B':
   valor = qtd * 7 
  else:
   valor = qtd * 4 
  soma = soma + valor
  cod = input('Digite o código correspondente: ')
print(soma)






flag = 0
print(f'Informe as idades, para encerrar digite: {flag}')
idade = int(input('Digite a idade do visitante: '))
cont = 0
soma = 0
menor = 100

while idade != flag:
 if idade < menor:
  menor = idade
 if idade <= 21 and idade >= 18:
 
idade = int(input('Digite a idade do visitante: '))
media = soma/cont+1
print()
print('Fim do programa.')