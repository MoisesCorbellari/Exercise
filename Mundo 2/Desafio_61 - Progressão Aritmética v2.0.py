# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('''
                        Gerando PA
      ''')
print('='*60)
a1 = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('Digite a razão da P.A.: '))
n = int(input('Digite a posição do termo da P.A.: '))
cont = 1
while cont <= n:
    print('{} 🠒 '.format(a1), end='')
    a1 += r
    cont += 1
print('FIM!')
