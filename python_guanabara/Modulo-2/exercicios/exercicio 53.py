palavra = input('Digite uma palavra para vermos se e um palindromo ou nao ').strip().lower()

separado = palavra.split()
junto = ''.join(separado)
invertida = ''
invertida = junto[::-1]

'''for letra in range(len(junto) - 1, -1, -1):
    invertida += junto[letra]'''

print(junto, invertida)

if junto == invertida:
    print('Temos um palindromo! ')

else:
    print('A frase digitada nao e um palindromo! ')

