class A:
    vc = 123 
    
    def __init__(self):
        pass


A.vc = 'Alterado'
a1 = A()
a2 = A()
a1.vc = 321  # isto não altera a classe, apenas configura um atributo
#A.vc = 321 isto causa confusão, pois altera todas as instâncias.


print(a1.vc)
print(a2.vc)
print(A.vc)

