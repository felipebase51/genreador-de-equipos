import time

while True:
    jugadores = {}

    # CARGA DE JUGADORES
    for i in range(1, 12):
        nombre = input('¿como se llama el jugador ' + str(i) + '? ')
        print('procesando')
        time.sleep(1)

        defensa = int(input('¿cuanta defensa tiene ' + nombre + '?(0-100) '))
        print('procesando')
        time.sleep(1)

        ataque = int(input('¿cuanta ataque tiene ' + nombre + '?(0-100) '))
        print('procesando')
        time.sleep(1)

        jugadores[nombre] = {"defensa": defensa, "ataque": ataque}

    # SISTEMA DE COMANDOS
    while True:
        accion = input('q quieres hacer? ')

        if accion == "":
            print("no escribiste nada")
            continue

        partes = accion.split()

        if partes[0] == "crear":
            print("creando equipo...")

        print("este print quedo mal ubicado entre if y elif")
        elif partes[0] == "editar":
            print("editar jugador")

        else:
            print("comando no valido")
