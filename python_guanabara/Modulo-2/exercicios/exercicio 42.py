P = float(input('Diga o tamanho da primeira reta '))
S = float(input('Diga o tamanho da segunda reta '))
T = float(input('Diga o tamanho da terceira reta '))

if P + T > S and P + S > T and S + T > P:
    if P == T == S:
        print('Triangulo Equilatero, pois todos os lados sao iguais! ')

    elif P == T and P != S or T == S and T != P or P == S and P != T:
        print('Triangulo Isoseles! pois existem dois lados iguais! ')

    else:
        print('Triangulo Escaleno, pois todos os lados sao diferentes! ')

else:
    print('Nao da para formar um triangulo! ')