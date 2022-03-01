from time import sleep
from threading import Thread

class MeuThread(Thread):
    def __init__(self, texto,  tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)

t1 = MeuThread('Thread1', 3)
t1.start()

t2 = MeuThread('Thread2', 8)
t2.start()

t3 = MeuThread('We are here!', 15)
t3.start()

for i in range(20):
    print(i)
    sleep(1)

