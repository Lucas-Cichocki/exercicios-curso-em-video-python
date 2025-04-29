produto = float(input('qual o preço do produto? R$'))

desconto = produto * 0.95

print(f'o produto que custava R${produto}, na promoçao com desconto de 5%' , end=' ')
print(f'vai custar R${desconto:.2f}')