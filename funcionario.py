class Funcionario:
  def __init__(self, nome: str = None, ramal: int = None):
    self.__nome = nome
    self.__ramal = ramal

  #getters
  @property
  def mostra_nome(self):
    return self.__nome

  @property
  def mostra_ramal(self):
    return self.__ramal

  #setters
  @mostra_nome.setter
  def definir_nome(self, nome: str = None):
    self.__nome = nome

  @mostra_ramal.setter
  def definir_ramal(self, ramal: str = None):
    self.__ramal = ramal
  
  def __str__(self):
    return (self.nome)


