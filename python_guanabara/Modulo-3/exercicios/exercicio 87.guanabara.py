m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0
soma = 0
for i in range(3):
    for j in range(3):
        m[i][j] = int(input(f'Diga um valor para a linha {i} coluna {j} '))

for i in range(3):
    for j in range(3):
        print(f'[ {m[i][j]:^5} ]', end= ' ')
        if m[i][j] % 2 == 0:
            par += m[i][j]

    print()

for i in range(0, 3):
    soma += m[i][2]

for i in range(0, 3):
    if i == 0:
        maior = m[1][i]
    
    elif m[1][i] > maior:
        maior = m[1][i]

print(f'A soma dos valores pares e: {par}')
print(f'A soma dos valores da terceira coluna e: {soma}')
print(f'O maior valor da segunda linha e: {maior}')