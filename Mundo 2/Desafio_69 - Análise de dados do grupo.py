'''Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

maior_18 = tot_homem = tot_menor_20 = 0
while True:
    print('='*40)
    print('Cadastro de usuários')
    print('='*40)
    idade = int(input('DIgite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        maior_18 += 1
    if sexo == 'M':
        tot_homem += 1
    elif sexo == 'F' and idade < 20:
        tot_menor_20 += 1
    ask = ' '
    while ask not in 'SN':
        ask = input('Continuar? [S/N] ').strip().upper()[0]
    if ask == 'N':
            break
print()
print('Cadastro Finalizado!')
print('='*40)
print(f'Maior de 18 anos: {maior_18}')
print(f'Homens cadastrados: {tot_homem}')
print(f'Mulheres com menos de 20 anos: {tot_menor_20}')
