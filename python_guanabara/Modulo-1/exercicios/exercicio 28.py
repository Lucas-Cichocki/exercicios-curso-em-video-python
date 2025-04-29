import random
from time import sleep #apenas para fazer uma graça, nesse codigo serve apenas para o computador demorar um pouco para escrever, para parecer q ele realmennte esta processando

n = random.randint(0, 5)

resposta = int(input('----------Tente advinhar o numero escolhido entre 0 e 5 pelo computador!-------------'))
print('PROCESSANDO...')

sleep(4)

if resposta == n:
    print('Parabens!! voce acertou o numero ')

else:
    print(f'Voce errou, o numero era {n}, mais sorte da proxima')