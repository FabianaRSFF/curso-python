"""
Combinations, permutations e product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repetem valores únicos
"""
from itertools import combinations, permutations, product
#Combinação - Ordem não importa
pessoas = ['Lia', 'Ju', 'Bia', 'Cris', 'Pati', 'Tom']
for grupo in combinations(pessoas, 2):
    print(grupo)

#Permutação - Ordem importa
for grupo in permutations(pessoas, 2):
     print(grupo)
