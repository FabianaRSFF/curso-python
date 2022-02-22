frase = 'O rato roeu a roupa do rei de Roma'
tamanho_da_frase = len(frase)
contador = 0
nova_str = ''

while contador < tamanho_da_frase:
    # print(frase[contador], contador)
    nova_str += frase[contador]
print(nova_str)
contador += 1

print(nova_str)