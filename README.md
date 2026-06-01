# Generador de Equipos

Este proyecto es un generador de equipos de futbol escrito en Python. Cargas jugadores con nombre, defensa y ataque, y el programa arma automaticamente una formacion eligiendo arquero, defensas, medios y delanteros segun sus estadisticas.

Todavia no llegamos ni a la 2.0. Esto recien empieza.

## Como funciona

1. Elegis cuantos jugadores cargar (minimo 2, contando al arquero).
2. Por cada jugador ingresas nombre, defensa (0-100) y ataque (0-100).
3. El sistema elige automaticamente al arquero (el de defensa mas alta).
4. Despues decidis cuantos defensas, medios y delanteros queres.
5. El programa ordena a los jugadores y muestra la formacion.

### Comandos disponibles

- `crear`: arma el equipo y pregunta cuantos defensas, medios y delanteros usar.
- `editar [nombre]`: cambia la defensa o el ataque de un jugador.
- `editname [nombre]`: cambia el nombre de un jugador.
- `print`: muestra la lista de jugadores cargados.
- `resetear si`: reinicia todo desde cero.

## Version actual

La version final es `1.4-preview-3 w-5` (solo import time, sin librerias extras). Esta en `versiones/version final/generador de jugadores.py`.

## Historial del proyecto

El proyecto arranco como una beta simple y fue evolucionando:

| Version | Que trajo |
|---|---|
| 0-beta | Primer prototipo con 11 jugadores fijos |
| 1.0 | Version estable inicial |
| 1.1 | Ayuda en pantalla y editname |
| 1.2 | Cantidad configurable de jugadores |
| 1.3-stable | Sistema consolidado con arquero automatico |
| 1.4-preview-1 | Validacion de stats 0-100 |
| 1.4-preview-2 | Mensajes iniciales explicativos |
| 1.4-preview-3 | pedir_numero anti-crash |
| w-1 a w-5 | Cambios microscopicos y limpieza |

El changelog completo esta en `CHANGELOG.md`.

## Estructura del proyecto

```
versiones/                  - historial completo de versiones
  version final/            - la version jugable actual
  versiones preliminares/   - cambios microscopicos (categoria W)
  betas/                    - betas historicas
crash_reports/              - reportes de errores criticos
jugables/                   - cache compilado (.pyc)
```

## Reglas del codigo

- No usar f-strings ni .format()
- Solo concatenacion con +
- Solo import time (para el codigo principal)
- Mantener __pycache__

## Nota sobre ejecucion

En el ejecutor Koodland no funciona con mas de 6 jugadores. Para mas jugadores, usa Python de Windows directamente.
