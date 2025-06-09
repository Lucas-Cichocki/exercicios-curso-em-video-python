def contador(*num):
    #for i in num:
    #   print(f'{i}', end= ' ')
    #print()
    tam = len(num)
    print(f'recebi os valores {num} e sao ao todo {tam} numeros')

contador(2,1,7)
contador(8,0)
contador(4, 4, 7, 6, 2)