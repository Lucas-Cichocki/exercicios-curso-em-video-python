geral = []
bonito = '=' * 40
while True:
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
   
    media = (n1 + n2) / 2
 
    geral.append([nome, [n1, n2], media])
    
    while True:
        r = input('Quer continuar? [S/N] ').strip().upper()[0]

        if r in 'SN':
            break

    if 'N' in r:
        break

print(bonito)

print(f'{'No.':<6}{'NOME':<12}{'MEDIA':>8}')
print('-' * 30)

for i, aluno in enumerate(geral):
    print(f'{i:<5} {aluno[0]:<12} {aluno[2]:>8.1f}')

while True:
    r = int(input('Mostrar as notas de qual aluno? (999 interrompe) '))

    if r == 999:
        break
    else:
        print(f'Notas de {geral[r][0]} sao: {geral[r][1]}')

