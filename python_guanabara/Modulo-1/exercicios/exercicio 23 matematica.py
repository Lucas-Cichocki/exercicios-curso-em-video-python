numero = int(input('Digite um numero entre 0 e 9999: '))

U = numero // 1 % 10
D = numero // 10 % 10
C = numero // 100 % 10
M = numero // 1000 % 100

print(f'Seu numero foi: {numero}')

print(f'Unidade {U}')
print(f'Dezena {D}')
print(f'Centena {C}')
print(f'Milhar {M}')