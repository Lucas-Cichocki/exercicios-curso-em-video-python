def fatorial(n, show = 'False'):
    """-> Calcula o fatorial de um numero.
    :param n: O numero a ser calculado.
    :param show: (opcional) Mostra ou nao a conta.
    :return: O valor do fatorial de um numero n."""
    f = 1
    for i in range(n, 0, -1):
        if show:
            print(f'{i}', end= ' x ' if i > 1 else ' = ')
        
        f *= i   
    return f
    

print(fatorial(5, False))
help(fatorial)
    




