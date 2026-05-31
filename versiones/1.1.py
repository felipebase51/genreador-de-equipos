import time

while True:
    jugadores = {}

    # CARGA DE JUGADORES
    for i in range(1, 12):
        nombre = input("como se llama el jugador " + str(i) + "? ")
        print("procesando")
        time.sleep(1)

        defensa = int(input("cuanta defensa tiene " + nombre + "?(0-100) "))
        print("procesando")
        time.sleep(1)

        ataque = int(input("cuanta ataque tiene " + nombre + "?(0-100) "))
        print("procesando")
        time.sleep(1)

        jugadores[nombre] = {"defensa": defensa, "ataque": ataque}

    print("Jugadores cargados:")
    for nombre in jugadores:
        print(nombre, "-", jugadores[nombre]["defensa"], "-", jugadores[nombre]["ataque"])

    # SISTEMA DE COMANDOS
    print("palabras clave: crear, editar nombre de jugador, editname nombre de jugador, print, resetear si")

    while True:
        accion = input("q quieres hacer? ")

        if accion == "":
            print("no escribiste nada")
            continue

        partes = accion.split()

        # CREAR EQUIPO
        if partes[0] == "crear":
            print("creando equipo...")
            time.sleep(1)

            # asignar posiciones
            for nombre in jugadores:
                defensa = jugadores[nombre]["defensa"]
                ataque = jugadores[nombre]["ataque"]

                if defensa > ataque + 10:
                    jugadores[nombre]["posicion"] = "defensa"
                elif ataque > defensa + 10:
                    jugadores[nombre]["posicion"] = "ataque"
                else:
                    jugadores[nombre]["posicion"] = "medio"

            # arquero
            arquero = None
            max_def = -1

            for nombre in jugadores:
                if jugadores[nombre]["defensa"] > max_def:
                    max_def = jugadores[nombre]["defensa"]
                    arquero = nombre

            # listas
            defensas = []
            medios = []
            ataques = []

            for nombre in jugadores:
                if nombre != arquero:
                    pos = jugadores[nombre]["posicion"]

                    if pos == "defensa":
                        defensas.append(nombre)
                    elif pos == "medio":
                        medios.append(nombre)
                    elif pos == "ataque":
                        ataques.append(nombre)

            # mostrar formacion
            print("      ARQUERO")
            print("      ", arquero)
            time.sleep(1)

            print("\nDEFENSAS")
            for d in defensas:
                print("   ", d)
            time.sleep(1)

            print("\nMEDIOS")
            for m in medios:
                print("   ", m)
            time.sleep(1)

            print("\nATAQUE")
            for a in ataques:
                print("   ", a)
            time.sleep(1)

        # EDITAR JUGADOR
        elif partes[0] == "editar":
            if len(partes) < 2:
                print("falta jugador")
            else:
                nombre = " ".join(partes[1:])

                if nombre in jugadores:
                    stat = input("def o atk? ")

                    if stat == "def":
                        nuevo = int(input("nuevo valor: "))
                        jugadores[nombre]["defensa"] = nuevo

                    elif stat == "atk":
                        nuevo = int(input("nuevo valor: "))
                        jugadores[nombre]["ataque"] = nuevo

                    print("jugador actualizado")

                else:
                    print("no existe")

        # EDITAR NOMBRE
        elif partes[0] == "editname":
            if len(partes) < 2:
                print("falta jugador")
            else:
                nombre = " ".join(partes[1:])

                if nombre in jugadores:
                    nuevo_nombre = input("nuevo nombre: ")

                    if nuevo_nombre == "":
                        print("el nombre no puede estar vacio")
                    elif nuevo_nombre in jugadores:
                        print("ya existe un jugador con ese nombre")
                    else:
                        jugadores[nuevo_nombre] = jugadores[nombre]
                        del jugadores[nombre]
                        print("nombre actualizado")

                else:
                    print("no existe")

        # MOSTRAR JUGADORES
        elif partes[0] == "print":
            print("Jugadores cargados:")
            for nombre in jugadores:
                print(nombre, "-", jugadores[nombre]["defensa"], "-", jugadores[nombre]["ataque"])

        # RESETEAR
        elif partes[0] == "resetear":
            if len(partes) > 1 and partes[1] == "si":
                print("reiniciando todo...")
                time.sleep(1)
                break
            else:
                print("pone: resetear si")

        else:
            print("comando no valido")
