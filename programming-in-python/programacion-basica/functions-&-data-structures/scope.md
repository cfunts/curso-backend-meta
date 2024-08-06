# Aquí tienes unas notas relevantes del texto sobre el concepto de alcance (scope) en Python:

1. **Alcance en Python (Scope)**:
   - Permite un mayor control sobre los elementos en el código, reduciendo las posibilidades de cambios accidentales o no deseados.

2. **Cuatro tipos de alcance (LEGB)**:
   - **Local**: Variables definidas dentro de una función.
   - **Enclosing (Cerrado)**: Variables definidas en funciones englobantes (funciones dentro de funciones).
   - **Global**: Variables definidas en el nivel superior del script o módulo.
   - **Built-in (Integrado)**: Palabras reservadas y funciones integradas de Python, accesibles desde cualquier parte del código.

3. **Accesibilidad de variables**:
   - Variables en los alcances global e integrado son accesibles desde cualquier parte del código.
   - Variables en alcances local y cerrado tienen un acceso más restringido.

4. **Ejemplo de alcance global**:
   - Una variable definida globalmente puede ser accesible dentro de funciones.
   - Ejemplo:
     ```python
     my_global = 10

     def fn1():
         local_v = 5
         print("Access to global:", my_global)

     fn1()  # Imprime 10
     ```

5. **Ejemplo de alcance local**:
   - Una variable definida dentro de una función no es accesible fuera de ella.
   - Ejemplo:
     ```python
     def fn1():
         local_v = 5

     print(local_v)  # Genera un error porque local_v no está definido fuera de fn1
     ```

6. **Ejemplo de alcance cerrado**:
   - Una función anidada puede acceder a variables definidas en la función englobante.
   - Ejemplo:
     ```python
     def fn1():
         enclosed_v = 8

         def fn2():
             print("Access to enclosed:", enclosed_v)

         fn2()

     fn1()  # Imprime 8
     ```

7. **Ejemplo de alcance integrado**:
   - Las palabras reservadas y funciones integradas de Python están siempre accesibles.
   - Ejemplo:
     ```python
     print("Hello, World!")  # print es una palabra reservada en el alcance integrado
     ```

8. **Regla general**:
   - Las variables de alcance global se desaconsejan en aplicaciones porque aumentan la posibilidad de errores.
   - Los elementos en los niveles internos tienen acceso a los elementos de los niveles externos, pero no al revés.

9. **Importancia del alcance**:
   - Protege las variables para que no sean modificadas por otras partes del código, lo que ayuda a evitar errores y mantener el código más seguro y manejable.