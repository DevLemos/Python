# Código abaixo será o mesma para todos os exercícios. O que irá mudar é o x e y
import numpy as np  # Importa biblioteca Numpy
from matplotlib import pyplot as plt  # Importa biblioteca para gerar o gráfico

# Pega os dados (Só um exemplo)
x = np.linspace(1, 15, 10)  # Variável X
y = np.arange(10, 20)  # Vriável Y

# plt é o objeto que contém as funções para editar
# e exibir a figura
plt.title("Variável X e Y")  # Define o título do gráfico
plt.xlabel("Variável X")  # Define a legenda para o eixo X
plt.ylabel("Variável Y")  # Define a legenda para o eixo Y

# 'Plota' (exibe) o gráfico passando x, y e o estilo dos pontos
plt.plot(x, y, 'ob')  # OB significa O é um circulo e B é a cor blue (azul)

# Realiza o cálculo do MMQ
equação = np.polyfit(x, y, 1)

# Adicionar a linha de tendência
linha_tendência = np.poly1d(equação)  # Realiza o cálculo da linha de tendência

# Calcula a correlação de Pearson
correlação = np.corrcoef(x, y)[0][1]

# Adiciona a linha na figura
plt.plot(x, linha_tendência(x), 'r--')

# Definindo a legenda para exibir na figura
legenda = f'Linha de tendência: y = {equação[0]:.6f}x {equação[1]:.6f}'
legenda += f'\nCoeficiente de Pearson (p): {correlação}'
plt.text(0.05, 0.9, legenda,
         transform=plt.gca().transAxes,
         fontsize=11)
# -------------------------------------------

# Exibe a figura completa
plt.show()
