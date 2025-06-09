import moeda

p = float(input('Digite um valor: R$'))

print(f'Aumentando em 10% esse valor vai ficar: {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo em 13% esse valor vai ficar: {moeda.moeda(moeda.diminuir(p, 13))}')
print(f'A metade de {moeda.moeda(p)} e: {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} e: {moeda.moeda(moeda.dobro(p))}')