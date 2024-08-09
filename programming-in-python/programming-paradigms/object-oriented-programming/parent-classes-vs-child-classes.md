# Parent classes vs. child classes

Aquí tienes las notas relevantes sobre el texto sobre la herencia en Python:

1. **Herencia en Python**: La herencia es un concepto central en la programación orientada a objetos (OOP) y es clave para la reutilización del código. En Python, todas las clases heredan de una clase base llamada `object`.

2. **Clases y objetos**: Una clase que hereda de otra se conoce como "clase hija" o "subclase", mientras que la clase de la cual hereda es llamada "clase padre", "superclase" o "clase base".

3. **Extensión de propiedades**: La clase hija extiende los atributos y comportamientos de la clase padre. Esto permite añadir nuevas propiedades o modificar las heredadas sin afectar la clase padre.

4. **Ejemplo básico**: Si una clase hija no tiene atributos propios, aún puede heredar y utilizar los atributos de la clase padre. Cambios en la clase padre se reflejan en las clases hijas.

5. **Ejemplo práctico**: Se crea una clase `Employees` con variables `name` y `last`. Luego se crean dos clases hijas: `Supervisors` y `Chefs`. `Supervisors` añade una variable `password`, y `Chefs` tiene un método `leave_request` que retorna una solicitud de días libres.

6. **Uso de `super()`**: En la clase `Supervisors`, el método `__init__` usa `super()` para acceder a las variables de la clase `Employees` y inicializarlas en la subclase.

7. **Instancias de las clases**: Se crean instancias de las clases `Supervisors` y `Chefs`, demostrando cómo se pueden acceder a los métodos y variables tanto de la clase padre como de las clases hijas.

8. **Reutilización de código**: La herencia facilita la organización del código, haciéndolo menos redundante y más fácil de mantener.

Aquí tienes un ejemplo práctico basado en el texto para ilustrar la herencia en Python:

```python
# Definición de la clase padre
class Employees:
    def __init__(self, name, last):
        self.name = name
        self.last = last

# Definición de la clase hija 'Supervisors' que hereda de 'Employees'
class Supervisors(Employees):
    def __init__(self, name, last, password):
        super().__init__(name, last)  # Llama al constructor de la clase padre
        self.password = password      # Añade una nueva propiedad a la clase hija

# Definición de la clase hija 'Chefs' que hereda de 'Employees'
class Chefs(Employees):
    def leave_request(self, days):
        return f"May I take leave for {days} days?"

# Creación de instancias de las clases
adrian = Supervisors("Adrian", "A", "apple")
emily = Chefs("Emily", "E")
juno = Chefs("Juno", "J")

# Uso de los métodos y propiedades de las instancias
print(emily.leave_request(3))    # Salida: May I take leave for 3 days?
print(adrian.password)           # Salida: apple
print(emily.name)                # Salida: Emily
```

### Explicación del ejemplo:

1. **Clase padre `Employees`**: Define dos atributos, `name` y `last`, que se inicializan en el constructor (`__init__`).

2. **Clase hija `Supervisors`**: Hereda de `Employees` y añade un atributo adicional `password`. Usa `super().__init__(name, last)` para llamar al constructor de la clase padre y asegurarse de que `name` y `last` sean inicializados correctamente.

3. **Clase hija `Chefs`**: También hereda de `Employees`, pero en lugar de añadir propiedades, define un nuevo método `leave_request` que retorna una solicitud de días libres.

4. **Instancias**: Se crean instancias de `Supervisors` y `Chefs` con los valores correspondientes.

5. **Salida**: Los `print` muestran cómo se accede a los métodos y propiedades tanto de las clases hijas como de la clase padre.