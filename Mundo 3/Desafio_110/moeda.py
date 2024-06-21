def aumento(preco=0, taxa=0, formatar=False):
    calc = preco + (preco * taxa/100)
    return calc if not formatar else coin(calc)

def diminuir(preco=0, taxa=0, formatar=False):
    calc = preco - (preco * taxa/100)
    return calc if not formatar else coin(calc)

def dobro(preco=0, formatar=False):
    calc = preco * 2
    return calc if not formatar else coin(calc)

def metade(preco=0, formatar=False):
    calc = preco / 2
    return calc if not formatar else coin(calc)

def coin(preco=0, coin='R$'):
    return f'{coin}{preco:.2f}'.replace('.', ',')

def tx(taxa=0):
    return f'{taxa:.2f}%'.replace('.', ',')

def title(txt, larg=70):
    print(f'{txt:^{larg}}')

def resumo(preco=0, taxa=0):
    print()
    title('Resumo da análise\n')
    print(f'Preço analisado: {coin(preco)}')
    print(f'Taxa informada: {taxa:.2f}%\n')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Aumento de {taxa:.2f}%: \t{aumento(preco, taxa, True)}')
    print(f'Redução de {taxa:.2f}%: \t{diminuir(preco, taxa, True)}\n')
