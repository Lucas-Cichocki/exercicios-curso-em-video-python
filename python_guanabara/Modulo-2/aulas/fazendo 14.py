cmc = int(input('Inicio '))
fim = int(input('Fim '))
passo = int(input('De quanto? '))

for i in range(cmc, fim, passo):

    n = int(input('Digite um numero '))
    total = total + n
    totaldiferente += n #só pra mim ver as diferentes formas
print(total)
print(totaldiferente)


