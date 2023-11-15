''' Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
e o programa vai informar quantas cédulas de cada valor serão entregues. 
OBS:considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1 '''

from time import sleep
from datetime import datetime
from tqdm import tqdm

def limpar_tela():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

print('{: ^60}'.format(' Bem-vindo ao Python Bank! '))

sleep(3)
limpar_tela()

cliente = input('Digite seu nome completo: ').strip().title()
conta = input('Insira o número da conta, com digito: ')
print(f'        Olá {cliente}, Seja Bem-Vindo ao banco!      ')

for i in tqdm(range(0, 100), desc='INICIANDO SISTEMA', ascii=True): sleep(.0140)

limpar_tela()

print(''' Cédulas disponíveis:

            R$50,00
            R$20,00
            R$10,00
            R$1,00 
      ''')
cedula = int(input('Qual valor deseja sacar? '))
quant = cedula
ced = 50
tot = 0

print('Aguarde a contagem das notas...')
sleep(5)

while True:
    if quant >= ced:
        quant -= ced
        tot += 1
    else:
        if tot > 0:
            print(f'São {tot} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tot = 0
        if quant == 0:
            break

now = datetime.now().hour

if now > 12:
    now = 'Tenha uma ótima tarde!'
elif now > 18:
    now = 'Tenha uma ótima noite!'
else:
    now = 'Tenha um ótima dia!'

print(f'\nVocê sacou R${cedula:.2f} \nO Python Bank agradece pela preferência. \n{now}')
