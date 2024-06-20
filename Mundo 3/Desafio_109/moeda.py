def aumento(preco=0, taxa=0, formatar=False):
    """
    Calcula o aumento de um preço com base em uma taxa percentual.

    :param preco - valor inicial do preço
    :param taxa - taxa de aumento em porcentagem
    :param formato - se True, retorna o valor formatado como moeda
    :return - valor com aumento aplicado, formatado ou não
    """
    calc = preco + (preco * taxa/100)
    return calc if not formatar else coin(calc)

def diminuir(preco=0, taxa=0, formatar=False):
    """
    Calcula a diminuição de um preço com base em uma taxa percentual.

    :param preco - valor inicial do preço
    :param taxa - taxa de diminuição em porcentagem
    :param formato - se True, retorna o valor formatado como moeda
    :return - valor com a diminuição aplicada, formatado ou não
    """
    calc = preco - (preco * taxa/100)
    return calc if not formatar else coin(calc)

def dobro(preco=0, formatar=False):
    """
    Calcula o dobro de um preço.

    :param preco - valor inicial do preço.
    :param formato - se True, retorna o valor formatado como moeda.
    :return - o dobro do valor, formatado ou não.
    """
    calc = preco * 2
    return calc if not formatar else coin(calc)

def metade(preco=0, formatar=False):
    """
    Calcula a metade de um preço.

    :param preco - valor inicial do preço.
    :param formato - se True, retorna o valor formatado como moeda.
    :return - a metade do valor, formatado ou não.
    """
    calc = preco / 2
    return calc if not formatar else coin(calc)

def coin(preco=0, coin='R$'):
    """
    Formata um valor numérico como moeda.

    :param preco - valor a ser formatado.
    :param coin - símbolo da moeda.
    :return - valor formatado como moeda.
    """
    return f'{coin}{preco:.2f}'.replace('.', ',')

def tx(taxa=0):
    """
    Formata uma taxa percentual.

    :param taxa: valor da taxa a ser formatada.
    :return - taxa formatada.
    """
    return f'{taxa:.2f}%'.replace('.', ',')

def title(txt, larg=70):
    """
    Imprime um título centralizado.

    :param txt: texto do título
    """
    print(f'{txt:^{larg}}')