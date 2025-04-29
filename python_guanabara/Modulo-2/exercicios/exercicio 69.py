m = h = mu = 0

while True:

    print('-' * 30)
    print('CADASTRE UMA PESSOA' .center(30))
    print('-' * 30)
    while True:
        i = int(input('Qual a sua idade? '))
        if i >= 0:
            break

    while True: 
        s = input('Qual o seu sexo? [F/M] ').strip().upper()[0]

        if s == 'F' or s == 'M':
            break

    if i >= 18:
        m += 1

    if s == 'M':
        h += 1

    if s == 'F' and i <= 20:
        mu += 1
    print('-' * 30)
    while True:    
        r = input('Voce gostaria de continuar? [S/N] ').strip().upper()[0]
        if r == 'S' or r == 'N':
            break

    if r == 'N':
        break

print(f'''Tem {m} pessoas com mais de 18 anos
Foram registrados {h} homens
 e tem {mu} mulheres com menos de 20 anos!''')
