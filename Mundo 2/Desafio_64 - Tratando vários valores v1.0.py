# Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

valor = soma = cont = 0
valor = int(input('Informe um valor [999 para finalizar]: '))
while True:
    if valor != 999:
        soma += valor
        cont += 1
        valor = int(input('Informe um valor [999 para finalizar]: '))
    else:
        break
print('Finalizado!','\n')
print('Números digitados: {} \nSoma entre os números digitados: {}'.format(cont,soma))
