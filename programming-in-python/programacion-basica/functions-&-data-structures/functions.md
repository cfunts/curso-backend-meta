# ¿Qué son las funciones?

- **Definición básica**: Las funciones son un conjunto de instrucciones que toman una entrada y devuelven una salida.
- **Ejemplo básico**: La función `print` imprime un valor en la pantalla. El valor se pasa a la función como argumento.

### Declarar una función en Python

- **Sintaxis básica**:
  - Se usa la palabra clave `def`.
  - Se sigue con el nombre de la función y una lista de parámetros opcionales entre paréntesis.
  - Ejemplo:
    ```python
    def suma(x, y):
        return x + y
    ```

### Reusabilidad de las funciones

- **Funciones modulares**: El código de una función puede reutilizarse múltiples veces.
- **Ejemplos comunes**: `print` e `input` son funciones que ya se han usado en este curso.

### Ejemplo práctico: Calcular impuestos

1. **Declarar variables**:
    ```python
    factura = 175.00
    tasa_impuesto = 15
    ```
2. **Calcular el impuesto total**:
    ```python
    impuesto_total = factura * tasa_impuesto / 100
    print(impuesto_total)  # Output: 26.25
    ```

### Creación de una función para calcular impuestos

- **Declaración de la función**:
    ```python
    def calcular_impuesto(factura, tasa_impuesto):
        return factura * tasa_impuesto / 100
    ```
- **Uso de la función**:
    ```python
    print(calcular_impuesto(175, 15))  # Output: 26.25
    print(calcular_impuesto(164.33, 22))  # Output: 36.15
    ```
- **Redondeo de resultados**:
    ```python
    print(round(calcular_impuesto(164.33, 22), 2))  # Output: 36.15
    ```

### Beneficios de las funciones

- **Eficiencia**: Actualizar una función una vez afecta a todas las partes del código que la llaman.
- **Claridad**: Facilitan la estructura y el mantenimiento del código al hacerlo más modular y reutilizable.

### Resumen del video

- Declaración de funciones en Python.
- Pasar y devolver datos en las funciones.
- Simplificación del código mediante el uso de funciones reutilizables.

---