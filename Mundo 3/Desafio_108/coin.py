def aumento(preco, tx):
    calc = preco + (preco * tx/100)
    return calc

def diminuir(preco, tx):
    calc = preco - (preco * tx/100)
    return calc

def dobro(preco):
    return preco * 2

def metade(preco):
    return preco / 2

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

def tx(valor):
    return f'{valor:.2f}%'.replace('.', ',')

def title(txt):
    print(f'{txt:^70}')