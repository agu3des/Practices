t=input('Bem-vindo ao mundo da programação!')

x = int(input('Digite um número: '))
d = x * 2
print('O dobro de {} vale {}.'. format(x, d))

numero1=input("Digite um número: ")
numero2=input("Digite um número: ")
soma=int(numero1)+int(numero2)
print(soma)

base = int(input("Digite um número para base: "))
altura = int(input("Digite um número para altura: "))
area = (base*altura)/2
print("A área do triângulo é:",area)

nome = input('Digite um nome: ')
sobrenome = input('Digite um sobrenome: ')
print(sobrenome, ',', nome)

dolar = float(input('Digite o valor em dólares: '))
cot = float(input('Digite a cotação do dólar: '))
convers = (dolar*cot*real)
print(f'O valor total corresponde a: {convers}')

kg = float(input('Digite o Kg: '))
preco = float(input('Digite o valor por Kg: '))
res = (kg*preco)
print(f' O valor a pagar é: {res}')

nome = input ('Digite um nome: ')
semestre1 = input ('Digite o semestre: ')
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
n3 = float(input('Terceira nota do aluno: '))
média = (n1 + n2 + n3) / 3
print(f'A média de {nome} entre {n1}, {n2} e {n3} é igual a {média}')


nome = input('Digite o nome do funcionário: ')
quantcar = int(input('Digite aqui a quantidade de carros vendidos: '))
valorvenda = int(input('Digite o valor da venda dos carros: '))
salario = 1000
comis = int((200 * quantcar))
carsell = int((0.05 * valorvenda))
saltotal = int(salario + comis + carsell)
print(f'O salário total do funcionário {nome} é igual a R${saltotal}')

nome = input('Digite o nome do aluno: ')
n1 = float(input('Digite a primeira nota do aluno: '))
p1 = 6
n2 = float(input('Digite a segunda nota do aluno: '))
p2 = 4
mediaPond = float(n1*p1+n2*p2)/(p1+p2)
print(f'A média ponderada do aluno {nome} é igual a {mediaPond}: ')

x = int(input("Digite um valor para x: "))
y = int(input("Digite um valor para y: "))
print('Antes da troca:')
print('x =', x)
print('y =',y)

aux = x
x = y
y = aux

print('Depois da troca;')
print('x =',x)
print('y =',y)

hodant = int(input('Digite o valor do hodômetro antes da viagem: '))
lantes = int(input('Digite a quantidade de litros antes do percurso: '))
hoddep = int(input('Digite o valor do hodômetro após a viagem: '))
ldepois = int(input('Digite a quantidade de litros depois do percurso: '))
captanq = int(input('Digite a capacidade máxima do tanque do veículo: '))
precocom = float(input('Digite o valor do litro da gasolina: '))
hodzero = float(input('Zere o hodômetro parcial. '
                   'Digite a quantidade de Km rodados até finalizar o tanque cheio: '))
quirod = int(hoddep - hodant)
lgastos = int(lantes - ldepois)
quiporl = int(quirod/lgastos)
autovel = int(hodzero//captanq)
custoviag = int(precocom * quirod)
print(f'A quantidade de quilômetros rodados foi {quirod}, de litros gastos {lgastos}.')
print(f'O carro roda {quiporl}Km/L.')
print(f'Sua autonomia é de {autovel}.')
print(f'E o custo total da viagem foi de R${custoviag}.')

segundos = int(input('Digite um valor inteiro em segundos: '))
minutos = int(segundos//60)
horas = int(minutos//60)
print(f'A quantidade em horas: {horas}.')
print(f'A quantidade em minutos: {minutos}.')
print(f'A quantidade em segundos: {segundos}.')

dinDes = int(input('Digite o valor desejado: '))
notas50 = int(dinDes//50)
resto50 = dinDes % 50
notas10 = int(resto50//10)
resto10 = resto50 % 10
notas5 = int(resto10//5)
resto5 = resto10 % 5
notas1 = int(resto5//1)
resto1 = resto5 % 1
print(f'A quantidade em notas de B$50: {notas50}.')
print(f'A quantidade em notas de B$10: {notas10}.')
print(f'A quantidade em notas de B$5: {notas5}.')
print(f'A quantidade em notas de B$1: {notas1}.')