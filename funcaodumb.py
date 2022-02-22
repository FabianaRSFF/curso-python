def dumb():
    return 1

    
print(dumb(), type(dumb()))


def f(var):
    print(var)


def dumb2():
    return f


var = dumb2()
var('Pode imprimir alguma coisa na tela.')
