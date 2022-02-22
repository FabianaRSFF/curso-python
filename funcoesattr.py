import sys
import time


# lista = list(range(100))
# print(sys.getsizeof(lista))
def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)

g = gera()
print(hasattr(g, '__iter__'))
print(hasattr(g, '__next__'))
