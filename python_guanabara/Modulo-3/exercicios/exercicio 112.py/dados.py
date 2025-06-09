def validarD():
    while True:
        n = input('Digite um valor: R$').strip()
        if n.replace('.', '').replace(',', '').isnumeric():
            break
        else: 
            print(f'\033[0;30;41m Erro! Digite um numero! \033[m')

    nNovo = n.replace(',', '.')
    nFormat = float(nNovo)

    return nFormat

def validarAu():
    while True:
        a = input('Digite uma porcentagem que gostaria de aumentar ').strip()
        if a.replace('%', '').isnumeric():
            break

        else:
            print(f'\033[0;30;41m Erro! Digite um numero! \033[m')

    aNovo = a.replace('%', '')
    aFormat = int(aNovo)
    return aFormat

def validarDe():
    while True:
        d = input('E outra que gostaria de diminuir ').strip()       
        dNovo = d.replace('%', '')
        if dNovo.isnumeric():
            break 
        else:
            print(f'\033[0;30;41m Erro! Digite um numero! \033[m')
    dFormat = int(dNovo)
    return dFormat