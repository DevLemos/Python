import requests
import xml.etree.ElementTree as ET

url = "https://www.w3schools.com/xml/note.xml"

resposta = requests.get(url)
raiz = ET.fromstring(resposta.content)
dados = {}

for elemento in raiz.iter():
    dados[elemento.tag] = elemento.text

print(dados)
