'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''

valor = tuple(int(input(f'Digite o {i + 1}º valor: '))for i in range(4))
quantNum = valor.count(9)
posNum = valor.index(3) if 3 in valor else None
parNum = tuple(x for x in valor if x % 2 == 0)
print(f'A) Quantas vezes apareceu o valor 9: {quantNum} vezes')
print(f'B) Em que posição foi digitado o primeiro valor 3: {posNum}ª')
print(f'C) Quais foram os números pares: {parNum}')
