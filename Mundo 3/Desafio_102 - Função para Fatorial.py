'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
o primeiro que indique o número a calcular e 
outro chamado show, que será um valor lógico (opcional) 
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''

import math
from time import sleep
from progress.spinner import PixelSpinner

def title(txt):
    msg = len(txt) + 50
    print(f'{txt:>40}')
    print('-'*msg)

def linha():
    print('-'*70)

def fatorial(n, show=False):
    f = math.factorial(n)
    if show:
        print(f'Resultado de {n}! -> ', end='')
        for c in range(n, 0, -1):
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f
title('Cálculo de Fatorial')
while True:
    try:
        num = int(input('\nDigite um valor: '))
    except ValueError:
        print('Valor inválido!')
        continue
    show = str(input('Quer exibir o cálculo [S/N]? ')).strip().upper()
    if show == 'S':
        print(f'{fatorial(num, show=True)}')
    else:
        print(f'Resultado -> {fatorial(num, show=False)}')
        linha()
        ask = str(input('\nQuer continuar [S/N]? ')).strip().upper()
        if ask == 'N':
            with PixelSpinner('Encerrando ... ') as bar:
                for _ in range(60):
                    sleep(0.02)
                    bar.next()
            break
