# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.

a1 = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('Digite a razão da P.A.: '))
n = int(input('Digite a posição do termo da P.A.: '))
an = a1 + (n - 1) * r
for c in range(a1,an+r,r):
    f = a1 + r
    print(c, end=' 🠒 ')
print('FIM.')
