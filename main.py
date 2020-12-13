from secretaria import Secretaria
from sala import Sala
from dia import Dia
from reserva import Reserva
from socio import Socio

socio = Socio()
socio.nome = 'Mathias'

socio2 = Socio()
socio2.nome = 'Lucas'

socio3 = Socio()
socio3.nome = 'Seu Zé'

func = Secretaria()
func.nome = 'Rita'
func.ramal = 6546543
func.cargo = 'Secretária'
func.socio = socio
func.socio2 = socio2
func.socio3 = socio3

sala = Sala()
sala.nome = 'SALA 1 - Sala de Reuniões'
sala.situacao = 'Ocupada'
sala.func = func

sala2 = Sala()
sala2.nome = 'SALA 2 - Sala de Reuniões'
sala2.situacao = 'Ocupada'
sala2.func = func

sala3 = Sala()
sala3.nome = 'SALA 3 - Sala de Reuniões'
sala3.situacao = 'Ocupada'
sala3.func = func

sala4 = Sala()
sala4.nome = 'SALA 4 - Sala de Reuniões'
sala4.situacao = 'Ocupada'
sala4.func = func

teste = Dia()
teste.definir_hora = '8:00 às 9h00'
teste.definir_dia = 15
teste.definir_mes = 'Agosto'
teste.sala = sala

teste2 = Dia()
teste2.definir_hora = '15h00 às 18h00'
teste2.definir_dia = 16
teste2.definir_mes = 'Setembro'
teste2.sala = sala

reserva = Reserva()


reserva.adicionar_reservas(sala.nome, teste.mostra_dia, teste.mostra_mes, teste.mostra_hora, teste.sala.func.socio.nome)
reserva.adicionar_reservas(sala2.nome, teste.mostra_dia, teste.mostra_mes, teste2.mostra_hora, teste.sala.func.socio2.nome)
reserva.troca_sala_socio('Lucas','João', 'SALA 2 - Sala de Reuniões')
reserva.exibir_reservas()




