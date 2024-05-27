'''
Faça um programa que tenha uma função chamada ficha(), 
que receba dois parâmetros opcionais: 
o nome de um jogador e quantos gols ele marcou. 
O programa deverá ser capaz de mostrar a ficha do jogador, 
mesmo que algum dado não tenha sido informado corretamente.
'''

from time import sleep
from progress.spinner import MoonSpinner
import os
from tabulate import tabulate

def limpar():
        os.system('cls' if os.name == 'nt' else 'clear')
        
def line():
        print('-'*70)

def title(txt):
    len(txt) + 50
    print(f'{txt:>40}')

def ficha(nome='Desconhecido', gols=0):
        """
        O programa permite o cadastro de jogadores de futebol, resgistrando seus nomes e gols marcados.
        São armazenados em uma lista de dicionários, e o usuário pode continuar cadastradando até decidir parar.
        Após o termino do cadastro, é exibida uma lista de todos os jogadores e suas informações.

        Funções:
                 - limpar(): para limpar a tela do console
                 - line(): imprime uma linha de separação com 70 caracteres
                 - title(txt): imprime um titulo centralizado
                 - ficha(nome='Desconhecido', gols=0): recebe e exibe a ficha com parâmetros opcionais

        Programa principal:
                1 Exibe o título "Cadastro do Jogador"
                2 Inicia o loop para cadastro de jogadores:
                 - Solicita o nome do jogador e os gols marcados
                 - Caso o nome e gols do jogador não forem fornecidos, atribui "Desconhecido" e 0
                 - Valida se os gols marcados é um numero inteiro
                 - Adiciona o jogador à lista de jogadores
                 - Exibe a ficha do jogador cadastrado
                 - Pergunta ao usuário se deseja continuar (S/N)
                3 Exibe um spinner de carregamento, após a saída do loop
                4 A função "limpar" é executada e exibe a ficha de todos os jogadores cadastrados

        Bibliotecas usadas:
                 - time: para executar pausas por breves intervalos
                 - progress.spinner: para exibir um spinner de carregamento, simulando o carregamento das informações
                 - os: para executar comandos do sistema operacional
                 - tabulate: para gerar uma tabela com as informações inseridas
        """
        
        print(f'\nCadastro Realizado com sucesso.\nNome: {nome} \nGols: {gols}')

jogadores = list()
count_id = 1

title('Cadastro do Jogador\n')

while True:
        jogador = dict()
        jogador['id'] = count_id
        jogador['Nome'] = input('Nome do jogador: ').capitalize().strip()
        jogador['Gols'] = input(f'Quantos gols {jogador["Nome"]} marcou: ').strip()

        if jogador['Nome'] == '':
                jogador['Nome'] = 'Desconhecido'
        if jogador['Gols'] == '':
                jogador['Gols'] = 0

        while True:
                try:
                        jogador['Gols'] = int(jogador['Gols'])
                        break
                except ValueError:
                        print('ERRO! Digite um número inteiro!')
                        jogador['Gols'] = input(f'Quantos gols {jogador["Nome"]} marcou: ').strip()
                        
        jogadores.append(jogador)
        ficha(jogador['Nome'], jogador['Gols'])
        line()
        count_id += 1

        while True:
                resp = input('Quer continuar? (S/N) ').strip().upper()
                print()
                if resp in 'SN':
                        break
                print('ERRO! Digite S ou N !')
        if resp == 'N':
                with MoonSpinner('Carregando tabela ... ') as bar:
                        for _ in range(50):
                                sleep(0.04)
                                bar.next()
                break
        limpar()
        
limpar()
title('Ficha dos Jogadores\n')
print(tabulate(jogadores, 
               headers='keys', # usa as chaves do dicionário como cabeçalhos da tabela
               tablefmt='rounded_grid', # define o formato da tabela
               stralign="center" # centraliza o conteúdo das células
               ))