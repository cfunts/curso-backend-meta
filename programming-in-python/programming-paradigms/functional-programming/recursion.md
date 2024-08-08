# Recursion

Aquí tienes unas notas relevantes sobre el texto que explica la recursión en programación:

1. **Definición de Recursión**:
   - La recursión es un método de resolución de problemas donde una función se llama a sí misma.
   - Es útil para problemas que pueden dividirse en problemas más pequeños y repetitivos, especialmente cuando hay muchas ramificaciones posibles.

2. **Ejemplo Común**:
   - La búsqueda en un sistema de archivos es un buen ejemplo de un problema que se presta para la recursión.

3. **Comparación con Iteración**:
   - La recursión es similar a un bucle `for` en que se repite varias veces, pero en lugar de iterar, la función se llama a sí misma.
   - La recursión puede ser más compacta que una solución iterativa, pero debe manejarse con cuidado para evitar bucles infinitos que consumen memoria.

4. **Ejemplo de Cálculo de Factorial**:
   - **Solución Iterativa**: Utiliza un bucle para multiplicar los números de 1 hasta `n`. Ejemplo para `n = 5`: 1 * 2 * 3 * 4 * 5 = 120.
   - **Solución Recursiva**: La función se llama a sí misma con `n-1` hasta llegar a 1. Ejemplo: `factorial(5)` llama a `factorial(4)`, que llama a `factorial(3)`, y así sucesivamente, hasta llegar a `factorial(1)`.

5. **Ventajas de la Recursión**:
   - Código más limpio y menos voluminoso.
   - Problemas complejos pueden descomponerse en sub-problemas más fáciles de entender.
   - Generación de secuencias puede ser más fácil de entender que con bucles anidados.

6. **Desventajas de la Recursión**:
   - La lógica puede ser más difícil de seguir.
   - Puede ser más costosa en términos de memoria y a veces ineficiente.
   - La depuración y el seguimiento del código pueden ser complicados.

7. **Precauciones**:
   - Asegúrate de incluir una condición base para detener la recursión y evitar bucles infinitos.

Estas notas deberían ayudarte a entender la recursión y sus aplicaciones en programación.