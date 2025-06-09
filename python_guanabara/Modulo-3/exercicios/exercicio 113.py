def leiaint():
    while True:
        try:
            n = int(input('Digite um numero inteiro '))

        except KeyboardInterrupt:
            print('\n\033[31m ERRO! O usuario preferiu nao digitar o numero \033[m')
            n = 0
            return n

        except:
            print('\033[31m ERRO! Digite um numero inteiro valido\033[m')

        else:
            return n
    
def leiafloat():
    while True:
        try:
            f = float(input('Digite um numero real '))

        except KeyboardInterrupt:
            print('\n\033[31m ERRO! O usuario preferiu nao digitar o numero \033[m')
            f = 0
            return f

        except:
            print('\033[31m ERRO! Digite um numero inteiro valido\033[m')

        else:
            return f

n = leiaint()
f = leiafloat()

print(f'O valor inteiro digitado foi {n} e o real foi {f}')