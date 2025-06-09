pessoas = {'nome': 'Gustavo', 'Sexo': 'M', 'idade': 22}

pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
del pessoas['Sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')