# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

homem_velho = ''
mulheres = 0
media = 0
soma = 0
maior = 0
for p in range(1,5):
    print('========== {}ª Pessoa =========='.format(p))
    nome = str(input('Digite seu nome: ')).strip()
    sexo = str(input('Masculino ou Feminino? [M/F]')).strip()
    idade = int(input('Digite sua idade: '))
    soma += idade
    if sexo in 'Mm' and idade > maior:
        maior = idade
        homem_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulheres += 1
media = soma / p
print('='*20)
print('Média das idades: {:.2f}'.format(media))
print('Homem mais velho: {}'.format(homem_velho))
if mulheres == 0:
    print('Não tem mulheres!')
else:
    print('Há somente {} mulher(es) com menos de 20 anos!'.format(mulheres))
