def aumento(preco=0, tx=0):
    calc = preco + (preco * tx/100)
    return calc

def diminuir(preco=0, tx=0):
    calc = preco - (preco * tx/100)
    return calc

def dobro(preco=0):
    return preco * 2

def metade(preco=0):
    return preco / 2

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

def tx(taxa=0):
    return f'{taxa:.2f}%'.replace('.', ',')

def title(txt):
    print(f'{txt:^70}')