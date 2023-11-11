# programa que lê a largura e altura de uma parede em metros,
# calcule sua área e a quantidade de tinta para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m².

alt = float(input('Qual a altura da parede? '))
larg = float(input('Qual a largura da parede? '))
area = alt * larg
tinta = area / 2
print('Para pintar uma área de {}m² é necessário {} litros de tinta.'.format(area, tinta))
