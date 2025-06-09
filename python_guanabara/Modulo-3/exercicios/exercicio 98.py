from time import sleep

def contagem(i, f, p):
    if f > i:      
        if p == 0:
            p = 1

    if f < i:
        if p > 0:
            p = -p
        if p == 0:
            p = -1

    for j in range(i, f + (1 if p > 0 else - 1), p):
        sleep(0.2)
        print(j, end= ' ', flush=True)
    print()

print('Contagem de 1 ate 10 de 1 em 1')
contagem(1, 10, 1)

print('Contagem de 10 ate 0 de 2 em 2')
contagem(10, 0, -2)

print('Agora e a sua vez de personalizar a contagem!')

i = int(input('Inicio: '))
f = int(input('Fim: '))   
p = int(input('Passo: '))

print(f'Contagem de {i} ate {f} de {p} em {p}')

contagem(i, f, p)