# variavel = 'valor'
#
# def func():
#     print(variavel)
# func()
#
# def func2():
#     global  variavel
#     variavel = 'Outro valor'
#     print(variavel)
#
# func()
# func2()
#
# print(variavel)

variavel = 'valor'


def func():
    print(variavel)

    
func()


def func2(arg=None):
    arg = arg.replace('v', 'c')
    return arg


func()
outra_variavel = func2(arg=variavel)

print(outra_variavel)

