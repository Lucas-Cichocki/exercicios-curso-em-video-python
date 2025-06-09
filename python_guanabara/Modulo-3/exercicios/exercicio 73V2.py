times = ('Palmeiras', 'Red Bull Bragantino', 'Flamengo', 'Cruzeiro', 'Fluminense', 'Bahia', 'Ceará','Corinthians', 'Internacional', 'Atlético Mineiro', 'São Paulo', 'Botafogo', 'Grêmio', 'Fortaleza', 'Juventude', 'Vasco da Gama', 'Santos', 'Mirassol', 'Vitória', 'Sport Recife')

print('=' * 129)

for i in times:
    print(f'{i}', end= ' - ')

print('\n' + '=' * 129)

print('Os primeiros cinco colocados sao: ', end= '')
for i in times[:5]:
    print(f'{i}', end= ' - ')

print('\n' + '=' * 129)

print('Os 4 ultimos sao: ', end= '')
for i in times[-4:]:
    print(f'{i}', end= ' - ')

print('\n' + '=' * 129)

print('Os times em ordem alfabetica: ', end= '')
for i in sorted(times):
    print(f'{i}', end= ' - ')
print('\n' + '=' * 129)

print(f'O time internacional esta na posiçao: {times.index('Internacional') + 1}')

print('=' * 129)