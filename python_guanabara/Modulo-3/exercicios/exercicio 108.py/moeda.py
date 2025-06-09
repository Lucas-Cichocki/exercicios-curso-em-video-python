def aumentar(preco= 0, aumentar = 0):

   return preco + (preco * aumentar / 100)

def diminuir(preco = 0, diminuir = 0):

    return preco - (preco * diminuir / 100)

def metade(preco = 0):

    return preco / 2

def dobro(preco = 0):

    return preco * 2

def moeda(preco = 0): 

    return f'R${preco:.2f}'.replace('.', ',') 
