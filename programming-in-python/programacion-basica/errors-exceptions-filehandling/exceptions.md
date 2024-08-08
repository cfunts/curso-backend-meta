# Exceptions

Aquí tienes unas notas relevantes del texto:

- **Errores y Excepciones en Python**: Importantes para desarrolladores novatos.
- **Errores**:
  - **Errores de Sintaxis**:
    - Causados por errores humanos como errores tipográficos o de sintaxis.
    - Ejemplos incluyen la falta de dos puntos al final de condiciones o declaraciones.
    - Generalmente detectados por los IDEs, como Visual Studio Code, que ofrecen advertencias y pistas.
    - Problemas comunes como errores de indentación.
  - **Excepciones**:
    - Ocurren durante la ejecución del código y pueden pasar desapercibidas.
    - Ejemplo: `ZeroDivisionError` si se intenta dividir por cero.
    - Python incluye excepciones integradas para identificar problemas potenciales.
- **Manejo de Excepciones**:
  - Necesario para evitar que la aplicación falle.
  - Los desarrolladores deben manejar estas excepciones para mantener la estabilidad del código.

Estos puntos cubren la diferencia entre errores y excepciones, y cómo cada uno debe ser abordado para mejorar la calidad del código en Python.


## Handling Exceptions

### Notas Relevantes del Texto sobre Manejo de Excepciones en Python

1. **Introducción a las Excepciones en Python**:
   - Se aprenderá a cambiar mensajes de error y a envolver código con declaraciones `try` y `except`.

2. **Función Ejemplo: División**:
   - Se define una función llamada `divide_by` que acepta dos parámetros `A` y `B`.
   - La función retorna el valor de la división de ambos números.

3. **Prueba de la Función**:
   - Se prueba la función con los valores 40 y 4, resultando en 10.
   - Se prueba la función con los valores 40 y 0, resultando en una excepción `ZeroDivisionError`.

4. **Manejo de Errores con `try` y `except`**:
   - Se envuelve el código de la función en una declaración `try`.
   - En la declaración `except`, se agrega un mensaje de error personalizado: "something went wrong".
   - Al ejecutar, se imprime el mensaje personalizado en caso de excepción.

5. **Especificidad de Excepciones**:
   - Se puede hacer que la declaración `except` sea más específica añadiendo la clase base `Exception`.
   - Utilizando `as E` después de `Exception`, se puede acceder a la información de la excepción.
   - Se puede imprimir la excepción con `E`, resultando en un mensaje más detallado.

6. **Clase de la Excepción**:
   - Se puede acceder a la clase de la excepción utilizando `E.__class__`.
   - Se imprime la clase de error como `ZeroDivisionError`.

7. **Mensajes de Error Específicos**:
   - Se reemplaza la clase base `Exception` por `ZeroDivisionError`.
   - Se imprime un mensaje más específico: "division by zero, we cannot divide by zero".

8. **Manejo de Múltiples Excepciones**:
   - Se pueden encadenar declaraciones `except` para manejar múltiples excepciones.
   - Se añade una declaración `except` genérica para manejar cualquier otra excepción no anticipada.

9. **Conclusión**:
   - Se ha aprendido a envolver código en `try` y `except` para manejar excepciones potenciales en el código.

Estas notas resumen los puntos clave del manejo de excepciones en Python, utilizando la estructura `try` y `except` para proporcionar mensajes de error personalizados y más amigables para el usuario.