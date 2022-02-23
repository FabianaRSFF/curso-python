def lista_de_clientes(clientes_iteravel, lista=[]):
    lista.extend(clientes_iteravel)
    return lista


clientes1 = lista_de_clientes(['Marcos', 'Maria','João'])
clientes2 = lista_de_clientes(['Léo', 'Rodrigo', 'Fabiana'])

print(lista_de_clientes)
print(clientes2)
