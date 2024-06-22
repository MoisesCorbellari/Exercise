import moeda

moeda.title('Analisando valores\n')
while True:
    try:
        p = float(input('Digite um valor: R$'))
        break
    except ValueError:
        print('\033[31mEntrada inválida! Informe um valor\033[0m\n')
while True:
    try:
        tx = float(input('Informe a taxa (em porcentagem " % "): '))
        if tx >= 0:
            break
        else:
            print('\033[31mTaxa não pode ser negativa!\033[0m\n')
    except ValueError:
        print('\033[31mEntrada inválida! Informe um valor\033[0m\n')
moeda.resumo(p, tx)