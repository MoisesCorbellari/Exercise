# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

input('Digite seu nome: ')
genero = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

while genero not in 'M/F':
    genero = str(input('Inválido! Insira a informação novamente: ')).strip().upper()[0]
    
print('Registrado com sucesso!')