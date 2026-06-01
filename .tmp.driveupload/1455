import time

print("ADVERTENCIA: en el ejecutor Koodland no se puede ejecutar con mas de 6 jugadores si deseas hacerlo con mas utiliza el ejecutor de phiton de windows")

def obtener_nombre_desde_comando(partes):
    nombre = ""

    for i in range(1, len(partes)):
        if nombre == "":
            nombre = partes[i]
        else:
            nombre = nombre + " " + partes[i]

    return nombre

while True:
    jugadores = {}
    cantidad_jugadores = int(input("cuantos jugadores queres cargar contando el arquero? "))

    while cantidad_jugadores < 2:
        print("tiene que haber por lo menos 2 jugadores")
        cantidad_jugadores = int(input("cuantos jugadores queres cargar contando el arquero? "))

    # CARGA DE JUGADORES
    for i in range(1, cantidad_jugadores + 1):
        nombre = input("como se llama el jugador " + str(i) + "? ")
        print('procesando')
        time.sleep(1)

        defensa = int(input('¿cuanta defensa tiene ' + nombre + '?(0-100) '))
        print('procesando')
        time.sleep(1)

        ataque = int(input('¿cuanta ataque tiene ' + nombre + '?(0-100) '))
        print('procesando')
        time.sleep(1)

        jugadores[nombre] = {"defensa": defensa, "ataque": ataque}

    print('Jugadores cargados:')
    for nombre in jugadores:
        print(nombre, "-", jugadores[nombre]["defensa"], "-", jugadores[nombre]["ataque"])

    # SISTEMA DE COMANDOS
    print('este programa crea un equipo segun las estadisticas de los jugadores. palabras clave: crear(crea el equipo y pregunta cuantos defensas, medios y delanteros queres), editar nombre de jugador(editar stat de jugador la maquina pregunta cual), editname player(editar el nombre del jugador), print(muestra la lista de jugadores con estadisticas) ADVERTENCIA CRITICA: USAR SIEMPRE EL ESPACIO DE LO CONTRARIO EL PROGRAMA SE ROMPERA')
        
    while True:
        accion = input('q quieres hacer? ')

        if accion == "":
            print("no escribiste nada")
            continue

        partes = accion.split()

        
        

        # CREAR EQUIPO
        if partes[0] == "crear":
            cant_defensas = int(input("cuantos defensas queres?"))
            cant_medios = int(input("cuantos medios queres?"))
            cant_ataques = int(input("cuantos delanteros queres?"))

            jugadores_de_campo = cantidad_jugadores - 1
            print("creando equipo...")
            time.sleep(1)
            if cant_defensas + cant_medios + cant_ataques != jugadores_de_campo:
                print("la suma de defensas, medios y delanteros tiene que dar " + str(jugadores_de_campo) + " sin contar el arquero")
                continue

            # arquero
            arquero = None
            max_def = -1

            for nombre in jugadores:
                if jugadores[nombre]["defensa"] > max_def:
                    max_def = jugadores[nombre]["defensa"]
                    arquero = nombre

            # listas
            disponibles = []
            for nombre in jugadores:
                if nombre != arquero:
                    disponibles.append(nombre)

            defensas_ordenadas = sorted(disponibles, key=lambda nombre: jugadores[nombre]["defensa"], reverse=True)
            defensas = defensas_ordenadas[:cant_defensas]

            restantes = []
            for nombre in disponibles:
                if nombre not in defensas:
                    restantes.append(nombre)

            ataques_ordenados = sorted(restantes, key=lambda nombre: jugadores[nombre]["ataque"], reverse=True)
            ataques = ataques_ordenados[:cant_ataques]

            medios = []
            for nombre in restantes:
                if nombre not in ataques:
                    medios.append(nombre)

            medios = sorted(medios, key=lambda nombre: jugadores[nombre]["defensa"] + jugadores[nombre]["ataque"], reverse=True)

            # mostrar formación
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
                nombre = obtener_nombre_desde_comando(partes)

                if nombre in jugadores:
                    stat = input('def o atk? ')

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
                nombre = obtener_nombre_desde_comando(partes)

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
