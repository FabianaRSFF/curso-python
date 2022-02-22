perguntas = {
    'pergunta1': {
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {'a': '1', 'b': '4', 'c': '5', },
        'resposta_certa': 'b',
    },
    'pergunta2': {
        'pergunta': 'Quanto é 3 * 2?',
        'respostas': {'a': '4', 'b': '10', 'c': '6', },
        'resposta_certa': 'c',
    },
    'pergunta3': {
        'pergunta': 'Quanto é 3 * 3?',
        'respostas': {'a': '9', 'b': '10', 'c': '6', },
        'resposta_certa': 'a',
    },

    'pergunta4': {
        'pergunta': 'Quanto é 100/2?',
        'respostas': {'a': '4', 'b': '50', 'c': '6', },
        'resposta_certa': 'b',
    },
    'pergunta5': {
        'pergunta': 'Quanto é 345 * 1?',
        'respostas': {'a': '4', 'b': '10', 'c': '345', },
        'resposta_certa': 'c',
    },
}
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Digite sua resposta: ')
    if resposta_usuario == pv['resposta_certa']:
        print('Correto')
        respostas_certas += 1
    else:
        print('Errou burro!!!!')

    print()

quantidade_de_perguntas = len(perguntas)
porcentagem_de_acerto = respostas_certas / quantidade_de_perguntas * 100
print(f'Você acertou {respostas_certas} respostas.')
print(f'Porcentage de acertos {porcentagem_de_acerto}%.')