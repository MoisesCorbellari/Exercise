'''
Crie um programa que leia nome e duas notas de vários alunos 
e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um 
e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''
from time import sleep
boletim = list()
while True:
    nome = str(input('Nome: ')).title().strip()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1+n2)/2
    aluno = {'Nome':nome,'Nota1':n1,'Nota2':n2,'Média':media}
    boletim.append(aluno)
    rsp = str(input('Continuar? [S/N]')).strip().upper()[0]
    if rsp != 'S':
        break
    print('-='*30)
print('\n\nBoletim:')
for aluno in boletim:
        print(f'Nome: {aluno["Nome"]}')
        print(f'Média: {aluno["Média"]}\n')

print('-'*60)

while True:
    rsp2 = input('\nDeseja ver as notas de algum aluno ?[S/N]:').strip().upper()
    if rsp2 == 'S':
        nome2 = input('Digite o Nome do Aluno: ')
        aluno_encontrado = False  
        for p in boletim:
            if p['Nome'] == nome2:
                print(f'\nBoletim do(a) aluno(a){p["Nome"]}:')
                print(f'Nota 1: {p["Nota1"]}')
                print(f'Nota 2: {p["Nota2"]}')
                print(f'Média: {p["Média"]}')
                aluno_encontrado = True
                break
        if not aluno_encontrado:
            print('Aluno não encontrado!')
    elif rsp2 == 'N':
        print('Finalizando...')
        sleep(1)
        break
    else:
        print('Digite uma opção válida!')
print('\nPrograma encerrado!')