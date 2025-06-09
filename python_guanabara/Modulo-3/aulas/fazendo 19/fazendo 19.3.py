galera = []
dado = []

for i in range(3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] > 21:
        print(p)