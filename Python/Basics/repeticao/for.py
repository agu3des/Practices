import math
print(f'   x      raiz(x)    cubo(x)')
for x in range (50,301,5):
 raiz = math.sqrt(x)
 cubo = x ** 3
 print(f'{x:5} {raiz:10.4f} {cubo:10}')

n = int(input('Digite um número inteiro: '))
soma = 0
for i in range (1,n+1):
  soma += i
print(f'{soma}')

s = 1
n = int(input('Entre com um número inteiro: '))
for i in range (1,n+1):
  s = s*i
print(f'soma = {s}')

qtd = 20
print(f'Digite {qtd} números inteiros')
n = int(input())
maior = n
for i in range (qtd-1):
   n= int(input())
   if n >maior:
     maior = n
print('Maior =',maior)

qtdm = 0
qtdf = 0
qtd = int(input('Digite a quantidade de pessoas:'))

for i in range (qtd):
 sexo = input('Digite o sexo (F/M):') .upper
 if sexo == 'M':
  qtdm = qtdm + 1
 else:
   qtdf = qtdf + 1

percentm = qtdm/qtd *100
percentf = qtdf/qtd *100

print(f'A porcentagem de homens é {percentm}% e de mulheres é {percentf}%.')

n = int(input('Digite um número inteiro n: '))
x = int(input('Digite um número inteiro x: '))
y = int(input('Digite um número inteiro y: '))
print('Os múltiplos de',n,'entre',x,'e',y,'são:')
for i in range (x,y+1):
  if i % n == 0:
      print(i,end=' ')

n = int(input('Digite um número inteiro: '))
cont = 0
for i in range(2,n):
  if n % i == 0:
    cont = cont + 1
if cont == 0 and n != 1:
  print('primo')
else:
  print('não é primo')

import math
a = 0
n = int(input('Digite um número inteiro: '))
for i in range(1,n+1):
  raiz = math.sqrt(i)
  if raiz == int(raiz) and i > a:
    result = i
print(f'O maior quadrado perfeito é {result}')