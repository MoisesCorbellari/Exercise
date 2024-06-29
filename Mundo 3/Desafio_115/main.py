from libs.screen import *
from libs.archive import *
from time import sleep
from progress.spinner import Spinner

dados = 'info.txt'
if not existe(dados):
    criar(dados)

clear()
title('Sistema de cadastro de pessoas')
sleep(3)
clear()

while True:
    resp = menu(['Cadastrar', 'Visualizar Cadastro', 'Sair'])
    if resp == 1:
        clear()
        title('Cadastrando Informação')
        nome = str(input('Nome: ')).capitalize().strip()
        idade = leiaInt('Idade: ')
        cadastrar(dados, nome, idade)
    elif resp == 2:
        clear()
        ler(dados)
    elif resp == 3:
        with Spinner('\033[36mSaindo do sistema\033[0m ') as bar:
            for _ in range(50):
                sleep(0.04)
                bar.next()
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[0m')
    sleep(2)