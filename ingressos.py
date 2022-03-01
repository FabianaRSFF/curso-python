from time import sleep
from threading import Thread
from threading import Lock

# def vai_demorar(texto, tempo):
#     sleep(tempo)
#     print(texto)
#
# t = Thread(target=vai_demorar, args=('Olá mundo', 5))
# t.start()
#
# # for i in range(20):
# #     print(i)
# #     sleep(.5)
#
# while t.is_alive():
#     print('esperando a thread')
#     sleep(2)
#

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        # self.lock = Lock()

    def comprar(self,quantidade):
        # self.lock.acquire()
        if self.estoque < quantidade:
            print("Estoque indisponível.")
            # self.lock.release()
            return
        self.estoque -= quantidade
        print(f'Você comprou {quantidade}. Ainda temos {self.estoque},'
              f' vai querer mais?')

        self.estoque != quantidade
        print(f'Ainda temos{self.estoque}, vai querer?')

        if self.estoque == 0:
            print(f'Ingressos esgotados.')



if __name__== '__main__':
    ingressos = Ingressos(10)
    ingressos.comprar(1)
    ingressos.comprar(1)
    ingressos.comprar(5)
    ingressos.comprar(8)
    ingressos.comprar(3)


