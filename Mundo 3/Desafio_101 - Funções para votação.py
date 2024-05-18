'''
Crie um programa que tenha uma função chamada voto() 
que vai receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto 
NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''
from datetime import date
from time import sleep
from progress.spinner import MoonSpinner

def linha():
    print('-'*80)

def title(txt):
    msg = len(txt) + 50
    print(f'{txt:>40}')
    print('-'*msg)

def voto(ano):
    idade = date.today().year - ano

    if 16 <= idade < 18 or idade > 65:
        return f'{idade} anos: voto OPCIONAL.'
    elif idade < 16:
        return f'{idade} anos: voto NEGADO.'
    else:
        return f'{idade} anos: voto OBRIGATÓRIO.'
# main program
title('SISTEMA DE VERIFICAÇÃO DE VOTO')

while True:
    ano = int(input('\nAno de nascimento: '))
    with MoonSpinner('Processando informação ... ') as bar:
        for i in range(100):
            sleep(0.02)
            bar.next()
    print(voto(ano))
    resp = input('\nDeseja continuar? [S/N] ').strip().upper()[0]
    linha()
    if resp == 'N':
        print('Encerrando ...')
        sleep(1)
        break