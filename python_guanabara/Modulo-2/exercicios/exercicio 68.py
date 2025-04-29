from random import randint

v = 0
depois = ''

print('=-' * 20)
print('VAMOS JOGAR PAR OU IMPAR!'.center(40))
print('=-' * 20)

while True:
    pc = randint(1, 10)
    n = int(input('Diga um valor: '))
    resposta = ''
    while resposta not in ['P', 'I']:
        resposta = (input('Par ou impar? [P/I] ')).strip().upper()
    saber = pc + n

    if saber % 2 == 0:
        res = 'PAR'
        depois = 'P'
    else:
        res = 'IMPAR'
        depois = 'I'

    print(f'Voce jogou {n} e o computador {pc}. Total de {saber} Deu {res}')

    if depois == resposta:
        print('Voce GANHOU! ')
        v += 1

    elif depois != resposta:
        print('Voce PERDEU! ')
        break

print(f'GAME OVER! voce venceu {v} vezes')