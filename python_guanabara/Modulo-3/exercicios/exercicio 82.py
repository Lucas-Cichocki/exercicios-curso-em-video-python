v = []
par = []
impar = []

while True:
    n = int(input('Digite um valor: '))
    v.append(n)

    while True:
        r = input('Voce quer continuar? [S/N] ').strip().upper()[0]

        if r == 'S' or r == 'N':
            break

        else:
            print('Digite uma opçao valida! ')

    if r == 'N':
        break


for i in range(len(v)):
    if v[i] % 2 == 0:
        par.append(v[i])

    else:
        impar.append(v[i])

print('=' * 50)
print(f'Voce digitou os valores: {v}')
print('=' * 50)
print(f'Destes, os numeros: {par} sao pares')
print('=' * 50)
print(f'E os: {impar} sao impares ')