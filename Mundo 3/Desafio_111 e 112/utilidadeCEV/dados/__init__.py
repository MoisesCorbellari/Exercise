def leiaDinheiro(prompt):
    valido = False
    while not valido:
        entrada = input(prompt).strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mO valor \"{entrada}\" é inválido!\033[0m\n')
        else:
            valido = True
            return float(entrada)