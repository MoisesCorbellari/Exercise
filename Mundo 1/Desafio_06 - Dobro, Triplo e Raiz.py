# Algoritmo que lê um determinado valor
# e mostra o dobro, triplo e raiz.

num = int(input('Digite um valor: '))
db = num * 2
tr = num * 3
rz = num ** (1/2)
print('O seu dobro é {},\n O seu triplo é {},\n E sua raiz é {:.2f}.'.format(db, tr, rz))
