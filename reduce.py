from dados import produtos, pessoas, lista
from functools import reduce
# ac =  acumulador

soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)

soma_preços = reduce(lambda ac, p: p['preço'] + ac, produtos, 0)
print(soma_preços)

soma_idades = reduce(lambda ac, p: p['idade'] + ac, pessoas, 0)
print(soma_idades/len(pessoas))

