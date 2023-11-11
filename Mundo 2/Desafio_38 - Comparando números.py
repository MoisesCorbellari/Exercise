# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
if num1 > num2:
    print('O PRIMEIRO valor é maior.')
elif num1 < num2:
    print('O SEGUNDO valor é maior.')
else:
    print('Não existe valor maior, os dois valores são iguais.')
