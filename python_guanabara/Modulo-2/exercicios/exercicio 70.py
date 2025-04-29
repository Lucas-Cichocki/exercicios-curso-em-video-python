total = maior = cont = 0
nome = ''

while True:
    n = input('Qual o nome do produto? ').strip()

    while True:
        v = float(input('Qual o valor desse produto? R$'))
        if v > 0:
            break

    cont += 1
    total += v

    if v > 1000:
        maior += 1

    if cont == 1 or v < valor:
        nome = n
        valor = v

    while True:
        r = input('Quer continuar? [S/N] ').strip().upper()[0]
        if r == 'S' or r == 'N':
            break

    if r == 'N':
        break

print(f'''Foi gasto um total de R${total} reais nessa compra
existem {maior} produtos que custam mais de R$1000
E o nome do produto mais barato e {nome} que custa R${valor}''')
