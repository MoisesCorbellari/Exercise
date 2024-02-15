'''
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

from time import sleep
tmp = []
pessoas = []
mai = men = 0
while True:
    tmp.append(str(input('Digite seu nome: ')))
    tmp.append(float(input('Digite seu peso: ')))
    if len(pessoas) == 0:
        mai = men = tmp[1]
    else:
        if tmp[1] > mai:
            mai = tmp[1]
        if tmp[1] < men:
            men = tmp[1]
    pessoas.append(tmp[:])
    tmp.clear()
    rsp = str(input(('Continuar [S/N]? ')))
    print("=" * 40)
    if rsp in 'Nn':
        print('\nEncerrando o programa...\n')
        sleep(1)
        break
print("=" * 40)
print('Resultados da análise:')
print("=" * 40)
print(f'A) Total de pessoas cadastradas: {len(pessoas)}')
print(f'B) Maior peso: {mai}kg', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print(f'\nC) Menor peso: {men}kg', end='')
for p in pessoas:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
        