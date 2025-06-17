# SOMA SIMPLES
soma = 0
A = int(input())
B = int(input())
if A >= 0 and B >= 0:
  soma = (A) + (B)
  print('SOMA =', soma)
else:
  soma = (A) + (B)
  print('SOMA =', soma)


# DIFERENÇA
A = int(input())
B = int(input())
C = int(input())
D = int(input())
DIFERENCA = (A * B) - (C * D)
print('DIFERENCA =', DIFERENCA)


# PRODUTO SIMPLES
n1 = int(input())
n2 = int(input())
PROD = n1 * n2
print('PROD =', PROD)


# ÁREA
A,B,C = input().split(' ')
a = float(A)
b = float(B)
c = float(C)
pi = 3.14159
areaTri = (a*c)/2
areaCir = pi*(c**2)
areaTra = (a + b)*c/2
areaQua = b**2
areaRet = a*b
print('TRIANGULO: {:.3f}'.format(areaTri))
print('CIRCULO: {:.3f}'.format(areaCir))
print('TRAPEZIO: {:.3f}'.format(areaTra))
print('QUADRADO: {:.3f}'.format(areaQua))
print('RETANGULO: {:.3f}'.format(areaRet))


# ÁREA CÍRCULO
r = float(input())
pi = 3.14159
area = pi*(r**2)
print('A = {:.4f}'.format(area))


#  CÁLCULO SIMPLES
c1,np1,vu1 = input().split(' ')
c2,np2,vu2 = input().split(' ')
codigo1 = int(c1)
numeroPecas1 = int(np1)
valorUnitario1 = float(vu1)
codigo2 = int(c2)
numeroPecas2 = int(np2)
valorUnitario2 = float(vu2)
total = (numeroPecas1*valorUnitario1)+(numeroPecas2*valorUnitario2)
print('VALOR A PAGAR: R$ {:.2f}'.format(total))


# ESFERA
r = float(input())
pi = 3.14159
volume = (4/3.0)*pi*(r**3)
print('VOLUME = {:.3f}'.format(volume))


# MÉDIA
A = float(input())*2
B = float(input())*3
C = float(input())*5
MEDIA = (A + B + C)/10
print('MEDIA ={:.1f}'.format(MEDIA))


# CONSUMO
X1,Y1 = input() .split(' ')
X2,Y2 = input() .split(' ')
x1 = float(X1)
x2 = float(X2)
y1 = float(Y1)
y2 = float(Y2)
d = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print('{:.4f}'.format(d))


# DISTÂNCIA
km = int(input())
min = 60
dx = 60/min
dy = 90/min
dyx = 30/min
tempdist = km/dyx
print('{:.0f} minutos'.format(tempdist))


# SALÁRIO
funcnum = int(input())
htrab = int(input())
valorh = float(input())
salario = htrab * valorh
print('NUMBER =', funcnum)
print('SALARY = U$ {:.2f}'.format(salario))


# SALÁRIO BÔNUS
vendNome = input()
salarioFixo = float(input())
totalVendas = float(input())
salarioTotal =  (0.15*totalVendas) + salarioFixo 
print('TOTAL = R$ {:.2f}'.format(salarioTotal))