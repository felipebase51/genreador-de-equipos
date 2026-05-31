# Changelog

Changelog unico del proyecto `generador de equipos`. Este archivo junta el historial desde la beta hasta la ultima version encontrada en `versiones/`.

## Reglas de versionado

- `beta`: primeras pruebas jugables o experimentales.
- `version estable`: version principal lista para usar.
- `preview`: version previa a una estable con cambios medianos o grandes.
- `versiones preliminares(cambios muy pequeÃ±os)`: carpeta para cambios microscopicos, tambien llamada categoria W-X en la organizacion del proyecto.
- `crash_reports`: solo para crashes criticos; no se ejecutan esos `.py` para evitar generar cache de versiones rotas.

## Historial

### 0-beta.py

- Primera version jugable.
- Carga 11 jugadores con nombre, defensa y ataque.
- Permite crear equipo, editar estadisticas y resetear.
- Elige arquero automaticamente por defensa mas alta.
- Reparte jugadores entre defensa, medio y ataque segun diferencia entre defensa y ataque.

### 1.0.py

- Version estable inicial.
- Conserva la base de carga de jugadores, creacion de equipo, edicion y reseteo.
- Normaliza textos y comillas respecto de la beta.

### 1.1.py

- Agrega ayuda de comandos en pantalla.
- Agrega `editname` para cambiar el nombre de un jugador.
- Agrega `print` para volver a mostrar jugadores cargados.
- Mantiene `crear`, `editar` y `resetear si`.

### 1.2.py

- Agrega cantidad configurable de jugadores.
- Permite elegir cuantos defensas, medios y delanteros usar.
- Ordena defensas por defensa, delanteros por ataque y medios por suma de defensa y ataque.
- Agrega advertencia sobre limite del ejecutor Koodland.

### 1.3-preview-1.py

- Preview previa a 1.3.
- Mejora el armado por formacion elegida.
- Agrega funcion para obtener nombres completos desde comandos con espacios.
- Mantiene comandos de edicion, cambio de nombre, impresion y reseteo.

### 1.3-stable.py

- Version estable de 1.3.
- Consolida el sistema de cantidad de jugadores contando al arquero.
- Mantiene seleccion de arquero automatica y reparto por posiciones elegidas.
- Deja la base preparada para previews 1.4.

### 1.4-preview-1.py

- Agrega validacion de estadisticas entre 0 y 100.
- Agrega regla para evitar dos jugadores con defensa 100.
- Centraliza la carga de estadisticas en `pedir_stat`.
- Mantiene la estructura de comandos de 1.3.

### 1.4-preview-2.py

- Agrega mensajes iniciales explicando que hace el programa.
- Mantiene la advertencia del ejecutor Koodland.
- Prepara el codigo para validaciones mas fuertes en entradas numericas.

### 1.4-preview-3.py

- Agrega imports permitidos por reglas del proyecto y deja comentario de no importar otros sin preguntar.
- Agrega `pedir_numero` para evitar crashes cuando el usuario aprieta Enter o escribe texto en entradas numericas.
- Usa `pedir_numero` en cantidad de jugadores y en la formacion.
- Mantiene validacion de estadisticas, defensa 100 unica, comandos y armado de equipo.

## Crash reports

- `crash-critico v-pre-1.0.py`: version previa con crash critico conservada para reporte.
- `crash-critico v-1.3.py`: crash critico relacionado con version 1.3.
- `crash-critico v-1.4 preview-2.py`: crash critico relacionado con preview 1.4.

## Cambios recientes

### 2026-05-15

- Se creo `crash_reports/crash reports.md` con los crashes anteriores y el reporte de `w-1`.
- Se actualizo `versiones/README-admin.md` para apuntar al indice general de crash reports.
- Se elimino `crash-critico w-1 elif print.md` porque el detalle quedo centralizado en `crash reports.md`.
- Se corrigio `1.4-preview-3  w-4.py`: tenia un string sin cerrar en la ayuda de comandos.
- Se actualizo `crash_reports/crash reports.md` con el crash de `w-4`.

### 2026-05-31

- Se recupero `versiones/versiones preliminares(cambios muy pequeños)/1.4-preview-3  w-5.py` desde el pycache.
- Se creo `actualizar_version_final.py` en la carpeta base para automatizar la actualizacion.
- Se confirmo que `versiones/version final/generador de jugadores.py` ya contiene el codigo de w-5.
- Se actualizo `CHANGELOG.md` con los cambios de hoy.

### 2026-05-22

- Se creo `versiones/versiones preliminares(cambios muy pequeños)/1.4-preview w-1.py`.
- Se amplio la explicacion inicial del programa sin cambiar la logica.
- Se dejo solo `import time`, sin imports extra heredados de versiones anteriores.
- Se actualizo `versiones/version final/generador de jugadores.py` con `1.4-preview w-1.py`.
