# def func(*args):
#     print(args)
#     print(args[0])
#     print(args[2])
#     print(len(args))
#
# func(1,2,3,4,5)
#
# def func(*args):
#     args = list(args)
#     args[0] = 20
#     print(args)
#     print(args[0])
#     print(args[2])
#     print(len(args))
#
# func(1,2,3,4,5)

# def func(*args):
#     for v in args:
#         print(v)
# func(1,2,3,4,5)

def func(*args, **kwargs):
    print(args)
    print(kwargs)


lista1 = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista1, *lista2, nome='joao', sobre='mario')

