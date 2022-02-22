"""
Funções - Def - Parte1 - O legal é que só é necessário alterar apenas o
que você quiser, sem ter que alterar várias vezes como no print().
"""
def funcao():
    print('Hello World!!!')
funcao()
funcao()
funcao()
funcao()
"""
Colocando parâmetros dentro da função, neste caso quando o parâmetro não for 
incluído na função, a mesma não será acessada e informará erro.
"""
def funcao(msg):
    print(msg)


funcao('mensagem')
# funcao()
# funcao()


def saudacao(msg='Olá', nome='usuário'):
    print(msg, nome)


saudacao(nome='Raul')
saudacao(nome='Gilda')
saudacao(msg='Hello!!!')


def saudacao(msg='Olá', nome='usuário'):
    nome = nome.replace('a', '@')
    msg = msg.replace('a', '@')
    print(msg, nome)

saudacao(nome='Raul')
saudacao(nome='Gilda')
saudacao(msg='Hello!!!')