# Faz uma requisição POST
import requests

url = 'https://www.example.com'
data = {'name': 'John Doe', 'email': 'johndoe@example.com'}
response = requests.post(url, data=data)

if response.status_code >= 200 or response.status_code <= 299:
    print('Envio realizado com sucesso')
else:
    print(f'Houve algum problema verifique o código de retorno {
          response.status_code}')


"""
import requests

url = "https://www.example.com/contact"

dados = {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "message": "Olá, gostaria de fazer uma pergunta sobre o seu produto."
}

resposta = requests.post(url, data=dados)

if resposta.status_code == 404:
  print('Página não encontrada')
elif resposta.status_code == 200:
  print('Post realizado com sucesso')

"""
