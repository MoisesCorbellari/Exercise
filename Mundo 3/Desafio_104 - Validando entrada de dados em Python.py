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
        n = str(input(prompt))
        if n.lstrip('-').isdigit():
            return int(n)
        else:
            print('\033[0;31mERRO! Digite um número válido.\033[m\n')

titulo('Validando entrada de dados em Python\n')

def main():
    while True:
        num = leiaInt('Digite um valor: ')
        print(f'Você digitou o número {num}\n')
        while True:
            resp = input('Continuar [S/N]? ').upper()
            if resp in 'SN':
                break
            else:
                print('\033[0;31mERRO! Digite S ou N !\033[m\n')
        if resp == 'N':
            break
    titulo('Fim!')

if __name__ == '__main__':
    main()