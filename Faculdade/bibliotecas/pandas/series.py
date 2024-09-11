import pandas as pd

# Criando uma série através de uma tupla

tupla_idades = (25, 32, 15, 26, 36, 33, 56)
# Convertendo a lista em uma série
serie_idades = pd.Series(tupla_idades)
print(serie_idades.describe())


lista_idades = [25, 32, 15, 26, 36, 33, 56]
serie_idades_lista = pd.Series(lista_idades)
print(serie_idades_lista[2])
print(serie_idades_lista.describe())

# Crie uma série com os dados filtrados a partir de outra série
serie_filtrado = serie_idades_lista[serie_idades_lista > 30]
print(serie_filtrado.describe())

serie = pd.Series(lista_idades, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
print(serie)
print(f'Idade do indice a {serie['a']}')
print('\n')

# Alterar as etiquetas para nomes de pessoas
serie = pd.Series(lista_idades, index=[
                  'Maria', 'João', 'José', 'Tais', 'Ana', 'Lais', 'Roberta'])
print(serie)
print(f"Idade da Maria {serie['Maria']}")

# Exibindo as primeiras 3 linhas da série
print(f"Os três primeiros itens\n{serie_idades.head(3)}\n")

# Exibindo as últimas 4 linhas da série
print(f"Os três últimos valores da lista\n{serie_idades.tail(3)}\n")

# Exibindo as estatísticas descritivas da série
print(f"Exibe informações de estatística descritiva da lista\n{
      serie_idades.describe()}\n")

# Exibindo o número de elementos não nulos na série
print(f"Exibe a quantidade de itens (não nulos) {serie_idades.count()}")

# Exibindo os valores únicos na série
print(f"Exibe os valores únicos da lista {serie_idades.unique()}")

# Exibindo a contagem de cada valor presente na série
print(f"Exibe a contagem de cada valor presente na série\n{
      serie_idades.value_counts()}\n")

# Ordenando a série por seus valores
print(f"Ordena a série em ordem crescente\n{serie_idades.sort_values()}\n")

# Ordenando a série por seus valores
print(f"Ordena a série em ordem decrescente\n{
      serie_idades.sort_values(ascending=False)}\n")

# Exibindo o índice do valor mínimo na série
print(f"Exibe o menor índice série\n{serie_idades.idxmin()}\b")

# Exibindo o índice do valor máximo na série
print(f"Exibe o maior índice da série\n{serie_idades.idxmax()}\n")

# Acessando elementos da série por rótulos de índice
print(f"Acessa o elemento da série por rótulos de índice\n{
      serie.loc[['Maria', 'José', 'Lais']]}\n")

# Acessando elementos da série por índices numéricos
print(f"Acessa os elementos da série por índice numéricos\n{
      serie.iloc[[0, 2, 4]]}\n")

# verificando se cada elemento da Series está contido em uma lista de valores
print(f"Retorna uma lista de boleanos de cada item está na lista de idade\n{
      serie.isin([20, 35, 45])}")

# Converte todos os tipos da série no que foi informado
print(f"Serie convertida para float: {serie.astype('float')}\n")

# Cria uma nova série
serie_quantidade_bens = pd.Series([5, 3, 3, 4, 0, 7, 6, 7])

# Aplicando uma função a cada elemento da série
# A função lambda x: x ** 2 pega cada elemento da série e eleva ao quadrado
print(f"Aplica uma função anônima em cada elemento e retorna uma nova série\n{
      serie_quantidade_bens.apply(lambda x: x ** 2)}\n")
print(f"Perceba que a lista não foi alterada\n{serie_quantidade_bens}\n")
