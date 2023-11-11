# Desafio_04
# Script que lê algo pelo teclado e mostra seu tipo primitivo
# e suas informações.

a = input('Digite algo, seja qual for: ')
print('O tipo primitivo é ', type(a))
print('Somente espaço? ', a.isspace())
print('É número? ', a.isnumeric())
print('Todas as letras são maiúsculas? ', a.isupper())
print('Toas as letras são minúsculas? ', a.islower())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('É capitalizada? ', a.istitle())
