''' Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
    Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso. '''

val = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
        'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze', 
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numb = int(input('Digite um número entre 0 a 20: '))
    if 0 <= numb <= 20:
        break
    else:
        print('Valor inválido.', end=' ')
print(f'O número digitado foi: {val[numb]}.'.title())