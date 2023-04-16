import requests

link = 'http://192.168.1.107:5000'

requisicao = requests.get(link)

print(requisicao)
print(requisicao.json())

dicionario = requisicao.json()

print(dicionario['total_vendas'])


