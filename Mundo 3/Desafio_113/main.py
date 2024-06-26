from teste import funcao

n1 = funcao.leiaInt("\nDigite um valor '\033[93mINTEIRO\033[0m': ")
n2 = funcao.leiaFloat("Digite um valor '\033[93mDECIMAL\033[0m': ")

funcao.msg('Valores digitados:')
print(f'\n\033[93mValor inteiro: {n1}\nValor decimal: {n2}\033[0m\n')