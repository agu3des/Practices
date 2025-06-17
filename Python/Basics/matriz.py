nlin = 2
ncol = 3

a = [[None]*ncol for i in range(nlin)]
b = [[None]*ncol for i in range(nlin)] #vai ter que multiplca para pegar a quantidade de linhas e colunas
c = [[None]*ncol for i in range(nlin)]

print('Digite os elementos da matriz A: ')
for i in range(nlin):
  for j in range(ncol):
    a[i][j] = int(input(f'A[{i}][{j}]: ')) #leitura

print()
print('Digite os elementos da matriz B: ')
for i in range(nlin):
  for j in range(ncol):
    b[i][j] = int(input(f'B[{i}][{j}]: '))

print()
for i in range(nlin):
  for j in range(ncol):
    c[i][j] = a[i][j] + b[i][j] # somo os dois de cada para darem os dois desse

print('Matriz A: ') # aqui é só a impressão dela, tem que ter
for i in range(nlin):
  for j in range(ncol):
    print(f'{a[i][j]:4}',end=' ')  
print()

print('Matriz B: ') # o outro é só a leitura
for i in range(nlin):
  for j in range(ncol):
    print(f'{b[i][j]:4}',end=' ')
print()

print('Matriz C: ') # para cada um eu tenho que ler e imprimir
for i in range(nlin):
  for j in range(ncol):
        print(f'{c[i][j]:4}',end='')
  print()



import random

n = int(input('Digite a ordem da matriz: ')) #dizer a quantidade de colunas e tabelas
print()

m = [[None]*n for i in range(n)] #formar a matriz de fato

for i in range(n):
  for j in range(n):
    m[i][j] = random.randint(1,20) #pegar os valores da matriz

print('Matriz: ') #impressão da matriz
for i in range(n):
  for j in range(n):
    print(f'{m[i][j]:4}', end=" ") #seu formato
  print() #pra ter o espaço na matriz
print() #ter espaço entre os comandos

print('Diagonal principal: ')
for i in range(n):#tem que fazer toda essa estrutura
  for j in range(n):  #p/ que ele entenda que é com os dois
   if i == j:
    print(f'{m[i][j]:4}', end=" ")



import random

n = int(input('Digite a ordem da matriz: '))
print()

a = [[None]*n for i in range(n)]
b = [[None]*n for i in range(n)]

for i in range(n):
  for j in range(n):
    a[i][j] = random.randint(1,20)

for i in range(n):
  for j in range(n):
    if  b[i] == b[j] or i + j == n - 1: #se os índices iguais #o 2° tem que ter para a diagonal no outro sentido
     b[i][j] = 0  
    else: #tem que botar a variação para quando não são iguais
     b[i][j] = a[i][j] + i + j

print('Matriz A:')
for i in range(n):
  for j in range(n):
    print(f'{a[i][j]:3}', end=" ") #impressão é separadaaaa
  print() #tem que tá dentro do laço

print()

print('Matriz B:')
for i in range(n):
  for j in range(n):
    print(f'{b[i][j]:3}', end=" ")
  print()



import random

m = int(input('Digite a quantidade de linhas: '))
n = int(input('Digite a quantidade de colunas: '))

c = [[None]*n for i in range(m)]
ct = [[None]*m for i in range(n)]

for i in range(m):
  for j in range(n):
    c[i][j] = random.randint(1,20)

for i in range(n):
  for j in range(m):
    ct[i][j] = c[j][i]

print('Matriz:')
for i in range(m):
  for j in range(n):
    print(f'{c[i][j]:3}', end=" ")
  print()

print('Matriz Transposta:')
for i in range(n):
  for j in range(m):
    print(f'{ct[i][j]:3}', end=" ")
  print()


#PROFESSOR - AULA
nlin = 2 #para cálculo, usar o 2
ncol = 4

m = [[None]*ncol for i in range(nlin)]

#leitura da matriz
for i in range(nlin):
  print(f'Aluno {i+1}')
  for j in range(ncol-1): #ideia de matriz com 2 for (-1 pq para antes)
   m[i][j] = int(input(f'{j+1}º nota: '))

#cáculo das médias
for i in range(nlin):
  soma = 0
  for j in range(ncol):
   soma += m[i][j]
   print(soma)

#impressão da matriz
print(f'{"N1":>4} {"N2":>4} {"N3":>4} {"Média":5}')
for i in range(nlin):
  print(f'Aluno {i+1}',end='')
  for j in range(ncol):
   print(f'{m[i][j]:4}', end=" ")
  print()

#média geral
soma = 0
for i in range(nlin):
   soma += m[i][j]
mg = (soma/nlin)
print(f'Média geral: {mg}')


#alunos com nota maior que a média geral
cont = 0
for i in range(nlin):
    if media > mg:
        cont += 1
print(f'\nNúmero de alunos com média superior à média geral da turma: {cont}')


nlin = 2
ncol = 4
m = [[None]*ncol for i in range(nlin)]
#leitura das notas
for i in range(nlin):
    print(f'Aluno {i+1}:')
    for j in range(ncol-1):
        m[i][j] = int(input(f'{j+1}ª Nota: '))
#cálculo das médias
for i in range(nlin):
    soma = 0
    for j in range(ncol-1):
        soma += m[i][j]
    m[i][3] = round(soma/(ncol-1))
#imprimir a matriz
print(f'        {"N1":>4}{"N2":>4}{"N3":>4} {"Média"}')
for i in range(nlin):
    print(f'Aluno {i+1}',end='')
    for j in range(ncol):
        print(f'{m[i][j]:4}',end='')
    print()
#calcular a média geral
soma = 0
for i in range(nlin):
    soma += m[i][3]
mg = soma / nlin
print('Média geral:',mg)
#Calcular o número de alunos com média superior à média geral
cont = 0
for i in range(nlin):
    if m[i][3] > mg:
        cont += 1
print('Nº de alunos com média superior à média geral:',cont)


n = int(input('Digite a ordem da matriz: '))

m = [[None]*n for i in range(n)]

print('Digite os elementos da matriz: ')
for i in range(n):
  for j in range(n):
   m[i][j] = int(input(f'M[{i}][{j}]: '))

print('Matriz: ')
for i in range(n):
  for j in range(n):
    print(f'{m[i][j]:4}', end=' ')
  print()



for i in range(n):
  for j in range(n):
    if i == j and m[i][j] == 1 and i != j and m[i][j] == 0:
      print('É uma matriz de permutação.')
    else:
      break
    print('Não é uma matriz de permutação.')   




#o que vai adicionar aqui que diferencia da 1 são as diagonais
# Leitura da ordem da matriz
n = int(input('Digite a ordem da matriz: '))
# Criação da matriz com valores nulos
m = [[None]*n for i in range(n)]
# Leitura dos elementos da matriz
print('\nDigite os elementos da matriz:')
for i in range(n):
    for j in range(n):
        m[i][j] = int(input(f'm[{i}][{j}]: '))
# Exibição da matriz 
print('\nMatriz:')
for i in range(n):
    for j in range(n):
        print(f'{m[i][j]:4}',end='')
    print()

# Inicialização da variável do resultado
quadradoM = True
# Verificando a soma da diagonal principal
diagP = 0
for i in range(n):
    diagP += m[i][i]
# Verificando a soma da diagonal secundária
diagS = 0 #tem que inicializar
for i in range(n):
    diagS += m[n-i-1][i] #quando o i for 0 dá 2, se for 1 dá 1, se for 2 dá 0; pode ser i+j = n-1
if diagS != diagP: #verificar a diferença
    quadradoM = False #tem que usar o if pq não necessariamente é o oposto
# Verificando a soma de cada linha
for i in range(n): #pode usar o if aqui do ok
    somaL = 0
    for j in range(n):
        somaL += m[i][j]
    if somaL != diagP: #se for diferente da principal já zera
        quadradoM = False
# Verificando a soma de cada coluna
for j in range(n): #lembrar de inverter os for
    somaC = 0
    for i in range(n):
        somaC += m[i][j]
    if somaC != diagP:
        quadradoM = False
# Exibição do resultado final
if quadradoM:
    print('\nÉ um quadrado mágico') #\n para pular linha
else:
    print('\nNão é um quadrado mágico')


n = 3  # Ordem da matriz quadrada
# Criação da matriz
m = [[None]*n for i in range(n)]
# Geração aleatória dos elementos da matriz 
import random
for i in range(n):
    for j in range(n):
        m[i][j] = random.randint(1,10)
# Exibição da matriz
print('\nMatriz:')
for i in range(n):
    for j in range(n):
        print(f'{m[i][j]:4}',end='')
    print()
# Soma das linhas
print('\nSoma de cada linha:')
for i in range(n):
    s = 0 #no meio dos for
    for j in range(n):
        s += m[i][j] #soma aqui dentro
    print(f'{s:4}')
# Soma das colunas
print('\nSoma de cada coluna:')
for j in range(n):
    s = 0
    for i in range(n):
        s += m[i][j]
    print(f'{s:4}',end='')
# Soma da diagonal principal
print('\n\nSoma da diagonal principal:')
s = 0 #para pegar toda a matriz esse zero tem que tá antes
for i in range(n): #usando dois for
    for j in range(n):
        if i == j:
            s += m[i][j]
print(f'{s:4}')
# Soma da diagonal secundária
print('\nSoma da diagonal secundária:')
s = 0
for i in range(n):
    for j in range(n):
        if i + j == n - 1:  # outra condição possível:  i == n-j-1 
            s += m[i][j]
print(f'{s:4}')
# Soma de toda a matriz
print('\nSoma de toda a matriz:')
s = 0
for i in range(n):
    for j in range(n):
        s += m[i][j]
print(f'{s:4}')


#inicialização das variáveis
ri = 30 #rua inicial
rf = 38 
ai = 1
af = 10 #avenida final
nlin = af - ai + 1 #o +1 para dar ajuste
ncol = rf - ri + 1
mat = [[0]*ncol for i in range(nlin)] #com zero pq é contador
flag = 0 #vai ser em while
#leitura e contagem dos acidentes
print('Informe o local de cada acidente')
print('Para encerrar, digite 0 para a Av.')
while True: #laço infinito
    print()
    av = int(input(f'Av. ({ai} a {af}): '))
    if av == flag: #avenida = 0 
        break #já fica aqui, pq se a avenida for zero, já para
    rua = int(input(f'Rua ({ri} a {rf}): ')) 
    lin = av - ai #ajustar, pq o índice é diferente do valor inserido, ex é 5, mas o índice é 4
    col = rua - ri 
    mat[lin][col] += 1 #ir na posição da matriz e adicionar
#exibição do cabeçalho das colunas
print('\nMAPA DOS ACIDENTES')
print('\nAv./Rua',end='')
for i in range(ncol):
    print(f'{i+ri:4}',end='') #para ir direto a distância
print()   #índice + ri
#exibição da matriz de acidentes
for i in range(nlin):
    print(f'{i+ai:4}   ',end='') #já mostrar o cabeçalho
    for j in range(ncol):
        if mat[i][j] == 0: #caso a quantidade de acidentes for 0, não tem a ver com a flag
            valor = '-'
        else:
            valor = mat[i][j]
        print(f'{valor:>4}',end='')
    print()


# Inicialização da matriz
m = [[0,15,30,5,12],[15,0,10,17,28],[30,10,0,3,11],[5,17,3,0,80],[12,28,11,80,0]]
#o percurso de cada cidade para outra, 
# Leitura do percurso e soma das distâncias
soma = 0 #inicia a soma antes de tudo
print('\nDigite as cidades do percurso (ou 0 para sair)')
orig = int(input()) #digitar de qual cidade sai, p/ criar o parâmetro, #a anterior sempre vira a origem e ele pega o próximo destino
while True: #laço infinito
    dest = int(input()) #a cidade de chegarda para fazer a comparação
    if dest == 0: #a flag de stop
        break #para logo
    soma += m[orig-1][dest-1] #a soma vai ser ela + a origem-1 (ajuste do índice) +o destino-1
    orig = dest #o ajuste para a próxima
# Exibição do resultado
print(f'\nDistancia percorrida: {soma} km')
