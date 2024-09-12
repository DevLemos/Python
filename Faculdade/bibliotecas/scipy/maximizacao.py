import numpy as np
from scipy.optimize import minimize

# Definir a função negativa para a maximização


def negative_objective_function(x):
    return -(x**2 - 4*x)


# Suponha um ponto de partida inicial
initial_guess = 0.0

# Realizar a otimização
resultado = minimize(negative_objective_function, initial_guess)

# Extrair o valor de x que maximiza a função
otimo_x = resultado.x

# Valor máximo da função (negativo do mínimo)
valor_maximizado = -resultado.fun

print(f"O valor de x que maximiza a função é: {otimo_x[0]}")
print(f"O valor máximo da função é: {valor_maximizado}")
