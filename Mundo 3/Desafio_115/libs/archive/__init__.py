from libs.screen import *
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def existe(doc):
    try:
        arq = open(doc, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar(nome):
    try:
        arq = open(nome, 'wt+')
    except:
        print(f'\n\033[31mErro ao criar arquivo!\033[0m\n')
    else:
        print(f'\n\033[92mArquivo {arq} criado com sucesso!\033[0m\n')

def ler(nome):
    try:
        arq = open(nome, 'rt')
    except:
        print(f'\n\033[31mErro ao ler arquivo!\033[0m\n')
    else:
        title('Pessoas Cadastradas')
        for linha in arq:
            info = linha.strip().split('-')
            if len(info) >= 2:
                nome = info[0].strip()
                idade = info[1].strip()
                print(f'Nome: {nome:<30}Idade:{idade:>3} anos')
    finally:
        arq.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        doc = open(arq, 'at')
    except:
        print('\033[92mErro ao abrir o arquivo!\033[0m')
    else:
        try:
            doc.write(f'\n{nome} - {idade}')
        except:
            print('\033[92mErro ao escrever os dados!\033[0m')
        else:
            print('\033[92mDados criado com sucesso!\033[0m')
        finally:
            doc.close()