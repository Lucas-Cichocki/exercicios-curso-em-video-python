n1 = float(input('Digite um numero da sua escolha! '))
n2 = float(input('Digite mais um '))

if n1 > n2:
    print(f'O numero {n1:.1f} e maior que o {n2:.1f} ')

elif n2 > n1:
    print(f'O numero {n2:.1f} e maior que o {n1:.1f} ')

else:
    print('nao existe numero maior, ambos sao iguais')
