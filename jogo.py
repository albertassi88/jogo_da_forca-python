import random
from forca import erro

palavras = ['python', 'forca', 'teclado', 'github']
ganhou = 0
perdeu = 1

computador = str(random.choice(palavras))
letra_acertou = ['_'] * len(computador)

while (ganhou != computador.__len__()) & (perdeu != 7):
    letra = str(input('Jogador tente acertar a palavra! digite uma letra:'))

    while (not letra.isalpha()) | (letra_acertou.__contains__(letra) | (len(letra) > 1)):
        letra = str(input('Opção Inválida! Digite só uma letra.'))

    posicao=0
    if computador.__contains__(letra):
        print('Você acertou a letra!')
        ganhou = ganhou + 1
        posicao = computador.index(letra)
        letra_acertou.pop(posicao)
        letra_acertou.insert(posicao, letra)
        letra_acertou_string = str(letra_acertou)
        print(letra_acertou_string.upper())
    else:
        print('Você errou a letra!')
        print(erro.desenho_forca[perdeu])
        perdeu = perdeu + 1

    if ganhou == computador.__len__():
        print('Parabéns você ganhou!')
    elif perdeu == 7:
        print(f'Você perdeu! a palavra era {computador.upper()}')


































