# Programa que leia qualquer ângulo qualquer
# e mostre o valor em Seno, Cosseno e Tangente.

from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo: '))

seno = sin(radians(ang))
print('O ângulo de {}° tem o seno de {:.2f}'.format(ang, seno))

cosseno = cos(radians(ang))
print('O ângulo de {}° tem o cosseno de {:.2f}'.format(ang, cosseno))

tangente = tan(radians(ang))
print('O ângulo de {}° tem a tangente de {:.2f}'.format(ang, tangente))
