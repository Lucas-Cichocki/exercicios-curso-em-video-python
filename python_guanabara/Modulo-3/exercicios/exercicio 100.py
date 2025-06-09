from random import randint
from time import sleep
numeros = []


def sorteia():
    print('sorteando os valores da lista', end= ' ')
    for i in range(5):
        numero = (randint(1, 10))
        sleep(0.3)
        print(f'{numero}', end= ' ', flush=True)
        numeros.append(numero)
    print('PRONTO!')        

def somaPar(numeros):
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {numeros}, temos {soma}')

sorteia()
somaPar(numeros)