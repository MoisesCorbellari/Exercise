''' Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. '''
valor = []
for p in range (5):
    pos = int(input(f'Digite o {p + 1}º valor: '))
    valor.append(pos)
maiorValor = max(valor)
menorValor = min(valor)
posMaior = valor.index(maiorValor) + 1
posMenor = valor.index(menorValor) + 1
print(f'Maior valor digitado: {maiorValor}, na {posMaior}ª posição.')
print(f'Menor valor digitado: {menorValor}, na {posMenor}ª posição.')
