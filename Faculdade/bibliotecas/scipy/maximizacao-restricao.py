import numpy as np
from scipy.optimize import minimize

# Definir a função que queremos maximizar (negativo da função original)


def funcao_objetivo(x):
    return -(x*2)

# Definir a restrição: -f(x) = -200


def restricao(x):
    return -funcao_objetivo(x) + 200


# Suponha um ponto de partida inicial
initial_guess = 0.0

# Definir a restrição como uma tupla de dicionários
constraints = ({'type': 'eq', 'fun': restricao})

# Realizar a otimização com a restrição
resultado = minimize(funcao_objetivo, initial_guess, constraints=constraints)

# Extrair o valor de x que maximiza a função
otimo_x = resultado.x

# Valor máximo da função (negativo do resultado da função)
valor_maximo = -resultado.fun

print(f"O valor de x que maximiza a função é: {otimo_x[0]}")
print(f"O valor máximo da função é: {valor_maximo}")
