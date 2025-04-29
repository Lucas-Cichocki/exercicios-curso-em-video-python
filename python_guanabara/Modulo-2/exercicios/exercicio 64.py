n = cont = total = 0

while n != 999:
    n = int(input('Digite um numero, ou digite 999 para parar '))

    if n != 999:
        cont += 1
        total += n

print(f'Voce digitou um total de {cont} e a soma de todos eles da {total}')