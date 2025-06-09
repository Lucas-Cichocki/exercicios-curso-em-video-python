def area(largura, comprimento):
    a = largura * comprimento
    print(f'A area de um terreno {largura} x {comprimento} e de {a}m².')


print('Controle de terrenos')
print('-' * 40)

l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))

area(l, c)
