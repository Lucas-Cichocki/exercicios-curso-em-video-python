def parOuImpar(n = 0):
    if n % 2 == 0:
        return True
    
    else:
        return False
    
jorangotango = int(input('Digite um numero: '))
print(parOuImpar(jorangotango))