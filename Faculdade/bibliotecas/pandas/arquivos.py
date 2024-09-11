import pandas as pd

# Lista de URLs
url_alunos = 'https://raw.githubusercontent.com/luiscarlosjunior/aulas-graduacao/master/data-science/analise-dados/datasets/csv/resumoAlunos.csv'
separador = ';'

# Lendo arquivo CSV
alunos = pd.read_csv(url_alunos, sep=separador)

# Exibindo as cinco primeiras linhas do DataFrame
print(alunos.head())
print('\n')
# Exibindo as 3 primerias linhas
print(alunos.head(3))
print('\n')
# Exibindo a primeira linha
print(alunos.head(1))
print('\n')

# mostra estatísticas descritivas do dataframe
print(alunos.loc[:, 'Idade'].describe())
print('\n')

# mostra informações sobre as colunas do dataframe
print(alunos.info())
print('\n')

# Pegando colunas de interesse, dessa forma podemos direcionar os nossos estudos
colunas_interesse = ['média', 'Idade', 'Total Faltas']
df_interesse = alunos[colunas_interesse]
print(f'Média das colunas\n{df_interesse.mean()}\n')  # média das colunas
print(f'Mediana das colunas\n{df_interesse.median()}\n')  # mediana das colunas
print(f'Moda das colunas\n{df_interesse.mode()}\n')  # moda das colunas
print(f'Descrição estatística das colunas\n{df_interesse.describe()}\n')
print(f'Informações gerais das colunas\n{df_interesse.info()}\n')

# A sintaxe é: dataframe.groupby('Nome Coluna')['Nome Coluna']
# A coluna dentro dos parenteses será utilizado para criar as categorias com dados unicos
# A coluna entre conchetes será de onde os dados serão coletados, segue abaixo um exemplo
grupo_alunos_matutinos = alunos.groupby('Periodo')['média']
# Esse função pega as informações básicas para análise
print(grupo_alunos_matutinos.describe())
print('\n')

# Aqui estamos querendo saber se o total de faltas é diferente entre os períodos
grupo_alunos_matutinos = alunos.groupby('Periodo')['Total Faltas']
print(grupo_alunos_matutinos.describe())
print('\n')

# Queremos fazer uma análise nas notas de cada periodo
grupo_alunos_matutinos = alunos.groupby('Periodo')['AV1']
print(grupo_alunos_matutinos.describe())
print('\n')

# Queremos fazer uma análise nas notas de cada periodo
grupo_alunos_matutinos = alunos.groupby('Periodo')['AV2']
print(grupo_alunos_matutinos.describe())
print('\n')
