n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
me = n1 - n2
m = n1 * n2
d = n1 / n2
dI = n1 // n2
po = n1 ** n2
r = n1 % n2


print(f'A soma vale: {s}, a subtracao vale: {me}, a multiplicacao vale: {m}' , end = '')
print(f'A divisao vale: {d:.2f}, a divisao inteira vale: {dI}')
print(f'a potencia vale: {po} e o resto vale: {r}')