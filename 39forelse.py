"""
For / Else
"""

variavel = ['Vai', 'a', 'merda', '!']
for valor in variavel:
    if valor.lower().startswith('J'):
        print('Começa com J', valor)
    else:
        print('Não começa com J', valor)
