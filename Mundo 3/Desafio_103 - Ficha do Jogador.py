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

def limpar():
        os.system('cls' if os.name == 'nt' else 'clear')
        
def line():
        print('-'*70)

def title(txt):
    msg = len(txt) + 50
    print(f'{txt:>40}')
    print('-'*msg)

def ficha(nome='Desconhecido', gols=0):
        """
        O programa permite o cadastro de jogadores de futebol, resgistrando seus nomes e gols marcados.
        São armazenados em uma lista de dicionários, e o usuário pode continuar cadastradando até decidir parar.
        Após o termino do cadastro, é exibida uma lista de todos os jogadores e suas informações.

        Funções:
                - limpar(): limpa a tela do console após a finalização do programa.
                - line(): imprime uma linha de separação com 70 caracteres.
                - title(txt): imprime um titulo centralizado com uma linha de separação.
                - ficha(nome='Desconhecido', gols=0): função que recebe dois parâmetros opcionais.
        Programa principal:
                1 Exibe o título "Cadastro do Jogador".
                2 Inicia o loop para cadastro de jogadores:
                 - Solicita o nome do jogador e os gols marcados.
                 - Caso o nome e gols do jogador não for fornecidos, atribui "Desconhecido" e 0.
                 - Valida se os gols marcados é um numero inteiro.
                 - Adiciona o jogador à lista de jogadores.
                 - Exibe a ficha do jogador cadastrado.
                 - Pergunta ao usuário se deseja continuar (S/N).
                3 Exibe um spinner de carregamento, após a saída do loop.
                4 A função "limpar" é executada e exibe a ficha de todos os jogadores cadastrados.
        Libs usadas:
                - time: executar pausas por breves intervalos.
                - progress.spinner: exibe um spinner de carregamento, simulando o carregamento das infos.
                - os: para executar comandos do sistema operacional
        """
        
        print(f'\nCadastro Realizado com sucesso.\nNome: {nome} \nGols: {gols}')

jogadores = list()
count_id = 1

title('Cadastro do Jogador')

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
                with MoonSpinner('Carregando às informações ... ') as bar:
                        for _ in range(50):
                                sleep(0.04)
                                bar.next()
                break
limpar()
title('Ficha dos Jogadores')
print(f'{"id":<5}{"Nome":<15}{"Gols":<25}')
for jogador in jogadores:
        print(f'{jogador["id"]:<5}{jogador["Nome"]:<15}{jogador["Gols"]:<25}')