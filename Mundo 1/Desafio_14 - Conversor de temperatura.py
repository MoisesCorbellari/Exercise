# Converter temperatura de °C para Fahrenheit e Kelvin.

C = float(input('Informe  a temperatura em °C: '))
print('''Escolha uma opção:

          Fahrenheit [1]
          Kelvin     [2]

''')

escolha = int(input('Escolha uma opção: '))

if escolha == 1:
    F = ((9 * C) / 5) + 32
    print('A temperatura em {:.2f}°C equivale a {:.2f}°F.'.format(C, F))

elif escolha == 2:
    K = C + 273.15
    print('A temperatura em {:.2f}°C equivale a {:.2f}°K.'.format(C, K))
