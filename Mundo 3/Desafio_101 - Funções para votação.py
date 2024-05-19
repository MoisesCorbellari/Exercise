'''
Crie um programa que tenha uma função chamada voto() 
que vai receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto 
NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''

from datetime import date # importa a função date para trabalhar com datas
from time import sleep # importa a função sleep para criar um atraso na animação de carregamento
from progress.spinner import MoonSpinner # importa a classe MoonSpinner para criar uma animação de carregamento

def linha():
    print('-'*80) # imprime uma linha com 80 hifens

def title(txt):
    msg = len(txt) + 50 # calcula o tamanho total da mensagem
    print(f'{txt:>40}') # centraliza o texto com padding à direita
    print('-'*msg) # imprime linha de hifens do tamanho da mensagem

def voto(ano): # recebe o ano de nascimento como entrada
    idade = date.today().year - ano # calcula a idade da pessoa subtraindo o ano de nascimento do ano atual
    # utiliza às instruções condicionais para determinar a situação do voto com base na idade:
    if 16 <= idade < 18 or idade > 65:
        return f' com {idade} anos seu voto é OPCIONAL.'
    elif idade < 16:
        return f'com {idade} anos você ainda NÃO POSSUI idade para votar.'
    else:
        return f'com {idade} anos seu voto é OBRIGATÓRIO.'
# main program
title('SISTEMA DE VERIFICAÇÃO DE VOTO')

while True:
    nome = input('\nInforme seu nome: ').strip().capitalize() # pede o nome, remove os espaços e deixa a primeira letra maiúscula 
    while True: # entra em um loop interno para validar o ano de nascimento
        try:
            ano = int(input('Ano de nascimento: ')) # pede o ano de nascimento do usuário
            ano_atual = date.today().year
            if ano > ano_atual or ano < 1900:
                print('\nAno inválido. Tente novamente.\n') # se digitar um ano menor que 1900, vai dar erro e pedir para digitar o ano novamente
                continue
            break
        except ValueError:
            print('\nEntrada inválida. Tente novamente.\n') # se apertar 'enter' sem digitar o ano de nascimento, vai dar erro e pedir para digitar o ano
            
    with MoonSpinner('Processando informação ... ') as bar: # animação de carregamento 
        for _ in range(50):
            sleep(0.04)
            bar.next()

    print(f'\n{nome}, {voto(ano)}') #informa o nome, a idade e situação do voto
    resp = input('\nDeseja sair? ("S" para sim, e "N" para não.): ').strip().upper()
    linha()
    if resp == 'S':
        print(f'\n{"Volte sempre! ...":>40}\n') # caso a resposta seja "sim (S)", o programa encerra exibindo uma mensagem de despedida
        sleep(1)
        break