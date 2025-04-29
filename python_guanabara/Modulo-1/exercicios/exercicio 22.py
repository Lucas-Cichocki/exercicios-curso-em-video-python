frase = input('Diga o seu nome completo: ').strip()


print(f'Seu nome e: {frase}')

print(f'Com todas as letras maisculas e: {frase.upper()}')
print(f'Com todas as letras minusculas e: {frase.lower()}')



print(f'A quantidade total de letras da frase, sem contar os espaços: {len(frase) - frase.count(' ')}')




print(f'O primeiro nome tem: {frase.find(' ')} letras')

frase = frase.split()
print(f'O seu primeiro nome tem: {frase[0].count()}')
