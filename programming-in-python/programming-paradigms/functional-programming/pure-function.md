# Pure Function

### Notas Relevantes del Texto sobre Pure Functions

1. **Definición de Pure Functions**:
   - Una pure function no cambia ni tiene efecto en variables, datos, listas o conjuntos fuera de su propio alcance.

2. **Ejemplo de Pure Function**:
   - Si una función modifica una lista global, no es una pure function.
   - Para convertir una función en una pure function, debe aceptar una lista como argumento, agregar el ítem a esta lista sin modificar la lista original y devolver una nueva lista con el ítem añadido.

3. **Beneficios de las Pure Functions**:
   - Consistencia: Siempre se sabe cuál será el resultado.
   - Previsibilidad: Hacen exactamente lo que están destinadas a hacer.
   - Cacheabilidad: Pueden almacenarse en caché ya que su salida siempre es la misma para los mismos argumentos.
   - Compatibilidad con multi-threading: Ayudan a evitar cambios en el alcance global, asegurando que los datos permanezcan fiables.

4. **Conversión de una Función Normal a una Pure Function**:
   - **Paso 1**: Crear una lista global `my_list` y una función `add_to_list` que toma un ítem y lo agrega a `my_list`.
   - **Paso 2**: Modificar la función para que acepte una lista como argumento y devolver una nueva lista con el ítem añadido sin modificar la original.
   - **Paso 3**: Crear una copia de la lista dentro de la función y agregar el ítem a la copia, luego devolver la copia.

5. **Demostración Paso a Paso**:
   - **Inicial**: La función `add_to_list` modifica `my_list` global directamente, no es una pure function.
   - **Modificación 1**: Aceptar un nuevo argumento y devolver la lista modificada, aún no es pure function.
   - **Modificación 2**: Aceptar `lst` y `item` como parámetros, modificar `lst` y devolverlo, aún no es pure function.
   - **Solución Final**: Crear una copia de `lst` dentro de la función, modificar la copia y devolver la copia.

6. **Conclusión**:
   - Las pure functions son útiles porque mantienen el código más limpio, más fácil de depurar y más fácil de extender.
   - En la carrera de programación, es probable que se usen pure functions regularmente para mantener la integridad del código y facilitar el desarrollo y mantenimiento.

Estas notas resumen los conceptos clave y pasos importantes para entender y aplicar pure functions en la programación funcional.

## Ejemplo

### Ejemplo de Pure Function

**Función No Pura:**

```python
my_list = [1, 2, 3]

def add_to_list(item):
    my_list.append(item)
    return my_list

new_list = add_to_list(4)
print("my_list:", my_list)  # Output: my_list: [1, 2, 3, 4]
print("new_list:", new_list)  # Output: new_list: [1, 2, 3, 4]
```

En este ejemplo, `add_to_list` no es una pure function porque modifica `my_list`, que es una variable global.

**Función Pura:**

```python
my_list = [1, 2, 3]

def add_to_list(lst, item):
    new_list = lst.copy()  # Crear una copia de la lista
    new_list.append(item)  # Agregar el item a la copia
    return new_list  # Devolver la nueva lista

new_list = add_to_list(my_list, 4)
print("my_list:", my_list)  # Output: my_list: [1, 2, 3]
print("new_list:", new_list)  # Output: new_list: [1, 2, 3, 4]
```

En este ejemplo, `add_to_list` es una pure function porque no modifica la lista original `my_list`. En su lugar, crea una nueva lista, agrega el ítem a esta nueva lista y la devuelve. De esta manera, `my_list` permanece inalterada y `new_list` contiene la nueva lista con el ítem añadido.