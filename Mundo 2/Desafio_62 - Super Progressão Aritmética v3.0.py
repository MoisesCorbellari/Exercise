# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('''
                        Gerando PA
      ''')
print('='*60)
a1 = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('Digite a razão da P.A.: '))
n = int(input('Digite a posição do termo da P.A.: '))
cont = 1
tot = 0
most_term = 10
while most_term != 0:
    tot += most_term
    while cont <= tot:
        print('{} 🠒 '.format(a1), end='')
        a1 += r
        cont += 1
    print('AGUARDANDO!')
    most_term = int(input('Mostrar mais quantos termos? '))
print('PA finalizada! Ao final foram mostrados {} termos.'.format(tot))
print('FIM!')
