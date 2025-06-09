aluno = {}

aluno['nome'] = input('Qual o seu nome? ')
aluno['media'] = float(input(f'Media do {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situaçao'] = 'aprovado' 

elif aluno['media'] < 5: 
    aluno['situaçao'] = 'reprovado'

else:
    aluno['situaçao'] = 'recuperaçao'


for i, j in aluno.items():
    print(f'{i} e igual a {j}')