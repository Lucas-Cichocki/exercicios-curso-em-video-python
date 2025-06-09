import requests

url = 'https://www.pudim.com.br/'

try:
    resposta = requests.get(url)
    print(f'Site acessado com sucesso! ')

except requests.exceptions.RequestException as e:
    print(f'Erro ao acessar o site: {e}')