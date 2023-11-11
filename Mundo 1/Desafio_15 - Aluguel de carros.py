# Calcular quantidade de km percorrido por um carro alugado
# e a quantidade de dias pelo quais ele foi alugado.
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias_alugado = int(input('Quantos dias foi alugado? '))
km_percorrido = float(input('Quantos km rodados? '))

total_pago = (dias_alugado * 60) + (km_percorrido * 0.15)

print('O total a ser pago é de R${:.2f}'.format(total_pago))
