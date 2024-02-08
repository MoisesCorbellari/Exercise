'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''
parnt = []
exp = str(input('Digite uma expressão qualquer: ')).strip().lower()
for simb in exp:
    if simb == '(':
        parnt.append(simb)
    elif simb == ')':
        if len(parnt) > 0:
            parnt.pop()  
        else: 
            parnt.append(simb)
if len(parnt) == 0:
    print('Expressão válida!')  
else: 
    print('Expressão inválida!')
