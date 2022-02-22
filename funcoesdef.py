# def ola_mundo():
#     return 'Olá Mundo'
#
# def mestre(funcao):
#     return funcao()
#
# executando = mestre(ola_mundo)
# print(executando)

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome}!'


def saudacao(saudacao, nome):
    return f'{saudacao} {nome}'


executando = mestre(fala_oi, 'Joaquim')
executando2 = mestre(saudacao, saudacao='Bom dia', nome='Lia!')
print(executando)
print(executando2)