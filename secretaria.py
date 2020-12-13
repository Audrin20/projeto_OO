from funcionario import Funcionario
from socio import Socio

class Secretaria(Funcionario):
  def __init__(self, nome: str = None, ramal: str = None, cargo: str = "Secretaria"):
    super().__init__(nome, ramal)
    self.__cargo = cargo

  def get_cargo(self):
    return self.__cargo		

  def set_cargo(self, cargo: str = None):
    self.__cargo = cargo

  def __str__(self):
    return self.nome