### Notas Relevantes del Texto sobre Control de Flujo en Programación

**Concepto de Control de Flujo**
- **Definición**: El control de flujo se refiere al orden en que se ejecutan las instrucciones en un programa.
- **Importancia**: Decisiones que toman diferentes acciones o direcciones dentro del programa.

**Tipos de Control de Flujo en Python**
1. **Sentencias Condicionales**: `if`, `else`, `elif` (o `else if`).
2. **Bucles**: `for` y `while`.

**Sentencias Condicionales**
- **`if`**: Si la condición es verdadera, se ejecuta una función.
- **`else`**: Captura todo lo que no cumple las condiciones anteriores.
- **`elif`**: Si las condiciones anteriores no son verdaderas, prueba esta condición.

**Ejemplo Práctico: Descuentos en un Restaurante**
- **Definición de Variables**:
  - `bill_total = 114`
  - `discount1 = 10`
  - `discount2 = 20`
- **Condiciones**:
  - Si `bill_total > 100`, aplicar `discount1`.
  - Si `bill_total > 200`, aplicar `discount2`.

**Código Explicado**
- **Inicialización de Variables**:
  ```python
  bill_total = 114
  discount1 = 10
  ```
- **Primera Condición**:
  ```python
  if bill_total > 100:
      bill_total = bill_total - discount1
      print("bill is greater than 100")
  ```
- **Salida del Resultado**:
  ```python
  print("total bill " + str(bill_total))
  ```

**Ejecución del Código con Diferentes Valores**
- **`bill_total = 95`**:
  - La condición `if` no se cumple.
  - Se usa la sentencia `else`:
    ```python
    else:
        print("bill is less than 100")
    ```
- **`bill_total = 210`**:
  - La condición `if` no se cumple.
  - Se usa la sentencia `elif`:
    ```python
    elif bill_total > 200:
        bill_total = bill_total - discount2
        print("bill is greater than 200")
    ```

**Resultado Final**
- **Ejecución con `bill_total = 210`**:
  - La salida del terminal muestra `bill is greater than 200` y `total bill is 190`, indicando que se aplicó `discount2`.

**Conclusión**
- **Importancia**: Controlar el flujo del programa usando `if`, `else` y `elif` es esencial para tomar decisiones dentro del código.
- **Recomendación**: Practicar el uso de sentencias condicionales para mejorar la habilidad en programación.

**Reflexión Final**
- **Aplicación en la Vida Real**: La próxima vez que necesites tomar una decisión, piensa en las condiciones involucradas y cómo podrían representarse en Python.