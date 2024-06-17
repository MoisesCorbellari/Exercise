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

def title(txt):
    print(f'{txt:^70}')