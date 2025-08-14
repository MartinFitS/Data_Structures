# Las queue o colas son una estructura de datos que siguen los principios de FIFO 
# (FIRST IN FIRST OUT), el primer elemento que entro es el primero que debe salir

# uso mas facil (List)

queue = []

# Enqueue
queue.append(2)
queue.append(3)
queue.append(9)
queue.append(8)
queue.append(13)
queue.append(12)

# eliminar el ultimo elemento (lentitud O(N))
queue.pop(0)

# Printear queue

print(queue)


# Usando collections.deque mejor optimizado (recomendado)

from collections import deque

queue2 = deque()

# Enqueue
queue2.append(10)
queue2.append(20)
queue2.append(100)
queue2.append(20222)

# Dequeue (O(1))
first = queue2.popleft()

print(queue2)  # deque([20])