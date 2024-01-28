'''
Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.
'''

from time import sleep
nums = set()
par = []
impar = []
while True:
    try:
        num = int(input('Digite um valor(para encerrar digite 0): '))
        if num == 0:
            print('Programa encerrado...')
            sleep(1)
            break
        nums.add(num)
        if num % 2 == 0 and num not in par:
            par.append(num)
        elif num % 2 != 0 and num not in impar:
            impar.append(num)
    except ValueError:
        print('Apenas números inteiros!')
nums = sorted(nums)
par = sorted(par)
impar = sorted(impar)
print('-='*60)
print(f'\nLista completa: \n{nums}')
print(f'\nLista par: \n{par}')
print(f'\nLista impar: \n{impar}\n')
