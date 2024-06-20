import moeda

moeda.title('Analise de valor\n')

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
        print('\033[31mEntrada inválido! Digite um número.\033[0m\n')
print()
moeda.title(f'Valor analisado: {moeda.coin(p)}\n')

print(f'-> O dobro de {moeda.coin(p)} é {moeda.dobro(p, True)}.')
print(f'-> A metade de {moeda.coin(p)}, é {moeda.metade(p, True)}.')
print(f'-> Com aumento de {moeda.tx(taxa)} sobre o valor de {moeda.coin(p)}, fica em {moeda.aumento(p, taxa, True)}.')
print(f'-> Com a diminuição de {moeda.tx(taxa)} sobre o valor de {moeda.coin(p)}, fica em {moeda.diminuir(p, taxa, True)}.\n')
