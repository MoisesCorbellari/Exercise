'''Faça um programa que leia nome e média de um aluno, 
guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.'''

alunos = {}
while True:
    nome = input('Digite o nome do aluno (ou digite "sair" para encerrar o programa): ')
    if nome.lower() == 'sair':
        break
    media = float(input('Informe a média do aluno: '))
    if media >= 7:
        situacao = 'Aprovado!'
    elif media >= 5:
        situacao = 'Recuperação!'
    else:
        situacao = 'Reprovado!'
    alunos[nome] = {'Média': media, 'Situação': situacao}

print('-'*10 + "Listagem dos Alunos" + '-'*10)
for aluno, info in alunos.items():
    print(f'Nome: {aluno} | Média: {info["Média"]} | Situação: {info["Situação"]}')