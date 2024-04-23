'''Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

from time import sleep

jogador = dict()
partidas = list()
time = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize().strip()
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(1, jogador['partidas']+1):
        partidas.append(int(input(f'    Quantos gols na partida {c}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar [S/N]? ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print(f'{"id":<5}{"nome":<15}{"gols":<25}{"total":<10}')
print('-'*60)
for k, v in enumerate(time):
    print(f'{k:<5}{v["nome"]:<15}{str(v["gols"]):<25}{v["total"]:<10}')
print('-='*45)
while True:
    info = int(input('Digite o "id" para mostrar os dados (para sair, digite 999, e pressione "enter"): '))
    if info == 999:
        print('Encerrando...')
        sleep(1)
        break
    if info >= len(time):
        print(f'ERRO! Não existe jogador com id {info}.')
    else:
        print('-='*45)
        print(f'{"INFORMAÇÕES DO JOGADOR - " + time[info]["nome"]:^40}\n')
        for i, g in enumerate(time[info]['gols']):
            print(f'      No {i+1}º jogo {time[info]["nome"]} fez {g} gols.')
    print('-='*45)