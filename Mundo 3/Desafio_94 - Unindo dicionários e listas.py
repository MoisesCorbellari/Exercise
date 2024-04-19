'''Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
No final, mostre:
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média'''

pessoa = dict()
dados = list()
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).capitalize().strip()
    pessoa['sexo'] = str(input('Informe o sexo [M/F]: ')).upper()[0].strip()
    pessoa['idade'] = int(input('Idade: '))
    while pessoa['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        pessoa['sexo'] = str(input('Informe o sexo [M/F]: ')).upper()[0].strip()
        print()
    dados.append(pessoa.copy())
    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'A) Quantas pessoas foram cadastradas? {len(dados)}')
soma_idade = sum(pessoa['idade'] for pessoa in dados)
media = soma_idade / len(dados)
print(f'B) A média de idade: {media:.2f} anos')
print('C) Uma lista com as mulheres:')
for pessoa in dados:
    if pessoa['sexo'] in 'F':
        print(f"{pessoa['nome']}")
print('D) Uma lista de pessoas com idade acima da média:')
for pessoa in dados:
    if pessoa['idade'] >= media:
        print('     ', end='')
        for k, v in pessoa.items():
            print(f'{k} = {v}; ', end='')
        print()
print('-=' * 30)
print(f'{"< ENCERRADO >":^60}')