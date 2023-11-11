# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

r1 = float(input('Primeira medida: '))
r2 = float(input('Segunda medida: '))
r3 = float(input('Terceira medida: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos formam um triângulo: ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO.')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('ISÓSCELES.')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO.')
else:
    print('Não formam um triângulo.')
