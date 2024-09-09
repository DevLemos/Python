import requests
url = "https://jsonplaceholder.typicode.com/posts"
resposta = requests.get(url)
dados = resposta.json()
print(dados)

print(type(dados))
print(dados.values)
