'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
while True:
    print('''            
            [1] Somar
            [2] Subtrair 
            [3] Multiplicar
            [4] Dividir
            [5] Maior
            [6] Novos Números
            [7] Sair            
        ''')
    seleciona = int(input('Selecione uma opção: '))
    if seleciona == 1:
        soma = v1 + v2
        print('O resultado da soma dos valores {} e {}, é {}'.format(v1,v2,soma))
    elif seleciona == 2:
        subtrair = v1 - v2
        print('O resultado da subtração dos valores {} e {}, é {}'.format(v1,v2,subtrair))
    elif seleciona == 3:
        multiplicar = v1 * v2
        print('O resultado da multiplicação dos valores {} e {}, é {}'.format(v1,v2,multiplicar))
    elif seleciona == 4:
        dividir = v1 / v2
        print('O resultado da divisão dos valores {} e {}, é {:.2f}'.format(v1,v2,dividir))
    elif seleciona == 5:
        if v1 > v2:
            print('O maior número digitado foi {}.'.format(v1))
        else:
            print('O maior número digitado foi {}.'.format(v2))
    elif seleciona == 6:
        v1 = int(input('1) Insira o novo valor: '))
        v2 = int(input('2) Insira o novo valor: '))
    elif seleciona == 7:
        print('Encerrando aplicação...')
        break
    else:
        print('OPÇÃO INVÁLIDA!')
    print('='*50)
    sleep(1.5)
print('Volte sempre!')
