from aula102a128.classeeletronico import Eletronico
from aula102a128.log import LogMixing


# Aqui importei dos meus arquivos, colocarei o arquivo com o número da  # aula para melhor compreensão.


class Smartphone(Eletronico, LogMixing):
    def __init__(self, nome):
        super(). __init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            info = f'{self._nome} não está ligado.'
            print(info)
            self.log_info(info)
            return

        if self._conectado:
            error = f'{self._nome} já está conectado.'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} está conectado.'
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} não está conectado.'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} foi desligado com sucesso.'
        print(info)
        self.log_info(info)
        self._conectado = False


smartphone = Smartphone('Fabiphone F1')
smartphone.conectar()
smartphone.ligar()
smartphone.conectar()
smartphone.conectar()
smartphone.conectar()
smartphone.desligar()
smartphone.conectar()
smartphone.desconectar()