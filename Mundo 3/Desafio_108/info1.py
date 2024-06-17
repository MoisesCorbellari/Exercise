import coin

coin.title('Analise de valor\n')

while True:
    try:
        p = float(input('Digite um valor: R$'))
        break
    except ValueError:
        print('\033[31mEntrada inválido! Digite um número.\033[0m\n')
while True:
    try:
        taxa = float(input('Informe a taxa (em porcentagem " % "): '))
        if taxa >= 0:
            break
        else:
            print('\033[31mTaxa não pode ser negativa!\033[0m\n')
    except ValueError:
        print('\033[31mEntrada inválido! Digite um número.\033[0m')
print(f'\nValor analisado: {coin.moeda(p)}\n')

print(f'-> O dobro de {coin.moeda(p)} é {coin.moeda(coin.dobro(p))}')
print(f'-> A metade de {coin.moeda(p)}, é {coin.moeda(coin.metade(p))}')
print(f'-> Aumentando em {coin.tx(taxa)} o valor de {coin.moeda(p)}, fica em {coin.moeda(coin.aumento(p, taxa))}')
print(f'-> Diminuindo em {coin.tx(taxa)} o valor de {coin.moeda(p)}, fica em {coin.moeda(coin.diminuir(p, taxa))}\n')