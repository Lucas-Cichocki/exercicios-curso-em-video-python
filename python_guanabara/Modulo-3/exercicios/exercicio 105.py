def notas(* notas, sit=False):
    """-> Funçao para analisar notas e situaçoes de varios alunos.
    :param notas: uma ou mais notas dos alunos (aceita varias).
    :param sit: valor opcional, indica se deve ou nao adicionar a situaçao.
    :param return: dicionario com varias informaçoes sobre a situaçao da turma."""
   
    total = {}
    
    total['Quantidade'] = len(notas)
    total['Maior'] = max(notas)
    total['Menor'] = min(notas)
    total['media'] = sum(notas) / len(notas)

    if sit:
        if total['media'] >= 7:
            total['situaçao'] = 'Boa'

        elif total['media'] < 5:
            total['situaçao'] = 'Ruim'

        else:
            total['situaçao'] = 'Razoavel'

    return total

resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)  
help(resp)          
    
