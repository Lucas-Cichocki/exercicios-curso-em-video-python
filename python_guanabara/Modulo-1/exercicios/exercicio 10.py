A = float(input('quantos reias voce tem na carteira ? R$'))

dolar = A / 5.84
euro = A / 6.39

print(f'Com R${A:.2f} voce pode comprar US${dolar:.2f} dolares ou pode comprar EU${euro} euros')