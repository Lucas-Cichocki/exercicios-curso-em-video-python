v = []

while True:
    r = int(input('Digite um valor: '))
    if r in v:
        print('Valor duplicado! Nao vou adicionar...')

    else:
        print('Valor adicionado com sucesso... ')
        v.append(r)

    resposta = input('Quer continuar? [S/N] ').strip().upper()[0]

    if resposta != 'S':
        break

print('=' * 30)
v.sort()
print(f'Voce digitou os valores: {v}')