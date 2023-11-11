# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
# Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
print('*'*50)
print('          Sequência de Fibonacci.          ')
print('*'*50)
term = int(input('Mostrar quantos termos da sequência Fibonacci? '))
elem = 0
fib = 1
print('{} 🠒 {}'.format(elem,fib), end='')
cont = 3
while cont <= term:
    seq = elem + fib
    print(' 🠒 {}'.format(seq), end='')
    elem = fib
    fib = seq
    cont += 1
print(' 🠒 ACABOU!')
