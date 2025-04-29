n = int(input('Digite um numero '))
cont = 0

for i in range(1, n + 1):
    

    if n % i == 0:
        print('\033[34m', end= ' ')
        cont += 1

    else:
        print('\033[31m', end= ' ')

    print(i, end= ' ')



if cont == 2:
    print(f'\n\033[m O numero {n} e primo! ')

else:
    print(f'\n\033[m O numero {n} nao e primo! ')

    