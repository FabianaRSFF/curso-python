a = lambda x, y: x * y
print(a(2, 2))

lista = [
    ['P1', 80],
    ['P2', 20],
    ['P3', 31],
    ['P4', 15],
    ['P5', 50],
]
# def func(item):
#     return item[1]
# lista.sort(key=func, reverse=True) #O reverse inverte os valores do maior p/menor!!!
# print(lista)
lista.sort(key=lambda item:item[1], reverse=True)
print(lista)