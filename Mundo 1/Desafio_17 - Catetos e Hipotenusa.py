# Programa que lê o comprimento do cateto oposto e adjacente de um triâgulo retângulo
# e calcula o comprimento da hipotenusa.

from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hip = hypot(co, ca)
print('A hipotenusa vale: {:.2f}'.format(hip))
