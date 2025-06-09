numeros = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Desseseis', 'Dessesete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    r = int(input('Digite um numero entre 0 e 20: '))

    if 0 <= r <= 20:
        break
    print('Tente novamente.', end=' ')


print(f'Voce digitou o numero {numeros[r]}')
    