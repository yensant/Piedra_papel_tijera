import random


def jugar():
    opciones = ['pi', 'pa', 'ti']
    intentos = 3

    while intentos > 0:
        usuario = input("Escoge una opción: 'pi' para piedra, 'pa' para papel, "
                        "'ti' para tijera.\n").lower()
        computadora = random.choice(opciones)

        if usuario == computadora:
            print(f'¡Empate! El oponente también eligió {computadora}.')
        elif gano_el_jugador(usuario, computadora):
            print(f'¡Ganaste! El oponente eligió {computadora}.')
            break
        else:
            print(f'¡Perdiste! El oponente eligió {computadora}.')
            intentos -= 1

        if intentos == 0:
            print('¡Se acabaron los intentos!.')


def gano_el_jugador(jugador, oponente):
    # Retornar True (verdadero) si gana o gano el jugador
    # Piedra gana a Tijera (pi > ti).
    # Tijera gana a Papel (ti > pa)
    # Papel gana a Piedra (pa > pi)
    if ((jugador == 'pi' and oponente == 'ti')
            or (jugador == 'ti' and oponente == 'pa')
            or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False


jugar()
