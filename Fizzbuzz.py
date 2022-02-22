# def saudacao(msg='Olá', nome='Usuário'):
#     # return f'{msg} {nome}'
#     print(msg, nome)
#
# saudacao(nome='joao')
# saudacao(nome='Maria')
#
# def soma(n1=8, n2=9, n3=10):
#     return n1 + n2 + n3
#
# variavel = soma(8, 9, 10)
# print(variavel)
#
# def somacem(num= 20, perc=10):
#     return  num + (num * perc) / 100
#
# var = somacem(20, 10)
# print(var)
# var = int(input('Digite um numero: '))
# var = fb
# var.isdigit(p1, p2, p3)
# var = p1, p2, p3
def fb(n):

    if n % 5 == 0 and n % 3 == 0:
        return 'fizzbuzz'
    if n % 5 == 0:
        return 'buzz'
    if n % 3 == 0:
        return 'fizz'
    return n


from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    print(fb(aleatorio))








