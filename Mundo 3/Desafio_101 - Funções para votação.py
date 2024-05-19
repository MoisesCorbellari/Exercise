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
        return f' com {idade} anos seu voto é OPCIONAL.'
    elif idade < 16:
        return f'com {idade} anos você não está HABILITADO(A) para votar.'
    else:
        return f'com {idade} anos seu voto é OBRIGATÓRIO.'
# main program
title('SISTEMA DE VERIFICAÇÃO DE VOTO')

while True:
    nome = input('\nInforme seu nome: ').strip().capitalize()
    while True:
        try:
            ano = int(input('Ano de nascimento: '))
            ano_atual = date.today().year
            if ano > ano_atual or ano < 1900:
                print('\nAno inválido. Tente novamente.\n')
                continue
            break
        except ValueError:
            print('\nEntrada inválida. Tente novamente.\n')
            
    with MoonSpinner('Processando informação ... ') as bar:
        for _ in range(50):
            sleep(0.04)
            bar.next()

    print(f'\n{nome}, {voto(ano)}')
    resp = input('\nDeseja sair? ("S" para sim, e "N" para não.): ').strip().upper()[0]
    linha()
    if resp == 'S':
        print(f'\n{'Volte sempre! ...':>40}\n')
        sleep(1)
        break