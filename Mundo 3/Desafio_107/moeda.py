def aumentar(preco, tx):
    pValor = preco * (tx/100)
    return preco + pValor

def diminuir(preco, tx):
    pValor = preco * (tx/100)
    return preco - pValor

def dobro(preco):
    return preco * 2

def metade(preco):
    return preco / 2

def title(txt):
    print(f'{txt:^70}')