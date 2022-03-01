from dados2 import produtos, pessoas, lista

# Utilizando Filter:
nova_lista = filter(lambda x: x > 5, lista)

#Utilizando list comprehension:


nova_lista = [x for x in lista if x > 5]
print(nova_lista)
print(list(nova_lista))