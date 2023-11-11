# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

from tqdm import tqdm
from time import sleep
km = float(input('Insira a velocidade do carro: '))
multa = (km - 80) * 7
for i in tqdm(range(0, 100), desc='Calculando'): sleep(.025)
if km > 80:
    print('MULTADO! Você irá pagar R${:.2f}'.format(multa))
else:
    print('Está no limite!')
print('Dirija com segurança!')
