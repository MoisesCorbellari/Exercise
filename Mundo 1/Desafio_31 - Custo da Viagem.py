# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = float(input('Informe a distancia da viagem, em km: '))
abaixo = km * 0.50
acima = km * 0.45
if km <= 200:
    print('Você pagará R${:.2f} pela viagem abaixo de 200km.'.format(abaixo))
else:
    print('O valor da viagem ficará em R${:.2f}, acima de 200km.'.format(acima))
