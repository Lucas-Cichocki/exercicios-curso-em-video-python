from datetime import date
hoje = date.today().year

ContM = 0
contMe = 0

for i in range(1, 8):
    idade = int(input(f'Em que ano a pessoa {i} nasceu? '))
    maior = hoje - idade
    
    if maior >= 21:
        ContM += 1

    else:
        contMe += 1

print(f'{ContM} sao maiores de 18 e {contMe} sao menores de 18')
    