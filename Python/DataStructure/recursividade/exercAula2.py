#EXERCÍCIO 1
from typing import List
lista = [5,6,8,3,7,9] #6

#no list eu posso passar n números
#percorre a lista até achar algo que indique que está vazia -> caso base
#o resto é caso padrão, tem que alterar o argumento até chegar no caso base
#pega o array, processa o elemento, feita a tarefa dele chama a próxima

def length(lst:List[any])->int:
    pass

#dessa forma, ele faz uma cópia da lista, apenas subtraindo um índice
def print_array(lst:List[any]):
    if len(lst) == 0: #caso base
        return
    print_array(lst[1:]) #aqui é onde altera o modo
    #invertando ele pega do lado contrário
    print(lst[0],end=' ')
    #print_array(lst[1:])
    #a cada número ele pega o índice zero e cria um "nova" lista que muda a posição dos índices
    #do índice 1 pra frente eu faço outra coisa
    #estrutura de pilha a primeira a ser chamada é a última a ser resolvida
    #a chamada que eu estou não entra na pilha, só após a finalização

print_array(lista)


#EXERCÍCIO 2
#eu e angelica
def compareStr(str1,str2):
    #compara em tamanho
    if (str1 and str2 ==''):
        return 
    if (len(str1) == len(str2)):
        return 0
    elif len(str1) > len(str2):
        return 1    
    elif len(str1) < len(str2):
        return -1   

#prof
def compareStr(s1,s2):
    #compara em ordem alfabética
    if len(s1)==0 or len(s2)==0:
            return 0
    elif s1[0] < s2[0]:
        return -1
    elif s1[0] > s2[0]:
        return 1
    elif s1[0] == s2[0]:
        return compareStr(s1[1:], s2[1:])
        
s1 = 'teste'
s2 = 'string'   
print(compareStr(s1,s2))



#EXERCÍCIO 3
def isPalindrome(str):
    if len(str) == 0:
        raise ValueError('String vazia. Não elegível para chamada da função is Palindrome.')
        # se não for uma palavra
    return isPalindromeStr(str)

def isPalindromeStr(str):
    if len(str) < 2:
        return True
        #se só tiver 1 retorne true para onde vc está chamando, ex: o d de radar
    elif str[0] != str[-1]:
        #se o 1° for diferente do último já quebra
        return False
    else:
        #se for ok, chame a função para chamar o 1º e o novo último
        return isPalindromeStr(str[1:-1])

palavras = ['radar','ana','arara','radax','anna','']
try:
    for p in palavras:
        print(p,isPalindrome(p))
except ValueError as ve:
    print(ve)
exit()