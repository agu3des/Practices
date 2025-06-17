#1. Escreva um programa que leia um vetor A de N números inteiros (N será lido) e um outro inteiro K, construa e exiba um outro vetor B cujos elementos são os respectivos elementos de a multiplicados por K.
#Ex: A = [1,2,3], K = 5, B = [5,10,15].

n = int(input('Digite o número de elementos: '))
a = [None]*n
b = [None]*n

#leitura do vetor a
print('Informe os valores dos elementos do vetor a: ')
for i in range(n):
  a[i] = int(input(f'A[{i}]: '))

#leitura do valor k
k = int(input('Informe o valor de K: '))

#cálculo de b 
for i in range(n):
  b[i] = a[i]*k

#exibição dos resultados
print(f'A = {a}')
print(f'K = {k}')
print(f'B = {b}')

#sem novas "tags"
#Escreva um programa que leia um vetor V (contendo 30 inteiros) e um valor inteiro K, calcule e exiba a quantidade de ocorrências de K dentro de V.
n = 5  #por praticidade coloquei 5
v = [None]*n

print('Informe os elementos do vetor: ')
for i in range(n):
 v[i] = int(input())

k = int(input('Informe o valor a ser contado: '))

cont = 0
for e in v:
  if e == k:
    cont += 1
print(f'{k} ocorre {cont} vezes dentro do vetor.')

#com novas "tags"
import random
n = 30
v = [None]*n

print('Informe os elementos do vetor: ')
for i in range(n):
 v[i] = random.randint(1,10) #para pegar números no aleatório, o computador escolhe
print(v)

k = int(input('Informe o valor a ser contado: '))
print(v.count(k))


#Escreva um programa que leia um vetor V (contendo 30 inteiros) e um valor inteiro K, calcule e exiba a quantidade de ocorrências de K dentro de V.
import random
n = 30
v = [None]*n

print('Informe os elementos do vetor: ')
for i in range(n):
 v[i] = random.randint(1,10) #para pegar números no aleatório, o computador escolhe
print(v)

k = int(input('Informe o valor a ser contado: '))

cont = 0
for e in v:
  if e == k:
    cont += 1
print(f'{k} ocorre {cont} vezes dentro do vetor.')


#sem novas "tags"
#Escreva um programa que leia um vetor V contendo N elementos inteiros (N será lido) e um valor inteiro K, verifique e exiba se o K está ou não no vetor. Se estiver, informe em que posição (índice).
#Obs: K pode se repetir no vetor, nesse caso, mostre todas as posições onde o K aparece.

n = int(input('Digite a quantidade de vetores: '))
v = [None]*n #para poder pegar a quantidade que coloquei

print('Informe os elementos do vetor: ')
for i in range(n):
  v[i] = int(input()) #ele botou aleatório, mas tá certo

k = int(input('Informe o valor a ser contado: '))

for i in range(n):
  if v[i] == k:
   print(f'{k} está contido no vetor.')
   print(f'Suas posições são: {i}')
if v[i] != k:
  print(f'{k} não está contido no vetor.') #errei pq botei essa decisão dentro, ela tinha que ser antes/fora

#Escreva um programa que leia 10 números e armazene-os em um vetor. Exiba:
# Os números que estão nos índices pares;
# Os números que estão nos índices ímpares.

n = 3
v = [None]*n

print('Digite os elementos do vetor:')
for i in range(n):
  v[i] = int(input())
for i in range(n):
  if i % 2 == 0:
   print([i])
for i in range (n):
   if i % 2 != 0:
    print([i])

#Escreva um programa que receba um vetor V de N números inteiros (N será lido), determine e exiba o maior e o menor elemento deste vetor e seus respectivos índices.
#Obs: suponha a inexistência de valores repetidos.

n = int(input('Digite os elementos do vetor: '))
v = [None]*n
print('Digite os elementos do vetor: ')
for i in range(n):
  v[i] = int(input())
print(f'O maior é: ', max(v))
print(f'O menor é: ', min(v))


#Escreva um programa que leia um vetor de N números inteiros (N será lido), inverta a ordem dos elementos do vetor e exiba o vetor invertido. Ex: V = [1, 3, 5, 7], após a inversão: V = [7, 5, 3, 1].
#Obs: É necessário inverter os elementos do vetor, não basta imprimi-los em ordem inversa!
n = int(input('Digite a quantidade de vetores: '))
v = [None]*n
print('Digite os elementos do vetor: ')
for i in range(n):
  v[i] = int(input())
print(v)
v.reverse()
print(v)


import random
n = int(input('Digite o tamanho do vetor: '))
v = []
vp = []
vi = []
for i in range(n):
  numero = random.randint(1,30) #aleatório
  v.append(numero)
  if numero % 2 == 0:
    vp.append(numero) #adiciona os elementos
  else:
    vi.append(numero)
print('Vetor: ',*v)
print('Pares: ',*vp)
print('Ímpares: ',*vi)



contp = len(vp) #conta o tamanho do vetor
conti = len(vi)
soma = sum(v)
media = soma/n
print(f'A quantidade de elementos pares: {contp}')
print(f'A quantidade de elementos ímpares: {conti}')
print(f'A soma de todos os elementos: {soma}')
print(f'A média dos elementos do vetor: {media}')



import random
n = int(input('Digite o número de elementpos do vetor: '))
a = [None]*n
b = [None]*n
c = [None]*n*2 # vai receber n e multiplicar por 2, já que quer o dobro
for i in range(n):
  a[i] = random.randint(1,20)
for i in range(n):
  b[i] = random.randint(1,20)
for i in range (n): #se o n for 6 vai até 5 
 c[i*2] = a[i] #pega o a, depois pega o b #quando for o a é sempre o dobro
 c[i*2+1] = b [i] #quando for b a relação é o dobro mais 1
print('A = ',*a) #a multiplicação é só pra não sair com os colchetes
print('B = ',*b)
print('C = ',*c)


v = [None]*6
print('Digite 6 números inteiros: ')
for i in range(6):
  v[i] = int(input())
for e in v:
  if v.count(e) > 1:
    print(e,'se repete.')
  else:
    print(e,'não se repete')

#PROFESSOR
v = []
while True:
  n = int(input('Digite um número inteiro: '))
  if n not in v:
     v.append(n) #vai adicionar
  else:
    print('Número já existente.') #se o número já existe ele não coloca dentro do vetor, nem conta no 6
  if len(v) == 6:  #vai repetir até o tamanho chegar em 6
    break
print(v)

vda = [None]*8
vs = [6,7,13,14,26]

for i in range(20): #pegar os 20 apostadores
  pontos = 0
  for j in range(8): #pegar as apostas de cada um
    vda[j] = int(input('Digite a dezena: '))
  for dezena in vda:
    if dezena<1 or dezena>80 or vda.count(dezena)>1:
      print('Aposta inválida')
      break
    else: 
      if dezena in vs:
         pontos += 1
  print('Aposta: ', vda)    
  print('Sorteio: ', vs)   
  print('Pontos: ', pontos)
  print()




n = int(input('Digite a quantidade de elementos do vetor: '))
k = int(input('Digite um valor: '))
a = [None]*n
b = [None]*n
for i in range(n):
    a[i] = int(input('Digite os elementos de a: '))
for i in range(n):
    b[i] = a[i]*k
print(a)
print(b)

cont = 0
n = 5
v = [None]*n
k = int(input('Digite um valor para K: '))
for i in range(n):
    v[i] = int(input('Elemento do vetor: '))
for i in range(n):
    if v[i] == k:
        cont += 1
print('Vetor:', v)
print('Quantidade de Ks no vetor: ', cont)


n = int(input('Digite a quantidade de elementos: '))
v = [None]*n
k = int(input('Digite um valor para K: '))
for i in range(n):
    v[i] = int(input('Digite o elemento: '))

if k in v:
 True
 for i in range(n):
    if k == v[i]:
        print(f'O valor {k} está no vetor.',end=' ')
        print(f'Índice: {i}')
else:
 False
 print(f'O valor {k} não está no vetor.')


n = 5
v = [None]*n
for i in range(n):
    v[i] = int(input('Elemento do vetor: '))
print(v)
for i in range(n):
    if i % 2 == 0:
        print('Pares: ',v[i])
    if i % 2 != 0:
        print('Ímpares: ',v[i])


