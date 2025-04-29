maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input(f'Qual o peso da {i} pessoa '))

    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        
        if peso < menor:
            menor = peso

print(f'O maior peso foi de {maior}Kg')
print(f'E o menor foi {menor}Kg')

'''pesos = []

for i in range(1, 6):
    peso = float(input(f'Qual o peso da {i} pessoa '))
    pesos.append(peso)

pesos.sort()

maior = pesos[-1]
menor = pesos[0]

print(f'O menor peso foi {menor} e o maior foi {maior} ')'''