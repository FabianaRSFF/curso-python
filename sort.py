from itertools import groupby

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
alunos.sort(key=lambda item: item['nota'])
for aluno in alunos:
    print(aluno)