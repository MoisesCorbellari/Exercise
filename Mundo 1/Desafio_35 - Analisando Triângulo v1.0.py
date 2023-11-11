#Desenvolva um programa que leia o comprimento de três retas 
# e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Primeira medida: '))
r2 = float(input('Segunda medida: '))
r3 = float(input('Terceira medida: '))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('O comprimento das retas podem formar um triângulo!')
else:
    print('Não podem formar um triângulo!')
