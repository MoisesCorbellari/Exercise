'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta.'''

from random import randint
from time import sleep
from rich.progress import Progress

palpites = []
print('_'*40 + f'\n{"MEGA SENA":^35}\n' + '_'*40)
qtjogos = int(input('\nQuantos jogos é para fazer? '))
with Progress() as progress:
    task = progress.add_task("[white]Gerando jogos...", total=qtjogos)
    print()

    for c in range(qtjogos):
        jogo = []
        for valores in range(6):
            sortear = randint(1,60)
            if sortear in jogo:
                sortear = randint(1,60)
                jogo.append(sortear)
            else:
                jogo.append(sortear)
        jogo.sort()
        palpites.append(jogo)
        progress.update(task, advance=1)
        sleep(.8)
        print(f'Jogo {c+1}: {palpites[c]}')
        sleep(.7)
    
    print('\n' + f'{"  BOM JOGO  ":^35}' + '\n')
