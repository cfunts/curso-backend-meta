# Instantiate a custom Object

Aquí tienes unas notas relevantes del texto:

1. **Reusabilidad del código**: La reusabilidad es un concepto fundamental en la programación que permite usar el código existente para construir nuevo software. En Python, esto se ejemplifica mediante la creación de clases e instancias.

2. **Creación de clases**: Se enseña cómo crear una clase en Python, en este caso, una clase llamada `recipe`, y cómo instanciarla con variables y métodos para producir diferentes resultados a partir de la misma estructura.

3. **Métodos especiales en Python**:
   - **`__new__`**: Es responsable de crear y devolver un nuevo objeto vacío. Usa la convención `cls` para pasar la clase como primer argumento.
   - **`__init__`**: Similar al constructor en otros lenguajes, inicializa el objeto creado por `__new__` con otros argumentos. Usa la convención `self` para la autorreferencia del objeto de instancia.

4. **Inicialización de variables**: El método `__init__` se utiliza para inicializar variables como `dish`, `items`, y `time` dentro de la clase. Estas variables representan el nombre del plato, los ingredientes y el tiempo de preparación, respectivamente.

5. **Método de contenido**: Se crea un método `contents` que genera una cadena de texto que describe el plato, sus ingredientes y el tiempo de preparación.

6. **Instanciación de objetos**: Se crean dos instancias de la clase `recipe`: `pizza` y `pasta`, cada una con diferentes ingredientes y tiempos de preparación. Se demuestra cómo, a pesar de usar el mismo método y variables, las instancias producen resultados diferentes.

7. **Acceso a atributos y métodos**: Se muestra cómo acceder a los atributos y métodos de las instancias, imprimiendo los ingredientes (`items`) y utilizando el método `contents` para describir cada receta.

8. **Diferentes resultados con el mismo código**: El texto concluye demostrando cómo el mismo código puede producir resultados distintos dependiendo de las instancias y los valores utilizados, lo que ejemplifica la reusabilidad del código.

## Ejemplo

Aquí tienes un ejemplo basado en el texto, mostrando cómo crear una clase en Python, instanciarla y obtener diferentes resultados utilizando el mismo código:

```python
# Definir la clase Recipe
class Recipe:
    def __new__(cls, *args, **kwargs):
        # Crear un nuevo objeto vacío
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, dish, items, time):
        # Inicializar el objeto con valores
        self.dish = dish
        self.items = items
        self.time = time
    
    def contents(self):
        # Crear una cadena de texto con la información del plato
        return f"The {self.dish} has {', '.join(self.items)} and takes {self.time} min to prepare."

# Crear instancias de la clase Recipe
pizza = Recipe("Pizza", ["cheese", "bread", "tomato"], 45)
pasta = Recipe("Pasta", ["penne", "sauce"], 55)

# Acceder a los atributos y métodos de las instancias
print(pizza.items)  # Output: ['cheese', 'bread', 'tomato']
print(pasta.items)  # Output: ['penne', 'sauce']

# Usar el método contents para describir cada receta
print(pizza.contents())  # Output: The Pizza has cheese, bread, tomato and takes 45 min to prepare.
print(pasta.contents())  # Output: The Pasta has penne, sauce and takes 55 min to prepare.
```

**Explicación**:
- **Clase `Recipe`**: Se define una clase que incluye los métodos especiales `__new__` y `__init__` para crear e inicializar objetos.
- **Instancias `pizza` y `pasta`**: Se crean dos instancias de la clase con diferentes ingredientes y tiempos de preparación.
- **Diferentes resultados**: Aunque se usa el mismo código para ambos objetos, los resultados son diferentes, lo que demuestra la reusabilidad y flexibilidad del código.