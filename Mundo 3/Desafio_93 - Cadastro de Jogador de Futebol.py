'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. No final, 
tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

jogador = dict()
gols = list()
soma = 0

jogador['nome'] = str(input('Nome do jogador: ')).capitalize().strip()
partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
for c in range(1, partidas+1):
    gols.append(int(input(f'    Quantos gols na partida {c}: ')))

jogador['gols'] = gols
for i in gols:
    soma += i
    jogador['total'] = soma
print('-='*30)
print(jogador)
print('-='*30)
print(' '*5 + "Resultados:\n")
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.\n')

for p, g in enumerate(jogador['gols']):
    print(f'    Na {p+1}ª partida, ele fez {g} gols.')
print(f'\nFoi um total de {jogador["total"]} gols.')
print()
