while True:
 # cpf = '16899535009'
    cpf = input('Digite um CPF: ')
    novocpf = cpf[:-2]
    reverso = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -= 9
        total += int(novocpf[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            novocpf += str(d)

    if cpf == novocpf:
        print('CPF válido')
    else:
        print('Inválido')


# for indice, valor in cpf:
#     cpf = enumerate(indice)
#     valor.isdigit()
#     cpf = valor * indice.enumerate(range(10, 1, -1))
#     print(cpf)



