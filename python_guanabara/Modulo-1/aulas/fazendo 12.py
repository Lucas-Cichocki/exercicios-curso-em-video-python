#-------------oO zero apos a chave é o formato das letras, sendo elas-------------:
#0 = sem mudança na letra
#1 = deixa a letra em negrito
#4 = vai sublinhar as palavras
#7 = inverte as mudanças


#--------------O 33 apos o zero é a cor das letras, e o 44 do lado é a cor de fundo sendo elas----------------:
#--------------Obs: as cores de fundo são iguais as letras, apenas muda de 30 para 40--------------
#30 = branco     ///    40
#31 = vermelho   ///    41
#32 = verde      ///    42
#33 = amarelo    ///    43
#34 = azul       ///    44
#35 = roxo       ///    45
#36 = ciano      ///    46
#37 = cinza      ///    47

print('\033[0;30;41m Teste \033[m') 
print('\033[4;33;44m Teste \033[m')
print('\033[1;35;43m Teste \033[m')
print('\033[30;42m Teste \033[m')
print('\033[m Teste \033[m')
print('\033[7;30m Teste \033[m')

a = 9
nome = 'Lucas'
Cores = {'limpa':'\033[m',
         'azul':'\033[34m',
          'amarelo':'\033[33m',
          'pretoebranco':'\033[7:30m'}

print(f'o valor de A e: \033[1;32m{a}\033[m')




