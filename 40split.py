"""
Split, join, Enumarate
Split - dividir uma string #str
Join - juntar uma lista #str
Enumarate - enumerar elementos de uma lista #list
"""
string = 'O Brasil está uma merda, fora bolsonaromerda, fora bolsonaro merda.'
lista = string.split(' ')
lista_2 = string.split(',')
print(lista_2)

# for valor in lista:
#    print(valor)
palavra = ''
contagem = 0
for valor in lista:
    qtd_de_vezes = lista.count(valor)


    if qtd_de_vezes > contagem:
        contagem = qtd_de_vezes
        palavra = valor

print(f'A palavra que apareceu , mais vezes é {palavra}({contagem}x)')

