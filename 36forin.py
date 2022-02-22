"""
For, in
Iterando strings com for
Função range, start, stop, step
"""
texto = 'Python'
# c = 0
# while c < len(texto):
#     print(texto[c])
#     c += 1
# for letra in texto:
#     print(letra)
for n in range(10):
    print(n)

print('##########')
texto = 'Python'
nova_string = ''
for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)
