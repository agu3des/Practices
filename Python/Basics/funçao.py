def menor(a,b,c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c

a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
m = menor(a,b,c)
print(f'O menor é {m}.')



def fatorial(a):
    fat = a
    while a-1 != 0:
       fat = fat*(a-1)
       a = a-1
    return fat
a = int(input('Digite um número: '))
fat = fatorial(a)
print(f'O fatorial de {a} é {fat}')


def vertical(n):
    vet = print(n[i])

n = input('Digite: ')
tam = len(n)
for i in range(tam):
  vet = vertical(n)


def soma(v):
    soma = 0
    for i in range(n):
     soma += v[i]
    return soma #não esquecer o return
n = int(input('Digite a quantidade de elementos do vetor: '))
v = [None]*n
for i in range(n):
  v[i] = int(input('Digite o elemento de v: '))
print(soma(v)) #já usa o print direto


def soma(a,b,c):
    soma = a+b+c
    return soma
def media(a,b,c):
    media = soma/3
    return media
def conceito():
  if media >= 8:
    return 'A'
  if media < 8 and media >= 5:
    return ' B'
  if media <= 5:
    return 'C'
n1 = int(input('Digite a 1º nota: '))
n2 = int(input('Digite a 2º nota: '))
n3 = int(input('Digite a 3º nota: '))
soma = soma(n1,n2,n3)
media = media(n1,n2,n3)
conceito = conceito()
print(f'{media}, {conceito}')



count = 0
def vogal(letra):
    if letra in 'AaEeIiOoUu':
        return True
    else:
        return False
f = input('Digite: ')
for caracter in f:
  if vogal(caracter):
    count += 1
print(count)


def email(login,provedor):
   return (f'{login}@{provedor}')
hey = []
while True:
   login = input('Digite seu login: ')
   if (login == 'x'):
    break
   else:
    provedor = input('Digite seu provedor: ')
    hey.append(email(login,provedor))
print(hey)


def primo(n):
    if n % 2 == 0:
     return False, 'Não é um número primo.'
    else:
     return True, 'É um número primo.'

num = int(input('Digite um número: '))
primo = primo(num)
print(primo)

for i in range(1,101):
 if primo(i):
  print(i,' ',end='')


#obs: para chamar um função tem que ser na ordem que ela está criada
def ler_vetor(n):
  v = [None]*n #vetor vazio
  for i in range(n): #para cada vetor
    v[i] = int(input('Digite os elementos do vetor: '))
  return v

def media_vetor(v):
  return sum(v)/len(v)

def cont_vetor(v,t):
  cont  = 0  #inicia a variável
  for elem in v: #testa o elemento
    if elem < t: #se for menor
      cont +=1 #adicione ao contador
  return cont

n = int(input('Digite a quantidade de números no vetor: '))
x = ler_vetor(n)
media = media_vetor(x)
quant = cont_vetor(x,media)
print(f'Existem {quant} elementos abaixo da média({media:.2f})')


def ler_matriz(lin,col):
  m = [[None]*col for i in range(lin)]
  for i in range(lin):
    for j in range(col):
      m[i][j] = int(input())
  return m

def imp_matriz(m):
  lin = len(m)
  col = len(m[0])
  for i in range():
    for j in range():
      print(f'{m[i][j]:4}', end='')
    print()

def soma_matriz(a,b):
  lin = len(a)
  col = len(a[0])
  c = [[None]*col for i in range(lin)]
  for i in range(lin):
    for j in range(col):
      c[i][j] = a[i][j] + b[i][j]
  return c

print('Digite a ordem das matrizes: ')
lin = int(input('Nº de linhas: '))
col = int(input('Nº de colunas: '))
m1 = ler_matriz(lin,col)
m2 = ler_matriz(lin,col)
m3 = soma_matriz(lin,col)
imp_matriz('1ª matriz: ',m1)
imp_matriz('2ª matriz: ',m2)
imp_matriz('3ª matriz: ',m3)


def fatorial(n):
  fat = 1
  for i in range(1,n+1):
    fat *= i
  return fat

def potencia(b,e):
  return b**e

import math
soma = 0
n = 0
x = float(input('Digite o valor do cosseno: '))
for i in range(1,21):
  termo = potencia(x,n)/fatorial(n)
  if i % 2 == 1:
    soma += termo
  else:
    soma -= termo
  n += 2
print(soma)
print(math.cos(x))


