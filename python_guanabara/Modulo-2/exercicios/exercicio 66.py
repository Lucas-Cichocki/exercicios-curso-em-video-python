count = 0
total = 0

while True:
    n = int(input('Digite um numero (ou 999 para parar) '))
   
    if n == 999:
        break
    count += 1
    total += n

print(f'Foram digitados {count} numeros e a soma entre eles e de {total}')