# Piedra papel tijera
# necesitamos 2 jugadores minimos
# variables
# jugador 1
# jugador 2
# opciones
# piedra
# papel
# tijera
# reglas
# piedra gana a tijera
# tijera gana a papel
# papel gana a piedra
# empate
# resultado
# ganador
# perdedor


import random
def juego_piedra_papel_tijera():
    opciones = ['piedra', 'papel', 'tijera']
    jugador1 = input('Elige una de las opciones: piedra papel o tijera: ').lower()
    jugador2 = random.choice(opciones)
    print(f'El jugador 2 eligio: {jugador2}')
    if jugador1 == jugador2:
        print('Empate')
    elif jugador1 == 'piedra' and jugador2 == 'tijera':
        print('Ganaste')
    elif jugador1 == 'papel' and jugador2 == 'piedra':
        print('Ganaste')
    elif jugador1 == 'tijera' and jugador2 == 'papel':
        print('Ganaste')
    elif jugador1 == 'piedra' and jugador2 == 'papel':
        print('Perdiste')
    elif jugador1 == 'papel' and jugador2 == 'tijera':
        print('Perdiste')
    elif jugador1 == 'tijera' and jugador2 == 'piedra':
        print('Perdiste')
juego_piedra_papel_tijera()


