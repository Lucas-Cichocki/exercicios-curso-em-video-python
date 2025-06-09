def aumentar(preco = 0, aumentar = 0, formato = False):
    resultado = preco + (preco * aumentar / 100)
    return resultado if formato is False else moeda(resultado)

def diminuir(preco = 0, diminuir = 0, formato = False):
    resultado = preco - (preco * diminuir / 100)
    return resultado if formato is False else moeda(resultado)

def metade(preco = 0, formato = False):
    resultado = preco / 2
    return resultado if formato is False else moeda(resultado)

def dobro(preco = 0, formato = False):
    resultado = preco * 2
    return resultado if formato == False else moeda(resultado)

def moeda(preco=0): 

    return f'R${preco:.2f}'.replace('.', ',') 

def resumo(p, aumento, decremento):
    print('-' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('-' * 40)

    print(f'{"Preço analisado:":<20} {moeda(p)}')
    print(f'{"Dobro do preço:":<20} {dobro(p, True)}')
    print(f'{"Metade do preço:":<20} {metade(p, True)}')
    print(f'{aumento}% de {"aumento:":<13} {aumentar(p, aumento, True)}')
    print(f'{decremento}% de {"reduçao:":<13} {diminuir(p, decremento, True)}')
    
    print('-' * 40)