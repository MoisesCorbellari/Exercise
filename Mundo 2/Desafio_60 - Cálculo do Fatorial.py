# Faça um programa que leia um número qualquer e mostre o seu fatorial. 
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('Digite um valor: '))
cont = num
fat = 1
print('Calculando fatorial de {}! = '.format(num), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x 'if cont > 1 else ' = ', end='')
    fat *= cont
    cont -= 1
print('{}.'.format(fat))
