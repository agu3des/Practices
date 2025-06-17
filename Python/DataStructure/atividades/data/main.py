from data import data

try:
    dia = int(input('Dia: '))
    mes = int(input('Mês: '))
    ano = int(input('Ano: '))
    
    data1 = data(dia, mes, ano)
    
except Exception as e: