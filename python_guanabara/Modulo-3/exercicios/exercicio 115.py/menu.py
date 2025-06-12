from time import sleep
import criacao


def c(c):
    if c == 0:
        co = '\033[m' 
    elif c == 1:
        co = '\033[0;31m'
    elif c == 2:
        co = '\033[0;32m'
    elif c == 3:
        co = '\033[0;33m'
    elif c == 4:
        co = '\033[0;34m' 
    elif c == 5:
         co = '\033[0;35m'
    elif c == 6:
         co = '\033[7;30m'
    
    return co

def menu():
    while True:
        try:
            linha = '=' * 50
            print(linha)
            print('MENU PRINCIPAL'.center(50))
            print(linha,c(3))
            print(f'''1 {c(0)}- {c(4)}Ver Pessoas cadastradas {c(3)}
2 {c(0)}- {c(4)}Cadastrar nova Pessoa {c(3)}
3 {c(0)}- {c(4)}Sair do sistema {c(0)}''')
            print(linha, c(3))
            r = int(input('Sua opçao: '))
            print(c(0))

        except KeyboardInterrupt:
            print(f'{c(1)}\n O usuario decidiu interromper o sistema ', c(0))
            return

        except:
            print(f'{c(1)} Erro! Digite um numero valido ')

        else:
            criacao.opçoes(r)
            sleep(2)
            if r == 3:
                break