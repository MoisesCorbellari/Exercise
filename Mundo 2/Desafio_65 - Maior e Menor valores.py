# Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

print('*'*50)
print('        Maior & Menor valores!        ')
print('*'*50)
quant = media = maior = menor = soma = 0
esc = ''
while esc != 'N':
    v1 = int(input('Digite um valor: '))
    soma += v1
    quant += 1
    if quant == 1:
        maior = menor = v1
    else:
        if v1 > maior:
            maior = v1
        if v1 < menor:
            menor = v1
    esc = str(input('Continuar [S/N]: ')).upper().strip()[0]
media = soma / quant
print('\nNúmeros digitados: {} \nMédia: {:.2f}.'.format(quant,media))
print('Maior valor: {} \nMenor valor: {}'.format(maior,menor))
