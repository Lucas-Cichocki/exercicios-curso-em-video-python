i = 0

while True:
    n = int(input('Digite um numero POSITIVO para saber a taboada dele '))
   
    if n < 0:
        break

    print('-' * 20)

    for i in range(1, 11):       
        taboada = n * i

        print(f'{n} x {i} = {taboada}')

    print('-' * 20)
    
print('Por ter digitado um numero negativo o programa foi interrompido')
