# Introduction to Object Oriented Programming

Aquí tienes las notas con ejemplos que ilustran cada uno de los principios de la Programación Orientada a Objetos (OOP) en Python:

### 1. **Encapsulación**
   - **Definición**: Agrupa datos (variables) y métodos (funciones) dentro de una clase, controlando el acceso a ellos.
   - **Ejemplo**:
     ```python
     class Employee:
         def __init__(self, name, position):
             self.name = name          # Público
             self._position = position # Protegido
             self.__salary = 50000     # Privado

         def get_salary(self):
             return self.__salary

         def set_salary(self, new_salary):
             if new_salary > 0:
                 self.__salary = new_salary

     emp = Employee("John Doe", "Developer")
     print(emp.name)        # Acceso directo al atributo público
     print(emp._position)   # Acceso al atributo protegido (convención)
     print(emp.get_salary()) # Acceso al atributo privado a través de un método público
     emp.set_salary(60000)
     print(emp.get_salary()) # Actualización del atributo privado a través de un método público
     ```

   - **Explicación**: `name` es un atributo público, `position` es protegido (accesible dentro de la clase y subclases), y `__salary` es privado (accesible solo dentro de la clase).

### 2. **Polimorfismo**
   - **Definición**: Permite que un objeto o método tome diferentes formas y se comporte de manera distinta según el contexto.
   - **Ejemplo 1**: Uso del operador `+` en diferentes contextos.
     ```python
     print(3 + 5)           # Suma de enteros
     print("Hello " + "World")  # Concatenación de cadenas
     print([1, 2] + [3, 4]) # Combinación de listas
     ```

   - **Ejemplo 2**: Uso de la función `len()` en diferentes tipos de datos.
     ```python
     print(len("Hello"))    # Longitud de una cadena
     print(len([1, 2, 3, 4])) # Longitud de una lista
     ```

   - **Explicación**: El operador `+` y la función `len()` funcionan de manera diferente según el tipo de dato con el que se utilicen.

### 3. **Herencia**
   - **Definición**: Permite crear una nueva clase que hereda atributos y métodos de una clase existente.
   - **Ejemplo**:
     ```python
     class Animal:
         def __init__(self, name):
             self.name = name

         def speak(self):
             return "Some sound"

     class Dog(Animal):
         def speak(self):
             return "Woof!"

     class Cat(Animal):
         def speak(self):
             return "Meow!"

     dog = Dog("Buddy")
     cat = Cat("Whiskers")

     print(dog.name, dog.speak()) # Buddy Woof!
     print(cat.name, cat.speak()) # Whiskers Meow!
     ```

   - **Explicación**: `Dog` y `Cat` heredan de `Animal` pero sobrescriben el método `speak()` para proporcionar un comportamiento específico.

### 4. **Abstracción**
   - **Definición**: Oculta detalles de implementación y muestra solo lo necesario, utilizando clases abstractas y métodos abstractos.
   - **Ejemplo**:
     ```python
     from abc import ABC, abstractmethod

     class Shape(ABC):
         @abstractmethod
         def area(self):
             pass

     class Rectangle(Shape):
         def __init__(self, width, height):
             self.width = width
             self.height = height

         def area(self):
             return self.width * self.height

     class Circle(Shape):
         def __init__(self, radius):
             self.radius = radius

         def area(self):
             return 3.1416 * (self.radius ** 2)

     rect = Rectangle(3, 4)
     circ = Circle(5)

     print("Area of rectangle:", rect.area())  # 12
     print("Area of circle:", circ.area())     # 78.54
     ```

   - **Explicación**: `Shape` es una clase abstracta que define un método abstracto `area()`. `Rectangle` y `Circle` son subclases que implementan el método `area()` con detalles específicos.

Estos ejemplos muestran cómo los principios de OOP se aplican en Python para crear código modular, reutilizable y fácil de mantener.

