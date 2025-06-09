import moeda

p = float(input('Digite um valor: R$'))

print(f'Aumentando em 10% esse valor vai ficar: {moeda.aumentar(p, 10)}')
print(f'Diminuindo em 13% esse valor vai ficar: {moeda.diminuir(p, 13)}')
print(f'A metade de {p} e: {moeda.metade(p)}')
print(f'O dobro de {p} e: {moeda.dobro(p)}')