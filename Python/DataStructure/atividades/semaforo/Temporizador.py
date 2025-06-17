import time

class Temporizador:
    def __init__(self):
        self.__duracao = 0 #inicia zerado

    #criar um método get
    @property
    def duracao(self)->int:
        return self.__duracao
    
    #criar um método set / nome da propriedade / vc não pega dirtamente a propriedade, vc passa pelo método
    @duracao.setter
    def duracao(self, novaDuracao):#chamo o novo tempo que eu quero
      self.__duracao = novaDuracao if novaDuracao > 0 else 5
      '''
      Define o tempo de duração em segundos
      Caso a novaDuração seja inválida(negativa), assume 5s como padrão
      ''' 
      self.__duracao = novaDuracao

    def ativar(self): #inicio a contagem
        for t in range(self.__duracao,0,-1):
            print(f'{t} seg', end='')
            time.sleep(1)#RECEBE UM ARGUMENTO DO TEMPO DE DORMIR
        print()



# # main teste / ps.isso está v
# t = Temporizador()
# print('Duração:', t.duracao) #pegar a duração usando getq vc tenta acessar como se fosse pública, de modo que pela forma que vc quer mexer ele sabe qual método usado
# t.duracao = 2 
# #t.setDuracao(3)
# #ativar não pode ficar privado, pois temos que mexer nele
# t.ativar() #vc tem que utilizar outro atributo, pq esse tá privado

# #como deixar privado: na sua propriedade adicione um duplo _ em todos os locais que aparece
# # ex:     def __init__(self):
# #         self.__duracao = 0
# #encapulamento: vc deve esconder a parte que utiliza,
# #cria-se uma estrutura de modo que a pessoa que usa o objeto não sabe que o está usando