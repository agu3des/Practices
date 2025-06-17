from enum import Enum

class combustivel(Enum):
    gasolina = 1
    alcool = 2
   
class escolhaombustivel(combustivel):
  def __init__(self):
      self.combustivel = {combustivel.gasolina, combustivel.alcool}
      self.valor = {combustivel.gasolina, combustivel.alcool}