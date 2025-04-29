print(f'{"Lojas Eu Mesmo":=^40}')


P = float(input('Quanto custa o produto que voce comprou? '))

print('1- Voce pode pagar A vista usando dinheiro ou cheque, isso lhe dara 10% de desconto')
print('2- A vista no cartao, voce ira ganhar 5% de desconto')
print('3- em 2x no cartao o preço sera normal')
print('4- 3x ou mais vezes no cartao tera um aumento de 20% ')


forma = int(input('Digite o numero correspondendo a forma com que deseja fazer! '))

if forma == 1:
    valor = P * 0.90

elif forma == 2:
    valor = P * 0.95

elif forma == 3:
    valor = P
    parcela = valor / 2
    print(f'Sua compra sera parcelada em 2x de {parcela:.2f}')

elif forma == 4:
    valor = P * 1.20
    vezes = int(input('Quantas vezes voce gostaria de parcelar? '))
    parcela = valor / vezes
    print(f'Sua compra sera parcelada em {vezes} de {parcela:.2f}')


else:
    valor = P
    print('Opçao invalida! Tente novamente! ')   
print(f'Seu produto que inicialmente custava R${P} agora ira custar um total de R${valor}')