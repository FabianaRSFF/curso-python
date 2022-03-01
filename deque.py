from collections import deque
from time import sleep


fila = deque()
fila.append('João')
fila.append('Maria')
fila.append('Zé')
fila.append('Lula')
fila.append('Dilma')
print(fila)
print(f'Saiu {fila.popleft()}')

fila2 = deque(maxlen=5)
fila2.extend([1, 2, 3, 4])
fila2.append(5)
fila2.append(6)
fila2.append(7)
fila2.append(8)
print(fila2)

fila3 = deque(maxlen=10)
for i in range(100):
    fila3.append(i)
    sleep(1)
    print(fila3)

"Aqui é first in, first out."