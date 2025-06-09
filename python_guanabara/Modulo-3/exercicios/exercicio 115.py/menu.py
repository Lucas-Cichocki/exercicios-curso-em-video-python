c = ('\033[m', 
     '\033[0;31m', 
     '\033[0;32m', 
     '\033[0;33m', 
     '\033[0;34m', 
     '\033[0;35m', 
     '\033[7;30m')

def menu():
    while True:
        try:
            linha = '=' * 50
            print(linha)
            print('MENU PRINCIPAL'.center(50))
            print(linha,c[3])
            print(f'''1 {c[0]}- {c[4]}Ver Pessoas cadastradas {c[3]}
2 {c[0]}- {c[4]}Cadastrar nova Pessoa {c[3]}
3 {c[0]}- {c[4]}Sair do sistema {c[0]}''')
            print(linha, c[3])
            r = int(input('Sua opçao: '))
            print(c[0])

        except KeyboardInterrupt:
            print(f'{c[1]}\n O usuario decidiu interromper o sistema ', c[0])

        except:
            print(f'{c[1]} Erro! Digite um numero valido ')

        #else:
            #if r == 1:

menu()
    