'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint

print('''
      
      Maior e Menor Valores em Tupla
      
      ''')

numAleatorio = tuple(randint(1,101)for _ in range(5))
menor_valor = min(numAleatorio)
maior_valor = max(numAleatorio)
print(f'Números gerados: {numAleatorio}')
print(f'Menor número gerado: {menor_valor}')
print(f'Maior número gerado: {maior_valor}')
