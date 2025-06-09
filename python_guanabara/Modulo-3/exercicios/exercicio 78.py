valor = []
posiçaom = []
posiçaome = []

for i in range(0, 5):
    valor.append(int(input(f'Digite um valor para a posiçao {i}: ')))

maior = max(valor)
menor = min(valor)

for p, v in enumerate(valor):
    if v == maior:
        posiçaom.append(p)

print('=' * 50)
print(f'Voce digitou os valores {valor}')

print(f'O mair valor foi: {maior} que esta na posiçao {posiçaom}')

for p, v in enumerate(valor):
    if v == menor:
        posiçaome.append(p)
        
print(f'E o menor valor foi: {menor} que esta na posiçao {posiçaome}')