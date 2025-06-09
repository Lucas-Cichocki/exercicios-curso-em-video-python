def fatorial(num = 1):
    f = 1
    for i in range(num, 0, -1):
        f *= i
    return f

n = int(input('Digite um numero: '))
print(f'O fatorial de {n} e igual a {fatorial(n)}')