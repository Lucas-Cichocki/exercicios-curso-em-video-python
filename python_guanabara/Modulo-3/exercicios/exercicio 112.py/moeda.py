def aumentar(preco = 0, aumentar = 0, formato = False):
    resultado = preco + (preco * aumentar / 100)
    return f'R${resultado:.2f}'.replace('.', ',') if formato else resultado

def diminuir(preco = 0, diminuir = 0, formato = False):
    resultado = preco - (preco * diminuir / 100)
    return f'R${resultado:.2f}'.replace('.', ',') if formato else resultado

def metade(preco = 0, formato = False):
    resultado = preco / 2
    return f'R${resultado:.2f}'.replace('.', ',') if formato else resultado

def dobro(preco = 0, formato = False):
    resultado = preco * 2
    return f'R${resultado:.2f}'.replace('.', ',') if formato else resultado

def moeda(preco=0, formato=True): 

    return f'R${preco:.2f}'.replace('.', ',') if formato else preco

def resumo(p, aumento, decremento):
    print('-' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('-' * 40)

    print(f'{"Preço analisado:":<20} {moeda(p, True)}')
    print(f'{"Dobro do preço:":<20} {dobro(p, True)}')
    print(f'{"Metade do preço:":<20} {metade(p)}')
    print(f'{aumento}% de {"aumento:":<13} {aumentar(p, aumento)}')
    print(f'{decremento}% de {"reduçao:":<13} {diminuir(p, decremento)}')