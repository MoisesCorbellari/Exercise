def leiaInt(prompt):
    while True:
        try:
            n = int(input(prompt))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite uma opção válida!\033[0m\n')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não informar uma opção!\033[0m\n')
            return 0
        else:
            return n

def linha(larg=70):
    return '-' * larg
        
def title(prompt):
    print(linha())
    print(prompt.center(70))
    print(linha())

def menu(lista):
    title('Menu Principal')
    c=1
    for opc in lista:
        print(f'{c} - {opc}')
        c+=1
    print('-'*70)
    opc = leiaInt('Escolha a opção: ')
    return opc