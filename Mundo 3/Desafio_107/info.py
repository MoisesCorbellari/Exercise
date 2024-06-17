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
        print('\033[31mEntrada inválido! Digite um número.\033[0m')
print(f'\nValor analisado: R${p:.2f}\n')

print(f'-> O dobro de R${p:.2f} é R${moeda.dobro(p):.2f}')
print(f'-> A metade de R${p:.2f}, é R${moeda.metade(p):.2f}')
print(f'-> Aumentando em {taxa}% o valor de R${p:.2f}, fica em R${moeda.aumento(p, taxa):.2f}')
print(f'-> Diminuindo em {taxa}% o valor de R${p:.2f}, fica em R${moeda.diminuir(p, taxa):.2f}\n')