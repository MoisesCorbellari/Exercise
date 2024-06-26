def msg(txt, larg=70):
    print('-' * larg)
    print(f'{txt:^{larg}}')

def leiaInt(prompt):
    while True:
        try:
            n = int(input(prompt))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um valor "INTEIRO" válido!\033[0m\n')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não informar um valor\033[0m\n')
            return 0
        else:
            return n
        
def leiaFloat(prompt):
    while True:
        try:
            n = float(input(prompt))
        except (ValueError, TypeError):
            print('\033[31mDigite um valor "DECIMAL" válido!\033[0m\n')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não informar um valor\033[0m\n')
            return 0
        else:
            return n