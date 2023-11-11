# Programa que lê quanto dinheiro uma pessoa tem na carteira 
# e mostra quantos dólares pode comprar.

real = float(input('Quantos reais você possui? R$'))
dolar = real / 4.87
print('Com R${:.2f}, é possível comprar Us${:.2f}.'.format(real, dolar))
