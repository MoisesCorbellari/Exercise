'''
Crie um programa que tenha a função leiaInt(), 
que vai funcionar de forma semelhante à função 'input() do Python, 
só que fazendo a validação para aceitar apenas um valor numérico. 
Ex: n = leiaInt('Digite um n: ')
'''

def titulo(msg):
    print(f'{msg:^70}')

def leiaInt(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n >= 0:
                return n
            else:
                print('Valor inválido. Digite um número inteiro positivo.\n')
        except ValueError:
            print('ERRO! Digite um número inteiro válido.\n')
def main():
    titulo('Validando entrada de dados em Python\n')
    num = leiaInt('Digite um valor: ')
    print(f'Você digitou o número {num}')

if __name__ == '__main__':
    main()