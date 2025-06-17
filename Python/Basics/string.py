frase = input('Digite: ') #pra digitar o desejado
quant = frase.count(' ') #contador de branco
print(f'A frase contém {quant} brancos')


frase = input('Frase: ')
saida = ''
for caracter in frase:
  if caracter != ' ': #se o caracter diferente de branco
    saida += caracter #adicione  saida e o caracter
print(saida)

frase = input('Frase: ')
saida = frase.upper() #deixa maiúsculo
print(saida)


frase = input('Frase: ')
saida = frase.title()
print(saida)

frase = input('Frase: ')
saida = ''
for i in range(len(frase)):
  if i == 0: #se for a primeira letra
    saida += frase[i].upper()
  elif frase[i-1] == ' ':
    saida += frase[i].upper() #as letras restantes
  else:
    saida += frase[i].lower() #ficar igual ao título
print(saida)


frase = input('Frase: ')
tam = len(frase)
for i in range(tam):
   print(frase[i]) #o print já quebra a linha automaticamente


frase = input('Digite: ')
tam = len(frase)
for i in range(tam-1,-1,-1): #um for de trás pra frente
  print(frase[i], end='')



email = input('Digite seu email completo: ')
tam = len(email)
for i in range(tam):
  n = email.find('@')
  dominio = email[n+1:]
  login = email[:n]
print(f'Login: {login}')
print(f'Domínio: {dominio}')



frase = input('Digite uma frase: ').upper()
n = len(frase)
for i in range(n):
  if frase[i] == 'A':
    print(' ',end='')
  if frase[i] == 'E':
    print('U',end='')
  if frase[i] == 'I':
    print('O',end='')
  if frase[i] == 'O':
    print('I',end='')
  if frase[i] == ' ':
    print('A',end='')
  if frase[i] != 'A' and frase[i] !='E' and frase[i] !='I' and frase[i] !='O' and frase[i] !='U' and frase[i] !=' ':
    print(frase[i],end='')



nome = input('Nome: ').upper()
n = nome.split() #separar
print(n[-1],', ', sep='', end='') #print pro último direto
for i in range(len(n)-1): #os que vem depois, menos 1
    print(n[i][0],'. ', sep='', end='') 


frase = input('Digite uma frase: ')
n = frase.count('e')
print(f"Possui {n} e's")


frase = input('Digite uma frase: ').lower()
n = int(input('Digite um número: '))
tam = len(frase)
for i in range(tam):
    if frase[i] == 'a' or frase[i] =='e' or frase[i] =='i' or frase[i] =='o' or frase[i] =='u':
        result = frase[i]*n
    else:
        result = frase[i]
    print(result, end='')



frase = input('Frase: ')
for e in frase:
  if frase[0]:
    print(frase[0])
  if frase[1]:
    print(frase[1]*2)
  if frase[2]:
    print(frase[2]*3)
  if frase[3]:
    print(frase[3]*4)
  if frase[4]:
   print(frase[4]*5)
  if frase[-1]:
   print(frase[-1]*5)
  if frase[-2]:
    print(frase[-2]*4)
  if frase[-3]:
    print(frase[-3]*3)
  if frase[-4]:
    print(frase[-4]*2)
  if frase[-5]:
    print(frase[-5]) 

frase = input('Frase:\n')
n = len(frase)
print('\nSaída:')
#pegar a primera leva
for i in range(n):
    print(frase[i]*(i+1))
#pegar a segunda leva
for i in range(n-2,-1,-1):
    print(frase[i]*(i+1))
  


verbo = input('Verbo: ')
n = len(verbo)
radical = verbo[:-2]
for i in range(1):
  if verbo[-2:] == 'ar':
    print(f'Eu {radical}o \nTu {radical}as \nEle {radical}a \nNós {radical}amos \nVós {radical}ais \nEles {radical}am')
  if verbo[-2:] == 'er':
    print(f'Eu {radical}o \nTu {radical}es \nEle {radical}e \nNós {radical}emos \nVós {radical}eis \nEles {radical}em')
  if verbo[-2:] == 'ir':
    print(f'Eu {radical}o \nTu {radical}es \nEle {radical}e \nNós {radical}imos \nVós {radical}is \nEles {radical}em')


frase = input('Digite uma frase: ')
n = frase.count('e')
print(f"Possui {n} e's")


