"""
Módulos padrão em Python:
São arquivos .py (que contém código Python) e servem para expandir as
funcionalidades da linguagem.
Veja todos em:
https://docs.python.org/3/py-modindex.html
"""
import sys
print(sys.platform)
# Se eu quiser importar apenas uma coisa do módulo sys( e colocar um apelido):
from sys import platform as pl

print(pl)

#Para gerar números aleatórios:
import random

print(random.randint(0, 10))
