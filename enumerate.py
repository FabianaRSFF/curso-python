"""
Enumarate
"""

lista = [
    ["Joca", 'Leo', 'Teo'],
    ["Jail", 'Luo', 'Tro'],
    ["Jaca", 'Teco', 'Tico'],
]
print(lista[0][2])
# enumerada = enumerate(lista)
# print(list(enumerada))
enumerada = list(enumerate(lista))
print(enumerada[0][1])
print((enumerada[1][1][2]))
for v1, v2 in enumerate(lista):
    print(v1, v2)