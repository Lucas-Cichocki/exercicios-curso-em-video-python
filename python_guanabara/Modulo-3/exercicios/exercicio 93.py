dados = {}
gols = []
total = 0

dados['nome'] = input('Qual o seu nome? ')
p = int(input(f'Quantas partidas voce jogou {dados["nome"]} '))

for i in range(p):
    gols.append(int(input(f'Quantos gols voce fez no {i + 1}° jogo? ')))

dados['gols'] = gols

dados['total'] = sum(gols)

print(f'O jogador {dados['nome']} jogou {p} jogos')

for i in range(p):
    print(f'=> Na partida {i + 1}, fez {dados["gols"][i]}')
    
print(f'Isso da um total de {dados["total"]} gols')
