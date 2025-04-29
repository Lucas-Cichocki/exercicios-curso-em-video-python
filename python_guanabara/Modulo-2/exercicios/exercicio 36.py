casa = float(input('Qual o valor da casa que voce deseja comprar? R$'))
salario = float(input('Qual o seu salario? R$'))
ano = int(input('Em quantos anos voce gostaria de parcelar? '))

mes = ano * 12

prestacao = casa / mes

porcentagem = prestacao * 1.30


print(porcentagem)

if salario < porcentagem:
    print('EMPRESTIMO RECUSADO!!! ')

else:
    print('EMPRESTIMO ACEITO!! ')
