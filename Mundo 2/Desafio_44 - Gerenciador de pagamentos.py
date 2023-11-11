# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço normal 
# – 3x ou mais no cartão: 20% de juros

val_prod = float(input('Informe o valor do produto a ser pago: '))
print('''
        [1] Á vista dinheiro ou cheque: desconto de 10%.
        [2] Á vista no cartão: desconto de 5%.
        [3] Até 2X no cartão: preço nomal.
        [4] 3X ou mais no cartão: Juros de 20%.
''')
opcao = int(input('Escolha a condição desejada: '))
if opcao == 1:
    calc = val_prod - (val_prod * 0.10)
elif opcao == 2:
    calc = val_prod - (val_prod * 0.05)
elif opcao == 3:
    calc = val_prod / 2
    print('Parcelando em 2X, o valor do produto de R${:.2f}, fica no valor de R${:.2f} mensais.'.format(val_prod, calc))
elif opcao == 4:
    calc = val_prod + (val_prod * 0.20)
    parcela = int(input('Informe as parcelas: '))
    n_valor = calc / parcela
    print('Parcelando em {} vezes, o valor fica em R${:.2f} mensais, incluindo os juros.'.format(parcela, n_valor))
if opcao in (1, 2, 3, 4):
    print('Seu produto que custa R${:.2f} sairá no valor final de R${:.2f}, escolhendo a opção {}.'.format(val_prod, calc, opcao))
