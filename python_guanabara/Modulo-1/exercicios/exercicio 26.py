frase = input('Digite uma frase: ').upper().strip()

print (f"""Essa frase tem um total de {frase.count('A')} letra A, 
A primeira letra a aparece na posiçao {frase.find('A')+1}
e a ultima letra A na posiçao {frase.rfind('A')+1}""")


