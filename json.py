from dados import *
import json

with open('clientes.json', 'w') as arquivo:
    json.dump(clientes_dicionario, arquivo, indent=4)

dicionario = json.loads(clientes_json)

for chave, valor in dicionario.items():
    print(chave)
    print(valor)








