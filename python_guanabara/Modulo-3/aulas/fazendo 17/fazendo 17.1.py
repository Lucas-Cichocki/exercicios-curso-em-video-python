lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata-Frita')
#Tuplas são imutaveis
#lanche[1] = 'refrigerante'

for i in lanche:
    print(f'Eu vou comer {i}') 

for i in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[i]} na posiçao {i}')


#print(len(lanche))
for pos, i in enumerate(lanche):
    print(f'Eu vou comer {i} na posiçao {pos}')

#print('Comi pacas agora! ')