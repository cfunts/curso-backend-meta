# Sets

Aquí tienes unas notas relevantes del texto sobre sets:

1. **Declaración de un Set:**
   - Para declarar un set, se usa una variable y se asigna con llaves `{}`.
   - Ejemplo: `set_a = {1, 2, 3, 4, 5}`.

2. **Propiedades de los Sets:**
   - Los sets no permiten valores duplicados.
   - Al intentar añadir un duplicado, éste no se imprime.
   
3. **Métodos Básicos:**
   - **Agregar elementos:** `set_a.add(6)` añade el número 6 al set.
   - **Eliminar elementos:** `set_a.remove(2)` elimina el número 2 del set.
   - **Descartar elementos:** `set_a.discard(2)` también elimina el número 2, similar a `remove`.

4. **Operaciones Matemáticas con Sets:**
   - **Unión:** `set_a.union(set_b)` combina ambos sets sin duplicados.
     - Alternativamente, se puede usar el símbolo `|`.
   - **Intersección:** `set_a.intersection(set_b)` obtiene elementos comunes en ambos sets.
     - Alternativamente, se puede usar el símbolo `&`.
   - **Diferencia:** `set_a.difference(set_b)` obtiene elementos solo en `set_a` y no en `set_b`.
     - Alternativamente, se puede usar el símbolo `-`.
   - **Diferencia Simétrica:** `set_a.symmetric_difference(set_b)` obtiene elementos que están en uno u otro set, pero no en ambos.
     - Alternativamente, se puede usar el símbolo `^`.

5. **Características Adicionales:**
   - Los sets no tienen índices y no mantienen un orden específico.
   - Intentar acceder a un elemento por índice, como `set_a[0]`, resulta en un error de tipo `TypeError`.

6. **Conclusión:**
   - Los sets son útiles para almacenar datos únicos y realizar operaciones matemáticas sobre colecciones de datos sin duplicados.

Estas notas resumen los conceptos y ejemplos clave del texto sobre el uso de sets en programación.