# Algoritmo que lê o preço de um produto e mostra seu novo preço,
# com x% de desconto.

produto1 = float(input('Digite o valor do produto 1: R$ '))
produto2 = float(input('Digite o valor do produto 2: R$ '))
produto3 = float(input('Digite o valor do produto 3: R$ '))

desconto1 = produto1 * 0.05
valor1 = produto1 - desconto1
print('O valor do produto 1 com desconto é de R${}'.format(valor1))

desconto2 = produto2 * 0.10
valor2 = produto2 - desconto2
print('O valor do produto 2 com desconto é de R${}'.format(valor2))

desconto3 = produto3 * 0.15
valor3 = produto3 - desconto3
print('O valor do produto 3 com desconto é de R${}'.format(valor3))
