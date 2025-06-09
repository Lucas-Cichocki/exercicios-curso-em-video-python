pessoa = []
grupo = []
ppesada = []
pleve = []

while True:
    pessoa.append(input('Qual o seu nome? '))
    pessoa.append(int(input('Quantos kilos voce pesa? ')))
    grupo.append(pessoa[:])
    pessoa.clear()

    while True:
        r = input('Quer continuar? [S/N] ').strip().upper()[0]

        if r in 'SN':
            break
    if 'N' in r:
        break

print(f'{len(grupo)} pessoas foram cadastradas ')

pesado = max(p[1] for p in grupo)
leve = min(p[1] for p in grupo)

ppesado = [p[0] for p in grupo if p[1] == pesado]
pleve = [p[0] for p in grupo if p[1] == leve]


print(f'O maior peso registrado foi de {pesado} Kgs Peso de {ppesado}')
print(f'O menor peso registrado foi de {leve} Kgs Peso de {pleve}')




