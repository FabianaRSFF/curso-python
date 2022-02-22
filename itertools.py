from itertools import product

pessoas = ['Lia', 'Ju', 'Bia', 'Cris', 'Pati', 'Tom']
for grupo in product(pessoas, repeat=2):
    print(grupo)
