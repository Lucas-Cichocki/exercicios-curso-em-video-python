
par = 0
cont = 0
for i in range(1, 7):
    n = int(input('Digite 6 numeros '))

    if n % 2 == 0:
        par += n
        cont += 1


print(f'Voce informou apenas {cont} numeros pares, a soma deles e de {par}')
