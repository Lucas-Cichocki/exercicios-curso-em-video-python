nota = 50

print('=' * 25)
print('Banco EU' .center(25))
print('=' * 25)
v = int(input('Qual o valor a ser sacado? R$'))  

total = v
numnota = 0

while True:
    if total >= nota:
        total -= nota
        numnota += 1

    else:
        print(f'Total de {numnota} de {nota}')
        if nota == 50:
            nota = 20

        elif nota == 20:
            nota = 10

        elif nota == 10:
            nota = 1

        elif nota == 1:
            break
        numnota = 0