n = int(input('Qual o tamanho da Sequencia? '))

s = 0
i = 0
m = 1

while s < n:

    print(i, end=' - ')
    i, m = m, i + m
      
    s += 1

print('FIM')
