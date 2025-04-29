nome = input('Qual o seu nome? ')

if nome == 'Lucas':
   print('Que nome bonito! ')

elif nome == 'Pedro' or  nome == 'maria' or nome == 'Paulo':
   print('seu nome e bem popular no brasil! ')

elif nome in 'Ana Claudia Jessica Juliana':
   print('Que belo nome feminino! ')
   
else:
   print('Seu nome e bem normal! ')
print(f'Tenha um bom dia! {nome}')