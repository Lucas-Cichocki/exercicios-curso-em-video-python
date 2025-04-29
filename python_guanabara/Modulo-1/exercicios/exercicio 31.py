km = float(input('quantos kms tem a sua viagem no total? '))

if km <= 200:
    passagem = km * 0.5


else:
    passagem = km * 0.45

print(f'A passagem para essa viagem ira custar R${passagem:.2f}')