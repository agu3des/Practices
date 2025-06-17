a = int(input('Digite um número de 1 a 7: '))
if a == 1:
  result = 'Domingo'
elif a == 2:
  result = 'Segunda-feira'
elif a == 3:
  result = 'Terça-feira'
elif a == 4:
  result = 'Quarta-feira'
elif a == 5:
  result = 'Quinta-feira'
elif a == 6:
  result = 'Sexta-feira'
else:
  result = 'Sábado'
  

n = input('Digite um caractere do teclado: ').upper()

if n >= 'A' and n <= 'Z':
  if n in ('A','E','I','O','U'):
   result = 'vogal'
  else:
    result = 'consoante'
else:
 if n >= '0' and n <= '9':
  result = 'número'
 else:
  result = 'caractere especial'
print(f'É um/a {result}')

ano = int(input('Digite um ano: '))
if (ano % 4 == 0) and (not ano % 100 == 0) or (ano % 400 == 0) :
  print("bissexto")
else:
  print("não bissexto")

hinicio = int(input('Digite a hora inteira de início do jogo: '))
hfim = int(input('Digite a hora inteira de fim do jogo: '))
durjogomax = 24
if hinicio < hfim:
 durjogo = hfim - hinicio
else:
  durjogo = 24 - hinicio + hfim
print(f'{durjogo} horas.')

import math

print('Digite os coeficientes da equação de segundo grau:')
a = float(input('Digite o coeficiente a da equação: '))
b = float(input('Digite o coeficiente b da equação: '))
c = float(input('Digite o coeficiente c da equação: '))

delta = (b**2) - (-4 * a * c)
if delta < 0:
  print('Não tem raiz.')
else:
 x1 = (-b + math.sqrt(delta)) / (2 * a)
 x2 = (-b - math.sqrt(delta)) / (2 * a)
 print(f'{x1:.1f},{x2:.1f}')

print('Primeira Etapa')
n1 = float(input('Digite a primeira nota do candidato: '))
n2 = float(input('Digite a segunda nota do candidato: '))
med1 = (n1 + n2)//2
print(f'{med1}')
if med1 < 7:
  print('Candidato desclassificado.')
else:
  print('Candidado classificado.')
n3 = float(input('Digite a nota da segunda etapa: '))
if n3 < 8:
  print('Reprovado.')
else:
  print('Aprovado.')

