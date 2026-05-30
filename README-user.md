# Generador de Equipos

## Descripción

Generador de Equipos es una aplicación de consola desarrollada en Python cuyo objetivo es crear automáticamente una formación de fútbol a partir de jugadores cargados por el usuario. Cada jugador posee estadísticas de defensa y ataque, y el sistema utiliza esos valores para determinar en qué posición rendiría mejor dentro del equipo.

El programa está pensado como una herramienta simple pero flexible para experimentar con la construcción de equipos utilizando criterios objetivos basados en estadísticas.

---

## Funcionamiento General

Al iniciar el programa, el usuario indica cuántos jugadores desea cargar. Para cada jugador se solicitan tres datos:

* Nombre.
* Nivel de defensa.
* Nivel de ataque.

Las estadísticas deben estar comprendidas entre 0 y 100. Además, existe una regla especial: solamente un jugador puede tener una defensa de 100 puntos, evitando empates absolutos para la selección automática del arquero.

Una vez finalizada la carga de datos, el sistema almacena toda la información y permite interactuar mediante distintos comandos.

---

## Selección Automática del Arquero

El arquero no es elegido manualmente.

El programa analiza todos los jugadores cargados y selecciona automáticamente como arquero al jugador con la mayor estadística de defensa. Esto garantiza que el jugador más apto para proteger el arco ocupe esa posición.

Después de elegir al arquero, el resto de los jugadores quedan disponibles para ocupar posiciones de campo.

---

## Creación de Formaciones

El usuario puede indicar cuántos defensas, mediocampistas y delanteros desea utilizar.

La suma de estas posiciones debe coincidir exactamente con la cantidad de jugadores de campo disponibles. Si la formación es inválida, el programa informa el error y solicita una nueva configuración.

Para construir el equipo:

1. Se seleccionan los mejores defensores según su estadística de defensa.
2. Se seleccionan los mejores delanteros según su estadística de ataque.
3. Los jugadores restantes son asignados al mediocampo.
4. Los mediocampistas se ordenan utilizando la suma de defensa y ataque para reflejar un mejor equilibrio entre ambas habilidades.

Este método permite generar equipos coherentes sin necesidad de asignar manualmente cada posición.

---

## Administración de Jugadores

El sistema permite modificar la información cargada en cualquier momento.

Las estadísticas de defensa y ataque pueden editarse individualmente, manteniendo las mismas validaciones utilizadas durante la carga inicial.

También es posible cambiar el nombre de un jugador ya existente sin perder sus estadísticas.

Todas las modificaciones se reflejan inmediatamente en futuras formaciones.

---

## Validación de Datos

El programa incorpora múltiples controles para evitar errores de entrada:

* Impide dejar campos numéricos vacíos.
* Rechaza textos cuando se esperan números.
* Verifica que las estadísticas estén dentro del rango permitido.
* Evita la existencia de múltiples jugadores con defensa máxima.
* Comprueba que las formaciones sean válidas antes de generarlas.
* Detecta comandos incompletos o inexistentes.

Estas validaciones buscan mantener la estabilidad del sistema y mejorar la experiencia de uso.

---

## Filosofía del Proyecto

El proyecto fue diseñado priorizando la simplicidad, la claridad del código y la facilidad de uso. Todas las decisiones de armado del equipo se basan exclusivamente en estadísticas objetivas, permitiendo obtener resultados consistentes y fáciles de comprender.

Además de servir como herramienta funcional, el proyecto también actúa como ejercicio práctico de programación, utilizando estructuras de datos, validación de entradas, algoritmos de selección y sistemas de comandos interactivos.

---

## Características Principales

* Carga dinámica de jugadores.
* Estadísticas de ataque y defensa personalizadas.
* Selección automática del arquero.
* Generación automática de formaciones.
* Edición de estadísticas.
* Cambio de nombres de jugadores.
* Validación robusta de entradas.
* Sistema de comandos interactivo.
* Organización automática de posiciones según rendimiento.

---

## Objetivo

El objetivo principal del proyecto es transformar una lista de jugadores y estadísticas en una formación completa y equilibrada, automatizando el proceso de selección mediante reglas simples y transparentes que facilitan la creación de equipos de manera rápida y eficiente.
