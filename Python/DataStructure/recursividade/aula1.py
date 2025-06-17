#interativo
str = 'ifpb'
for s in str:
    print( s)

str = 'ifpb'

#de forma recursiva
#caso base
def printstr(str):
    if (str == ''): #se ela for nula, retorna
        return
    print(str[0], end='') 
    printstr( str[1:])#a patir do primeiro chama recursivamente a mesma str

def printstrinv(str):
    if (str == ''): #se ela for nula, retorna
        return
    printstrinv( str[1:])#a patir do primeiro chama recursivamente a mesma str
    print(str[0], end='') 

def tamanhostr(str):
    if (str == ''): #se ela for nula, retorna
        return 0 #no caso base não tem nada/ está vazia
    else:
        return 1 + tamanhostr(str[1:]) 
    #quando estiver no 1° caractere, não entro no caso base, retorno 1 + chamando ifpb
    
    printstrinv( str[1:])
    print(str[0], end='') 

printstr(str)
print()
printstrinv(str)
print()
print('Tamanho: ', tamanhostr(str))


#EXERCÍCIO 1

def potencia(base, exp):
    if exp == 0:
        return
    res = 1
    for i in range(exp):
        res*= base
    return res

def potenciaRecursiva(base, exp, chamada):
    #1. identificcar o padrão do problema que repete
    #2. determinar o(s) caso(s) base
    #3. realizar a chamada recursiva alterando o parâmetro
    #caso base:
    print(f'Chamada {chamada}: base = {base} expoente = {exp}')
    if exp == 0:
        return 1 #quando chega aqui ele quebra a recursividade
    else:
        return base * potenciaRecursiva(base, exp-1, chamada+1)
    #não pode ser o exp pq ele cria uma repetição infinita
    #logo esse expoente em algum momento deve chegar a zero
    #ele tem que alcaçar o caso base, nesse caso o zero
    #o expoente que atinge meu caso base, logo quem eu altero é ele

#main
try:
    for i in range(1,6):
        print(f'Potência(2,{i})={potencia(2,i)}')
    for i in range(0,6):    
        print(f'Potência(2,{i}) = {potenciaRecursiva(2,i,1)}')
except RecursionError:
    print('Erro: número limite de chamadas recursivas alcançadas.')
except ValueError:
    ('Erro: Expoente da função.')




#EXERCÍCIO 2

#"minha solução"
def invictus(massa, tempo = 0):
    if massa < 0.8:
        return(massa, tempo)
    else:
        massa /= 2
        return invictus(massa, tempo + 50)

#"solução do professor"
def invictus(massa):
    if massa < 0.8:
        return massa, 0
            #  t[0] t[1]
    else:
        t = invictus(massa/2)
        return t[0], t[1] + 50   

#main
massa = 1.8
print(f'Massa: {massa}, {invictus(massa)}')




#PRÁTICA
#duas chamadas recursivas 

def fib(n):
    return n if n == 0 or n == 1 else fib(n-1) + fib(n-2)
#faz primeiro o que está na esquerda 
try:
    print(f'Fibonaci(5): {fib(5)}')
except RecursionError:
    print('Erro: número limite de chamadas recursivas alcançadas.')