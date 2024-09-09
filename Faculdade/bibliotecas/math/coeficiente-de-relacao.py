import math

# Lista de valores X e Y
valores_x = [10, 8, 12, 15, 13]
valores_y = [2, 1, 3, 6, 4]

# Cálculo da média
media_x = sum(valores_x) / len(valores_x)
media_y = sum(valores_y) / len(valores_y)

# Cálculo do coeficiente de correlação
num = sum((x - media_x) * (y - media_y) for x, y in zip(valores_x, valores_y))
den1 = math.sqrt(sum((x - media_x) ** 2 for x in valores_x))
den2 = math.sqrt(sum((y - media_y) ** 2 for y in valores_y))
coef_correlacao = num / (den1 * den2)

print(coef_correlacao)
