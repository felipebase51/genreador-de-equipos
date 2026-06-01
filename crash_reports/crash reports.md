# Crash reports

Indice general de crashes criticos del proyecto. Los archivos `.py` dentro de esta carpeta se conservan como evidencia historica y no deben ejecutarse.

## crash-critico v-pre-1.0.py

- Version afectada: previa a `1.0.py`.
- Tipo de crash: `SyntaxError`.
- Causa: habia un `print` colocado entre un `if` y un `elif`.
- Detalle: en Python, un `elif` debe venir inmediatamente despues del `if` o de otro `elif`; una instruccion suelta en el medio rompe la sintaxis.
- Estado: registrado como crash critico historico.

## crash-critico v-1.3.py

- Version afectada: `1.3`.
- Tipo de crash: `IndentationError` / error de indentacion.
- Causa: la linea `print("creando equipo...")` quedo con indentacion incorrecta dentro del comando `crear`.
- Detalle: la indentacion extra rompe el bloque antes de que el programa pueda ejecutarse.
- Estado: registrado como crash critico historico.

## crash-critico v-1.4 preview-2.py

- Version afectada: `1.4-preview-2`.
- Tipo de crash: error de entrada numerica.
- Causa: varias entradas numericas usaban `int(input(...))` directamente.
- Detalle: si el usuario apretaba Enter o escribia texto donde iba un numero, el programa podia crashear.
- Estado: corregido luego con funciones de validacion como `pedir_numero` y `pedir_stat`.

## crash-critico w-1 elif print.md

- Version afectada: `1.4-preview-3  w-1.py`.
- Tipo de crash: `SyntaxError`.
- Causa: separadores `print('============================')` colocados entre bloques `elif`.
- Detalle: se movieron los separadores dentro del bloque `elif partes[0] == "print":`.
- Estado: corregido en `1.4-preview-3  w-2.py`.
