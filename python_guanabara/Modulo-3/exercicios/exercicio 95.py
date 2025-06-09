dados = {}
jogadores = []
bonito = '-' * 40

while True:
    dados['nome'] = input('Qual o seu nome? ')
    p = int(input(f'Quantas partidas voce jogou {dados["nome"]}? '))
    
    gols = []

    for i in range(p):
        gol = int(input(f'Quantos gols voce fez no {i + 1}° jogo? '))
        gols.append(gol)
        
    dados['gols'] = gols[:]
    dados['total'] = sum(gols)

    jogadores.append(dados.copy())  
    dados.clear()
   
    while True:
        r = input('Voce quer continuar? [S/N] ').upper().split()[0]

        if r in 'SN':
            break
    
    if r == 'N':
        break

    else:
        print(bonito)

print(bonito)

for i, j in enumerate(jogadores):
    print(f'{i:<5}', end= '')
    for d in j.values():
        print(f'{str(d):<14}', end= '')
    print()
print(bonito)   

while True:
    busca = int(input('Qual o codigo do jogador que voce quer ver? (999 para parar) '))

    if busca == 999:
        break
    
    if busca >= len(jogadores):
        print('Erro, nao existe jogador com esse codigo! ')
    
    else: 
        print(f'Levantamento do jogador {jogadores[busca]["nome"]}')
        for i, j in enumerate(jogadores[busca]["gols"]):
            print(f'  No jogo {i + 1} fez {j} gols ')
    
    print(bonito)
        
    