'''
Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta.
'''
matriz = []
for l in range(0,3):
    linha = []
    for c in range(0,3):
        valor = int(input(f'Digite valores para [{l},{c}]:'))
        linha.append(valor)
    matriz.append(linha)
print('='*40)
print('''
        MATRIZ 3x3:
''')
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('='*40)
