'''from math import factorial
n = int(input('Digite um numero qualquer '))
f = factorial(n)
print(f'O Fatorial de {n} e {f}')'''

n = int(input('Digite um numero '))
f = n
fa = 1

print(f'{n}! = {n} x', end= ' ')

while f > 0: 
    print(f, end = '')

    if f > 1:
        print(' x ', end= '')
        
    else:
        print(' = ', end= '')

    fa *= f
    f -= 1
print(fa)