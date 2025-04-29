n = int(input('Diga um numero inteiro de sua escolha! '))

print ('Agora escolha para qual forma voce quer converter!')

print('1-Binario')
print('2-Octal')
print('3-hexadecimal')

resposta = int(input(''))

if resposta == 1:
    forma = bin(n)
    print(f'O numero {n} em Binario fica: {forma}')

elif resposta == 2:
    forma = oct(n)
    print(f'O numero {n} em Octal fica: {forma}')

elif resposta == 3:
    forma = hex(n)
    print(f'O numero {n} em Hexadecimal fica: {forma}')

else:
    print('Escolha uma das opçoes validas ')