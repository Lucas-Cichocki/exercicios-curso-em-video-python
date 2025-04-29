from random import randint

pc = randint(0, 10)

acertou = False
tentativa = 0

while not acertou:

    resposta = int(input('Tente advinhar um numero entre 0 a 10: '))

    if resposta == pc:
        print(f'Parabens!! o numero era {pc}')
        print(f'Porem voce precisou de {tentativa} tentativas ')
        acertou = True 

    elif resposta < pc:
        print('Que pena, o numero que voce colocou e menor que o numero misterioso')
        tentativa += 1

    elif resposta > pc:
        print('Que pena voce errou, o numero que voce digitou e maior que o numero misterioso! ')
        tentativa += 1

print(f'Parabens! o numero misterioso era {pc} e voce levou {tentativa} tentativas para acha-lo')