from random import randint
from operator import itemgetter
from time import sleep

numeros = {}
numeroscerto = {}

for i in range(4):
    numeros[f'Jogador{i + 1}'] = randint(1, 6)  
    
for k, j in numeros.items():
    print(f'O {k} tirou {j}')
    sleep(1)
print('=' * 30)

numeroscerto = sorted(numeros.items(), key=itemgetter(1), reverse=True)


for i, j in enumerate(numeroscerto):
    print(f'{i + 1} Lugar: {j[0]} com {j[1]}')
    
    


