def voto(idade = 0):
    from datetime import date
    hoje = date.today().year
    voto = ''

    anos = hoje - idade

    if anos < 16:
        return f'com {anos} anos Nao vota!'
    
    elif 65 >= anos >= 18:
        return f'com {anos} anos o Voto e obrigatorio!'
    
    else:
        return f'com {anos} anos o Voto e opcional!'
    

pergunta = int(input('Em que ano voce nasceu? '))

print(voto(pergunta))



    