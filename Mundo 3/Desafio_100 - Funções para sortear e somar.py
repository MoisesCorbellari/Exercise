''' Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai 
mostrar a soma entre todos os valores pares sorteados pela função anterior. '''

from random import randint
from time import sleep

def sortear(lista):
    print('Sorteando 5 valores:')
    for _ in range(5):
        nums = randint(1, 10)
        lista.append(nums)
        sleep(1)
        print(nums, end='  ')
    print('\nFim!')

def soma_par(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'\nResultado da soma dos pares {lista}: {soma}\n')

nums = []
sortear(nums)
soma_par(nums)