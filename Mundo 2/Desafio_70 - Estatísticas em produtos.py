# Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar ou não. 
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print('{: ^60}'.format(' Estatística em Produtos! '))
tot = maior_mil = cont = menos = 0
prod_barato = ''
produto = ''
caro = ''
while True:
    print('{:=^60}'.format(''))
    nome = str(input('Qual o nome do produto? ')).strip().upper()
    valor = float(input('Digite o preço do produto: R$'))
    cont += 1
    tot += valor

    if  valor > 1000:
        maior_mil += 1
        produto = valor
        caro = nome
    if cont == 1 or valor < menos:
        menos = valor
        prod_barato = nome
    
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Continuar? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
        break

print('{:_^60}'.format(' Programa Finalizado! '))

print(f'Total gasto: R${tot:.2f}')
print(f'Quantos produtos custam mais de R$1000? {maior_mil}')
print(f'Qual o produto mais caro? {caro}, e seu valor é de R${produto}')
print(f'Qual o roduto mais barato? {prod_barato}, e seu valor é de R${menos:.2f}')
