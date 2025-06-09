def escreva(msg):
    tam = len(msg) + 4
    moldura = '~' * tam
    print(moldura)
    print(f'{msg:^{tam}}')
    print(moldura)

escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')
 