'''
Crie um programa que vai ler vários números e colocar em uma lista.                  
Depois disso, mostre:                                                                                                                                                
A) Quantos números foram digitados.                                                                                                                    
B) A lista de valores, ordenada de forma decrescente.                                                                                          
C) Se o valor 5 foi digitado e está ou não na lista.
'''
vNum = []
while True:
    try:
        num = int(input('Digite um valor(ou digite 0 para sair): '))
        if num == 0:
            break
        vNum.append(num)
    except ValueError:
        print('Digite um número válido!')
print('='*60)
qDig = len(vNum)
print(f'A) Quantos números foram digitados? {qDig}')
vNum.sort(reverse=True)
print(f'\nB) A lista de valores, ordenada de forma decrescente: {vNum}\n')
if 5 in vNum:
    print('C) O valor 5 está na lista? Sim.\n')
else:
    print('C) O valor 5 está na lista? Não.\n')
