m = []
bonito = '=' * 35

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f'Digite um valor para [{i}, {j}] '))
        linha.append(valor)
    m.append(linha)

print(bonito)

for i in range(3):
    for j in range(3):
        print(f'[ {m[i][j]} ]', end= ' ')
    print()