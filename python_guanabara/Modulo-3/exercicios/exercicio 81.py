v = []

while True:
    n = int(input('Digite um numero! '))
    
    v.append(n)

    while True:
        r = input('Deseja continuar? [S/N] ').strip().upper()[0]
       
        if r == 'S' or r == 'N':
            break

        else:
            print('digite uma opçao valida!' )

    if r == 'N':
        break

print(f'Foram digitados {len(v)} numeros! ')

v.sort(reverse=True)
print(f'lista em ordem decrescente: {v}')

if 5 in v:
    print(f'Sim, um numero cinco foi digitado pelo usuario! ele esta na posiçao {v.index(5) + 1}')

else:
    print('Nao, o usuario nao digitou nenhum numero cinco! ')
