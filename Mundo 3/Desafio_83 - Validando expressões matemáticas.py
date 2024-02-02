'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''
parent = []
exp = input('Digite uma expressão algébrica: ').strip().lower()
for simb in exp:
    if simb == '(':
        parent.append(simb)
    elif simb == ')':
        parent.pop() if len(parent) > 0 else parent.append(')')
print('Expressão válida!' if len(parent) == 0 else 'Expressão inválida!')
