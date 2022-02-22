from itertools import groupby, tee

alunos = [
    {'nome': 'Fabi', 'nota': 'A'},
    {'nome': 'Mia', 'nota': 'B'},
    {'nome': 'Raul', 'nota': 'A'},
    {'nome': 'Luca', 'nota': 'C'},
    {'nome': 'Bia', 'nota': 'A'},
    {'nome': 'Lia', 'nota': 'D'},
    {'nome': 'Mau', 'nota': 'A'},
    {'nome': 'Juca', 'nota': 'A'},
    {'nome': 'Adri', 'nota': 'A'},
    {'nome': 'Val', 'nota': 'A'},
    {'nome': 'Nina', 'nota': 'A'},
]
ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)
for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)
    print(f'Agrupamento: {agrupamento}')
    for aluno in va1:


#for aluno in valores_agrupados:
        print(f'\t{aluno}')

#print()
    quantidade = len(list(va2))
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')
    for aluno in valores_agrupados:
        print(aluno)
