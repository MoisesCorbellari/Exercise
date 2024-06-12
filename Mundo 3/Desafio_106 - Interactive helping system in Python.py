'''
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
Importante: use cores.
'''
from time import sleep
import os

c = (
        '\033[97m', # 0 - white
        '\033[92m', # 1 - green
        '\033[96m', # 2 - cyan
        '\033[35m', # 3 - magenta
        '\033[93m', # 4 - yellow
        '\033[31m'  # 5 - pink
)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def title(txt, cor=0):
    tmh = len(txt) + 4
    print(c[cor], end='')
    print(f'\n            {txt.center(tmh, " ")}\n')
    print(c[0], end='')
    sleep(1)
clear()
def helpDesk(prompt):
    title(f'Acessando o manual do comando \' {prompt} \'', 4)
    print(c[2], end='')
    help(prompt)
    print(c[5], end='')
    sleep(2)
clear()
cmd = ''
while True:
    title('Sistema de ajuda', 1)
    cmd = str(input('Função ou Biblioteca: '))
    if cmd.upper() == 'SAIR':
        break
    else:
        helpDesk(cmd)
title('Até breve!', 5)