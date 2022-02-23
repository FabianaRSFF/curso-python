class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self,cidade,estado):
        self.enderecos.append(Endereco(cidade,estado))

    def lista_endereco(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.lista_endereco()
print()

cliente2 = Cliente('Ana', 65)
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.lista_endereco()
print()

cliente3 = Cliente('Maria', 55)
cliente3.insere_endereco('Salvador', 'Ba')
cliente3.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente3.nome)
cliente3.lista_endereco()
print()



