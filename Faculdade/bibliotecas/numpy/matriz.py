"""
import numpy as np # Por convenção atribuimos o apelido np para facilitar a escrita e leitura
"""
import numpy as np
print(f'A versão da biblioteca Numpy é {np.__version__}')

# Criando matrizes com numpy
matriz1 = np.array([1, 2, 3, 4, 5, 6])
matriz2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(matriz1[1])
print(matriz2[1, :].sum())

# Funções das matrizes
print("--------------")
print(matriz1.sum())  # Faz a soma
print(matriz2.transpose())  # Converte linhas em coluna e colunas em linhas
print(type(matriz1))

# Formato das matrizes
print(matriz1.shape)  # Temos uma matriz com 6 colunas
print(matriz2.shape)  # Temos uma matriz com 3 linhas e 4 colunas

# Redimensionar uma matriz
print(matriz1.reshape(2, 3))  # Transforma a matriz com shape (6,) para (2,3)
print(matriz2.reshape(12))  # Transforma a matriz com shape (3,4) para (12,)

print(matriz2.reshape(12).shape)
print(matriz1.reshape(2, 3).shape)


# Gerando matrizes básicas
"""
np.array(), np.zeros(), np.ones(), np.empty(), np.arange(), np.linspace(),dtype
"""
vetor = np.array([1, 2, 3])  # Cria array simples
print(vetor)

# Criando vetor e matriz com zeros
vetor = np.zeros(5, dtype=np.int32)
print(vetor)
vetor = np.zeros(5)  # Float
print(vetor)

matriz = np.zeros((2, 3))
print(matriz)

"""
Criando vetor e matriz com a função empty. A função empty é utilizada 
quando se quer somente criar um objeto que será utilizado depois. 
Ele preenche o vetor e matriz com zeros ou muito próximo de zero
"""

# Cria um array vazio com 2 elementos
vetor = np.empty(5)
print(vetor)

# Cria um array vazio com 2 elementos
matriz = np.empty((2, 5))
print(matriz)


# Criando matriz com uma variedade de elementos
vetor = np.arange(4)  # Cria vetor de 0 até 3, com 4 elementos
matriz = vetor.reshape(2, 2)  # Cria uma matriz 2x2 com os elementos acima
print(vetor)
print(matriz)

# Cria um vetor no qual o valor começa em 2 até o valor 8 em dois em dois
vetor = np.arange(2, 9, 2)
print(vetor)

matriz = np.arange(6)
print(matriz.reshape(3, 2))

"""
A função linspace cria um arranjo seguindo um padrão. Por exemplo, 
podemos criar uma arranjo de 0 até 10, sendo que só posso possuir 4 números.
"""
vetor = np.linspace(0, 10, num=4)
print(vetor, '\n')
matriz = vetor.reshape(2, 2)  # Convertendo em 2x2
print(matriz)

vetor = np.linspace(0, 20, 6).reshape(2, 3)
print(vetor)

print("-----------------------------")
vetor = np.linspace(0, 20, num=20)
print(vetor)

# Especificando seus dados
vetor = np.ones(5, dtype=np.int64)
print(vetor)
vetor = np.ones(5, dtype=np.float32)
print(vetor)
matriz = np.ones((3, 5), dtype=np.int64)
print(matriz)

# Adicionando, removendo e classificando elementos
vetor = np.array([2, 1, 5, 3, 7, 4, 6, 8])

# https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort
print(np.sort(vetor))

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# Unindo dois vetores
print(np.concatenate((a, b)))

# Retorna o formato de uma matriz.
print(np.concatenate((a, b)).shape)

# Dá uma nova forma a uma matriz sem alterar seus dados.
print(np.concatenate((a, b)).reshape(2, 4))

# Ou, se você começar com estes arrays:
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])

print(np.concatenate((x, y), axis=0))

"""
Como você sabe a forma e o tamanho de uma matriz?

ndarray.ndim lhe dirá o número de eixos, ou dimensões, da matriz.

ndarray.size informará o número total de elementos da matriz. Este é o produto dos elementos da forma da matriz.

ndarray.shape exibirá uma tupla de inteiros que indicam o número de elementos armazenados ao longo de cada dimensão
do array. Se, por exemplo, você tiver um array 2-D com 2 linhas e 3 colunas, a forma do seu array é (2, 3).
"""
print()
array_example = np.array([[[0, 1, 2, 3], [4, 5, 6, 7]],
                          [[0, 1, 2, 3], [4, 5, 6, 7]],
                          [[0, 1, 2, 3], [4, 5, 6, 7]]])
print(array_example)
print(array_example.ndim)
print(array_example.size)
print(array_example.shape)

# Como converter uma matriz 1D em uma matriz 2D (como adicionar um novo eixo a uma matriz)
a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape)

a2 = a[np.newaxis, :]
print(a2.shape)

row_vector = a[np.newaxis, :]
print(row_vector.shape)

col_vector = a[:, np.newaxis]
print(col_vector.shape)

"""
Você também pode expandir uma matriz inserindo um novo eixo em uma posição especificada withnpnp.expand_dims.
"""
a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape)

b = np.expand_dims(a, axis=1)
print(b.shape)

c = np.expand_dims(a, axis=0)
print(c.shape)


# Indexação e fatiamento
data = np.array([1, 2, 3])
print(data[1])
print(data[0:2])
print(data[-2:])

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[a < 5])

divisivel_por_2 = a[a % 2 == 0]
print(divisivel_por_2)

c = a[(a > 2) & (a < 11)]
print(c)

acima_cinco = (a > 5) | (a == 5)
print(acima_cinco)
