'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

palavra = (
    'ceu', 'azul', 'branco', 'comida', 'fato', 'todo', 'estar', 'analogo', 'almejar', 'aspecto',
    'sentido', 'pandemia', 'obstinado', 'cognitivo', 'humilde', 'liberdade', 'maturidade', 'trabalho',
    'importante', 'sagacidade', 'subestimar', 'finalidade', 'desprovido', 'felicidade', 'conhecimento',
    'python', 'programaçao', 'computador', 'sistemas', 'desenvolvimento'
)

def show_vogal(palavra):
    vogais = [letra for letra in palavra if letra.lower() in 'aeiou']
    return vogais
for p in palavra:
    vogal_palavra = show_vogal(p)
    print(f'Vogais em "{p.upper()}": {vogal_palavra}\n' + '-'*60)
    