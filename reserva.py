class Reserva:
  def __init__(self):
    self.__reserva = []
  
  # --------------- ADICIONAR RESERVA
  def adicionar_reservas(self, reserva, dia, mes, hora, socio):
    dic = {"nome":reserva, "dia":dia, "mes":mes, "hora":hora, "solicitante":socio}

    if len(self.__reserva) == 0:
      self.__reserva.append(dic)
    elif len(self.__reserva) > 0:
      for i in range(len(self.__reserva)):
        if self.__reserva[i]["nome"] == dic["nome"] and self.__reserva[i]["hora"] == dic["hora"]:
          if self.__reserva[i]["dia"] == dic["dia"] and self.__reserva[i]["mes"] == dic["mes"]:
            print(f'Sua solicitação da "{reserva}" não foi aceita pois está reservada para outra pessoa')
            return
      self.__reserva.append(dic)

  # --------------- REMOVER RESERVA
  def remover_reserva(self, reserva, dia, mes, hora, socio):
    dic = {"nome":reserva, "dia":dia, "mes":mes, "hora":hora, "solicitante":socio}

    if len(self.__reserva) == 0:
      print("Não existem reservas no sistema")

    elif len(self.__reserva) > 0:
      for i in range(len(self.__reserva)):
        if self.__reserva[i]["nome"] == dic["nome"]:
          if self.__reserva[i]["dia"] == dic["dia"]:
            if self.__reserva[i]["mes"] == dic["mes"]:
              if self.__reserva[i]["hora"] == dic["hora"]:
                del (self.__reserva[i])
                print(f"Esta reserva foi removida")

  # --------------- PESQUISAR SÓCIO

  def pesquisar_socio(self, nomeSocio):
    print(150*'-')
    print(f"RESERVAS PARA O SÓCIO: {nomeSocio.upper()}")
    for i in range (len(self.__reserva)):
      if self.__reserva[i]["solicitante"] == nomeSocio:
        print(self.__reserva[i]) 
    print(150*'-')

  # --------------- TROCA DE SALA ENTRE SÓCIOS
  def troca_sala_socio(self, nomeSocio, novoNomeSocio, nomeSala):
    for i in range (len(self.__reserva)):
      if self.__reserva[i]["solicitante"] == nomeSocio and self.__reserva[i]["nome"] == nomeSala:
        self.__reserva[i]["solicitante"] = novoNomeSocio
    if len(self.__reserva) == 0:
      print("Não existem reservas no sistema")

  # --------------- ALTERAÇÃO DE HORÁRIO
  # def troca_horario_sala(self, sala, horarioNovo):
  #   if sala == self.__reserva[i]["nome"] and horarioNovo == self.__reserva[i]["hora"]:
  #     print('ocupado')
  #   for i in range(len(self.__reserva)):
  #     horarioSala = self.__reserva[i]["hora"].split()
      

  def exibir_reservas(self):
    for i in range(len(self.__reserva)):
      print("Solicitante:", self.__reserva[i]["solicitante"]," | ","Sala:",self.__reserva[i]["nome"]," | ","Hora Marcada:",self.__reserva[i]["hora"]," | ","Dia marcado:",self.__reserva[i]["dia"]," | ","Mês:",self.__reserva[i]["mes"])

    if len(self.__reserva) == 0:
      print("Não existem reservas no sistema")

