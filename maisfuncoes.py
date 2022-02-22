variavel = 'casa'


def func():
    print(variavel)


def func2(arg=None):
    arg = 'sol', 'lua'
    return arg


def func3(arg=None):
    arg = 'amarelo', 'azul'
    return arg


outra_variavel = func2(arg='sol''lua'), func3(arg='amarelo''azul')
print(outra_variavel)



