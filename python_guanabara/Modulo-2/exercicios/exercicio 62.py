n = int(input('escolha um numero '))
r = int(input('Escolha a razao '))

a = 0
v = 10
c = 0
while v != 0:
    while a < v:
        print(n, end= ' ')
        a += 1
        n += r
        
    print('PAUSA')
    v = int(input('\nQuantos termos a mais voce gostaria de ver? '))
    a = 0

print('A progressao acabou')