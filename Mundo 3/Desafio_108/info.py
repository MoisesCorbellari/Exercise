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
print(f'\nValor analisado: {moeda.moeda(p)}\n')

print(f'-> O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'-> A metade de {moeda.moeda(p)}, é {moeda.moeda(moeda.metade(p))}')
print(f'-> Com aumento de {moeda.tx(taxa)} sobre o valor de {moeda.moeda(p)}, fica em {moeda.moeda(moeda.aumento(p, taxa))}')
print(f'-> Com a diminuição de {moeda.tx(taxa)} sobre o valor de {moeda.moeda(p)}, fica em {moeda.moeda(moeda.diminuir(p, taxa))}\n')
