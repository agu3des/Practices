n = int(input("Número de termos (valor maior ou igual a 2): "))
a = 0
b = 1
print(a,b,end=" ")
for i in range(3, n+1):
 c = a + b
 a = b
 b = c
 print(c, end=" ")

n = int(input('Informe o valor de N: '))
for i in range(1,n+1):
  cont = 0
  for a in range (2,i):
   if i % a == 0:
    cont = cont + 1 
    break
  if cont == 0 and i != 1:
     print(i, end=" ")

print('Informe dois números inteiros: ')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

while True:
  n = n1 % n2
  if n == 0:
    print('MDC =', n2 )
    break
  n1 = n2
  n2 = n

n = float(input('Digite a quantidade de massa: '))
tempo = 0
while True:
  tempo = tempo + 50
  n = n / 2
  if n < 0.5:
    break
print(f'Tempo = {tempo} segundos')

ndias = 3
tempquente = -100
tempfrio = 100

for dia in range(1,ndias+1):
  temp = int(input('Temperatura do dia ' + str(dia) + ': '))
  if temp > tempquente:
    tempquente = temp
    diaquente = dia
  if temp < tempfrio:
    tempfrio = temp
    diafrio = dia
print()
print(f'O dia mais quente: dia {diaquente}, com {tempquente} graus.')
print(f'O dia mais frio: dia {diafrio}, com {tempfrio} graus.')

senha = 'abcd'
for i in range(3):
  tent = input('Digite a senha: ')
  if tent == senha:
    print('Senha Correta!')
    break
  print('Senha incorreta! Tente novamente.')

