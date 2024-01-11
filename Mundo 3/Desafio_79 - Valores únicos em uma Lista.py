'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
from time import sleep
cadNum = list()
while True:
    num = int(input('Digite um valor para cadastro: '))
    if num not in cadNum:
        cadNum.append(num)
        print('Valor cadastrado!')
    else:
        print('Valor já cadastrado!')
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        sleep(1)
        break
cadNum.sort()
print('=' * 30)
print(f'Valores que você cadastrou:\n{cadNum}')