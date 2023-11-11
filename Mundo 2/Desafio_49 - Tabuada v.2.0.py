# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um valor: '))
for tab in range(0,11):
    print('{} x {} = {}'.format(num,tab,num*tab))
    