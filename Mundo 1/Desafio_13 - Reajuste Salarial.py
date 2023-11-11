# Algoritmo que lê o salário de funcionário e mostra seu novo salário,
# com 15% de aumento.

salario = float(input('Digite o valor do seu salário: R$ '))
reajuste = salario + (salario*0.15)
print('Com aumento de 15%, seu salário passa ser de R${:.1f}'.format(reajuste))
