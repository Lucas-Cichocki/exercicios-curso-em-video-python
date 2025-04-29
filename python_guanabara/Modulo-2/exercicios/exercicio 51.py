n = int(input('Digite um numero '))

r = int(input('Agora diga qual a razao aritmetica '))

decimo = n + 10 * r


for i in range(n, decimo, r):
    print(i, end= ' - ')

print('ACABOU')