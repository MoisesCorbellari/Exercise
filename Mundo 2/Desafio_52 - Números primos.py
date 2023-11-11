# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um número: '))
t = 0
for c in range(1,num + 1):
    if num % c == 0:
        print('\033[32m', end=' ')
        t += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi dividido {} vezes'.format(num,t))
if t == 2:
    print('É PRIMO!')
else:
    print('NÃO É PRIMO!')
