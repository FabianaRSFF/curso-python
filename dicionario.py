"""
Dicionários
"""
# d1 = {'chave':'valor'}
# d1['nova_chave'] = 'valor da nova_chave'
# print(d1)
# print(d1['chave'])
#
# # Ou:
#
# d2 = dict(chave1 = 'Valor chave1', chave2 = 'outra chave')
# print(d2)
# print(d2['chave1'])

d1 = {
     'str': 'valor',
     123: 'Outro valor',
     (1, 2, 3, 4): 'tupla'

}

d1['str'] = 'Agora ela existe'
if d1.get('str') is not None:
    print(d1.get('str'))

print(123)