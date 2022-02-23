from abc import ABC, abstractmethod
# Aula113

class A(ABC):
    @abstractmethod
    def falar(self):
        pass


class B(A):
    def falar(self):
        print('Falando...B.')


a = B()
a.falar()

