'''Faça um programa que tenha uma função chamada área(), 
que receba as dimensões de um terreno retangular 
(largura e comprimento) e mostre a área do terreno.'''

def mensagem(msg):
    tm = len(msg) + 50
    print(f'{msg:>40}')
    print('-'*tm)

def area(b, h):
    a = b*h
    print(f'\nAs dimensões da área do terreno de {b} x {h} é de {a:.2f}m².')

mensagem('Cálculo de área')
base = float(input('Qual o valor da base do terreno (m)? '))
altura = float(input('Qual o valor da altura do terreno(m)? '))
area(base,altura)