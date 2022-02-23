"""
Implementando um iterador
"""


class Minha_Lista:
    def __init__(self):
        self._items = []
        self._index = 0

    def add(self, valor):
        self._items.append(valor)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, valor):
        if index >= len(self._items):
            self._items.append(valor)
        self._items[index] = valor

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self._items[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration

    def __str__(self):
        return f'{self.__class__.__name__}({self._items})'

    if __name__=='__main__':
        lista = Minha_Lista()
        lista.add('Luiz')
        lista.add('Dilma')
    for valor in lista:
        print(valor)

    lista[0] = 'Joao'
    lista[1]= 'Luiz'
    lista[2] = 'Dilma'
    lista[3] = 'Funciona'
    print(lista[0])
    print(lista)