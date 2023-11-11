""" Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas e minúsculas.
Quantas letras ao todo (sem considerar espaços).
Quantas letras tem o primeiro nome. """

nome = str(input('Digite seu nome: ')).strip()
separa = nome.split()
print('Seu nome em maiusculo: {}'.format(nome.upper()))
print('Seu nome em minusculo: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras '.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))
