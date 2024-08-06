# List

1. **Definición de Listas**:
   - Las listas son secuencias de uno o más tipos de datos diferentes o similares.
   - En Python, una lista es esencialmente un array dinámico que puede contener cualquier tipo de dato.

2. **Declaración de Listas**:
   - Se declara una lista utilizando corchetes y separando los elementos con comas:
     ```python
     list1 = [1, 2, 3, 4, 5]
     list2 = ['A', 'B', 'C']
     list3 = ['string', 10, True, 3.14]
     ```

3. **Acceso a Elementos de la Lista**:
   - Los elementos de la lista se acceden utilizando índices que empiezan desde cero:
     ```python
     list1[2]  # Accede al tercer elemento, que es 3.
     ```

4. **Listas Anidadas**:
   - Es posible tener listas dentro de otras listas:
     ```python
     list4 = [1, [2, 3, 4], 5, 6]
     ```

5. **Impresión de Listas**:
   - Para imprimir una lista completa, se puede usar el comando `print`:
     ```python
     print(list1)  # Imprime la lista como está.
     ```

6. **Agregar Elementos a una Lista**:
   - **Insertar**: Añade un elemento en una posición específica.
     ```python
     list1.insert(len(list1), 6)  # Inserta 6 al final de la lista.
     ```
   - **Añadir**: Agrega un elemento al final de la lista.
     ```python
     list1.append(6)
     ```
   - **Extender**: Añade múltiples elementos al final de la lista.
     ```python
     list1.extend([6, 7, 8, 9])
     ```

7. **Eliminar Elementos de una Lista**:
   - **Pop**: Elimina y devuelve el elemento en una posición específica.
     ```python
     list1.pop(4)  # Elimina el quinto elemento.
     ```
   - **Del**: Elimina un elemento en una posición específica.
     ```python
     del list1[2]  # Elimina el tercer elemento.
     ```

8. **Iteración a través de una Lista**:
   - Se puede usar un bucle `for` para iterar y acceder a los elementos de la lista:
     ```python
     for x in list1:
         print(x)
     ```

9. **Resumen**:
   - Las listas en Python funcionan como arrays dinámicos.
   - Se pueden usar varias funciones integradas para acceder, modificar, añadir y eliminar elementos de las listas.
   - La iteración a través de listas permite manejar grandes cantidades de datos de manera eficiente.