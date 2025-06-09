d = input('Digite a expressao: ')
v = []

for i in d:
    if d == '(':
        v.append('(')
    elif d == ')':
        if len(v) > 0:
            v.pop
        else:
            v.append(')')
            break
if len(v) == 0:
    print('Sua expressao e valida! ')

else:
    print('Sua expressao esta errada! ')
