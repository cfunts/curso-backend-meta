# Comportamiento

Claro, explicaré cómo cambia el comportamiento del código de las Torres de Hanoi paso a paso y cómo se modifican los registros durante la ejecución.

### Ejemplo Paso a Paso

Supongamos que llamamos a la función `hanoi` con 3 discos y las torres etiquetadas como 'A' (origen), 'B' (auxiliar) y 'C' (destino).

```python
hanoi(3, 'A', 'B', 'C')
```

### Paso 1: Llamada Inicial

**`hanoi(3, 'A', 'B', 'C')`**

1. **Verificación de la Condición Base**:
   - `disks = 3`, no es igual a 1, así que no se cumple la condición base.

2. **Primera Llamada Recursiva**:
   - Se llama a `hanoi(2, 'A', 'C', 'B')` (mover 2 discos de 'A' a 'B', usando 'C' como auxiliar).

### Paso 2: Primera Llamada Recursiva

**`hanoi(2, 'A', 'C', 'B')`**

1. **Verificación de la Condición Base**:
   - `disks = 2`, no es igual a 1.

2. **Segunda Llamada Recursiva**:
   - Se llama a `hanoi(1, 'A', 'B', 'C')` (mover 1 disco de 'A' a 'C', usando 'B' como auxiliar).

### Paso 3: Segunda Llamada Recursiva

**`hanoi(1, 'A', 'B', 'C')`**

1. **Verificación de la Condición Base**:
   - `disks = 1`, cumple la condición base.

2. **Impresión del Movimiento**:
   - Imprime: `Disk 1 moves from tower A to tower C.`

3. **Retorno**:
   - La función retorna y vuelve a la llamada anterior (`hanoi(2, 'A', 'C', 'B')`).

### Continuación de la Primera Llamada Recursiva

**`hanoi(2, 'A', 'C', 'B')`** (Continuación)

1. **Impresión del Movimiento del Disco 2**:
   - Imprime: `Disk 2 moves from tower A to tower B.`

2. **Tercera Llamada Recursiva**:
   - Se llama a `hanoi(1, 'C', 'A', 'B')` (mover 1 disco de 'C' a 'B', usando 'A' como auxiliar).

### Paso 4: Tercera Llamada Recursiva

**`hanoi(1, 'C', 'A', 'B')`**

1. **Verificación de la Condición Base**:
   - `disks = 1`, cumple la condición base.

2. **Impresión del Movimiento**:
   - Imprime: `Disk 1 moves from tower C to tower B.`

3. **Retorno**:
   - La función retorna y vuelve a la llamada anterior (`hanoi(2, 'A', 'C', 'B')`), que a su vez retorna a la llamada inicial (`hanoi(3, 'A', 'B', 'C')`).

### Continuación de la Llamada Inicial

**`hanoi(3, 'A', 'B', 'C')`** (Continuación)

1. **Impresión del Movimiento del Disco 3**:
   - Imprime: `Disk 3 moves from tower A to tower C.`

2. **Cuarta Llamada Recursiva**:
   - Se llama a `hanoi(2, 'B', 'A', 'C')` (mover 2 discos de 'B' a 'C', usando 'A' como auxiliar).

### Paso 5: Cuarta Llamada Recursiva

**`hanoi(2, 'B', 'A', 'C')`**

1. **Verificación de la Condición Base**:
   - `disks = 2`, no es igual a 1.

2. **Quinta Llamada Recursiva**:
   - Se llama a `hanoi(1, 'B', 'C', 'A')` (mover 1 disco de 'B' a 'A', usando 'C' como auxiliar).

### Paso 6: Quinta Llamada Recursiva

**`hanoi(1, 'B', 'C', 'A')`**

1. **Verificación de la Condición Base**:
   - `disks = 1`, cumple la condición base.

2. **Impresión del Movimiento**:
   - Imprime: `Disk 1 moves from tower B to tower A.`

3. **Retorno**:
   - La función retorna y vuelve a la llamada anterior (`hanoi(2, 'B', 'A', 'C')`).

### Continuación de la Cuarta Llamada Recursiva

**`hanoi(2, 'B', 'A', 'C')`** (Continuación)

1. **Impresión del Movimiento del Disco 2**:
   - Imprime: `Disk 2 moves from tower B to tower C.`

2. **Sexta Llamada Recursiva**:
   - Se llama a `hanoi(1, 'A', 'B', 'C')` (mover 1 disco de 'A' a 'C', usando 'B' como auxiliar).

### Paso 7: Sexta Llamada Recursiva

**`hanoi(1, 'A', 'B', 'C')`**

1. **Verificación de la Condición Base**:
   - `disks = 1`, cumple la condición base.

2. **Impresión del Movimiento**:
   - Imprime: `Disk 1 moves from tower A to tower C.`

3. **Retorno**:
   - La función retorna y vuelve a la llamada anterior (`hanoi(2, 'B', 'A', 'C')`), que a su vez retorna a la llamada inicial (`hanoi(3, 'A', 'B', 'C')`).

### Conclusión

La función ha terminado y todos los movimientos han sido impresos en el orden correcto. El comportamiento recursivo sigue descomponiendo el problema en sub-problemas más pequeños hasta que llega al caso base, y luego reconstruye la solución completa.