m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
bonito = '=' * 35
par = 0
soma = 0

for i in range(3):
    linha = []
    for j in range(3):
        m[i][j].append(int(input(f'Digite um valor para [{i}, {j}] ')))
        
print(bonito)
for i in range(3):
    for j in range(3):
        print(f'[ {m[i][j]} ]', end= ' ')
        if m[i][j] % 2 == 0:
            par += m[i][j]
            
        if j == 2:
            soma += m[i][j]
    print()

maior = max(m[1])

print(bonito)
print(f'A soma dos valores pares e: {par}')
print(f'A soma dos valores da terceira coluna e: {soma}')
print(f'O maior valor da segunda linha e: {maior}')