from random import choice

pc = ['pedra', 'papel', 'tesoura']

Eu = input('O que voce deseja jogar? pedra, papel, ou tesoura? ').lower()


pc = choice(pc) 

print('-=' * 15)
print(f'Voce jogou... {Eu}')
print(f'O computador jogou... {pc}')

print('-='*15)

if Eu == 'pedra':
    if pc == 'pedra':
        print('Empate!! ')

    elif pc == 'papel':
        print('Derrota!! ')

    elif pc == 'tesoura':
        print('Vitoria!! ')

elif Eu == 'papel':
    if pc == 'pedra':
        print('Vitoria!! ')

    elif pc == 'papel':
        print('Empate!! ')

    else:
        print('Derrota! ')

elif Eu == 'tesoura':
    if pc == 'pedra':
        print('Derrota!! ')

    elif pc == 'papel':
        print('Vitoria!! ')

    else:
        print('Empate! ')

else:
    print('Opçao invalida! ')