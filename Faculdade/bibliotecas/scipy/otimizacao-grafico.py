import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import differential_evolution

# Definir a função que queremos minimizar


def objective_function(xy):
    x, y = xy
    return x**2 + y**2


# Definir limites para x e y
bounds = [(-5, 5), (-5, 5)]

# Gerar uma grade de pontos para o gráfico
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

# Realizar a otimização global
result = differential_evolution(objective_function, bounds)

# Extrair os valores de x e y que minimizam a função
optimal_xy = result.x

# Valor mínimo da função
minimized_value = result.fun

# Plotar o gráfico de contorno
plt.figure(figsize=(8, 6))
plt.contourf(X, Y, Z, levels=20, cmap='viridis')
plt.colorbar()
plt.scatter(optimal_xy[0], optimal_xy[1], color='red',
            marker='x', label='Mínimo Global')
plt.title('Otimização de Função Bidimensional')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

print(f"Os valores de x e y que minimizam a função são: {optimal_xy}")
print(f"O valor mínimo da função é: {minimized_value}")
