D = int(input('Quantos dias alugados? '))
K = float(input('Quantos kms foram rodados? '))

valor = (D * 60) + (K * 0.15)

print(f'O total a pagar e de R${valor:.2f}')