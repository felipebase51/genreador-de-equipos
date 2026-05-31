# README Admin

Este proyecto es un generador de equipos segun estadisticas de jugadores. Mantiene versiones historicas, previews, versiones preliminares para cambios muy pequeños, cache generado y reportes de crashes criticos.

## Estructura principal

`jugador_equipo.py`

Archivo principal del proyecto. Debe representar la version estable o la version de trabajo que se quiera ejecutar desde la raiz.

`versiones/`

Carpeta con el historial de versiones del programa. Se usa un sistema parecido al de Minecraft:

- `0-beta.py`: primera version del proyecto.
- `1.0.py`, `1.1.py`, `1.2.py`: versiones estables anteriores.
- `1.3-preview-1.py`: preview previa de la version 1.3.
- `1.3-stable.py`: version estable 1.3.
- `1.4-preview-1.py`, `1.4-preview-2.py`, `1.4-preview-3.py`: previews actuales de la version 1.4.
- `versiones preliminares(cambios muy pequeños)/`: subcategoria para cambios micro o ajustes minimos que no justifican preview nueva.
- `version final/`: subcarpeta con el archivo jugable final.

Las previews van antes que la estable de su version. Cuando una preview se vuelve estable, se crea el archivo estable correspondiente.

`versiones/version final/`

Carpeta donde esta `generador de jugadores.py`, el archivo jugable final armado desde la ultima version preliminar.

`versiones/versiones preliminares(cambios muy pequeños)/`

Carpeta para guardar versiones W-X o cambios muy pequeños. Se usa cuando el cambio es microscopico, por ejemplo texto, documentacion, orden interno o ajuste minimo. Cada cambio, aunque sea pequeño, debe quedar registrado en `CHANGELOG.md`.

`CHANGELOG.md`

Changelog unico del proyecto. Reemplaza la idea de tener muchos changelogs sueltos: ahi se registra la historia desde `0-beta.py` hasta la ultima version disponible, incluyendo versiones preliminares y previews.

`crash_reports/`

Carpeta con reportes de crashes criticos. No se registran errores menores arreglados en previews. Cada reporte debe explicar:

- descripcion del crash;
- archivo donde ocurrio;
- version afectada;
- causa;
- arreglo aplicado.

Reportes actuales:

- `crash reports.md`: indice general con todos los crashes criticos, incluyendo `w-1`.
- `crash-critico v-pre-1.0.py`: version previa con crash critico conservada como referencia.
- `crash-critico v-1.3.py`: crash critico relacionado con version 1.3.
- `crash-critico v-1.4 preview-2.py`: crash critico relacionado con preview 1.4.

`__pycache__/`

Cache generado del archivo principal. No borrar. El proyecto lo conserva porque forma parte de la organizacion pedida.

`versiones/__pycache__/`

Cache generado de los archivos dentro de `versiones/`. No borrar. Debe mantenerse actualizado cuando se compilan o prueban versiones.
## Reglas del proyecto

- No usar f-strings.
- No usar `.format()`.
- Revisar sintaxis despues de cada modificacion.
- Mantener `__pycache__`.
- Registrar solo crashes criticos en `crash_reports/`.
- Para cambios microscopicos, crear o guardar la version en `versiones/versiones preliminares(cambios muy pequeños)/`.
- Para cambios chicos, crear preview.
- Para cambios importantes o arreglos criticos, avanzar version.
- Actualizar `CHANGELOG.md` despues de cualquier cambio, incluso si es minimo.
- Mantener la carpeta `versiones/` ordenada por version.
