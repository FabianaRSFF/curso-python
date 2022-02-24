# import os
# from utilidades import formata_tamanho
#
# caminho_pesquisa = input('Digite um caminho: ')
# termo_procura = input('Digite um termo: ')
#
#
# conta = 0
# for raiz, diretorios, arquivos in os.walk(caminho_pesquisa):
#     for arquivo in arquivos:
#         try:
#             conta += 1
#             pesquisa_completa = os.path.join(raiz, arquivo)
#             nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
#             tamanho = os.path.getsize(pesquisa_completa)
#
#             print()
#             print('Encontrei o arquivo:', arquivo)
#             print('Caminho:', pesquisa_completa)
#             print('Nome:', nome_arquivo)
#             print('Extensão:', ext_arquivo)
#             print('Tamanho:', tamanho)
#             print('Tamanho formatado: ', formata_tamanho(tamanho))
#         except PermissionError as e:
#             print('Sem permissão de acesso.')
#         except FileNotFoundError as e:
#             print('Arquivo não encontrado.')
#         except Exception as e:
#             print('Erro desconhecido.', e)
#
# print()
# print(f'{conta} arquivo(s) encontrado(s).')