# Reversing a string on Python

Aquí tienes unas notas relevantes sobre el texto que explica cómo invertir una cadena en Python utilizando dos métodos:

### Método 1: Usando el Slice Function

- **Concepto**: Python no tiene una función incorporada para invertir cadenas, pero se puede hacer mediante la técnica de "slice".
- **Sintaxis de Slice**:
  - La sintaxis general es: `string[start:stop:step]`.
  - `start` y `stop` indican los índices entre los cuales se manipula la cadena.
  - `step` determina el salto entre los índices.
- **Inversión de Cadena**:
  - Para invertir una cadena, se utiliza `step` con el valor `-1`, lo que recorre la cadena desde el final al inicio.
  - Ejemplo: 
    ```python
    trial = "reversal"
    new_trial = trial[::-1]
    print(new_trial)  # Imprime "lasrever"
    ```
  - `trial[::-1]` crea una nueva cadena invertida.
- **Nota**: Se puede usar el mismo variable para la manipulación, pero se usó una variable diferente para claridad.

### Método 2: Usando Recursión

- **Concepto**: La recursión puede ser utilizada para invertir una cadena.
- **Definición de Función**:
  - Se define una función que toma una cadena y la invierte recursivamente.
  - Ejemplo:
    ```python
    def string_reverse(str):
        if len(str) == 0:
            return str
        else:
            return string_reverse(str[1:]) + str[0]
    ```
  - **Explicación**:
    - Base del caso: Si la longitud de la cadena es 0, se devuelve la cadena.
    - Caso recursivo: Llama a la función con la cadena sin el primer carácter y añade el primer carácter al final.
- **Uso**:
  - Llama a la función con la cadena que se desea invertir y almacena el resultado.
  - Ejemplo:
    ```python
    original_str = "reversal"
    reversed_str = string_reverse(original_str)
    print(reversed_str)  # Imprime "lasrever"
    ```

### Resumen
- **Método 1**: Utiliza el slice function para invertir la cadena de forma simple y directa.
- **Método 2**: Utiliza recursión para lograr el mismo resultado, demostrando el uso de funciones recursivas en Python.