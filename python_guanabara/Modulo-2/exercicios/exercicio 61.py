n1 = int(input('Me diga o numero inicial '))
r = int(input('Agora me diga a razao dele '))

a = n1
para = a + 10

while a < para:
    print(n1, end= ' ')
    a += 1
    n1 += r
