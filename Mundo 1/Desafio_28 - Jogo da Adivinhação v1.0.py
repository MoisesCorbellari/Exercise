# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
from emoji import emojize
comp = randint(0,5)
print('''
      Sorteando um número de 0 a 5...
      ''')
user = int(input('Vou escolher o número... '))
print(emojize('PENSANDO...:thinking_face:'))
sleep(1)
if user == comp:
    print(emojize('Parabéns, você acertou!:party_popper:'))
else:
    print(emojize('Você errou, pensei no número {} e não no número {}!:face_with_rolling_eyes:'.format(comp, user)))
