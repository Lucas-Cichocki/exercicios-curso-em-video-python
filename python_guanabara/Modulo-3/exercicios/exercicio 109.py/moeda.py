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