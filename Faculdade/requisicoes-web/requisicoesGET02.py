import requests

url = 'https://www.google.com'
response = requests.get(url)

print(response.content)
print(response.headers)
print(response.status_code)

if response.status_code == 200:
    print('Requisição foi feita com sucesso')
else:
    print(f'Houve algum erro segue o código {response.status_code}')
