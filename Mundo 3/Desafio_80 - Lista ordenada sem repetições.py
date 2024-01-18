'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()). 
No final, mostre a lista ordenada na tela.
'''
lista = []
for c in range(0, 5):
    val = int(input('Digite um valor: '))
    if c == 0 or val > lista[-1]:
        lista.append(val)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if val <= lista[pos]:
                lista.insert(pos, val)
                print(f'Valor adicionado na posição {pos} da lista.')
                break
            pos += 1
print('='*45)
print(f'Valores digitados em ordem: {lista}')
