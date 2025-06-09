m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        m[i][j] = int(input(f'Diga um valor para a linha {i} coluna {j} '))



for i in range(3):
    for j in range(3):
        print(f'[ {m[i][j]:^5} ]', end= ' ')
    print()