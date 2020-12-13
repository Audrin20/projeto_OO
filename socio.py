class Socio:
  def __init__(self, nome: str = None):
    self.__nome = nome

  @property
  def mostra_nome_socio(self):
    return self.__nome
  
  @mostra_nome_socio.setter
  def definir_nome_socio(self, nome: str = None):
    self.__nome = nome
  
  def __str__(self):
    return str(self.nome)

