n1 = (int(input('Digite um numero: ')),
      int(input('Digite mais um numero: ')),
      int(input('Digite outro numero: ')),
      int(input('Digite o ultimo numero: ')))
      


print('=' * 40)
print(f'Voce digitou os valores {n1}')
print(f'O numero nove se repetiu {n1.count(9)} vezes! ')

if 3 in n1:
    print(f'O Tres aparece pela primeira vez na posiçao {n1.index(3) + 1}')

else:
    print('Nenhum numero tres foi digitado! ')


print('Os valores pares digitados foram', end= ' ')
for i in n1:
    if i % 2 == 0:
        print(i, end= ' ')


