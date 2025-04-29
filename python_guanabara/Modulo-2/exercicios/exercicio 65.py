r = 'S'
total = cont = menor = maior = 0

while r in "S":
    n = int(input('Digite um numero '))
    r = input('Quer continuar? [S/N] ').strip().upper()[0]

    cont += 1
    total += n
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
    
        elif n < menor:
            menor = n


m = total / cont
print(f'Foram digitados um total de {cont} numeros e a media foi {m}')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}')