n1 = int(input('Digite um numero '))
n2 = int(input('Digite outro numero '))
n3 = int(input('E mais um '))

maior = n1 
menor = n1

if n2 < menor and n2 < n3:
   menor = n2

if n3 < menor and n3 < n2:
  menor = n3

if n2 > maior and n2 > n3:
  maior = n2

if n3 > maior and n3 > n2:
  maior = n3

print(f'Maior numero: {maior}')
print(f'Menor numero: {menor}')