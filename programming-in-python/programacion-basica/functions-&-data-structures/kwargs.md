# kwargs (key words arg)

### Notas Relevantes sobre `args` y `kwargs` en Python

#### Introducción a `args` y `kwargs`
- **args** y **kwargs** permiten pasar una cantidad variable de argumentos a una función.
- `args` se usa para pasar cualquier cantidad de variables no keyword.
- `kwargs` se usa para pasar cualquier cantidad de argumentos keyword (pares clave-valor).

#### Ejemplo con `args`
1. **Función simple:**
   - Definición: `def sum_of(a, b):`
   - Suma de dos parámetros: `return a + b`
   - Uso: `print(sum_of(4, 5))` devuelve `9`.

2. **Problema con más argumentos:**
   - Si se agrega un tercer valor: `sum_of(4, 5, 6)`, se produce un error.
   - El error: "la función sum_of toma dos argumentos posicionales, pero se dieron tres."

3. **Uso de `args`:**
   - Definición: `def sum_of(*args):`
   - Permite cualquier número de argumentos.
   - Suma de todos los valores:
     ```python
     sum = 0
     for x in args:
         sum += x
     return sum
     ```
   - Ejemplo: `sum_of(4, 5, 6)` devuelve `15`.

#### Ejemplo con `kwargs`
1. **Ejemplo de Factura en un Restaurante:**
   - Elementos: café (2.99), pastel (4.55), jugo (2.99).

2. **Uso de `kwargs`:**
   - Definición: `def total_bill(**kwargs):`
   - Permite cualquier número de argumentos clave-valor.
   - Suma de valores:
     ```python
     sum = 0
     for key, value in kwargs.items():
         sum += value
     return sum
     ```

3. **Redondeo del Total:**
   - Uso de la función `round` para limitar a dos decimales:
     ```python
     return round(sum, 2)
     ```
   - Ejemplo: `total_bill(coffee=2.99, cake=4.55, juice=2.99)` devuelve `10.53`.

#### Resumen
- **`args`:**
  - Permite pasar cualquier cantidad de variables no keyword.
  - Ideal para funciones donde el número de argumentos puede variar.

- **`kwargs`:**
  - Permite pasar cualquier cantidad de argumentos keyword.
  - Útil para funciones que requieren pares clave-valor, como parámetros opcionales.

Estas notas proporcionan una visión clara y concisa sobre cómo utilizar `args` y `kwargs` en Python para manejar argumentos variables en funciones.

### Ejemplos de Uso de `args` y `kwargs` en Python

#### Ejemplo con `args`

**Definición de una función que suma una cantidad variable de números:**
```python
def sum_of(*args):
    total = 0
    for num in args:
        total += num
    return total
```

**Uso de la función con diferentes cantidades de argumentos:**
```python
print(sum_of(4, 5))           # Output: 9
print(sum_of(4, 5, 6))        # Output: 15
print(sum_of(1, 2, 3, 4, 5))  # Output: 15
```

#### Ejemplo con `kwargs`

**Definición de una función que calcula el total de una factura con ítems y sus precios:**
```python
def total_bill(**kwargs):
    total = 0
    for item, price in kwargs.items():
        total += price
    return round(total, 2)
```

**Uso de la función con diferentes ítems y precios:**
```python
print(total_bill(coffee=2.99, cake=4.55, juice=2.99))  # Output: 10.53
print(total_bill(sandwich=5.49, soda=1.99))           # Output: 7.48
print(total_bill(burger=8.99, fries=2.99, shake=3.49)) # Output: 15.47
```

#### Ejemplo Combinado de `args` y `kwargs`

**Definición de una función que imprime los valores y los detalles de los ítems:**
```python
def print_order_summary(*args, **kwargs):
    print("Items Ordered:")
    for item in args:
        print(f"- {item}")
    
    print("\nPrices:")
    total_price = 0
    for item, price in kwargs.items():
        print(f"{item}: ${price}")
        total_price += price
    
    print(f"\nTotal Price: ${round(total_price, 2)}")
```

**Uso de la función:**
```python
print_order_summary("coffee", "cake", "juice", coffee=2.99, cake=4.55, juice=2.99)
```

**Salida esperada:**
```
Items Ordered:
- coffee
- cake
- juice

Prices:
coffee: $2.99
cake: $4.55
juice: $2.99

Total Price: $10.53
```

Estos ejemplos ilustran cómo utilizar `args` para pasar una cantidad variable de argumentos posicionales y `kwargs` para pasar una cantidad variable de argumentos clave-valor, proporcionando flexibilidad y dinamismo a las funciones en Python.