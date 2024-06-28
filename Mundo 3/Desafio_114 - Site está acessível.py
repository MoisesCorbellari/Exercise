'''
Crie um código em Python que teste 
se o site pudim está acessível pelo computador usado.
'''

import urllib
import urllib.error
import urllib.request

try:
    site = 'http://www.pudim.com.br/'
    response = urllib.request.urlopen(site)
    print(f'\n\033[92m{" Conectado com sucesso ":^50}\033[0m')
    print(f'\033[92m{" Status code: 200 ":^50}\033[0m')
    print(f'\033[92mUrl: {site}\033[0m\n'.center(60))

except urllib.error.URLError:
    print(f'\n\033[31m{" Não foi possível acessar o site ":^50}\033[0m')
    print(f'\033[31m{" Status code: 404 ":^50}\033[0m')
    print(f'\033[31mUrl: {site}\033[0m\n'.center(60))