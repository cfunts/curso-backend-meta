# Tuples

1. **Definición y Uso de Tuplas**:
   - Las tuplas son estructuras de datos en Python que permiten almacenar diferentes tipos de datos.
   - Ayudan a crear código sólido y con buen rendimiento.

2. **Declaración de Tuplas**:
   - Para declarar una tupla, se usa una variable y el operador de asignación `=`.
   - La tupla se define utilizando paréntesis `()`.
   - Ejemplo: `my_tuple = (1, "string", 4.5, True)`.
   - Una tupla puede contener una mezcla de tipos de datos (enteros, cadenas, flotantes, booleanos).

3. **Acceso a Elementos**:
   - Los elementos de una tupla se pueden acceder de manera similar a los de una lista, usando índices.
   - Los índices comienzan desde 0.
   - Ejemplo: `print(my_tuple[1])` imprime el segundo elemento de la tupla.

4. **Tipo de Dato**:
   - Se puede determinar el tipo de una tupla utilizando la función `type()`.
   - Ejemplo: `print(type(my_tuple))` retorna `class 'tuple'`.

5. **Declaración Sin Paréntesis**:
   - Es posible declarar una tupla sin usar paréntesis, pero la práctica recomendada es utilizarlos.

6. **Métodos de Tuplas**:
   - `count()`: Cuenta el número de ocurrencias de un valor en la tupla.
     - Ejemplo: `my_tuple.count("string")` retorna 1.
   - `index()`: Retorna el índice de la primera ocurrencia de un valor en la tupla.
     - Ejemplo: `my_tuple.index(4.5)` retorna 2.

7. **Iteración a Través de una Tupla**:
   - Se puede iterar a través de los valores de una tupla utilizando un bucle `for`.
     - Ejemplo:
       ```python
       for x in my_tuple:
           print(x)
       ```

8. **Inmutabilidad**:
   - Una característica clave de las tuplas es que son inmutables, lo que significa que sus valores no pueden cambiarse después de su creación.
   - Intentar cambiar un valor en una tupla resultará en un error de tipo `TypeError`.
     - Ejemplo: Intentar `my_tuple[0] = 5` causará un error.

9. **Resumen**:
   - Las tuplas se declaran y trabajan con ellas de diversas maneras.
   - Se destaca su inmutabilidad y los métodos específicos como `count` e `index` que permiten trabajar con sus datos de manera eficiente.

Estas notas capturan los puntos principales del texto sobre tuplas en Python.