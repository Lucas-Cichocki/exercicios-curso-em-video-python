from datetime import date
dataAgora = date.today().year


genero = input('Qual seu genero? F ou M?').lower()


if genero == 'm':
  data = int(input('Em qual ano voce nasceu? '))



  idade = dataAgora - data



  if idade < 18:
    
    tempo = 18 - idade
    print(f'Voce e muito novo ainda, faltam {tempo} anos')

    falta = dataAgora + tempo

    print(f'Seu alistamento sera em {falta}')
    
  elif idade == 18:
    print('Voce esta na idade exata!! se aliste ainda esse ano')

  else:
    tempo = idade - 18
    print(f'Voce ja deveria ter se alistado, voce esta {tempo} anos atrasado! ')

    falta = dataAgora - tempo
    print(f'Voce deveria ter se alistado em {falta}')

else:
  print('Voce nao precisa se alistar! ')