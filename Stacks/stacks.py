# Un stack es una estructura de datos que sigue el principio LIFO (Last In, First Out)
# El último elemento en entrar es el primero en salir.
# Ejemplo: pila de platos — no podemos acceder al plato de abajo si hay otros encima.

# -----------------------------
# Stack con list (forma simple)
# -----------------------------
stack = []

# Agregar elementos (Push)
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

print("Stack (list):", stack)

# Eliminar el último elemento (Pop)
stack.pop()
print("Stack después de pop:", stack)

# Ver el elemento superior (Peek)
print("Elemento en la cima:", stack[-1])

# -----------------------------
# Stack con deque (más eficiente)
# -----------------------------
from collections import deque

stack2 = deque()

# Agregar elementos (Push)
stack2.append(1)
stack2.append(2)
stack2.append(3)
stack2.append(4)

print("Stack (deque):", stack2)

# Eliminar el último elemento (Pop)
stack2.pop()
print("Stack después de pop:", stack2)

# Ver el elemento superior (Peek)
print("Elemento en la cima:", stack2[-1])
