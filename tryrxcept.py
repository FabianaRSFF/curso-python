try:
    a = []
    print(a)
except NameError as erro:
    print('Erro do desenvolvedor. Fale com ele.')
except Exception as erro:
    print('Ocorreu um erro inesperado.')

print('Bora continuar...')
