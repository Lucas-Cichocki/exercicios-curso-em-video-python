M = int(input('diga quantos metros quer converter: '))

km = M / 1000
hm = M / 100
dam = M / 10
D = M * 10
C = M * 100
Mi = M * 1000

print(f'{M} metros e equivalente a: \n{km} quilometros \n{hm} Hectometros \n{dam} Decametros')
print(f'{D} Decimetros \n{C} centimetros \n{Mi} milimetros')