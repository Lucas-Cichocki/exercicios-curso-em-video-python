from time import sleep

c = ('\033[m', 
     '\033[0;30;41m', 
     '\033[0;30;42m', 
     '\033[0;30;43m', 
     '\033[0;30;44m', 
     '\033[0;30;45m', 
     '\033[7;40m')

def ajuda(com):
    escreva(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6])
    help(com)
    print(c[0])
    sleep(2)

def escreva(msg, cor= 0):
    tam = len(msg) + 4
    moldura = '~' * tam
    print(c[cor])  
    print(moldura)
    print(f'{msg:^{tam}}')
    print(moldura)
    print(c[0])
    sleep(1)

def manual():
    while True:
        escreva('Sistema de Ajuda PyHelp', 2)

        duvida = input('Funçao ou biblioteca > ')

        if duvida.upper() == 'FIM':
            escreva('Ate logo!', 1)
            break

        ajuda(duvida)

manual()