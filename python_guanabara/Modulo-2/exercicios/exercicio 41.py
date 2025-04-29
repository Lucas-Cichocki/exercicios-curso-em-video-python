from datetime import date

nasc = int(input('Em que ano voce nasceu? '))

agora = date.today().year

idade = agora - nasc

if idade <= 9:
    print('Voce e Mirim!! ')

elif idade <= 14:
    print('Voce e Infantil! ')

elif idade <= 19:
    print('Voce e Junior! ')

elif idade <= 25:
    print('Voce e Senior! ')

else:
    print('Voce e Master!!')