from time import sleep

def maior (* n):
    m = cont = 0
    print('=' * 50)
    print('Analisando os valores passados...')

    for i in n:
        sleep(0.3)
        print(i, end= ' ', flush=True)

        if cont == 0:
            m = i

        else:
            if i > m:
                m = i
                
        cont += 1

    tam = len(n)
    print(f'Foram informados {tam} valores ao todo.')
    print(f'O maior valor informado foi {m}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

