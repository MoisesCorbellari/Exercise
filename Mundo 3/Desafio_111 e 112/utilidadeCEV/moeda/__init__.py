def aumento(preco=0, taxa=0, formato=False):
    calc = preco + (preco * taxa/100)
    return calc if not formato else coin(calc)

def diminuir(preco=0, taxa=0, formato=False):
    calc = preco - (preco * taxa/100)
    return calc if not formato else coin(calc)

def dobro(preco=0, formato=False):
    calc = preco * 2
    return calc if not formato else coin(calc)

def metade(preco=0, formato=False):
    calc = preco / 2
    return calc if not formato else coin(calc)

def coin(preco=0, coin='R$'):
    return f'{coin}{preco:,.2f}'.replace('.', '#').replace(',', '.').replace('#', ',')

def tx(taxa=0):
    return f'{taxa:.2f}%'.replace('.', ',')

def title(txt, larg=70):
    print('-' * larg)
    print(f'{txt:^{larg}}')

def resumo(preco=0, taxa=0):
    print()
    title('Resumo da análise\n')
    print(f'Preço analisado: \t{coin(preco)}')
    print(f'Taxa informada: \t{tx(taxa)}\n')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Aumento de {tx(taxa)}: \t{aumento(preco, taxa, True)}')
    print(f'Redução de {tx(taxa)}: \t{diminuir(preco, taxa, True)}\n')