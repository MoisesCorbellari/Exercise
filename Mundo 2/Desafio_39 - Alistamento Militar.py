# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
print('''Informe uma opção:
      
      [M] Masculino
      [F] Feminino
      ''')
sexo = str(input('Informe uma opção: '))
if sexo == 'F':
    print('Não precisa se alistar!')
else:
    nasc = int(input('Informe o ano de nascimento: '))
    atual = date.today().year
    alist = atual - nasc
    print('Você tem {} anos, RECRUTA!'.format(alist))
    if alist < 18:
        print('Ainda não é hora de seu alistamento!')
        pas_temp = 18 - alist
        print('Falta {} anos para se alistar!'.format(pas_temp))
    elif alist == 18:
        print('Chegou a hora de seu alistamento!')
    elif alist > 18:
        print('Aliste-se já.')
        pas_temp = alist - 18
        print('Deveria ter se alistado a {} anos. Vá ao posto de alistamento!'.format(pas_temp))
        