frase = 'Curso em video Python'

print (len(frase))
print (frase.count('o', 0, 13))

print(frase.find('android'))
print('Curso' in frase)
print(frase.replace('python','Android'))

print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())

print(frase.split(), '-'.join(frase))

dividido = frase.split()

print(dividido[0][3])