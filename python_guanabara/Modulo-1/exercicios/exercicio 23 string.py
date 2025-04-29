numero = input('Digite um numero qualquer entre 0 a 9999 ')

numero = numero.zfill(4)

print(f'O numero digitado foi: {numero}')

print(f'Unidade: {numero[3]}')
print(f'Dezena: {numero[2]}')
print(f'Centena: {numero[1]}')
print(f'Milhar: {numero[0]}')
