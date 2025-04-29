P = float(input('Quantos kilos voce pesa? '))
A = float(input('E qual a sua altura? '))


imc = P / (A * A)

if imc < 18.5:
  print('Voce esta abaixo do peso! ')


elif 18.5 <= imc < 25:
  print('Voce esta no peso ideal! ')

elif 25 <= imc < 30:
  print('Voce esta com sobrepeso! ')

elif 30 <= imc < 40:
  print('Voce esta com obesidade! ')

else:
  print('Voce esta com obesidade morbida! ')

