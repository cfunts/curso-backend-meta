# Algorithmic complexity

Aquí tienes unas notas relevantes del texto proporcionado:

1. **Tarea principal del desarrollador**:
   - Escribir código que se adapte a las necesidades del negocio.
   - Refactorización: reescribir o rehacer el código para hacerlo más manejable o eficiente.

2. **Refactorización**:
   - Parte estándar del ciclo de desarrollo de software.
   - Busca hacer el código más fácil de gestionar y mejorar su rendimiento.

3. **Medición del rendimiento del código**:
   - **Tiempo**: cuánto tiempo tarda en ejecutarse.
   - **Espacio**: cuánta memoria utiliza.
   - Uso de la notación Big O para medir la eficiencia del algoritmo en términos de tiempo y espacio.

4. **Complejidades de tiempo en la notación Big O**:
   - **Tiempo constante**: El tiempo de ejecución es el mismo sin importar el tamaño del input.
     - Ejemplo: búsqueda en un diccionario usando una clave.
   - **Tiempo lineal**: El tiempo de ejecución crece proporcionalmente al tamaño del input.
     - Ejemplo: iteración a través de un array.
   - **Tiempo logarítmico**: El tiempo de ejecución crece logarítmicamente con el tamaño del input.
     - Ejemplo: búsqueda binaria.
   - **Tiempo cuadrático**: El tiempo de ejecución crece proporcionalmente al cuadrado del tamaño del input.
     - Ejemplo: bucles anidados.
   - **Tiempo exponencial**: El tiempo de ejecución se duplica con cada incremento del input.
     - Ejemplo: secuencia de Fibonacci.

5. **Ejemplos de complejidades**:
   - **Constante**: Obtener un valor en un diccionario por clave.
   - **Lineal**: Recorrer un array de números.
   - **Logarítmico**: Búsqueda binaria dividiendo el array en dos partes cada vez.
   - **Cuadrático**: Bucle anidado con iteraciones múltiples.
   - **Exponencial**: Cálculo de la secuencia de Fibonacci.

6. **Importancia de entender la complejidad algorítmica**:
   - Facilita la optimización del código.
   - Conocer las diferentes complejidades ayuda a alcanzar el objetivo de ser un desarrollador eficiente.


## Notas Relevantes sobre Big-O Notation

**Introducción a la Notación Big-O**

- La notación Big O es fundamental en ciencias de la computación y programación para analizar y describir la eficiencia de los algoritmos.
- Proporciona una manera estandarizada de expresar cómo el tiempo de ejecución o el uso de recursos de un algoritmo crece a medida que aumenta el tamaño de los datos de entrada.

**¿Qué es la Notación Big-O?**

- La notación Big O describe el límite superior o el peor caso de la complejidad temporal de un algoritmo.
- Responde a preguntas como:
  - ¿Cómo cambia el tiempo de ejecución de un algoritmo a medida que aumentan los datos de entrada?
  - ¿Cómo escala un algoritmo con el aumento del tamaño de la entrada?
- Se escribe como "O(f(n))", donde "f(n)" es una función que representa la relación entre el tamaño de entrada (n) y el tiempo de ejecución o uso de recursos del algoritmo.

**Ejemplos Comunes de Notación Big-O**

1. **O(1) - Tiempo Constante**
   - El tiempo de ejecución no depende del tamaño de los datos de entrada.
   - Ejemplo: Acceder a un elemento en un array por su índice.

2. **O(n) - Tiempo Lineal**
   - El tiempo de ejecución crece linealmente con el tamaño de los datos de entrada.
   - Ejemplo: Buscar un valor específico en una lista desordenada.

3. **O(n^2) - Tiempo Cuadrático**
   - El tiempo de ejecución crece con el cuadrado del tamaño de los datos de entrada.
   - Ejemplo: Bubble Sort.

4. **O(log n) - Tiempo Logarítmico**
   - El tiempo de ejecución crece logarítmicamente con el tamaño de los datos de entrada.
   - Ejemplo: Búsqueda binaria en una lista ordenada.

**Resumen de la Complejidad Temporal**

- **Más Rápido:**
  - O(1) - Tiempo Constante: La velocidad no depende de la cantidad de datos.
- **Rápido:**
  - O(log n) - Tiempo Logarítmico: Crece lentamente a medida que se añaden más datos.
- **Moderado:**
  - O(n) - Tiempo Lineal: El tiempo de ejecución crece linealmente con los datos.
- **Más Lento:**
  - O(n log n) - Tiempo Linealítmico: Más rápido que cuadrático pero más lento que lineal.
  - O(n^2) - Tiempo Cuadrático: Se vuelve más lento a medida que se añaden datos.
- **Muy Lento:**
  - O(2^n) - Tiempo Exponencial: Crece rápidamente con los datos.
- **Extremadamente Lento:**
  - O(n!) - Tiempo Factorial: Crece de manera explosiva con los datos.

**Importancia de la Notación Big O**

- Comparación de Algoritmos: Permite comparar objetivamente diferentes algoritmos y elegir el más eficiente para una tarea específica.
- Optimización del Rendimiento: Ayuda a identificar cuellos de botella en el código y optimizar algoritmos.
- Escalabilidad: Los algoritmos eficientes son vitales a medida que crecen las aplicaciones y los tamaños de datos.
- Gestión de Recursos: En entornos con recursos limitados, es esencial elegir algoritmos eficientes.
- Entrevistas de Programación: La notación Big O es común en entrevistas técnicas y desafíos de programación.

**Análisis de Código con Notación Big O**

1. Identificar el Tamaño de Entrada: Determinar qué representa "n" en el código.
2. Identificar Bucles e Iteraciones: Los bucles suelen ser los principales factores que afectan la complejidad temporal.
3. Contar Operaciones Dentro de los Bucles: Contar las operaciones que dependen del tamaño de la entrada "n".
4. Combinar Complejidad: Si hay bucles anidados, multiplicar sus complejidades.
5. Elegir el Término Dominante: En casos de complejidad combinada, centrarse en el término con la tasa de crecimiento más alta.
6. Simplificar: Simplificar la expresión eliminando factores constantes.

Al seguir estos pasos, se puede determinar la complejidad temporal de un algoritmo y comprender cómo funcionará a medida que aumente el tamaño de la entrada.

**Resumen**

- La notación Big O es esencial en ciencias de la computación para analizar y comparar la eficiencia de los algoritmos.
- Comprender sus conceptos básicos y aplicarla al código permite tomar decisiones informadas sobre la selección y optimización de algoritmos, garantizando que los programas funcionen de manera eficiente, incluso cuando los tamaños de los datos crecen.

## Ejemplos

### Ejemplos de Notación Big-O con Python

**1. O(1) - Tiempo Constante**

El tiempo de ejecución no depende del tamaño de los datos de entrada. Siempre es constante.

```python
# Acceder a un elemento en un array por su índice
def get_element(arr, index):
    return arr[index]

arr = [1, 2, 3, 4, 5]
print(get_element(arr, 2))  # Output: 3
```

**2. O(n) - Tiempo Lineal**

El tiempo de ejecución crece linealmente con el tamaño de los datos de entrada.

```python
# Buscar un valor específico en una lista desordenada
def linear_search(arr, target):
    for element in arr:
        if element == target:
            return True
    return False

arr = [1, 2, 3, 4, 5]
print(linear_search(arr, 3))  # Output: True
print(linear_search(arr, 6))  # Output: False
```

**3. O(n^2) - Tiempo Cuadrático**

El tiempo de ejecución crece con el cuadrado del tamaño de los datos de entrada.

```python
# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))  # Output: [11, 12, 22, 25, 34, 64, 90]
```

**4. O(log n) - Tiempo Logarítmico**

El tiempo de ejecución crece logarítmicamente con el tamaño de los datos de entrada.

```python
# Búsqueda binaria en una lista ordenada
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(arr, 4))  # Output: 3
print(binary_search(arr, 10)) # Output: -1
```

**5. O(n log n) - Tiempo Linealítmico**

El tiempo de ejecución crece más rápido que lineal pero más lento que cuadrático.

```python
# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))  # Output: [3, 9, 10, 27, 38, 43, 82]
```

Estos ejemplos ilustran cómo se aplican las distintas complejidades temporales a algoritmos comunes, ayudando a entender su eficiencia relativa.