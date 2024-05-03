'''Faça um programa que tenha uma função chamada maior(), 
que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

from time import sleep
from random import randint

def linha():
    print('-'*50)
    
def msg(txt):
    escreva = len(txt) + 40
    print('-'*escreva)
    print(f'{txt:>40}')
    print('-'*escreva)

def maior(*num):
    cont = maior = 0
    print('''
                Analisando os parâmetros...
          ''')
    sleep(1)
    for valor in num:
        sleep(1)
        print(f'{valor}', end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam analisados {cont} valores.')
    print(f'O maior valor informado é: {maior}')
    linha()

#main program
msg('Descorindo o maior número!')
n = int(input('Defina a quantidade de parâmetros para análise: '))
for _ in range(0,n):
    maior(
        randint(0, 100), randint(0, 100), 
        randint(0, 100), randint(0, 100),
        randint(0, 100), randint(0, 100)
        )