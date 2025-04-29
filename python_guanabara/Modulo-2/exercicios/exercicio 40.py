n1 = float(input('Digite a sua primeira nota! '))
n2 = float(input('Digite a sua segunda nota! '))

media = (n1 + n2) / 2

if media < 5.0:
    print(f'Sua media foi de {media} por ser muito baixa, voce foi reprovado! ')


elif 5 < media <= 7.0:
    print(f'Sua media foi de {media}, ela nao alcançou o ideal, por isso vc ficou de recuperaçao! ')

else:
    print(f'Parabens, sua media foi de {media} voce passou!! ')