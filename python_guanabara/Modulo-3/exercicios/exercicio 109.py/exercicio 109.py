import moeda

p = float(input('Digite um valor: R$'))

print(f'Aumentando em 10% esse valor vai ficar: {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo em 13% esse valor vai ficar: {moeda.diminuir(p, 13, True)}')
print(f'A metade de {moeda.moeda(p)} e: {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} e: {moeda.dobro(p, True)}')