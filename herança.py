from classes3 import *

"""
Associação - Usa , Agregação - Tem , Composição-É dono, Herança - É
"""

c1 = Cliente('Luiz', 45)
print(c1.nome)
c1.falar()
c1.comprar()


c2 = ClienteVip('Rose', 25, 'Miranda')
c2.falar()
