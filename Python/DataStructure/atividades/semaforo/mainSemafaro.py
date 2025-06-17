from SemaforoTemporizado import SemaforoTemporizado, Estado


s1 = SemaforoTemporizado(Estado.Verde)
s2 = SemaforoTemporizado()
print(id(s1))
print(id(s2))

print(s1.__dict__)#consultar o estado do dicionário
s1.setup(9, 9, 9)
print(s1.__dict__)
print(s1.estadoAtual()) #se mexeu no get e no set, tem que alterar em todos os locais que vc utiliza a propriedade
print('Semáforo 1')
print(s1) #vai mostrar a localização na memória
s1.start(2)

print('Semáforo 2')
print(s2)