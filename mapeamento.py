from dados2 import produtos, pessoas, lista

#nova_lista = map(lambda x: x * 2, lista) SOLUÇÃO EM MAPEAMENTO
#SOLUÇÃO EM LIST COMPREHENSION:
"""nova_lista = (x * 2 for x in lista)
print(lista)
print(list(nova_lista))"""


def aumenta_preco(p):
    p['preço'] = round(p['preço'] * 1.05, 2)
    return p


novos_produtos = map(aumenta_preco, produtos)
for produto in novos_produtos:
    print(produto)