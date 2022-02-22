"""
Funções - Def - Parte 2
"""


def saudacao(msg='Olá', nome='usuário'):
    nome = nome.replace('á', '@')
    msg = msg.replace('á', '@')
    return f'{msg} {nome}'


variavel = saudacao()
print(variavel)
