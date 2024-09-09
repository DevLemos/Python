# importa a biblioteca
import requests

url = 'https://www.google.com'
response = requests.get(url)
print(response.content)  # Exibi o conteúdo
print(response.headers)  # Exibi o cabeçalho
print(response.status_code)  # Exibi o código de retorno
print(response.cookies)  # Exibi o código de retorno

print(type(response.headers))

dicionario_header = dict(response.headers)
print(type(dicionario_header))
print(dicionario_header)

for item in dicionario_header.keys():
    print(item)

for item in dicionario_header:
    print(dicionario_header[item])

chaves = dicionario_header.keys()
valores = dicionario_header.values()
print(chaves)
print(valores)
