# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pess in range(1,8):
    nasc = int(input('Digite o ano de nascimento da {}ª: '.format(pess)))
    if atual - nasc >= 18:
        maior += 1
    elif atual - nasc < 18:
        menor += 1
print('Temos: \n{} maiores de idade \n{} menores de idade.'.format(maior,menor))