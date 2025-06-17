#FATORIAL
def fatorial (n):
    if (n == 0): #caso base
        return 1
    x = n - 1 #decrementa = quebra do laço
    y = fatorial(x) #ocorre a recursiva, ela vai lá chamar a funcção novamente
    return (n * y) #estabelece a regra matemática n" = n*(n-1)!
def fatorial (n):
    if (n == 0):
        return 1
    else:
      return (n * fatorial(n-1))
def fatorial (n):
    return 1 if (n == 0) else (n * fatorial(n-1))
#main
for i in range(1,5):
  print(f'Fatorial de {i}: {fatorial(i)}')
'''
Se n = 4
1. entra no caso base e verifica se não é zero
2. x recebe o valor de n-1 ou seja 3
3. y vai chamar, recursivamente, o fatorial de x
4. vai para o caso base, e verifica
5. x recebe o valor de n-1 ou seja 2
6. y vai chamar, recursivamente, o fatorial de x
7. vai para o caso base, e verifica
8. x recebe o valor de n-1 ou seja 1
9. y vai chamar, recursivamente, o fatorial de x
10. vai para o caso base, e verifica
11. x recebe o valor de n-1 ou seja 0
12. y vai chamar, recursivamente, o fatorial de x
13. vai para o caso base, que encaixa pois o x agora é zero, então ele retorna 1
14. o 1 retornado entra no y do 1
15. o y encontrado entra no n*y = 1*1 = 1
16. esse retornado vai para o y da que chamou ele anteriormente
o  que é retornado vai para a original que o chamou
'''

#1. LENGTH
def recursiveLength(str):
    if (str == ''): #se for nula
        return 0
    else:
        return 1 + recursiveLength(str[1:])
#main
str1 = 'ifpb'
print(recursiveLength(str1))


#2. PRINTSTR
def printStr(str):
    if str == '':
        return 
    else:
        print(str[0], end='') #aqui eu não chamo a recursividade, só a primeira string pq ela inicia
        printStr(str[1:]) #aqui eu chamo a recursiva 
        #pq a partir do segundo caractere que eu vou ir chamando ela e atualizando dando print sem a quebra
#main
str='ifpb'
printStr(str)


#3. INVERTSTR
def invertStr(str):
    if str == '':
        return
    else:
        invertStr(str[1:])
        print(str[0], end='')
#main
str = 'bpfi'
invertStr(str)


#4. PRINTINVERSE
def printStrInv(str):
    if str == '':
        return
    else:
        printStrInv(str[1:])
        print(str[0], end='')
#main
str = 'ifpb'
printStrInv(str)


#5.STRCMP
def strCmp(str1,str2):
    if str1 == '' or str2 == '':
        return 0
    else:
        if str1[0] == str2[0]:
            return strCmp(str1[1:], str2[1:]) 
        #só preciso chamar a recursiva aqui, que é quando vou ter os primeiros iguais
        # retorno a recursiva dos duas a partir do segundo índice, entrando na recursividade ele já irá dizer a partir da primeira diferença
        if str1[0] > str2[0]:
            return 1
        #se eu já comparei o primeiro não preciso comparar outros
        if str1[0] < str2[0]:
            return -1
        #logo, nenhuma dessas duas precisam de recursividade
#main
str1 = 'Maria'
str2 = 'Alexandre'
str3 = 'ifpb'
str4 = 'ifpb'
str5 = 'MARIA' 
str6 = 'maria'
print(strCmp(str1,str2))
print(strCmp(str3,str4))
print(strCmp(str5,str6))


#6. ISPALINDROME
# def isPalindrome(str):

#main


#7. SOMA
def soma(n):
    if n == 0:
        return 0
    else:
      return n + soma(n-1)
#main
for n in range(0,5):
    print(f'Soma de {n}: {soma(n)}')


#8. MENORESREC
def menoresRec(list, key):
    if list == []:
        return 0
    if list[0] == key:
        return 1 + menoresRec(list[1:],key)
    else:
        return menoresRec(list[1:],key)
#main
chave = 40
lista = [12,40,30,40,50,75,40,83]
print(f'Chave = {chave}  Ocorrências = {menoresRec(lista, chave)}')
chave1 = 4
lista1 = [12,4,30,4,50,75,4,83,4]
print(f'Chave = {chave1}  Ocorrências = {menoresRec(lista1, chave1)}')


#FUNÇÃO SOMA
def func( n ):
    if ( n == 0 ):
        return 0
    else:
        return (n % 10 + func(int(n/10)))
print(f'O resultado da soma foi {func(35)}')
print(f'O resultado da soma foi {func(47)}')



#9. DECTOBIN
def decToBin(n):
    if n == 0:
        return 0
    else:
        r = n%2
        decToBin(n//2)
        print(r, end='')
    
decToBin(10)
print()

#10. INVICTUS
def massaInv(m, t = 0):
    if m < 0.8:
        print(f'Massa final= {m}, Tempo necessário= {t}s')
    else:
        m /= 2
        return massaInv(m, t+50)
    
massaInv(1.8)