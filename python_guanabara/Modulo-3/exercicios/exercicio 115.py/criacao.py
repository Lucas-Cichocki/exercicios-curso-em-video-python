import menu
import os

caminhoCa = os.path.join(os.path.dirname(__file__), 'Cadastros.txt')

def opçoes(r):
    if r == 1:
        with open(caminhoCa, 'r') as arquivo:
            for linha in arquivo:
                print(linha.strip())

    elif r == 2:
        nome = input('Qual o nome? ')
        idade = int(input('Qual a idade? '))
        with open(caminhoCa, "a") as arquivo:
            arquivo.write(f'{nome:<10}' + str(idade) + '\n')

    elif r == 3:
        print('Encerrando...')

    else:
        print(f'{menu.c(1)}Digite uma opçao valida!', menu.c(0))
