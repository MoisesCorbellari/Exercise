# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_imovel = float(input('Informe o valor da casa: '))
salario = float(input('Informe seu salário: '))
tempo = int(input('Informe em quantos anos irá pagar o empréstimo: '))
prest_men = valor_imovel / (tempo * 12)
if prest_men <= salario*30/100:
    print('APROVADO!')
else:
    print('NEGADO!')
print('Para pagar o valor do imovel de R${:.2f}, em {} anos, \nas parcelas serão de R${:.2f}'.format(valor_imovel, tempo, prest_men))
