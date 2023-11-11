# Criar um programa que leia um número real qualquer pelo teclado
# e mostre sua porção inteira.

from math import trunc
n1 = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua parte inteira é {}'.format(n1, trunc(n1)))
