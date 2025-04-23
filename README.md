## Cálculo de Conjuntos Primero, Siguiente y Predicción

Este proyecto proporciona un script en Python para calcular los conjuntos **PRIMERO**, **SIGUIENTE** y **PREDICCIÓN** de una gramática libre de contexto, facilitando la construcción de tablas para parsers LL(1).

---

## Descripción

- **`calcular_primeros`**: calcula el conjunto PRIMERO para cada no-terminal.
- **`calcular_siguientes`**: calcula el conjunto SIGUIENTE para cada no-terminal, usando los resultados de PRIMERO.
- **`calcular_predicciones`**: para cada producción `A → α`, construye su conjunto de PREDICCIÓN (FIRST(α) ∖ {ε} ∪ {FOLLOW(A) si α puede derivar ε}).

Este script itera hasta que no hay más cambios, siguiendo las definiciones canónicas de teoría de compiladores.

---

## Prerrequisitos

- Python 3.6 o superior

No se requieren librerías externas; el script usa únicamente la librería estándar de Python.

---

## Instalación y uso

1. Define tu gramática dentro del diccionario `gramatica`:
    ```python
    gramatica = {
        'S': [['A','B','C'], ['D','E']],
        'A': [['dos','B','tres'], ['ε']],
        ...
    }
    ```
2. Ejecuta el script desde la terminal:
    ```bash
    python Prim-Sig-Pred.py
    ```
3. Verás en pantalla los conjuntos PRIMERO, SIGUIENTE y PREDICCIÓN para cada no-terminal y producción.

---

## Formato de la gramática

- La gramática se define como un diccionario de Python:
  - **Clave**: no-terminal (string).
  - **Valor**: lista de producciones.
    - Cada producción es una lista de símbolos (strings).
    - Los símbolos que no aparecen como clave se consideran terminales.
    - La cadena vacía se representa con `'ε'`.

**Ejemplo minimal:**
```python
gramatica = {
    'S': [['a', 'S'], ['ε']],
}
```

---

## Ejemplo de salida

```text
Primero(S) = {'a', 'ε'}
Siguiente(S) = {'$'}
PREDICCIÓN(S → a S) = {'a'}
PREDICCIÓN(S → ε) = {'$'}
```

