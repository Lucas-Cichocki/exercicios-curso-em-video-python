full = [[], []]

for i in range(7):
    n = (int(input('Digite um valor! ')))
    if n % 2 == 0:
        full[0].append(n)

    else:
        full[1].append(n)

full[0].sort()
full[1].sort()  



print(f'Os valores pares digitados foram: {full[0]}')
print(f'Os valores impares digitados foram {full[1]}')