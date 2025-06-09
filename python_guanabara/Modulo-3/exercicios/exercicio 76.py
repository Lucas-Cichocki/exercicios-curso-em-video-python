lista = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-' * 40)
print('LISTAGEM DE PREÇO'.center(40))
print('-' * 40)

for i in range(0, len(lista), 2):
    produto = lista[i]
    preco = lista[i + 1]

    print(f'{produto:.<30}R$ {preco:>7.2f}')


print('-' * 40)