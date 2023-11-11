# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
jogada = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('''Opções:
      [0] Pedra
      [1] Papel
      [2] Tesoura
      ''')
player = int(input('Sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('=' * 30)
print(f'Computador joga: {jogada[comp]}')
print(f'Jogador joga: {jogada[player]}')
print('=' * 30)
if comp == 0:
    if player == 0:
        print('EMPATE!')
    elif player == 1:
        print('JOGADOR VENCEU!')
    elif player == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif comp == 1:
    if player == 0:
        print('COMPUTADOR VENCEU!')
    elif player == 1:
        print('EMPATE!')
    elif player == 2:
        print('JOGADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif comp == 2:
    if player == 0:
        print('JOGADOR VENCEU!')
    elif player == 1:
        print('COMPUTADOR VENCEU!')
    elif player == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')