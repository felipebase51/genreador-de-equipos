import time
import os

print("Actualizador de version final del generador de equipos")
print("======================================================")
print("")
time.sleep(1)

versiones_dir = os.path.join(os.path.dirname(__file__), "versiones")
version_final_dir = os.path.join(versiones_dir, "version final")
version_final_path = os.path.join(version_final_dir, "generador de jugadores.py")
changelog_path = os.path.join(os.path.dirname(__file__), "CHANGELOG.md")

# buscar archivos .py en versiones/
archivos = []
for entrada in os.listdir(versiones_dir):
    ruta = os.path.join(versiones_dir, entrada)
    if os.path.isfile(ruta) and entrada.endswith(".py"):
        archivos.append((entrada, ruta))

if len(archivos) == 0:
    print("ERROR: no se encontraron versiones en la carpeta versiones/")
    exit()

print("Versiones encontradas:")
for i in range(len(archivos)):
    print(str(i + 1) + " - " + archivos[i][0])

print("")
print("Elegi el numero de la version que queres pasar a version final")
print("o apreta Enter para usar la mas nueva:")
seleccion = input("> ")

if seleccion == "":
    archivos.sort(key=lambda x: x[0], reverse=True)
    archivo_elegido = archivos[0]
    print("Se eligio automaticamente: " + archivo_elegido[0])
else:
    try:
        indice = int(seleccion) - 1
        if indice < 0 or indice >= len(archivos):
            print("ERROR: numero invalido")
            exit()
        archivo_elegido = archivos[indice]
    except ValueError:
        print("ERROR: tenes que escribir un numero")
        exit()

print("")
print("Procesando: " + archivo_elegido[0])
time.sleep(1)

# leer la version elegida
with open(archivo_elegido[1], "r", encoding="utf-8") as f:
    contenido = f.read()

lineas = contenido.split("\n")

# VALIDACIONES
errores = []

# revisar f-strings
for i in range(len(lineas)):
    linea = lineas[i]
    if "f\"" in linea or "f'" in linea:
        errores.append("linea " + str(i + 1) + " tiene f-string: " + linea.strip())

# revisar .format()
for i in range(len(lineas)):
    linea = lineas[i]
    if ".format(" in linea:
        errores.append("linea " + str(i + 1) + " usa .format(): " + linea.strip())

# revisar imports (solo import time)
imports_lineas = []
for i in range(len(lineas)):
    linea = lineas[i].strip()
    if linea.startswith("import ") or linea.startswith("from "):
        imports_lineas.append((i + 1, linea))

imports_validos = 0
for num, linea in imports_lineas:
    if linea == "import time":
        imports_validos = imports_validos + 1
    else:
        errores.append("linea " + str(num) + " tiene import no permitido: " + linea)

if len(errores) > 0:
    print("")
    print("ERRORES ENCONTRADOS:")
    for e in errores:
        print(" - " + e)
    print("")
    print("No se actualizo la version final. Corregi los errores primero.")
    exit()

print("Validaciones pasadas: sin f-strings, sin .format(), solo import time")
time.sleep(1)

# guardar en version final
with open(version_final_path, "w", encoding="utf-8") as f:
    f.write(contenido)

print("")
print("Archivo copiado a: versiones/version final/generador de jugadores.py")
time.sleep(1)

# actualizar CHANGELOG.md
fecha_actual = "2026-05-31"  # hardcodeado segun rules

nueva_entrada = ""
nueva_entrada = nueva_entrada + "### " + fecha_actual + "\n"
nueva_entrada = nueva_entrada + "\n"
nueva_entrada = nueva_entrada + "- Se ejecuto actualizar_version_final.py con " + archivo_elegido[0] + ".\n"
nueva_entrada = nueva_entrada + "- Se actualizo versiones/version final/generador de jugadores.py.\n"

contenido_changelog = ""
with open(changelog_path, "r", encoding="utf-8") as f:
    contenido_changelog = f.read()

lineas_changelog = contenido_changelog.split("\n")

# buscar donde insertar (despues del ultimo "###" en "Cambios recientes")
indice_cambios_recientes = -1
for i in range(len(lineas_changelog)):
    if lineas_changelog[i].strip() == "## Cambios recientes":
        indice_cambios_recientes = i
        break

if indice_cambios_recientes == -1:
    print("ADVERTENCIA: no se encontro '## Cambios recientes' en CHANGELOG.md")
    print("El changelog no se actualizo automaticamente.")
else:
    # buscar el primer "###" despues de "Cambios recientes"
    primer_fecha = -1
    for i in range(indice_cambios_recientes + 1, len(lineas_changelog)):
        if lineas_changelog[i].strip().startswith("### "):
            primer_fecha = i
            break

    if primer_fecha == -1:
        # no hay entradas, agregar al final de Cambios recientes
        nuevas_lineas = lineas_changelog[:indice_cambios_recientes + 1]
        nuevas_lineas.append("")
        for l in nueva_entrada.split("\n"):
            nuevas_lineas.append(l)
        for l in lineas_changelog[indice_cambios_recientes + 1:]:
            nuevas_lineas.append(l)
    else:
        # insertar antes de la primera fecha existente
        nuevas_lineas = lineas_changelog[:primer_fecha]
        nuevas_lineas.append("")
        for l in nueva_entrada.split("\n"):
            nuevas_lineas.append(l)
        for l in lineas_changelog[primer_fecha:]:
            nuevas_lineas.append(l)

    with open(changelog_path, "w", encoding="utf-8") as f:
        f.write("\n".join(nuevas_lineas))

    print("CHANGELOG.md actualizado correctamente.")

print("")
print("Listo. La version final ahora es: " + archivo_elegido[0])
