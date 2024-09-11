import pandas as pd
import numpy as np

# Cria uma lista com lista de nome e idade
dados = [['Ana', 25], ['Maria', 30], [
    'Carla', 35], ['Robert', 35], ['João', 35]]
# Converte os dados acima em um dataframe e atribui nomes as colunas
df_dados = pd.DataFrame(dados, columns=['Nome', 'Idade'])
print(df_dados)
print('\n')

idades = {'Nome': ['Ana', 'Bob', 'Carla'], 'Idade': [25, 30, 35]}
df_idades = pd.DataFrame(idades)

# Cria um df com filtro
df_filtrado = df_idades[df_idades['Idade'] > 28]
print(df_filtrado)
print('\n')

# Gera uma nova coluna com base na informação de outra
df_idades['Ano Nascimento'] = 2023 - df_idades['Idade']
print(df_idades)
print('\n')

# Gera uma nova coluna aplicando a função apply, no qual eleva ao quadrado cada idade
df_idades['Idade ao Quadrado'] = df_idades['Idade'].apply(lambda x: x ** 2)
print(df_idades)
print('\n')

# inplace = True é para permitir a modificação interna
df_idades.rename(columns={'Nome': 'Nome do aluno'}, inplace=True)
print(df_idades)
print('\n')

# Deleta uma coluna (axis=1 diz ao algoritmo que Idade é uma coluna)
df_idades.drop('Idade', axis=1, inplace=True)
print(df_idades)
print('\n')

# Deleta uma linha (axis=0 diz ao algoritmo que a linha de indice 1 será deletado e é uma linha)
df_idades.drop(1, axis=0, inplace=True)
print(df_idades)
print('\n')

df_alunos = pd.DataFrame({'Nome': ['Ana', 'Bruno', 'Carla', 'Maria'],
                          'Idade': [20, 17, 30, 35],
                          'Sexo': ['F', 'M', 'F', 'M']})
print(df_alunos)
print('\n')
df_alunos['Hobby'] = ['Futebol', 'Leitura', 'Volei', 'Professor']
print(df_alunos)
print('\n')

print(df_alunos)
# A função where da biblioteca numpy fornece uma forma de criar uma classificação com condições
df_alunos['Categoria'] = np.where(df_alunos['Idade'] >= 18, 'Adulto', 'Menor')
print(df_alunos)
print('\n')

# Aplicando as operações em python

# Cria data frame de exemplo de salários
df_salario = pd.DataFrame(
    {'salario': [2000, 2500, 1500, 4000, 5000, 3500, 2500]})

# calcular média
média = df_salario['salario'].mean()
print('Média aritmética:', média)

# calcular mediana
mediana = df_salario['salario'].median()
print('Mediana:', mediana)

# calcular valor mínimo
minimo = df_salario['salario'].min()
print('Valor mínimo:', minimo)

# calcular valor máximo
maximo = df_salario['salario'].max()
print('Valor máximo:', maximo)
print('\n')

# Captar a quantidade de itens
quantidade_itens_não_nulos = df_salario['salario'].count()
print('Retorna a quantidade de itens não nulos:', quantidade_itens_não_nulos)

# Função describe() gera um resumi estatístico de um dataframe
# Contagem, desvio padrão, mínimo, máximo e quartis
descricao = df_salario['salario'].describe()
print('Descrição estatística:\n', descricao)
print('\n')

# calcular variancia
var = df_salario['salario'].var()
print('Variância:', var)

# calcular desvio padrão
std = df_salario['salario'].std()
print('Desvio padrão:', std)
print('\n')

# calcular primeiro quartil
quartil1 = df_salario['salario'].quantile(0.25)
print('Primeiro quartil:', quartil1)

quartil1 = df_salario['salario'].quantile(0.75)
print('terceiro quartil:', quartil1)
print('\n')

# Criando um DataFrame
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8], 'C': [9, 10, 11, 12]})

# Usando o método corr()
correlação = df.corr()
print(correlação)
print('\n')
