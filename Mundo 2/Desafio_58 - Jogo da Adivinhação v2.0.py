# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

comp = randint(0, 10)
tentativa = 0
acertos = False
print('''
                                            Pensando em um número entre 0 e 10...
''')

while not acertos:
    user = int(input('Digite um valor entre 0 e 10: '))
    print('PENSANDO...')
    sleep(1)
    tentativa += 1
    if user == comp:
        acertos = True
    else:
        if user < comp:
            print('Mais...')
        elif user > comp:
            print('Menos...')

print('Parabéns, você acertou! Escolhi o número {}, e você tentou {} vezes acertar o número que escolhi'.format(comp,tentativa))