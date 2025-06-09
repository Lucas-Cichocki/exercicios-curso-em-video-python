estado = {}
brasil = []

for i in range(3):
    estado['uf'] = input('Unidade federativa: ')
    estado['sigla'] = input('Sigla do estado: ')
    brasil.append(estado.copy())

for i in brasil:
    for v in i.values():
        print(v, end= ' ')
    print()