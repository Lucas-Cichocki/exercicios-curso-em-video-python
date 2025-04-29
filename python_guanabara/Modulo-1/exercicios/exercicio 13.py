salario = float(input('qual e o salario do funcionario? R$'))

aumento = salario * 1.15

print(f'um fucionario que ganhava R${salario}, com 15% de aumento, passa a receber', end=' ')
print(f'passa a receber R${aumento:.2f}')