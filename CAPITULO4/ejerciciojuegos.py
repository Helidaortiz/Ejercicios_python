print("Piedra,papel o tijera:  ")
turno1=input("jugador1:")
turno2=input("jugador2:")
if turno1=='papel'and turno2=='tijera':
    print("jugador2 gana---porque tijera daña papel")
if turno1=='papel' and turno2=='piedra':
    print("Jugador1 gana---porque papel enrolla piedra")
if turno1=='tijera' and turno2=='papel':
    print("jugador1 gana ---porque tijera corta papel")
if turno1=='tijera' and turno2=='piedra':
    print("jugador2 gana---porque piedra daña tijera")
if turno1=='piedra' and turno2=='papel':
    print("juagador2 gana---papel enrolla piedra")
if turno1=='piedra' and turno2=='tijera':
    print("jugador1 gana---piedra daña tijera")
if turno1 == turno2:
    print("empate")