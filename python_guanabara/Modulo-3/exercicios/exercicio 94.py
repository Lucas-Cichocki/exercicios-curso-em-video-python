total = []
pessoas = {}
smedia = 0
mulheres = []
mulheresn = 0
bonito = '=' * 50

while True:
    pessoas['nome'] = input('Qual o seu nome? ')
    while True:
        pessoas['sexo'] = input('Qual seu sexo? [F/M] ').upper().split()[0]

        if pessoas['sexo'] in 'FM':
            break

    pessoas['idade'] = (int(input(f'Quantos anos voce tem {pessoas["nome"]}? ')))

    if pessoas['sexo'] == 'F':
        mulheres.append(pessoas.copy())
        mulheresn += 1
    
    smedia += pessoas['idade']
    total.append(pessoas.copy())

    while True:
        r = input('Voce quer continuar? [S/N] ').upper().split()[0]

        if r in 'SN':
            break
    if 'N' in r:
        break

print(bonito)
print(f'Foram cadastradas {len(total)} pessoas')

smedia /= len(total)

print(f'A media de idade das pessoas e {smedia}')

print(f'As mulheres cadastradas foram: ', end= '')

for i in total:
    if 'F' in i['sexo']:
        print(f'{i["nome"]} ', end= '')

print()

print('As pessoas com idade acima da media sao:')
for i in total:
    if i["idade"] >= smedia:
        print(f'{i}')
        print()
        


