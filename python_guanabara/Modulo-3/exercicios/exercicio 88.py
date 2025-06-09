from random import sample
from time import sleep
palpite = []
jogos = []

r = int(input('Quantos jogos serao feitos? '))

for i in range(r):  
    palpite = sample(range(1, 60),6)
    palpite.sort()
    jogos.append(palpite)
    
print('=' * 10, end= ' ')
print(f' SORTEANDO {r} JOGOS', end= ' ')
print('=' * 10)

for i in range(r):
    print(f'Jogo {i + 1} {jogos[i]}')
    sleep(1)

print('=' * 13, end= ' ')
print(' BOA SORTE! ', end= ' ')
print('=' * 14)