'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import datetime

funcionario = {}
ano_atual = datetime.now().year
funcionario['Nome'] = str(input('Informe o nome: ')).capitalize().strip()
nascimento = int(input('Informe o ano de nascimento: '))
funcionario['Idade'] = ano_atual - nascimento
funcionario['ctps'] = int(input('Número da CTPS (caso não tenha, digite 0): '))
if funcionario['ctps'] > 0:
    funcionario['Contratação'] = int(input('Informe o ano de contratação: '))
    funcionario['Salário'] = float(input('Salário: R$'))
    funcionario['Aposentadoria (em anos)'] = funcionario['Idade'] + ((funcionario['Contratação'] + 35) - datetime.now().year)
print('='*60)
for k, v in funcionario.items():
    if k == 'ctps':
        if v == 0:
            print('Não tem carteira de trabalho.')
    else:
        print(f'{k}: {v}')
print()
