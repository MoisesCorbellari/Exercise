# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
# desconsiderando os espaços.

palin = str(input('Digite uma palavra: ').upper().replace(' ','.'))
if palin == palin[:: -1]:
    print('\033[32mÉ um palíndromo.')
else:
    print('\033[31mNão é um palíndromo.')
print('\033[mPalavra digitada: {}.'.format(palin))
