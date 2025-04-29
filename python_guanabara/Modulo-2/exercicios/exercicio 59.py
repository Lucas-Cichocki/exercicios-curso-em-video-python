from time import sleep

n1 = int(input('Digite um valor '))
n2 = int(input('Digite outro valor '))

r = 0

while r != 5:
    print('O que voce deseja fazer agora? ')
    print('-=' * 10)
    r = int(input('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos numeros\n[5] Parar\nR: '))
    print('-=' * 10)
    if r == 1:
        print(f'A soma entre {n1} + {n2} = {n1 + n2} ')
    
    elif r == 2:
        print(f'A multiplicaçao de {n1} x {n2} = {n1 * n2} ')

    elif r == 3:
        if n1 > n2:
            print(f'O maior numero e o {n1} ')

        else:
            print(f'O maior numero e o {n2} ')

    elif r == 4:
        n1 = int(input('Digite outros numeros '))
        n2 = int(input('Digite novos numeros '))

    elif r != 5:
        print(f'a opçao {r} e invalida! ')
    sleep(2)
print('Fim do programa! volte sempre')
