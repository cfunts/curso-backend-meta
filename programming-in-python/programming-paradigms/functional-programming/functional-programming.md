# Functional Programming

### Notas Relevantes sobre el Texto de Programación Funcional

1. **Programación Funcional (FP)**:
   - Paradigma diferente al orientado a objetos.
   - Adecuado para procesar grandes cantidades de datos a alta velocidad.
   - Se enfoca en la utilización de funciones para un código limpio, consistente y mantenible.

2. **Funciones en FP**:
   - **Funciones Tradicionales**:
     - Pueden acceder y modificar variables en el estado global.
     - Pueden cambiar variables locales.
     - El resultado no depende necesariamente de los inputs.

   - **Funciones Puras**:
     - Siempre producen el mismo resultado con los mismos inputs.
     - No pueden acceder ni modificar variables globales.
     - No pueden cambiar variables locales.
     - El resultado depende únicamente de los inputs.

3. **Diferencias entre FP y Programación Orientada a Objetos (OOP)**:
   - FP evita modificar datos fuera del alcance de la función.
   - Las funciones son autónomas e independientes, favoreciendo un código limpio y elegante.

4. **Funciones en Python**:
   - Las funciones son "ciudadanos de primera clase" (first-class citizens):
     - Pueden asignarse a variables.
     - Pueden pasarse como argumentos.
     - Pueden devolverse a sus llamadores.

5. **Ejemplos de Funciones en Python**:
   - **sorted**:
     - Acepta una lista y la devuelve en orden ordenado.
     - Ejemplo: ordenar una lista de nombres de cafés alfabéticamente.

   - **Crear Funciones Propias**:
     - Se puede crear una función para invertir cadenas de texto.
     - Ejemplo: definir una función `reverse` que invierta nombres de cafés.

6. **Uso de `map` en Python**:
   - La función `map` acepta una función y un iterable.
   - Aplica la función a cada elemento del iterable.
   - Ejemplo: usar `map` para aplicar la función `reverse` a una lista de cafés.

7. **Conclusión**:
   - La programación funcional en Python permite crear y reutilizar funciones, facilitando el desarrollo y mantenimiento del código.