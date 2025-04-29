S = float(input('Qual o seu salario? '))

if S <= 1.250:
    aumento = S * 1.15
    bonus = 15
else:
    aumento = S * 1.10
    bonus = 10

print(f'voce teve um aumento de {bonus}%, com isso seu salario foi para R$${aumento:.2f}')

