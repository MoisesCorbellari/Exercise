def leiaDinheiro(prompt):
    valido = False
    while not valido:
        entrada = input(prompt).strip().replace('.', '').replace(',', '.').replace(',', '')
        try:
            valor = float(entrada)
            valido = True
            return valor
        except ValueError:
            print(f'\033[31mO valor \"{entrada}\" é inválido!\033[0m\n')
            