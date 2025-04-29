Cidade = input('Diga o nome da sua cidade: ').lower()

cidade = Cidade.split()

print(f'Sua cidade começa com o nome "Santo"? {'santo' in cidade[0]}')

#ou tambem posso fazer assim:
# cidade = input('Diga o nome da sua cidade: ').strip()
#print(cidade[:5].upper/lower() == 'SANTO/santo')