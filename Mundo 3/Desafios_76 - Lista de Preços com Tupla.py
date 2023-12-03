'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''
from prettytable import PrettyTable
lista = (
    ('Camiseta', 25.00),
    ('Calça Jeans', 49.99),
    ('Relógio', 125.87),
    ('Smartphone', 955.42),
    ('Livro', 86.00),
    ('Fone de Ouvido', 99.00),
    ('Headset', 100.00),
    ('Óculos de sol', 115.00),
    ('Jogo de faca', 78.00),
    ('Notebook', 3064.00)
)
tabular = PrettyTable(['Produto', 'Valor'])
tabular.align['Produto'] = 'l'
tabular.align['Valor (R$)'] = 'r'

for produto, valor in lista:
    tabular.add_row([produto, f'R$ {valor:.2f}'])

print(f'{"Lista de produtos":^35}')
print(tabular)
