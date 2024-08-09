Aquí tienes las notas relevantes sobre el texto que explica la herencia simple, múltiple y el uso de la función `super()` en Python:

### Herencia Simple

1. **Definición**: La herencia simple en Python se realiza cuando una clase hereda de otra única clase. Esto permite que la clase hija acceda a los atributos y métodos de la clase padre.
   
   ```python
   class A:
       pass

   class B(A):
       pass
   ```

2. **Acceso a atributos**: La clase hija (`B`) puede acceder directamente a los atributos y métodos de la clase padre (`A`).

### Herencia Múltiple

1. **Definición**: Python permite la herencia múltiple, donde una clase puede heredar de más de una clase.
   
   ```python
   class A:
       a = 1

   class B:
       b = 2

   class C(A, B):
       pass

   c = C()
   print(c.a, c.b)  # Salida: 1 2
   ```

2. **Importancia del orden**: El orden de las clases en la definición de la clase hija es importante, aunque en el ejemplo dado no afecta el resultado.

### Herencia en Múltiples Niveles

1. **Definición**: La herencia en múltiples niveles ocurre cuando una clase hija hereda de una clase que a su vez es hija de otra clase.
   
   ```python
   class A:
       a = 1

   class B(A):
       a = 2

   class C(B):
       pass

   c = C()
   print(c.a)  # Salida: 2
   ```

2. **Resultado**: En el ejemplo, la clase `C` hereda de la clase `B`, que a su vez hereda de la clase `A`. El valor del atributo `a` es 2 porque `C` hereda el valor más reciente definido en `B`.

### Funciones Incorporadas: `issubclass()` y `isinstance()`

1. **`issubclass()`**: Determina si una clase es una subclase de otra.
   
   ```python
   print(issubclass(B, A))  # True
   print(issubclass(A, B))  # False
   ```

2. **`isinstance()`**: Determina si un objeto es una instancia de una clase.
   
   ```python
   b = B()
   print(isinstance(b, B))  # True
   print(isinstance(b, A))  # True
   ```

### Uso de la Función `super()`

1. **Definición**: La función `super()` se utiliza en una clase derivada para llamar a métodos o inicializadores de la clase padre, permitiendo la reutilización del código de la clase base.
   
   ```python
   class Fruit:
       def __init__(self, fruit):
           print('Fruit type:', fruit)

   class FruitFlavour(Fruit):
       def __init__(self):
           super().__init__('Apple')
           print('Apple is sweet')

   apple = FruitFlavour()
   ```

2. **Salida**:
   - Con `super()`:  
     ```
     Fruit type:  Apple
     Apple is sweet
     ```
   - Sin `super()`:  
     ```
     Apple is sweet
     ```

3. **Beneficio de `super()`**: Garantiza que el inicializador de la clase base también sea llamado cuando se inicializa la clase derivada, lo que es crucial para mantener la coherencia del estado del objeto.

Estas notas resumen los conceptos clave de herencia simple, múltiple, herencia en múltiples niveles, y el uso de `super()` en Python.