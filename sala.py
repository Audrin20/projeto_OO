class Sala:
  def __init__(self, nome: str = None, situacao: str = None):
    self.__nome = nome
    self.__situacao = situacao

  @property
  def mostra_nome_sala(self):
    return self.__nome

  @property
  def mostra_situacao_sala(self):
    return self.__situacao

  @mostra_nome_sala.setter
  def definir_nome_sala(self, nome: str = None):
    self.__nome = nome

  @mostra_situacao_sala.setter
  def definir_situacao_sala(self, situacao: str = None):
    self.__situacao = situacao

  def __str__(self):
    return (self.nome)