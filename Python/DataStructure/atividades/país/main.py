from pais import Pais

pais1 = Pais('Alemanha', 'Brasília', 200000000)
pais1.paisFronteira = 'argentina'
print(pais1.listaFronteiras)
print(pais1)
pais2 = Pais('França', 'Bom Ar', 125615325761)
pais2.paisFronteira = 'brasil'
print(pais2.listaFronteiras)
print(pais2)
print(pais1.fazFronteiraCom(pais2))
try:
    pais1.addFronteira('Áustria')
    pais1.addFronteira('Chile')
    pais1.addFronteira('Polônia')
    pais1.addFronteira('ÁUSTRIA')

    print(pais1.listaFronteiras)
except Exception as e: #se tal erro, mostre isso e continue o código
    #o e é uma refrência para conectar com o objeto exception
    #print('Ocorreu um erro ao adicionar fronteira.') #pode colocar só um pass, pq aí ele passa o erro
    print(e)
print(pais1.listaFronteiras)
print('Fim do programa.')