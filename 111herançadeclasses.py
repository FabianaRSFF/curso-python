class A:
    def falar(self):
        print('Falando...estou em A.')


class B(A):
    def falar(self):
        print('Falando...estou em B.')


class C(A):
    def falar(self):
        print('Falando...estou em C.')


class D(B, C):
    pass


d = D()
d.falar()


