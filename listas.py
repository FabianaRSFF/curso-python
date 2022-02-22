l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [variavel for variavel in l1]
print(l2)   # l2 = l1

# Multiplicando a lista:

l3 = [v * 2 for v in l1]
print(l3)

# Criando coordenadas com tuplas:

l4 = [(v, v2) for v in l1 for v2 in range(3)]
print(l4)

l5 = ['Luiz', 'Mauro', 'Maria']
ex5 = [v.replace('a', '@').title() for v in l5]
print(ex5)

tupla = [
    ('chave', 'valor'),
    ('chave1', 'valor1'),
]
ex6 = [(y, x) for x, y in tupla]
ex6 = dict(ex6)
print(ex6)

l6 = list(range(0, 100))
ex7 = [v for v in l6 if v % 3 == 0 if v % 8 == 0]
print(ex7)
ex8 = [v if v % 3 == 0 else 'Não é' for v in l6]
print(ex8)


