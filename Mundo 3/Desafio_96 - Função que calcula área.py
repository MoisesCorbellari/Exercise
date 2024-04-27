'''Faça um programa que tenha uma função chamada área(), 
que receba as dimensões de um terreno retangular 
(largura e comprimento) e mostre a área do terreno.'''

def mensagem(msg):
    tm = len(msg) + 25
    print(f'{msg:>25}')
    print('-'*tm)

def area(l, c):
    calc = l*c
    print(f'\nAs dimensões de um terreno {l}x{c} é de {calc:.2f}m².')

mensagem('Cálculo de área')
larg = float(input('Digite a largura do terreno (m): '))
comp = float(input('Digite o comprimento do terreno(m): '))
area(larg,comp)