class Dia:
  def __init__(self, hora: str = None, dia: int = None, mes: str = None):
    self.__hora = hora
    self.__dia = dia
    self.__mes = mes


  #Getters
  @property
  def mostra_hora(self):
    return self.__hora

  @property
  def mostra_dia(self):
    return self.__dia

  @property
  def mostra_mes(self):
    return self.__mes

  #Setters
  @mostra_hora.setter
  def definir_hora(self, hora: str = None):
    self.__hora = hora

  @mostra_dia.setter
  def definir_dia(self, dia: int = None):
    self.__dia = dia

  @mostra_mes.setter
  def definir_mes(self, mes: str = None):
    self.__mes = mes