import random

A = input('Primeiro Aluno: ')
B = input('Segundo Aluno ')
C = input('Terceiro Aluno ')
D = input('Quarto aluno ')

lista = [A, B, C, D]

sorteado = random.choice(lista)

print(f'O aluno sorteado foi o: {sorteado}')

