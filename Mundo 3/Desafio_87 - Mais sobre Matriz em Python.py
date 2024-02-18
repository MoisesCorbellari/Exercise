'''
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

matriz = []
somaPar = terceiraColuna = mSegundaLinha = 0
for l in range(3):
    linha = []
    for c in range(3):
        valor = int(input(f'Digite valores para [{l},{c}]:'))
        linha.append(valor)
        if valor % 2 ==0:
            somaPar += valor
        if c == 2:
            terceiraColuna += valor
        if l == 1:
            mSegundaLinha = max(mSegundaLinha, valor)
    matriz.append(linha)
print('='*40)
print('''
        SOMA DE MATRIZ 3x3:
''')
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('='*40)
print(f'A) Soma dos valores pares digitados: {somaPar}')
print(f'B) Soma dos valores da terceira coluna: {terceiraColuna}')
print(f'C) Maior valor da segunda linha: {mSegundaLinha}')