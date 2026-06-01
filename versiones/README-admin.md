# README Admin

Proyecto: generador de equipos.

Mantiene versiones historicas, previews, cambios microscopicos, cache compilado y reportes de crashes.

## Estructura

- `versiones/`: historial completo (beta, estables, previews).
- `versiones/version final/`: el archivo jugable final `generador de jugadores.py`.
- `versiones/versiones preliminares(cambios muy pequeños)/`: cambios microscopicos (categoria W).
- `versiones/betas/`: betas historicas.
- `crash_reports/`: solo crashes criticos.
- `jugables/`: cache .pyc movido desde las versiones.
- `CHANGELOG.md`: historial unico del proyecto.
- `actualizar_version_final.py`: script para copiar automaticamente una version a version final.

## Versionado

- beta: pruebas jugables.
- version estable: version principal lista para usar.
- preview: version previa a estable con cambios medianos.
- versiones preliminares (W-X): cambios microscopicos.
- crash_reports: solo crashes criticos, no ejecutar los .py.

## Reglas

- No usar f-strings ni .format().
- Solo import time (para el codigo principal).
- Revisar sintaxis despues de cada modificacion.
- Mantener __pycache__.
- Actualizar CHANGELOG.md siempre.
- Registrar solo crashes criticos.

## Versiones actuales

| Archivo | Descripcion |
|---|---|
| 0-beta.py | Primera version jugable |
| 1.0.py a 1.2.py | Estables anteriores |
| 1.3-stable.py | Version estable 1.3 |
| 1.4-preview-1 a 5 | Previews de 1.4 |
| 1.4-preview w-1 | Version con explicacion inicial ampliada |
| 1.4-preview-3 w-1 a w-5 | Cambios microscopicos sobre preview-3 |
| version final/ | w-5 (solo import time) |
