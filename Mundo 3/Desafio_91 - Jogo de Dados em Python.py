'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. 
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
from random import randint
from time import sleep

player = {}
count = 0
print(' '*5 + "Resultados: ")
for p in range(4):
    sleep(1)
    dado = randint(1,6)
    player[f'jogador {p + 1}'] = dado
    print(f'O player {p + 1} tirou {dado} pontos no dado.')
print('='*40)
print(' '*5 + "Ranking dos resultados: ")
p_list = sorted(list(zip(player.values(),player.keys())), reverse=True)

for i, players in enumerate(p_list):
    sleep(1)
    print(f'{i+1}º lugar: {p_list[i][1]} com {p_list[i][0]} pontos.')
    count += 1