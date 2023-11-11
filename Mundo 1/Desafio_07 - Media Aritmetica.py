# Criar um programa que lê duas notas de um aluno
# e mostre sua média.

nome = input('Informe seu nome: ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A média do aluno {} é {}.'.format(nome, m))