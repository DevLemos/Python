import numpy as np
from scipy.optimize import minimize

# definir a função que queremos minimizar


def funcao_objetivo(x):
    return x ** 2 + 4*x + 4


# Suponha um ponto de partida inicial
chute_inicial = 0.0

# Realizar a otimização
OptimizeResult = minimize(funcao_objetivo, chute_inicial)

# Extrair o valor de x que minimiza a função
optimal_x = OptimizeResult.x

# Valor mínimo da função
minimized_value = OptimizeResult.fun

print(f"O valor de x que minimiza a função é: {optimal_x[0]}")
print(f"O valor mínimo da função é: {minimized_value}")
