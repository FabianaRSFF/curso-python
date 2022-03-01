from collections import deque
from time import sleep

fila = deque(maxlen=10)
fila.extend([1, 2, 3, 4, 5])
fila.insert(2, 'Fabi')
print(fila)
print(fila.index(2))
fila.reverse()
print(fila)
fila.rotate(1)