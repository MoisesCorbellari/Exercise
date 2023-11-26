'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. 
Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
'''

fut = ('Flamengo', 'Corinthians', 'Atlético Mineiro', 'Grêmio', 'Palmeiras',
       'Vasco Da Gama', 'Fluminense', 'Cruzeiro', 'Sport Recife', 'São Paulo', 
       'Santos', 'América-MG', 'Chapecoense', 'Atlético-PR', 'Botafogo',
       'Internacional', 'Bahia', 'EC Vitória', 'Ceará SC', 'Paraná Clube',)

print(f'\na) Os 5 primeiros times: \n{fut[0:5]}')

print(f'\nb) Os últimos 4 colocados: \n{fut[-4:]}')

print(f'\nc) Times em ordem alfabética: \n')
for time in sorted(fut):
    print(time)

posicao_chapecoense = fut.index('Chapecoense') +1
print(f'\nd) Em que posição está o time da Chapecoense: {posicao_chapecoense}ª')
