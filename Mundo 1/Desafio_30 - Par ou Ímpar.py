# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR..

from time import sleep
from emoji import emojize
num = int(input('Digite um valor qualquer: '))
print(emojize('Analisando...:thinking_face:'))
sleep(0.80)
print('PAR' if num % 2 == 0 else 'IMPAR')
