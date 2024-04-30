'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''
from time import sleep

def linha():
    print('-'*40)


def cont(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contando de {inicio} até {fim}, de {passo} em {passo}:')
    if inicio <= fim:
        for c in range(inicio, fim+1, passo):
            sleep(1)
            print(f'{c}', end=' ')
        print('\nFim!')
    else:
        for c in range(inicio, fim-1, -passo):
            sleep(1)
            print(f'{c}', end=' ')
        print('\nFim!')
    linha()


#Programa principal
linha()
cont(1,10,1)
cont(10,0,2)
print('Personalize a contagem!')
inicio = int(input('Início: '))
fim = inicio
while fim <= inicio:
    fim = int(input('Fim: '))
    if inicio < fim:
        print('Inicio não pode ser menor que fim!')
    else:
        break
passo = int(input('Passo: '))
if passo == 0:
    passo = 1
cont(inicio, fim, passo)