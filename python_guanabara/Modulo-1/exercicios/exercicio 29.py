v = float(input('A qual velocidade voce estava dirigindo? '))

if v > 80:
    M = (v - 80) * 7

    print(f'Por estar acima da velocidade permitida, voce sera multado em R${M:.2f}!')


print('Tenha um bom dia, dirija com segurança! ')