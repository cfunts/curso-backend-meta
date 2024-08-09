# Instance Methods

Aquí tienes unas notas relevantes del texto:

- **Problema a resolver**: Los gerentes de un restaurante tienen poco tiempo para manejar las solicitudes de pago de los empleados y actualizarse entre ellos cada vez que un empleado solicita su pago. El sistema actual es engorroso y requiere una automatización.

- **Objetivo del video**: Enseñar a usar variables y métodos de instancia para cambiar el estado de un objeto de instancia.

- **Clase `PaySlips`**:
  - Se crea una clase `PaySlips` con tres variables de instancia: `name`, `pay_status` y `amount`.
  - Se inicializan en el método `__init__` usando `self.variable = variable`.
  
- **Métodos en la clase**:
  - **Método `pay`**: Cambia el estado del pago a "sí" (`self.payment = 'yes'`).
  - **Método `status`**: Muestra el estado de pago del empleado. Si el pago ha sido realizado, muestra el nombre del empleado y la cantidad pagada; si no, indica que aún no ha sido pagado.

- **Creación de instancias**:
  - Se crean dos instancias de la clase `PaySlips` para los empleados Nathan y Roger, con sus respectivos nombres, estados de pago ("no") y montos de pago (1000 y 3000).

- **Uso de métodos de instancia**:
  - Se verifica el estado de pago de Nathan y Roger usando el método `status`.
  - Se actualiza el estado de pago de Nathan usando el método `pay` y se muestra el nuevo estado de pago.
  
- **Importancia de las instancias**:
  - Cada objeto de instancia (Nathan y Roger) tiene su propio estado independiente. Al cambiar el estado de Nathan, el estado de Roger no se ve afectado.
  
- **Aplicación práctica**: Este código podría ser la base para un sistema de pago en línea, donde los gerentes actualizan el estado de pago de los empleados con un clic, eliminando la necesidad de llamadas entre ellos.

Estas notas resumen los puntos clave sobre cómo utilizar variables y métodos de instancia para automatizar procesos y gestionar estados de manera eficiente en un sistema de pago.

## Ejemplo

Aquí tienes un ejemplo de código basado en el texto, que demuestra el uso de variables y métodos de instancia en una clase para gestionar el estado de pago de empleados:

```python
# Definición de la clase PaySlips
class PaySlips:
    def __init__(self, name, pay_status, amount):
        self.name = name
        self.pay_status = pay_status
        self.amount = amount

    def pay(self):
        self.pay_status = 'yes'

    def status(self):
        if self.pay_status == 'yes':
            return f"{self.name} has been paid {str(self.amount)}"
        else:
            return f"{self.name} has not been paid yet"

# Creación de instancias de la clase para empleados
nathan = PaySlips("Nathan", "no", 1000)
roger = PaySlips("Roger", "no", 3000)

# Verificar el estado de pago de Nathan y Roger
print(nathan.status())
print(roger.status())

# Actualizar el estado de pago de Nathan
nathan.pay()

# Verificar el estado de pago de Nathan y Roger después del pago
print("\nAfter payment:")
print(nathan.status())
print(roger.status())
```

### Explicación del código:

1. **Clase `PaySlips`**:
   - La clase tiene tres variables de instancia: `name`, `pay_status` y `amount`.
   - El método `__init__` inicializa estas variables cuando se crea una instancia de la clase.
   - El método `pay` actualiza el estado de pago (`pay_status`) a "yes".
   - El método `status` devuelve un mensaje que indica si el empleado ha sido pagado o no.

2. **Creación de instancias**:
   - Se crean dos instancias de la clase `PaySlips`, una para Nathan y otra para Roger, con sus nombres, estados de pago iniciales ("no") y montos de pago.

3. **Uso de los métodos**:
   - Se llama al método `status` para verificar si Nathan y Roger han sido pagados.
   - Luego, se actualiza el estado de pago de Nathan usando el método `pay`.
   - Finalmente, se llama de nuevo al método `status` para verificar el estado después de la actualización.

### Salida esperada:

```plaintext
Nathan has not been paid yet
Roger has not been paid yet

After payment:
Nathan has been paid 1000
Roger has not been paid yet
```

Este ejemplo muestra cómo las instancias de una clase pueden manejar estados individuales y cómo un método puede actualizar estos estados sin afectar a otras instancias.