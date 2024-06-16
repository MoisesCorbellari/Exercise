import moeda

moeda.title('Analise de valor\n')

p = float(input('Digite um valor: '))
print(f'Valor analisado: R${p:.2f}\n')

print(f'-> O dobro de R${p:.2f} é R${moeda.dobro(p):.2f}')
print(f'-> A metade de R${p:.2f}, é R${moeda.metade(p):.2f}')
print(f'-> Aumentando em 20% o valor de R${p:.2f}, fica em R${moeda.aumentar(p, 20):.2f}')
print(f'-> Diminuindo em 72% o valor de R${p:.2f}, fica em R${moeda.diminuir(p, 72):.2f}\n')