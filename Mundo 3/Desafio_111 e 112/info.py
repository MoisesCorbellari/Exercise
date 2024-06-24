from utilidadeCEV import moeda
from utilidadeCEV import dados

moeda.title('Analisando valores\n')

p = dados.leiaDinheiro('Digite um valor: R$')
taxa = float(input('Digite a taxa (em "%"): ').replace(',', '.'))

moeda.resumo(p, taxa)