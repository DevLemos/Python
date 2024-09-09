import requests
import random
indice = int(random.random() * 6)  # Escolhendo o índice do dataset
print(f'Seu índice é o número: {indice + 1}')

# Montando uma lista com as URLs (Não altere essa célula, somente execute)
lista_url = list()
lista_url.append(
    'https://raw.githubusercontent.com/luiscarlosjunior/aulas-graduacao/master/data-science/analise-dados/datasets/csv/dsfaltas/faltasAlunos1.csv')
lista_url.append(
    'https://raw.githubusercontent.com/luiscarlosjunior/aulas-graduacao/master/data-science/analise-dados/datasets/csv/dsfaltas/faltasAlunos2.CSV')
lista_url.append(
    'https://raw.githubusercontent.com/luiscarlosjunior/aulas-graduacao/master/data-science/analise-dados/datasets/csv/dsfaltas/faltasAlunos3.csv')
lista_url.append(
    'https://raw.githubusercontent.com/luiscarlosjunior/aulas-graduacao/master/data-science/analise-dados/datasets/csv/dsfaltas/faltasAlunos4.csv')
lista_url.append(
    'https://raw.githubusercontent.com/luiscarlosjunior/aulas-graduacao/master/data-science/analise-dados/datasets/csv/dsfaltas/faltasAlunos5.csv')
lista_url.append(
    'https://raw.githubusercontent.com/luiscarlosjunior/aulas-graduacao/master/data-science/analise-dados/datasets/csv/dsfaltas/faltasAlunos6.csv')

# URL escolhida
url_escolhida = lista_url[indice]
print(f'URL escolhida: {url_escolhida}')
# Fazemos a requisição dos dados e atribuimos o resulta a variável resposta
resposta = requests.get(url_escolhida)

# Para exibirmos o texto presente na URL podemos usar o atributo text
print(resposta.text)

texto = resposta.text
itens = texto.split('\n')  # Quebra o texto usando o \n

print(f"A primeira linha é o cabeçalho do arquivo:\n{
      itens[0]}\n")  # Pega a primeira linha
print(f"A segunda linha será o dado correspondendo aos cabeçalhos da linha:\n{
      itens[1]}\n")  # Pega a segunda linha

print(f"Aqui será mostrada a última linha do arquivo:\n{
      itens[-1]}\n")  # Pega a última linha

print(f'Último item antes de deletar\n{itens[-1]}')
del itens[-1]  # Remove último item
print(f'Último item depois de deletar\n{itens[-1]}')


print(len(itens))  # Exibe a quantidade de itens daquela lista


# Como podemos ver com o próximo código, cada linha é uma sequencia de
# caracteres
for item in itens[:3]:
    print(item)

for item in itens[:3]:
    print(item.split(';'))


"""
Precisamos criar um tabela
"""

# Pegar a primeira linha
cabecalhos = itens[0]

# Separar os dados da linha e transformar em uma lista
lista_cabecalhos = cabecalhos.split(';')
print(f'Lista de cabeçalhos: {lista_cabecalhos}')
# Com a lista, podemos aplicar como chaves em um dicionário e associa-los
# aos valores


for item in itens[:3]:
    # Pego o campo RA e média
    print(item.split(';')[0], '\t\t', item.split(';')[6])


"""
Agora vamos criar uma estrutura de dados no qual podemos associa

O caractere \ufeff é conhecido como "marca de ordem zero" (BOM - Byte Order Mark, em inglês) e é usado em algumas codificações de caracteres, como UTF-8, para indicar a ordem dos bytes.
"""

# Criando um dicionário e com as colunas e atribuindo uma referência ao objeto lista
# Cria um dicionário onde cada índice tem com valor o cabeçalho
dicionario_alunos = dict()
for item in lista_cabecalhos:
    cabecalho = item.lstrip('\ufeff')
    dicionario_alunos[cabecalho] = list()

print(dicionario_alunos)

# Cria um dicionário onde cada índice tem com valor o cabeçalho
# dicionario_alunos = dict()
# for i in range(len(lista_cabecalhos)):
#  cabecalho = lista_cabecalhos[i].lstrip('\ufeff')
#  dicionario_alunos[cabecalho] = list()

# print(dicionario_alunos)

# Exibe o conteúdo do dicionário
for item in dicionario_alunos:
    print(item)

chave_dicionario = list(dicionario_alunos.keys())
print(chave_dicionario)

for linha in range(1, 3):
    print(itens[linha].split(';'))

"""
Cria uma lista para armazenar as colunas do arquivo. Para isso é criando
uma linha em branco e adicionado uma nova lista para cada coluna, assim 
nos preenchemos cada indice dessa lista com os dados de cada coluna
"""
lista_itens = []
for lista in range(0, len(chave_dicionario)):
    lista_itens.append(list())

print(lista_itens[0])
print(len(lista_itens))

"""
Pega cada linha do arquivo, quebra e adiciona os itens separados
em cada lista da lista criada anteriormente
"""
for linha in range(1, len(itens)):
    item = itens[linha].split(';')
    lista_itens[0].append(item[0])
    lista_itens[1].append(item[1])
    lista_itens[2].append(item[2])
    lista_itens[3].append(item[3])
    lista_itens[4].append(item[4])
    lista_itens[5].append(item[5])
    lista_itens[6].append(item[6])

print(lista_itens[6])  # Exibi o tamanho da lista

# Adiciona cada coluna da lista anterior para cada chave do dicionário

# Cria um dicionário de itens a partir das linhas
dicionario_alunos[chave_dicionario[0]] = lista_itens[0]
dicionario_alunos[chave_dicionario[1]] = lista_itens[1]
dicionario_alunos[chave_dicionario[2]] = lista_itens[2]
dicionario_alunos[chave_dicionario[3]] = lista_itens[3]
dicionario_alunos[chave_dicionario[4]] = lista_itens[4]
dicionario_alunos[chave_dicionario[5]] = lista_itens[5]
dicionario_alunos[chave_dicionario[6]] = lista_itens[6]

print(dicionario_alunos)

# Apresenta dados da coluna RA
print(dicionario_alunos['RA'])

print(type(dicionario_alunos['Total Faltas'][1]))

# Total de faltas
lista_total_faltas = dicionario_alunos['Total Faltas']
print(lista_total_faltas)

print(type(lista_total_faltas))
print(type(lista_total_faltas[0]))

"""
Veja que no exemplo acima temos uma lista, era o esperado, porém quando pegamos 
a idade vemos que ela está em formato de texto. Logo precisamos converter para 
um formato ideial.
"""
# Converter o tipo de dados de str para int

# Temos algumas formas de fazer, inclusive com ajuda de biblioteca,
# mas vamos realizar sem uso de biblioteca externas.
# 1° forma de fazer

# lista_faltas_int = []
# for falta in lista_total_faltas:
#    lista_faltas_int.append(int(falta))


# 2° - Podemos usar uma nova sintaxe em python, chamada de 'compreensão de lista'
# No qual é uma maneira concisa de criar uma nova lista. Sua sintaxe é
# [novo_valor for valor in lista]
lista_idade_int = [int(idade) for idade in lista_total_faltas]
print(lista_idade_int)
print(type(lista_idade_int))
print(type(lista_idade_int[0]))

dicionario_alunos['Total Faltas'] = lista_idade_int
print(type(dicionario_alunos['Total Faltas'][0]))

lista_total_faltas = dicionario_alunos['Total Faltas']
print(lista_total_faltas)
print(type(lista_total_faltas))
print(len(lista_total_faltas))

# Realindo a operação de média
# Vamos realizar alguma operações estatísticas
soma_total_faltas = sum(lista_total_faltas)
média_das_idades = soma_total_faltas / len(lista_total_faltas)
print(lista_total_faltas)
print(média_das_idades)
# Porém, agora podemos começar a usar algumas bibliotecas

# Converter todas as colunas de mêses e converter para inteiro
# Fev
# Mar
# Abr
# Mai
# Jun

lista_mes_fevereiro = [int(falta) for falta in dicionario_alunos['Fev']]
lista_mes_março = [int(falta) for falta in dicionario_alunos['Mar']]
lista_mes_abril = [int(falta) for falta in dicionario_alunos['Abr']]
lista_mes_maio = [int(falta) for falta in dicionario_alunos['Mai']]
lista_mes_junho = [int(falta) for falta in dicionario_alunos['Jun']]

# Captura a média do mês mais faltante
media_mes_fevereiro = sum(lista_mes_fevereiro) / len(lista_mes_fevereiro)
media_mes_março = sum(lista_mes_março) / len(lista_mes_março)
media_mes_abril = sum(lista_mes_abril) / len(lista_mes_abril)
media_mes_maio = sum(lista_mes_maio) / len(lista_mes_maio)
media_mes_junho = sum(lista_mes_junho) / len(lista_mes_junho)
print(media_mes_fevereiro)
print(media_mes_março)
print(media_mes_abril)
print(media_mes_maio)
print(media_mes_junho)
