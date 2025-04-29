n1 = float(input('Diga o tamanho da primeira reta '))
n2 = float(input('Agora diga o tamanho da segunda '))
n3 = float(input('Agora o da terceira '))

if n1 + n3 > n2 and n1 + n2 > n3 and n2 + n3 > n1:    
    print('da para formar um triangulo! ')
                                 
else:
    print('nao da para formar um triangulo! ')