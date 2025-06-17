from Temporizador import Temporizador
from enum import Enum

class Estado(Enum):
  Vermelho = 1
  Amarelo = 2  #atriubui um valor, uma enumeração de modo a apenas relacionar os estados a códigos
  Verde = 3

class SemaforoTemporizado:
    #definindo construtor
  def __init__(self, estadoInicial:Estado = Estado.Vermelho):
   #se eu não fornecer o estado que eu quero, ele começa no vermelho
   #estado atual não pode ficar ara ser alterado, pois bagunçaria o funcionamento
    self.__estadoAtual = estadoInicial #self:  para propriedade ou método
    self.__timer = Temporizador() #não bota o get, pq não precisa ver
    self.__tempoDeTransicao = {Estado.Verde:20, 
                             Estado.Amarelo:5, 
                             Estado.Vermelho:10}
    
  @property  
  def estadoAtual(self)->Estado: #referencia do objeto . o nome da propriedade
    return self.__estadoAtual
  
  @property
  def tempoDeTransicao(self)->dict:
    return self.__tempoDeTransicao
  
  def __str__(self):
    return f'''
    +-----+
    | ({"X" if self.__estadoAtual == Estado.Vermelho else " "}) | 
    | ({"X" if self.__estadoAtual == Estado.Amarelo else " "}) |
    | ({"X" if self.__estadoAtual == Estado.Verde else " "}) |
    +-----+
    '''
  #para mostrar qual a posição
  
  def setup(self, tempoVermelho:int, tempoAmarelo:int, tempoVerde:int):
    '''
    Método que permite ajustar o tempo dos estados do semáforo
    Aceita um tempo em segundos entre 0 e 59

    Argumentos
    ----------
    tempoVermelho(int): tempo em segundos de permanência no vermelho
    tempoAmarelo(int): tempo em segundos de permanência no amarelo
    tempoVerde(int): tempo em segundos de permanência no verde
    '''
    if tempoVermelho < 1 or tempoVermelho > 59:
      return
    elif tempoAmarelo < 1 or tempoAmarelo > 59:
      return
    elif tempoVerde < 1 or tempoVerde > 59:
      return

    self.tempoDeTransicao[Estado.Vermelho] = tempoVermelho
    self.tempoDeTransicao[Estado.Amarelo] = tempoAmarelo
    self.tempoDeTransicao[Estado.Verde] = tempoVerde

  def proximoEstagio(self):
   if :
     self.__estadoAtual = Estado.Vermelho
   elif :
     self.__estadoAtual = Estado.Amarelo
   elif :
     self.__estadoAtual = Estado.Verde
   else:
    self.__estadoAtual = Estado.Vermelho
  
  def start(self, numCiclos:int):
    for i in range(numCiclos):
      print(self) #print o objeto que está executando, no caso o semáforo
      self.__timer.duracao(self.tempoDeTransicao [self.__estadoAtual])
      self.__timer.ativar()
      self.__proximoEstagio()




  # def __init__(self):
  #   # 1: verde, 2: laranja, 3: vermelho
  #   self.estadoAtual = Estado.Verde #self:  para propriedade ou método
  #   self.timer = Temporizador()
  #   self.tempoDeTransicao = {1:20, 2:5, 3:10} #para chave 1 tanto #começa com esses valores
  #   #para requerer o tempo de cada cor: tempoDeTransicao[2] ---> 5 / você pode começar com ele vazio e ir adicionando
