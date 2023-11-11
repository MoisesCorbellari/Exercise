# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.

from tqdm import tqdm
from time import sleep
salario = float(input('Informe seu salário: '))
for i in tqdm(range(0, 100), desc='Aguarde, estamos calculando seu salário'): sleep(.025)
if salario > 1250:
    maior = salario + (salario * 10/100)
    print('Obteve um aumento de 10% no seu salário. Novo salário: R${:.2f}'.format(maior))
else:
    maior = salario + (salario * 15/100)
    print('Obteve um aumento de 15% no seu salário. Novo salário: R${:.2f}'.format(maior))
