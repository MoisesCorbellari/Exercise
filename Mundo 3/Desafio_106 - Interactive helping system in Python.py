'''
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
Importante: use cores.
'''
from time import sleep
import os

c = (
        '\033[31m', # red
        '\033[32m', # green
        '\033[33m', # orange
        '\033[34m', # blue
        '\033[35m', # purple
        '\033[93m', # yellow
        '\033[95m', # pink
        '\033[0m'   # reset
)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def title(msg, cor=0):
    tmh = len(msg) + 4
    print(c[cor], end='')
    print(f'\n            {msg.center(tmh, " ")}\n')
    print(c[7], end='')
    sleep(1)
clear()
def helpDesk(comm):
    title(f'Acessando o manual do comando \'{comm}\'', 5)
    print(c[3], end='')
    help(comm)
    print(c[4], end='')
    sleep(2)
clear()
cmd = ''
while True:
    print
    title('Sistema de ajuda', 2)
    cmd = str(input('Função ou Biblioteca: '))
    if cmd.upper() == 'SAIR':
        break
    else:
        helpDesk(cmd)
title('Até breve', 1)