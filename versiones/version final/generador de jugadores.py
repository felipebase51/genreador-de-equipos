import time
print("Este programa sirve para generar un equipo a partir de jugadores cargados por vos.")
print("Primero vas a escribir cuantos jugadores queres cargar contando al arquero.")
print("Despues el programa te va a pedir el nombre, la defensa y el ataque de cada jugador.")
print("Con esos datos, el sistema elige automaticamente al arquero usando la defensa mas alta.")
print("Cuando escribas crear, vas a elegir cuantos defensas, medios y delanteros queres usar.")
print("El programa ordena los jugadores segun sus estadisticas para armar la formacion.")
print("Tambien podes editar estadisticas, cambiar nombres, ver la lista de jugadores o resetear.")
print("ADVERTENCIA: en el ejecutor Koodland no se puede ejecutar con mas de 6 jugadores.")
print("Si queres usar mas de 6 jugadores, usa el ejecutor de python de Windows.")

def obtener_nombre_desde_comando(partes):
    nombre = ""

    for i in range(1, len(partes)):
        if nombre == "":
            nombre = partes[i]
        else:
            nombre = nombre + " " + partes[i]

    return nombre

def existe_defensa_100(jugadores, jugador_ignorado):
    for nombre in jugadores:
        if nombre != jugador_ignorado and jugadores[nombre]["defensa"] == 100:
            return True

    return False

def pedir_numero(texto):
    while True:
        valor = input(texto)

        if valor == "":
            print("no escribiste nada")
        elif valor.isdigit():
            return int(valor)
        else:
            print("tenes que escribir un numero")

def pedir_stat(nombre, stat, jugadores, jugador_ignorado):
    while True:
        valor = pedir_numero("cuanta " + stat + " tiene " + nombre + "?(0-100) ")

        if valor < 0 or valor > 100:
            print("la stat tiene que estar entre 0 y 100")
        elif stat == "defensa" and valor == 100 and existe_defensa_100(jugadores, jugador_ignorado):
            print("ya hay un jugador con 100 de defensa, no puede haber dos")
        else:
            return valor

while True:
    jugadores = {}
    cantidad_jugadores = pedir_numero("cuantos jugadores queres cargar contando el arquero? ")

    while cantidad_jugadores < 2:
        print("tiene que haber por lo menos 2 jugadores")
        cantidad_jugadores = pedir_numero("cuantos jugadores queres cargar contando el arquero? ")

    # CARGA DE JUGADORES
    for i in range(1, cantidad_jugadores + 1):
        nombre = input("como se llama el jugador " + str(i) + "? ")
        print('procesando')
        time.sleep(1)
        print('============================')

        defensa = pedir_stat(nombre, "defensa", jugadores, nombre)
        print('procesando')
        time.sleep(1)
        print('============================')

        ataque = pedir_stat(nombre, "ataque", jugadores, nombre)
        print('procesando')
        time.sleep(1)
        print('============================')

        jugadores[nombre] = {"defensa": defensa, "ataque": ataque}
    print('Jugadores cargados:')
    for nombre in jugadores:
        print(nombre, "-", jugadores[nombre]["defensa"], "-", jugadores[nombre]["ataque"])

    # SISTEMA DE COMANDOS
    print('============================')
    print('este programa crea un equipo segun las estadisticas de los jugadores. palabras clave:')
    print('crear(crea el equipo y pregunta cuantos defensas, medios y delanteros queres)')
    print('editar nombre de jugador(editar stat de jugador la maquina pregunta cual)')
    print('editname player(editar el nombre del jugador)')
    print('print(muestra la lista de jugadores con estadisticas)')
    print('============================')
    while True:
        accion = input('q quieres hacer? ')
        print('============================')
        if accion == "":
            print('============================')
            print("no escribiste nada")
            print('============================')
            continue

        partes = accion.split()

        
        

        # CREAR EQUIPO
        if partes[0] == "crear":
            cant_defensas = pedir_numero("cuantos defensas queres?")
            cant_medios = pedir_numero("cuantos medios queres?")
            cant_ataques = pedir_numero("cuantos delanteros queres?")

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
            print('============================')
            print("      ARQUERO")
            print("      ", arquero)
            time.sleep(1)
            print('============================')

            print("\nDEFENSAS")
            for d in defensas:
                print("   ", d)
            time.sleep(1)
            print('============================')

            print("\nMEDIOS")
            for m in medios:
                print("   ", m)
            time.sleep(1)
            print('============================')

            print("\nATAQUE")
            for a in ataques:
                print("   ", a)
            time.sleep(1)
            print('============================')

        # EDITAR JUGADOR
        elif partes[0] == "editar":
            if len(partes) < 2:
                print("falta jugador")
            else:
                nombre = obtener_nombre_desde_comando(partes)

                if nombre in jugadores:
                    stat = input('def o atk? ')

                    if stat == "def":
                        nuevo = pedir_stat(nombre, "defensa", jugadores, nombre)
                        jugadores[nombre]["defensa"] = nuevo

                    elif stat == "atk":
                        nuevo = pedir_stat(nombre, "ataque", jugadores, nombre)
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

        elif partes[0] == "print":
            print('============================')
            print("Jugadores cargados:")
            for nombre in jugadores:
                print(nombre, "-", jugadores[nombre]["defensa"], "-", jugadores[nombre]["ataque"])
            print('============================')

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
        

