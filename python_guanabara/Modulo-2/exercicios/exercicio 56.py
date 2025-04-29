m = 0
idade = 0
velho = 0
nomev = ''


for i in range(1, 5):

    print(f"{'-' * 5} PESSOA {i} {'-' * 5}")
    N = input('Nome ').strip()
    I = int(input('Idade '))
    G = input('Sexo [F/M] ').strip().upper()

    m += I / 4

    if G == 'M':
        if velho == 0 or I > velho:
            velho = I
            nomev = N
        

    if G == 'F' and I < 20:    
        idade += 1

print(f'A Media de idade do grupo e de {m} ')
print(f'O homem mais velho tem {velho} anos e se chama {nomev}')
print(f'Tem {idade} mulheres abaixo dos 20 anos ')