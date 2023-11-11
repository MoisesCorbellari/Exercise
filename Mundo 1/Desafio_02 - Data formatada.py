# Desafio_02
# Script python que lê o dia, mes e ano de nascimento de uma pessoa
# e mostra uma mensagem com a data formatada.

import datetime

print('='*18)
print("Desafio 02: Data formatada")
print('='*18)
nome = input ("Como se chama? ")
ano = eval (input ("Nasceu em que ano? "))
mes = eval (input ("Nasceu em que mês? "))
dia = eval (input ("Nasceu em que dia? "))
dataNasc = datetime.date(ano, mes, dia)
print('Data de nascimento: {}/{}/{}'.format(dia, mes, ano))
