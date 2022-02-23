# class A:
#     def __new__(cls, *args, **kwargs):
#         print('Eu sou o new.')
#         cls.nome = 'Fabi'
#
#         return object.__new__(cls)
#
#     def __init__(self):
#
#         print('Eu sou o Init')
#
# a = A()
# print(a.nome)

# class A:
#     def __init__(self):
#         pass
#     def __call__(self, *args, **kwargs):
#         resultado = 1
#
#         for i in args:
#             resultado *= i
#         return resultado
#
# a = A()
# variavel = a(1, 2, 3, 6, 6, 3, 8)
# print(variavel)

class A:
    def __init__(self):
        pass

    def __setattr__(self, key, value):
        self.__dict__[key] = value

a = A()
a.nome = 'Luiz'
print(a.nome)

