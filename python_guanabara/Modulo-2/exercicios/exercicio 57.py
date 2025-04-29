sexo = input('Informe seu sexo: [F/M] ').strip().upper()[0]

while sexo not in 'MF':
    sexo = input('Voce digitou uma opçao invalida! Tente novamente ').strip().upper()[0]

print(f'Sexo {sexo} registrado com sucesso! ')

