lista = [0, 1, 2, 3, 4, 5]
# lista = 12345
# lista1 = 'string'
# print(hasattr(lista1, '_iter_'))
lista = iter(lista)
print(hasattr(lista, '__next__'))
for v in lista:
    print(v)