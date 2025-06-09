from datetime import date
hoje = date.today().year

carteira = {}

carteira['nome'] = input('Qual o seu nome? ')
carteira['idade'] = hoje - int(input(f'Em que ano voce nasceu {carteira["nome"]}? ')) 
carteira['carteira'] = int(input(f'Qual o numero da sua carteira, {carteira["nome"]}? (0 se nao tiver): '))

if carteira["carteira"] != 0:
    carteira['ano'] = int(input('Em que ano voce foi contratado? '))
    carteira['salario'] = float(input('E qual era o seu salario? '))

    tempo = (hoje - carteira['ano']) 
    if tempo < 30:
        temp = 30 - tempo
        carteira['tempo'] = f'Voce ira se aposentar com {temp + carteira["idade"]} anos'

    else:
        carteira['tempo'] = 'Voce ja pode se aposentar'

for i, j in carteira.items():
    print(f'{i:<10} {j:<10}')