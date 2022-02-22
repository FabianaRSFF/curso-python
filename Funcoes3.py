def funcao(var):
    return var
    print(var)


variavel = funcao('valor que eu quero')

if variavel:
    print(variavel)
else:
    print('nenhum valor')


def divisao(n1, n2):
    return n1/n2


divide = divisao(8, 2)
print(divide)


def divisao(n1, n2):
    if n2 > 0:
        return n1/n2
        

divide = divisao(8, 0)
if divide:
    print(divide)
else:
    print('Valor nulo')
