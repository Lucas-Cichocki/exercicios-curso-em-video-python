from math import hypot 

CO = float(input('digite o comprimeto do cateto oposto '))
CA = float(input('Digite o comprimeto do cateto adjascete '))

HI = hypot(CO, CA)

print(f'o comprimento da hipotenusa e de: {HI:.2f}')
