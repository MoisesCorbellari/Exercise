# Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
vitoria = 0

while True:
    num = int(input('Digite um número: '))
    comp = randint(0,10)
    soma = num + comp
    esc = ' '
    while esc not in 'PI':
        esc = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Usuário jogou {num} e o Computador jogou {comp}. Total de {soma} -> Resultado: ', end='')
    print('PAR' if soma % 2 == 0 else 'IMPAR')
    if esc == 'P':
        if soma % 2 == 0:
            print('VENCEU!')
            vitoria += 1
        else:
            print('PERDEU!')
            break
    elif esc == 'I':
        if soma % 2 == 1:
            print('VENCEU!')
        else:
            print('PERDEU!')
            break
    print('Jogar Novamente...')
print(f'GAME OVER! Nº de vitórias: {vitoria}.')
