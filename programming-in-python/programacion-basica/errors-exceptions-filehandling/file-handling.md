# File handling in Python

### Notas Relevantes sobre el Manejo de Archivos en Python

1. **Importancia del Manejo de Archivos**:
   - El manejo de archivos es esencial en Python, ya que permite abrir, leer y escribir archivos.
   - Es crucial para trabajar con grandes cantidades de datos, ya sea en la computadora, en la web o en la nube.

2. **Funciones Principales**:
   - **open**: Utilizada para leer, escribir y crear archivos.
     - Acepta dos argumentos: el nombre/ubicación del archivo y el modo de apertura (lectura, escritura, creación).
     - Modos comunes:
       - `r`: Leer archivo en formato de texto.
       - `rb`: Leer archivo en formato binario.
       - `r+`: Leer y escribir.
       - `w`: Escribir (sobrescribe el archivo existente).
       - `a`: Añadir datos al archivo.
   - **close**: Cierra la conexión abierta del archivo, no toma argumentos.

3. **Formatos de Archivos**:
   - **Texto**: Formato legible por humanos, más amigable pero menos eficiente.
   - **Binario**: No legible por humanos, más compacto y eficiente en rendimiento.
   - Por defecto, Python maneja archivos en formato de texto. Para formato binario, se añade `b` al modo (`rb`, `wb`, `ab`).

4. **Ejemplo Práctico con `open`**:
   - Abrir un archivo `test.txt` en modo lectura (`r`).
   - Leer la primera línea usando `readline()` y almacenarla en una variable.
   - Imprimir el contenido y cerrar el archivo.

5. **Uso de `with open`**:
   - Mejora el manejo de excepciones y cierra automáticamente el archivo.
   - Sintaxis: `with open("test.txt", "r") as file`.
   - Leer la primera línea y asignarla a una variable.
   - Imprimir el contenido.

6. **Conclusión**:
   - El manejo de archivos en Python incluye funciones para crear y manipular archivos, así como para abrir, leer y escribir en ellos.
   - `with open` es preferible por su manejo automático de excepciones y cierre de archivos.

Estas notas cubren los puntos esenciales sobre el manejo de archivos en Python, incluyendo las funciones y modos de apertura, así como ejemplos prácticos de cómo trabajar con archivos en formato de texto y binario.

## Ejemplos

Claro, aquí tienes algunos ejemplos prácticos sobre el manejo de archivos en Python:

### Ejemplo 1: Leer un Archivo de Texto

```python
# Crear un archivo de texto para el ejemplo
with open("test.txt", "w") as file:
    file.write("Hello there, good.\n")

# Abrir y leer el archivo
file = open("test.txt", "r")
data = file.readline()
print(data)  # Salida: Hello there, good.
file.close()
```

### Ejemplo 2: Escribir en un Archivo de Texto

```python
# Abrir el archivo en modo escritura
file = open("example.txt", "w")
file.write("Este es un archivo de ejemplo.\n")
file.write("Añadiendo otra línea de texto.\n")
file.close()

# Leer el archivo para verificar el contenido
file = open("example.txt", "r")
print(file.read())
file.close()
```

### Ejemplo 3: Añadir Datos a un Archivo

```python
# Abrir el archivo en modo añadir
file = open("example.txt", "a")
file.write("Añadiendo una nueva línea al archivo.\n")
file.close()

# Leer el archivo para verificar el contenido
file = open("example.txt", "r")
print(file.read())
file.close()
```

### Ejemplo 4: Manejo de Archivos con `with open`

```python
# Crear y escribir en un archivo utilizando with open
with open("test_with.txt", "w") as file:
    file.write("Esta línea se escribe utilizando with open.\n")

# Leer el archivo utilizando with open
with open("test_with.txt", "r") as file:
    data = file.readline()
    print(data)  # Salida: Esta línea se escribe utilizando with open.
```

### Ejemplo 5: Leer un Archivo en Formato Binario

```python
# Crear un archivo binario para el ejemplo
with open("binary_test.bin", "wb") as file:
    file.write(b'\x00\x01\x02\x03')

# Leer el archivo binario
with open("binary_test.bin", "rb") as file:
    data = file.read()
    print(data)  # Salida: b'\x00\x01\x02\x03'
```

### Ejemplo 6: Leer un Archivo Línea por Línea

```python
# Crear un archivo de texto para el ejemplo
with open("multiline.txt", "w") as file:
    file.write("Primera línea.\nSegunda línea.\nTercera línea.\n")

# Leer el archivo línea por línea
with open("multiline.txt", "r") as file:
    for line in file:
        print(line.strip())
```

Estos ejemplos muestran cómo manejar archivos en Python para diversas operaciones, incluyendo la lectura y escritura tanto en formato de texto como en formato binario.


## Creación de archivos

### Notas Relevantes sobre la Creación de Archivos en Python

1. **Creación y Almacenamiento de Archivos:**
   - Los archivos se utilizan para almacenar datos de manera permanente.
   - Los datos en las variables del código existen en la memoria RAM, que se pierde cuando se apaga la computadora.
   - Es importante crear archivos para que los datos estén disponibles para su uso futuro o como un registro permanente.

2. **Función `open` en Python:**
   - Para crear nuevos archivos se usa la función `open` en modo escritura.
   - Ejemplo de uso con la declaración `with`:
     ```python
     with open('newfile.txt', 'w') as file:
         file.write('This is a new file created.')
     ```
   - `w` representa el modo de escritura, que puede reemplazar `mode='w'`.

3. **Agregar Contenido a Archivos:**
   - Se puede agregar contenido a un archivo utilizando la función `write`:
     ```python
     file.write('This is a new file created.')
     ```
   - Para agregar múltiples líneas, se utiliza la función `writelines` que acepta una lista:
     ```python
     file.writelines(['This is the first line.\n', 'This is the second line.'])
     ```
   - Para asegurar que cada línea comience en una nueva línea, se usa `\n`.

4. **Modos de Apertura de Archivos:**
   - `w`: Escribe en el archivo, reemplazando su contenido cada vez.
   - `a`: Añade contenido al final del archivo sin reemplazar el contenido existente.

5. **Ejemplo de Reemplazo y Adición:**
   - Reemplazar contenido:
     ```python
     with open('newfile.txt', 'w') as file:
         file.write('This is a new file created.')
     ```
   - Añadir contenido:
     ```python
     with open('newfile.txt', 'a') as file:
         file.write('\nThis is an appended line.')
     ```

6. **Manejo de Excepciones:**
   - Es esencial manejar excepciones utilizando `try` y `except`:
     ```python
     try:
         with open('sample/newfile.txt', 'w') as file:
             file.write('This is a new file created.')
     except FileNotFoundError as e:
         print('Error:', e)
     ```
   - En caso de errores como `FileNotFoundError`, se debe verificar la existencia del directorio o crearlo.

7. **Conclusión del Video:**
   - Se abordaron la creación de archivos en Python utilizando los modos de escritura (`w`) y de adición (`a`).
   - Se explicó cómo insertar contenido de una sola línea o de múltiples líneas en el archivo.
   - Se subrayó la importancia de manejar excepciones al trabajar con archivos.

Estas notas cubren los aspectos esenciales para entender cómo crear y manejar archivos en Python, incluyendo la inserción de contenido y el manejo de excepciones comunes.

### Función Writelines

### Notas Relevantes sobre el Uso de la Función `writelines` en Python

1. **Función `writelines`:**
   - `writelines` se utiliza para escribir múltiples líneas en un archivo de una sola vez.
   - Acepta una lista de cadenas, cada una representando una línea a escribir en el archivo.

2. **Uso Básico de `writelines`:**
   ```python
   with open('newfile.txt', 'w') as file:
       file.writelines(['This is the first line.', 'This is the second line.'])
   ```
   - Este código escribe las líneas en el archivo sin agregar saltos de línea automáticos entre ellas.

3. **Agregar Saltos de Línea:**
   - Para asegurar que cada línea comience en una nueva línea, es necesario incluir `\n` al final de cada cadena en la lista:
     ```python
     with open('newfile.txt', 'w') as file:
         file.writelines(['This is the first line.\n', 'This is the second line.\n'])
     ```

4. **Reemplazar Contenido vs. Añadir Contenido:**
   - En modo escritura (`w`), el contenido del archivo se reemplaza cada vez que se ejecuta el código.
   - Para añadir contenido al archivo en lugar de reemplazarlo, se debe usar el modo de adición (`a`):
     ```python
     with open('newfile.txt', 'a') as file:
         file.writelines(['This is an appended line.\n', 'This is another appended line.\n'])
     ```

5. **Ejemplo Completo de Uso de `writelines`:**
   ```python
   with open('newfile.txt', 'w') as file:
       file.writelines(['This is the first line.\n', 'This is the second line.\n'])
   
   with open('newfile.txt', 'a') as file:
       file.writelines(['This is an appended line.\n', 'This is another appended line.\n'])
   ```

6. **Consideraciones Adicionales:**
   - Cada vez que se ejecute el script en modo `w`, el contenido del archivo se sobrescribirá.
   - En modo `a`, el nuevo contenido se añadirá al final del archivo existente.

Estas notas detallan cómo utilizar la función `writelines` para escribir múltiples líneas en un archivo en Python, incluyendo la importancia de agregar saltos de línea y la diferencia entre los modos de apertura de archivos.

## Reading Files