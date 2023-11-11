# Faça um programa que ajude o professor sortear um aluno
# para apagar o quadro.

from random import choice
a1 = str(input('Informe o primeiro aluno: '))
a2 = str(input('Informe o segundo aluno: '))
a3 = str(input('Informe o terceiro aluno: '))
a4 = str(input('Informe o quarto aluno: '))
lista = [a1, a2, a3, a4]
sorteado = choice(lista)
print('A pessoa escolhida foi {}'.format(sorteado))
