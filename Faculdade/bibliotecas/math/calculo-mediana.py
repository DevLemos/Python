import math

# Lista de valores
valores = [10, 8, 12, 15, 13]

# Ordenar a lista
valores_ordenados = sorted(valores)
print(valores_ordenados)

# Cálculo da mediana
meio = len(valores_ordenados) // 2
if len(valores_ordenados) % 2 == 0:
    mediana = (valores_ordenados[meio - 1] + valores_ordenados[meio]) / 2
else:
    mediana = valores_ordenados[meio]

print(mediana)
