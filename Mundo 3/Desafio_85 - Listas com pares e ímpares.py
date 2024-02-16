'''
Crie um programa onde o usuário possa digitar sete valores numéricos 
e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.
'''
num = []
par = []
impar = []
for i in range(7):
    num.append(int(input(f'Digite o {i+1}º valor: ')))
for valor in num:
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
par.sort()
impar.sort()
print('Números pares:', par)
print('Números impares:', impar)
