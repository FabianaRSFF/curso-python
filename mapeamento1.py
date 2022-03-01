from dados2 import produtos, pessoas, lista

nomes = map(lambda p: p['nome'], pessoas)
for pessoa in nomes:
    print(pessoa)