### Notas Relevantes sobre Operadores en Python

**Introducción a los Operadores:**
- Un operador es un símbolo que indica a Python realizar una operación específica.
- Pueden ser operadores matemáticos, lógicos y de comparación.
- Los operadores funcionan con dos valores la mayoría de las veces.

**Operadores Matemáticos:**
- **Suma (+):** Se usa para añadir números. Ejemplo: `2 + 3`.
- **Resta (-):** Se usa para restar números. Ejemplo: `3 - 2`.
- **División (/):** Se usa para dividir un número por otro. Ejemplo: `35 / 5` (Resultado: 7.0, un float).
- **Multiplicación (*):** Se usa para multiplicar números. Ejemplo: `7 * 4`.

**Operadores Lógicos:**
- Se utilizan en declaraciones condicionales para determinar un resultado verdadero o falso.
- **AND:** Verifica que todas las condiciones sean verdaderas. Ejemplo: `a > 5 and a < 10`.
- **OR:** Verifica que al menos una de las condiciones sea verdadera. Ejemplo: `a > 5 or b > 10`.
- **NOT:** Devuelve un valor falso si el resultado es verdadero. Ejemplo: `not a > 5`.

**Ejemplos Prácticos:**
- **Adición:** `print(2 + 2)` devuelve `4`.
- **Sustracción:** `print(2 - 2)` devuelve `0`.
- **División:** `print(35 / 5)` devuelve `7.0`.
- **Multiplicación:** `print(25 * 7)` devuelve `175`.

**Uso de Operadores Lógicos con If Statements:**
- **AND:** 
  ```python
  a = True
  b = True
  if a and b:
      print("all true")  # Se imprime porque ambas condiciones son verdaderas.
  ```
- **OR:**
  ```python
  a = True
  b = False
  if a or b:
      print("all true")  # Se imprime porque al menos una condición es verdadera.
  ```
- **NOT:**
  ```python
  a = False
  b = False
  if not a:
      print("all true")  # Se imprime porque `not a` es verdadero.
  ```

**Conclusión:**
- Los operadores matemáticos permiten realizar cálculos simples y complejos como en una calculadora.
- Los operadores lógicos controlan el flujo del programa basado en condiciones específicas.
- Se recomienda practicar con ejemplos adicionales para familiarizarse con su uso en Python.