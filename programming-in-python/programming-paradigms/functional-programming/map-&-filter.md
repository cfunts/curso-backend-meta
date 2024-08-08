# Map & filter

Aquí tienes unas notas relevantes sobre el texto:

1. **Objetivo del Video:**
   - Aprender a procesar una lista usando las funciones `map` y `filter` en Python.

2. **Ejemplo de Lista:**
   - Se usa una lista llamada `menu` que contiene diferentes tipos de cafés.

3. **Uso de `map`:**
   - **Propósito:** Aplicar una función a cada elemento de la lista para generar una nueva lista con los resultados.
   - **Proceso:**
     - Crear una función (por ejemplo, `find_coffee`) que evalúe si un elemento cumple con una condición (por ejemplo, si empieza con la letra 'C').
     - Usar `map` con la función creada y la lista `menu`.
     - La salida es un objeto `map` que se puede iterar para obtener los resultados.

4. **Uso de `filter`:**
   - **Propósito:** Filtrar elementos de una lista basándose en una condición, retornando solo aquellos que cumplen la condición.
   - **Proceso:**
     - Similar al uso de `map`, pero el filtro retorna solo los elementos que cumplen con la condición especificada en la función.
     - Se declara una variable (por ejemplo, `filter_coffee`) y se asigna la función `filter` con la función de filtrado y la lista `menu`.

5. **Diferencias entre `map` y `filter`:**
   - **`map`:** Aplica una función a todos los elementos de la lista y devuelve una nueva lista con los resultados de la función.
   - **`filter`:** Aplica una función a todos los elementos de la lista pero devuelve una nueva lista solo con los elementos para los cuales la función devuelve `True`.

6. **Resultado:**
   - En el caso de `map`, se obtienen valores `None` para los elementos que no cumplen la condición.
   - En el caso de `filter`, solo se retornan los elementos que cumplen la condición, sin valores `None`.

Estos puntos resumen cómo usar `map` y `filter` para procesar listas en Python y las diferencias clave entre estas dos funciones.

Aquí tienes un ejemplo simple en Python usando las funciones `map` y `filter` con una lista de cafés:

```python
# Lista de cafés
menu = ['Espresso', 'Latte', 'Cappuccino', 'Caffè Mocha', 'Cortado']

# Función para verificar si el café empieza con 'C'
def starts_with_c(coffee):
    return coffee.startswith('C')

# Usando map para aplicar la función a cada elemento de la lista
map_coffee = map(starts_with_c, menu)
print("Resultados de map:")
for result in map_coffee:
    print(result)  # Imprime True o False si el café empieza con 'C'

# Volver a crear la lista original para usar filter
menu = ['Espresso', 'Latte', 'Cappuccino', 'Caffè Mocha', 'Cortado']

# Usando filter para filtrar los cafés que empiezan con 'C'
filter_coffee = filter(starts_with_c, menu)
print("\nResultados de filter:")
for coffee in filter_coffee:
    print(coffee)  # Imprime solo los cafés que empiezan con 'C'
```

**Explicación del código:**

1. **Lista Original:**
   - `menu` contiene diferentes tipos de cafés.

2. **Función `starts_with_c`:**
   - Verifica si el nombre del café empieza con la letra 'C'.

3. **Uso de `map`:**
   - Aplica la función `starts_with_c` a cada elemento en `menu`.
   - El resultado es una secuencia de valores booleanos (`True` o `False`) indicando si cada café empieza con 'C'.

4. **Uso de `filter`:**
   - Filtra la lista `menu` para mantener solo los cafés que cumplen con la condición de la función `starts_with_c`.
   - El resultado es una lista de cafés que empiezan con la letra 'C'.

Cuando ejecutes este código, verás cómo `map` muestra `True` o `False` para cada café, mientras que `filter` muestra solo los cafés que empiezan con 'C'.