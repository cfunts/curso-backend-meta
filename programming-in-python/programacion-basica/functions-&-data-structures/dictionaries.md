# Dictionaries

Aquí tienes unas notas relevantes sobre el texto acerca de los diccionarios en Python:

1. **Definición y Comparación**:
   - Un diccionario en Python es similar a un diccionario físico.
   - Mientras que en un diccionario físico se busca una palabra por su primera letra y orden alfabético, en Python, los diccionarios están optimizados para recuperar valores usando claves en lugar de posiciones de índice.

2. **Acceso a Valores**:
   - Los diccionarios en Python permiten acceder a valores basados en claves, lo que es más rápido y flexible en comparación con el acceso basado en índices de las listas.

3. **Clave-Valor**:
   - En un diccionario de Python, una clave está asignada a un valor específico, formando un par clave-valor.
   - Este método es más rápido que usar listas tradicionales, donde se requiere revisar la lista hasta encontrar el elemento.

4. **Mutabilidad**:
   - Aunque un diccionario es mutable, los valores asociados a las claves pueden ser cambiados o actualizados.
   - Ejemplo: Se puede cambiar un valor asociado a una clave específica utilizando el operador de asignación.

5. **Creación de Diccionarios**:
   - Se pueden crear diccionarios usando llaves `{}` con pares clave-valor separados por comas.
   - Ejemplo: `sample_dictionary = {1: 'coffee', 2: 'tea'}`

6. **Acceso y Modificación**:
   - Para acceder a un valor, se utiliza la clave entre corchetes `[]`.
   - Ejemplo: `sample_dictionary[1]` devuelve `'coffee'`.
   - Para actualizar un valor, se asigna un nuevo valor a la clave.
   - Ejemplo: `sample_dictionary[2] = 'mint tea'`

7. **Eliminación de Elementos**:
   - Se puede eliminar un elemento utilizando la función `del` seguida del nombre del diccionario y la clave del elemento a eliminar.
   - Ejemplo: `del sample_dictionary[3]` elimina el elemento con clave `3`.

8. **Iteración sobre Diccionarios**:
   - Existen tres métodos para iterar sobre diccionarios: iteración estándar, la función `items` y la función `values`.
   - Iteración estándar: Itera sobre las claves.
   - Función `items`: Permite acceder tanto a las claves como a los valores.
   - Función `values`: Itera solo sobre los valores.

9. **Ejemplo de Uso**:
   - Crear y declarar un diccionario: `my_d = {}` (diccionario vacío).
   - Agregar valores: `my_d[1] = 'test'`, `my_d['name'] = 'Jim'`.
   - Acceder a valores: `my_d[1]`, `my_d['name']`.
   - Actualizar valores: `my_d[1] = 'not a test'`.
   - Eliminar valores: `del my_d[1]`.
   - Iterar sobre diccionario:
     ```python
     for key, value in my_d.items():
         print(f"Key: {key}, Value: {value}")
     ```

10. **Evitar Duplicados**:
    - Los diccionarios no permiten claves duplicadas. Si se intenta asignar un valor a una clave existente, este sobrescribirá el valor anterior.

Estas notas proporcionan una visión general de cómo funcionan los diccionarios en Python y sus beneficios en términos de rendimiento y flexibilidad.

Aquí tienes algunos ejemplos prácticos que ilustran los conceptos mencionados sobre los diccionarios en Python:

### 1. Creación de un Diccionario
```python
# Crear un diccionario vacío
mi_diccionario = {}

# Crear un diccionario con pares clave-valor
mi_diccionario = {1: 'café', 2: 'té', 3: 'jugo'}
```

### 2. Acceso a Valores
```python
# Acceder al valor asociado con la clave 1
print(mi_diccionario[1])  # Salida: café

# Acceder al valor asociado con la clave 2
print(mi_diccionario[2])  # Salida: té
```

### 3. Actualización de Valores
```python
# Actualizar el valor asociado con la clave 2
mi_diccionario[2] = 'té de menta'
print(mi_diccionario[2])  # Salida: té de menta
```

### 4. Eliminación de Elementos
```python
# Eliminar el elemento con la clave 3
del mi_diccionario[3]
print(mi_diccionario)  # Salida: {1: 'café', 2: 'té de menta'}
```

### 5. Iteración sobre el Diccionario
#### Iteración estándar (solo claves)
```python
for clave in mi_diccionario:
    print(clave)  # Salida: 1, 2 (en diferentes líneas)
```

#### Usando `items` para obtener claves y valores
```python
for clave, valor in mi_diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")
# Salida:
# Clave: 1, Valor: café
# Clave: 2, Valor: té de menta
```

#### Usando `values` para obtener solo valores
```python
for valor in mi_diccionario.values():
    print(valor)  # Salida: café, té de menta (en diferentes líneas)
```

### 6. Evitar Duplicados de Claves
```python
# Intentar agregar una clave duplicada
mi_diccionario[1] = 'nuevo café'
print(mi_diccionario)  # Salida: {1: 'nuevo café', 2: 'té de menta'}
```

### 7. Creación y Declaración de un Diccionario
```python
# Crear un diccionario vacío
mi_diccionario = {}

# Agregar pares clave-valor
mi_diccionario[1] = 'test'
mi_diccionario['nombre'] = 'Jim'

# Imprimir el diccionario
print(mi_diccionario)  # Salida: {1: 'test', 'nombre': 'Jim'}
```

### 8. Acceder y Actualizar Claves en el Diccionario
```python
# Acceder a un valor por su clave
print(mi_diccionario[1])  # Salida: test
print(mi_diccionario['nombre'])  # Salida: Jim

# Actualizar un valor existente
mi_diccionario[1] = 'no es un test'
print(mi_diccionario[1])  # Salida: no es un test
```

### 9. Iteración sobre Claves y Valores del Diccionario
```python
# Iterar sobre las claves
for clave in mi_diccionario:
    print(clave)  # Salida: 1, 'nombre' (en diferentes líneas)

# Iterar sobre claves y valores
for clave, valor in mi_diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")
# Salida:
# Clave: 1, Valor: no es un test
# Clave: nombre, Valor: Jim
```

### 10. Eliminación de un Elemento por su Clave
```python
# Eliminar el valor asociado con la clave 1
del mi_diccionario[1]
print(mi_diccionario)  # Salida: {'nombre': 'Jim'}
```

Estos ejemplos cubren la creación, acceso, actualización, eliminación e iteración de diccionarios en Python, demostrando su uso práctico y flexibilidad.