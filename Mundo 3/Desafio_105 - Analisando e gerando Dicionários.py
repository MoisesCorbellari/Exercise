'''
Faça um programa que tenha uma função notas() que pode receber 
várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota                
- A menor nota
- A média da turma
- A situação (opcional)
'''

from tabulate import tabulate

def titulo(txt):
    """
    Exibe o título centralizado na tela.
    :param txt: Texto do título a ser exibido.
    """
    print(f'{txt:^70}')

def notas(*numb, sit=False):
    """
    Calcula e retorna as estatísticas das notas fornecidas.
    :param numb: Notas dos alunos.
    :param sit: (Opcional) Indica se a situação da turma deve ser incluída.
    :return: Dicionário com a quantidade, maior, menor, média das notas e a situação.
    """
    alunos = dict()
    alunos['Quantidade'] = len(numb)
    alunos['Maior'] = max(numb)
    alunos['Menor'] = min(numb)
    alunos['Média'] = round(sum(numb) / len(numb), 2)

    if sit:
        if alunos['Média'] >= 7:
            alunos['Situação'] = 'Muito bom!'
        elif alunos['Média'] >= 5:
            alunos['Situação'] = 'Mais ou menos'
        else:
            alunos['Situação'] = 'Ruim'
    return alunos
def coletar():
    """
    Coleta as notas dos alunos inseridas pelo usuário.
    :return: Lista de notas inseridas.
    """
    nota_list = list()
    while True:
        nota = input(f'Digite a nota: ')
        try:
            nota = float(nota)
            nota_list.append(nota)
        except ValueError:
            print('Dado inválido! Digite novamente!')
            continue
        
        while True:
            resp = input('Continuar [S/N]? ').strip().upper()
            print()
            if resp in ['S', 'N']:
                break
            else:
                print('\033[0;31mERRO! Digite S ou N !\033[m\n')
        
        if resp == 'N':
            break

    return nota_list

titulo('Analisando e gerando Dicionários\n')
notas_user = coletar()
info = notas(*notas_user, sit=True)
print(f'Notas digitadas: {notas_user}', end=', ')
print()
print(tabulate([info], 
                headers='keys',
                tablefmt='rounded_grid',
                stralign="center"
                ))